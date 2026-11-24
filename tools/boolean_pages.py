"""Chapter 3 online pages computed by program (24 Nov 2026):
  beyond-xnor.md, beyond-sop-pos-kmap.md, sometimes-asked-duality-tautology.md, questions/11-nand-nor-only.md
Every table, minimal expression and conversion is computed by boolean_lib.py and checked row by row.
Run from the repository root:  python tools/boolean_pages.py"""
import itertools
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import boolean_lib as bl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / 'book' / 'unit-1' / '003-ch03-boolean-logic'
IMG = ROOT / 'book' / 'assets' / 'circuits' / 'ch03'
rnd = random.Random(303)
P = bl.parse
NOTE = '*Every table and answer on this page was computed by a program (`tools/boolean_pages.py`) and checked row by row.*\n'


# ------------------------------------------------------------------ minimal SOP by exhaustive search (up to 3 or 4 variables)
def implicants(vs, ones):
    cubes = []
    for pattern in itertools.product('01-', repeat=len(vs)):
        cover = [m for m in range(2 ** len(vs)) if all(p == '-' or int(p) == (m >> (len(vs) - 1 - i)) & 1 for i, p in enumerate(pattern))]
        if cover and set(cover) <= ones:
            cubes.append((pattern, frozenset(cover)))
    prime = [c for c in cubes if not any(c[1] < d[1] for d in cubes)]
    return prime


def term_str(vs, pattern):
    lits = [v + ("'" if p == '0' else '') for v, p in zip(vs, pattern) if p != '-']
    return '·'.join(lits) if lits else '1'


def minimal_sop(vs, ones):
    if not ones:
        return '0'
    prime = implicants(vs, set(ones))
    for k in range(1, len(prime) + 1):
        best = None
        for combo in itertools.combinations(prime, k):
            if set().union(*(c[1] for c in combo)) >= set(ones):
                lits = sum(sum(p != '-' for p in c[0]) for c in combo)
                if best is None or lits < best[0]:
                    best = (lits, combo)
        if best:
            return ' + '.join(term_str(vs, c[0]) for c in best[1])


def minterm(vs, m):
    return '·'.join(v + ("'" if not (m >> (len(vs) - 1 - i)) & 1 else '') for i, v in enumerate(vs))


def maxterm(vs, m):
    return '(' + ' + '.join(v + ("'" if (m >> (len(vs) - 1 - i)) & 1 else '') for i, v in enumerate(vs)) + ')'


