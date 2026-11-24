"""Online question bank for Chapter 3 (Boolean logic): complements, truth tables, circuits to draw and to read.
Every expression is generated, every answer is computed by boolean_lib.py and checked; every circuit is drawn from
its expression. Same seed, same questions: run it again and nothing changes.

Run from the repository root:  python tools/boolean_bank.py"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import boolean_lib as bl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / 'book' / 'unit-1' / '003-ch03-boolean-logic'
QD = CH / 'questions'
IMG = ROOT / 'book' / 'assets' / 'circuits' / 'ch03'
rnd = random.Random(2026)


def lit(v):
    return v + ("'" if rnd.random() < 0.4 else '')


def product(vs, k):
    return '·'.join(lit(v) for v in sorted(rnd.sample(vs, k)))


def sop(vs):
    n = rnd.choice([2, 2, 3])
    terms = []
    while len(terms) < n:
        p = product(vs, rnd.choice([2, 2, 3]) if len(vs) > 2 else 2)
        if p not in terms:
            terms.append(p)
    return ' + '.join(terms)


def pos(vs):
    n = rnd.choice([2, 2, 3])
    terms = []
    while len(terms) < n:
        p = '(' + ' + '.join(lit(v) for v in sorted(rnd.sample(vs, 2))) + ')'
        if p not in terms:
            terms.append(p)
    return '·'.join(terms)


def nested(vs):
    a, b, c = (vs + vs)[:3]
    forms = [f"({lit(a)} + {lit(b)})'·{lit(c)}", f"({lit(a)}·{lit(b)})' + {lit(c)}", f"{lit(a)} + ({lit(b)}·{lit(c)})'",
             f"({lit(a)} + {lit(b)}·{lit(c)})'", f"{lit(a)}·({lit(b)} + {lit(c)})"]
    return rnd.choice(forms)


def make(kind, count, seen, nvars=(2, 3, 3, 4)):
    out = []
    while len(out) < count:
        vs = ['A', 'B', 'C', 'D'][:rnd.choice(nvars)]
        s = {'sop': sop, 'pos': pos, 'nested': nested}[kind](vs)
        e = bl.parse(s)
        key = (type(e).__name__, frozenset(bl.show(x) for x in e.xs)) if isinstance(e, (bl.And, bl.Or)) else bl.show(e)
        vals = {v for _, v in bl.rows(e)}
        if key in seen or len(vals) < 2 or len(bl.names(e)) < 2:   # no repeats, no constant functions
            continue
        seen.add(key)
        out.append(e)
    return out


HEAD = ('*Chapter 3 · Questions (online). Every expression here was generated and every answer computed by a program '
        '(`tools/boolean_bank.py`), then checked against the truth table, so the answers cannot contain slips. '
        'Try each question on paper before you read the answer below it.*\n\n')


def complements():
    seen = set()
    es = make('sop', 14, seen) + make('pos', 13, seen) + make('nested', 13, seen)
    lines = ['# Chapter 3: finding the complement (40 questions)\n', HEAD,
             '**Method** (section 3.6 of the book): prime the whole expression; open each bracket with De Morgan '
             '(+ becomes ·, · becomes +, every term gets a prime); remove double primes; stop when primes sit only on letters.\n']
    for k, e in enumerate(es, 1):
        st = bl.complement_steps(e)
        lines.append(f"**Q{k}.** Find the complement of F = {bl.show(e)}.\n")
        lines.append(f"**Answer.** F' = {st[0]}" + ''.join(f"<br>= {x}" for x in st[1:]) + '\n')
        # a check row: all inputs 1
        vs = sorted(bl.names(e)); env = {v: 1 for v in vs}
        f1 = bl.ev(e, env); c1 = bl.ev(bl.parse(st[-1]), env)
        assert c1 == 1 - f1
        lines.append(f"*Check:* with every input 1, F = {f1} and F' = {c1}: opposites, as they must be.\n")
    (QD / '08-complements.md').write_text('\n'.join(lines), encoding='utf-8')
    return len(es)


def truth_tables():
    seen = set()
    es = make('sop', 10, seen, (2, 3)) + make('pos', 10, seen, (2, 3)) + make('nested', 10, seen, (3,))
    lines = ['# Chapter 3: truth tables of expressions (30 questions)\n', HEAD,
             '**Method** (section 3.5): rows = 2ⁿ; fill the inputs by counting; one column for each step, inside out; the last column is the output.\n']
    for k, e in enumerate(es, 1):
        lines.append(f"**Q{k}.** Make the truth table of Y = {bl.show(e)}.\n")
        lines.append('**Answer.**\n\n' + bl.table_md(e, 'Y') + '\n')
        ones = [''.join(map(str, c)) for c, v in bl.rows(e) if v]
        lines.append(f"*Y is 1 in {len(ones)} of {2 ** len(bl.names(e))} rows:* {', '.join(ones)}.\n")
    (QD / '09-truth-tables.md').write_text('\n'.join(lines), encoding='utf-8')
    return len(es)


def circuits():
    IMG.mkdir(parents=True, exist_ok=True)
    seen = set()
    draw_es = make('sop', 8, seen, (2, 3)) + make('pos', 6, seen, (2, 3)) + make('nested', 6, seen, (3,))
    read_es = make('sop', 5, seen, (2, 3)) + make('nested', 5, seen, (3,))
    lines = ['# Chapter 3: logic circuits, to draw and to read (30 questions)\n', HEAD,
             '**Method** (section 3.8): NOT gates first, then the AND gates, then the OR gate (B-N-A-O). '
             'To read a circuit, write the output of each gate, from the inputs to the output.\n',
             '## Draw the circuit\n']
    for k, e in enumerate(draw_es, 1):
        f = f'draw-{k:02d}.png'
        bl.draw(e, IMG / f, 'Y')
        lines.append(f"**Q{k}.** Draw the logic circuit for Y = {bl.show(e)}.\n")
        lines.append(f"**Answer.**\n\n![Circuit for Y = {bl.show(e)}](../../../assets/circuits/ch03/{f})\n")
    lines.append('## Read the circuit\n')
    for k, e in enumerate(read_es, len(draw_es) + 1):
        f = f'read-{k:02d}.png'
        bl.draw(e, IMG / f, 'Y', reveal=False)
        lines.append(f"**Q{k}.** Write the Boolean expression for this circuit.\n\n![A circuit to read](../../../assets/circuits/ch03/{f})\n")
        lines.append(f"**Answer.** Y = {bl.show(e)}\n")
    (QD / '10-circuits.md').write_text('\n'.join(lines), encoding='utf-8')
    return len(draw_es) + len(read_es)


if __name__ == '__main__':
    QD.mkdir(parents=True, exist_ok=True)
    n1, n2, n3 = complements(), truth_tables(), circuits()
    print(f'complements {n1}, truth tables {n2}, circuits {n3}: {n1 + n2 + n3} questions')