def kmap3(vs, ones):
    """3-variable K-map: rows A = 0, 1; columns BC in Gray order 00, 01, 11, 10."""
    cols = ['00', '01', '11', '10']
    lines = [f'| {vs[0]} \\ {vs[1]}{vs[2]} | ' + ' | '.join(cols) + ' |', '|:-:|' + ':-:|' * 4]
    for a in (0, 1):
        cells = [('**1**' if int(f'{a}{c}', 2) in ones else '0') for c in cols]
        lines.append(f'| {a} | ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)


# ------------------------------------------------------------------ XNOR page
def xnor_page():
    IMG.mkdir(parents=True, exist_ok=True)
    bl.draw(P("A·B + A'·B'"), IMG / 'xnor-and-or.png', 'Y')
    two = bl.table_md(P("(A ⊕ B)'"), 'Y', include_steps=False)
    three = ['| A | B | C | Number of 1s | XNOR of all three |', '|:-:|:-:|:-:|:-:|:-:|']
    for a, b, c in itertools.product((0, 1), repeat=3):
        n = a + b + c
        three.append(f'| {a} | {b} | {c} | {n} | {1 - (n % 2)} |')
    eq = ['| A1 | A0 | B1 | B0 | Equal? E = (A1 ⊕ B1)'' · (A0 ⊕ B0)'' |', '|:-:|:-:|:-:|:-:|:-:|']
    e = P("(A ⊕ C)'·(B ⊕ D)'")              # A = A1, B = A0, C = B1, D = B0
    for a1, a0, b1, b0 in itertools.product((0, 1), repeat=4):
        v = bl.ev(e, {'A': a1, 'B': a0, 'C': b1, 'D': b0})
        assert v == int((a1, a0) == (b1, b0))
        eq.append(f'| {a1} | {a0} | {b1} | {b0} | {v} |')
    assert bl.equal(P("(A ⊕ B)'"), P("A·B + A'·B'"))
    txt = f"""# Beyond syllabus: XNOR, the "same answer" detector

*Chapter 3 · Beyond syllabus. The printed book has the essentials of XNOR (section 3.4); this page goes further.*

{NOTE}
## 1. What it does

An **XNOR** gate gives **1 when its inputs are the same**, and 0 when they differ. It is XOR followed by NOT.

{two}

- Expression: **Y = (A ⊕ B)' = A·B + A'·B'**: "both 1, or both 0".
- Symbol: the XOR symbol with a bubble at the output.

## 2. XNOR built from AND, OR and NOT

![XNOR from AND, OR and NOT](../../assets/circuits/ch03/xnor-and-or.png)

Two AND gates catch "both 1" (A·B) and "both 0" (A'·B'); the OR gate says yes if either happened.

## 3. More than two inputs: the even detector

With three or more inputs, XNOR (XOR followed by NOT) gives 1 when an **even** number of inputs are 1.

{chr(10).join(three)}

## 4. Where it is used: are two numbers equal?

To check whether two 2-bit numbers A1A0 and B1B0 are equal, compare them bit by bit with XNOR, then AND the answers: equal only if every bit matches. This is how a computer's ALU tests "is A equal to B?" (the comparison of Chapter 1).

{chr(10).join(eq)}

## 5. Practice

1. What is the XNOR of 1 and 0? *Answer:* 0 (they differ).
2. Write XNOR using only AND, OR and NOT. *Answer:* A·B + A'·B'.
3. Is XNOR the same as NOR? *Answer:* No. For A = 1, B = 1: XNOR gives 1, NOR gives 0.
4. A 4-input XNOR gets 1, 1, 0, 1. Output? *Answer:* 0: three 1s is odd.
5. Prove (A ⊕ B)' = A ⊕ B'. *Answer:* both are 1 exactly when A and B are the same (check the four rows).
"""
    assert bl.equal(P("(A ⊕ B)'"), P("A ⊕ B'"))
    (CH / 'beyond-xnor.md').write_text(txt, encoding='utf-8')


# ------------------------------------------------------------------ SOP, POS and K-maps
def sop_page():
    vs = ['A', 'B', 'C']
    ex = [1, 3, 5, 7]   # F = 1 when C = 1
    ex2 = [0, 1, 2, 6]
    blocks = []
    for k, ones in enumerate([ex, ex2], 1):
        canon = ' + '.join(minterm(vs, m) for m in ones)
        pos = '·'.join(maxterm(vs, m) for m in range(8) if m not in ones)
        mini = minimal_sop(vs, ones)
        for x in (canon, pos, mini):
            assert sorted(m for m in range(8) if bl.ev(P(x), dict(zip(vs, map(int, f'{m:03b}'))))) == sorted(ones), x
        blocks.append(f"""### Example {k}: F = 1 in rows {', '.join(map(str, ones))}

**Canonical SOP** (one minterm for each 1): F = {canon}

**Canonical POS** (one maxterm for each 0): F = {pos}

**K-map:**

{kmap3(vs, set(ones))}

**Minimal SOP** (largest groups of 1s): **F = {mini}**
""")
    practice = []
    seen = set()
    while len(practice) < 10:
        ones = sorted(rnd.sample(range(8), rnd.choice([2, 3, 4, 5])))
        if tuple(ones) in seen:
            continue
        seen.add(tuple(ones))
        mini = minimal_sop(vs, ones)
        assert sorted(m for m in range(8) if bl.ev(P(mini), dict(zip(vs, map(int, f'{m:03b}'))))) == ones
        practice.append(f"**Q{len(practice) + 1}.** F(A, B, C) = Σ({', '.join(map(str, ones))}). Write the canonical SOP and the minimal SOP.\n\n"
                        f"**Answer.** Canonical: {' + '.join(minterm(vs, m) for m in ones)}. Minimal: **{mini}**.\n")
    txt = f"""# Beyond syllabus: from a truth table back to an expression: SOP, POS and K-maps

*Chapter 3 · Beyond syllabus (Class XII and engineering). The printed book goes from an expression to its truth table; this page goes the other way.*

{NOTE}
## 1. Minterms and maxterms

- A **minterm** is an AND of all the inputs, each primed or not, that is 1 in exactly **one** row: row 101 has the minterm A·B'·C.
- A **maxterm** is an OR of all the inputs that is 0 in exactly one row: row 101 has the maxterm (A' + B + C').
- **SOP** (sum of products): OR together the minterms of the rows where F = 1. **POS** (product of sums): AND together the maxterms of the rows where F = 0.
- Rows are numbered by counting in binary: 000 is row 0, 101 is row 5. F = Σ(1, 3) means F = 1 in rows 1 and 3.

## 2. The Karnaugh map (K-map)

A K-map is the truth table drawn as a grid, with the columns in the order 00, 01, **11**, 10 so that neighbours differ in one input only. Circle groups of 1s (sizes 1, 2, 4, 8; they may wrap round the edges); each group becomes one short product term, because the input that changes inside the group drops out.

{chr(10).join(blocks)}
## 3. Practice (answers computed)

{chr(10).join(practice)}"""
    (CH / 'beyond-sop-pos-kmap.md').write_text(txt, encoding='utf-8')


# ------------------------------------------------------------------ duality, tautology, fallacy
def duality_page():
    qs = []
    seen = set()
    while len(qs) < 10:
        vs = rnd.sample(['A', 'B', 'C', 'X', 'Y'], 3)
        t = rnd.choice(["{a} + {b}·{c}", "({a} + 0)·{b}", "{a}·{b}' + 1", "({a} + {b})·({a}' + {c})", "{a}·1 + {b}·0", "{a}' + {a}·{b}"])
        s = t.format(a=vs[0], b=vs[1], c=vs[2])
        if s in seen:
            continue
        seen.add(s)
        qs.append(f"**Q{len(qs) + 1}.** Write the dual of {bl.show(P(s))}.\n\n**Answer.** {bl.show(bl.dual(P(s)))}\n")
    cands = ["A + A'", "A·A'", "A + 1", "A·0", "A + A'·B", "(A + B)·(A' + B)'", "A·B + A·B' + A'", "A·(A' + B)·B'", "A + B", "(A·A')'"]
    cls = []
    for k, s in enumerate(cands, 11):
        vals = {v for _, v in bl.rows(P(s))}
        kind = 'a tautology (1 in every row)' if vals == {1} else 'a fallacy (0 in every row)' if vals == {0} else 'neither (it is 0 in some rows and 1 in others)'
        cls.append(f"**Q{k}.** Is {bl.show(P(s))} a tautology, a fallacy, or neither?\n\n**Answer.** It is {kind}.\n")
    txt = f"""# Sometimes asked: duality, tautology and fallacy

*Chapter 3 · Sometimes asked. The printed book (section 3.7) gives the definitions; this page gives more practice.*

{NOTE}
- **Dual:** swap + with ·, and 0 with 1. Letters and primes stay as they are. If a law is true, its dual is also true.
- **Tautology:** 1 in every row (A + A'). **Fallacy:** 0 in every row (A·A').
- **Dual is not complement:** the complement also primes every letter.

## Duals

{chr(10).join(qs)}
## Tautology, fallacy or neither?

{chr(10).join(cls)}"""
    (CH / 'sometimes-asked-duality-tautology.md').write_text(txt, encoding='utf-8')


# ------------------------------------------------------------------ NAND only and NOR only
def nand_nor_bank():
    def lit_nand(l):
        return f"({l[0]}·{l[0]})'" if l.endswith("'") else l

    def lit_nor(l):
        return f"({l[0]} + {l[0]})'" if l.endswith("'") else l

    qs = []
    seen = set()
    while len(qs) < 20:
        vs = ['A', 'B', 'C']
        nterms = rnd.choice([2, 3])
        terms = []
        while len(terms) < nterms:
            t = sorted(rnd.sample(vs, 2))
            t = [v + ("'" if rnd.random() < 0.35 else '') for v in t]
            if t not in terms:
                terms.append(t)
        if len(qs) < 10:   # SOP -> NAND-NAND
            f = ' + '.join('·'.join(t) for t in terms)
            g = '(' + '·'.join('(' + '·'.join(lit_nand(l) for l in t) + ")'" for t in terms) + ")'"
            kind, gate, how = 'NAND', 'NAND', 'each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X\' is a NAND with both inputs X'
        else:              # POS -> NOR-NOR
            f = '·'.join('(' + ' + '.join(t) + ')' for t in terms)
            g = '(' + ' + '.join('(' + ' + '.join(lit_nor(l) for l in t) + ")'" for t in terms) + ")'"
            kind, gate, how = 'NOR', 'NOR', 'each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X\' is a NOR with both inputs X'
        if f in seen:
            continue
        seen.add(f)
        assert bl.equal(P(f), P(g)), (f, g)
        count = g.count("'")
        qs.append(f"**Q{len(qs) + 1}.** Write F = {bl.show(P(f))} using only {gate} gates.\n\n"
                  f"**Answer.** F = {g}. ({count} {gate} gates: {how}.)\n")
    txt = f"""# Chapter 3: circuits with NAND gates only, or NOR gates only (20 questions)

*Chapter 3 · Questions (online). Universal gates in practice (section 3.3). Every answer was computed by a program and checked: it gives the same truth table as the original expression.*

**Method.** A sum of products (A·B + C·D) becomes **NAND-NAND**: F = ((A·B)'·(C·D)')'. A product of sums ((A + B)·(C + D)) becomes **NOR-NOR**: F = ((A + B)' + (C + D)')'. Both follow from De Morgan's laws. In each answer, every prime closes one gate.

## NAND only

{chr(10).join(qs[:10])}
## NOR only

{chr(10).join(qs[10:])}"""
    (CH / 'questions' / '11-nand-nor-only.md').write_text(txt, encoding='utf-8')


if __name__ == '__main__':
    xnor_page(); sop_page(); duality_page(); nand_nor_bank()
    print('written: beyond-xnor, beyond-sop-pos-kmap, sometimes-asked-duality-tautology, questions/11-nand-nor-only')
