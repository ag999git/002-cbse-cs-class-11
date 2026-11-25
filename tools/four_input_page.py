"""Chapter 3 online page: gates with four inputs (AND, OR, NAND, NOR, XOR, XNOR), 26 Nov 2026.
Every table and answer is computed by boolean_lib.py; the symbols are drawn with Schemdraw.

Run from the repository root:  python tools/four_input_page.py"""
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import boolean_lib as bl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / 'book' / 'unit-1' / '003-ch03-boolean-logic' / 'beyond-four-input-gates.md'
IMG = ROOT / 'book' / 'assets' / 'circuits' / 'ch03'
V = ['A', 'B', 'C', 'D']
GATES = [  # name, expression in the book's notation, Schemdraw class
    ('AND', 'A·B·C·D', 'And'), ('OR', 'A + B + C + D', 'Or'),
    ('NAND', "(A·B·C·D)'", 'Nand'), ('NOR', "(A + B + C + D)'", 'Nor'),
    ('XOR', 'A ⊕ B ⊕ C ⊕ D', 'Xor'), ('XNOR', "(A ⊕ B ⊕ C ⊕ D)'", 'Xnor'),
]
P = {n: bl.parse(e) for n, e, _ in GATES}


def out(name, combo):
    return bl.ev(P[name], dict(zip(V, combo)))


def symbol(name, cls):
    import matplotlib
    matplotlib.use('Agg')
    import schemdraw
    from schemdraw import logic
    schemdraw.config(fontsize=13, lw=1.6)
    path = IMG / f'four-{name.lower()}.png'
    with schemdraw.Drawing(show=False) as d:
        g = getattr(logic, cls)(inputs=4)
        for k, v in enumerate(V, 1):
            logic.Line().at(getattr(g, f'in{k}')).left(0.6).label(v, 'left')
        logic.Line().at(g.out).right(0.6).label(f'Y = {bl.show(P[name])}', 'right')
        d.save(str(path), dpi=300)
    return f'![{name} gate with four inputs](../../assets/circuits/ch03/four-{name.lower()}.png){{ width="300" }}'


# ------------------------------------------------------------------ checks of every rule stated on the page
combos = list(itertools.product((0, 1), repeat=4))
ones = {c: sum(c) for c in combos}
assert [c for c in combos if out('AND', c)] == [(1, 1, 1, 1)]
assert [c for c in combos if not out('OR', c)] == [(0, 0, 0, 0)]
assert [c for c in combos if not out('NAND', c)] == [(1, 1, 1, 1)]
assert [c for c in combos if out('NOR', c)] == [(0, 0, 0, 0)]
assert all(out('XOR', c) == ones[c] % 2 for c in combos)
assert all(out('XNOR', c) == 1 - ones[c] % 2 for c in combos)
assert sum(out('XOR', c) for c in combos) == 8 and sum(out('XNOR', c) for c in combos) == 8
# building from 2-input gates
assert bl.equal(P['AND'], bl.parse('(A·B)·(C·D)')) and bl.equal(P['XOR'], bl.parse('(A ⊕ B) ⊕ (C ⊕ D)'))
assert bl.equal(P['NAND'], bl.parse("((A·B)·(C·D))'")) and not bl.equal(P['NAND'], bl.parse("((A·B)'·(C·D)')'"))
assert bl.equal(bl.parse("((A·B)'·(C·D)')'"), bl.parse('A·B + C·D'))
assert bl.equal(P['NOR'], bl.parse("A'·B'·C'·D'"))

# ------------------------------------------------------------------ the page
rows = ['| A B C D | 1s | AND | OR | NAND | NOR | XOR | XNOR |', '|' + ':-:|' * 8]
for c in combos:
    rows.append('| ' + ' '.join(map(str, c)) + f' | {ones[c]} | '
                + ' | '.join(str(out(n, c)) for n, _, _ in GATES) + ' |')
IMG.mkdir(parents=True, exist_ok=True)
pics = {n: symbol(n, cls) for n, _, cls in GATES}

practice = [
    ('A 4-input AND gate gets A = 1, B = 1, C = 0, D = 1. What is its output?', '**0**: one input is 0, and AND needs all four to be 1.', ('AND', (1, 1, 0, 1), 0)),
    ('A 4-input OR gate gets 0, 0, 1, 0. What is its output?', '**1**: one input is 1 is enough for OR.', ('OR', (0, 0, 1, 0), 1)),
    ('A 4-input NAND gate gets 1, 1, 1, 1. What is its output?', '**0**: the only row where NAND gives 0.', ('NAND', (1, 1, 1, 1), 0)),
    ('A 4-input NOR gate gets 0, 0, 0, 1. What is its output?', '**0**: NOR gives 1 only when all four inputs are 0.', ('NOR', (0, 0, 0, 1), 0)),
    ('A 4-input XOR gate gets 1, 1, 1, 0. What is its output?', '**1**: three 1s, an odd number.', ('XOR', (1, 1, 1, 0), 1)),
    ('A 4-input XOR gate gets 1, 1, 1, 1. What is its output?', '**0**: four 1s, an even number. *Trap:* not 1 because "all are 1".', ('XOR', (1, 1, 1, 1), 0)),
    ('A 4-input XNOR gate gets 1, 0, 0, 1. What is its output?', '**1**: two 1s, an even number.', ('XNOR', (1, 0, 0, 1), 1)),
    ('A 4-input XNOR gate gets 0, 0, 0, 0. What is its output?', '**1**: no 1s at all, and 0 counts as even.', ('XNOR', (0, 0, 0, 0), 1)),
    ('How many rows has the truth table of a 4-input gate? In how many of them does a 4-input XOR give 1?', '2⁴ = **16** rows; XOR gives 1 in **8** of them (exactly half: the rows with 1 or 3 ones).', None),
    ('How many 2-input AND gates make one 4-input AND gate? Write the expression.', '**3**: (A·B) and (C·D), then an AND of the two results: Y = (A·B)·(C·D).', None),
]
for _, _, chk in practice:
    if chk:
        n, c, want = chk
        assert out(n, c) == want, (n, c)

qs = '\n'.join(f'**Q{i}.** {q}\n\n**Answer.** {a}\n' for i, (q, a, _) in enumerate(practice, 1))
PAGE.write_text(f"""# Beyond syllabus: gates with four inputs

*Chapter 3 · Beyond syllabus. The printed book (section 3.5) shows gates with three inputs; this page goes one step further. Every table and answer here was computed by a program (`tools/four_input_page.py`) and checked row by row.*

## 1. The same rules, more inputs

A gate can have any number of inputs. Its rule stays the same; only the table grows. With four inputs A, B, C and D there are 2 × 2 × 2 × 2 = **2⁴ = 16** rows.

| Gate | Expression | Gives 1 when … | Rows with 1 (of 16) |
|---|:-:|---|:-:|
| AND | {bl.show(P['AND'])} | **all four** inputs are 1 | {sum(out('AND', c) for c in combos)} |
| OR | {bl.show(P['OR'])} | **at least one** input is 1 | {sum(out('OR', c) for c in combos)} |
| NAND | {bl.show(P['NAND'])} | **not all** inputs are 1 | {sum(out('NAND', c) for c in combos)} |
| NOR | {bl.show(P['NOR'])} | **all four** inputs are 0 | {sum(out('NOR', c) for c in combos)} |
| XOR | {bl.show(P['XOR'])} | an **odd** number of inputs are 1 | {sum(out('XOR', c) for c in combos)} |
| XNOR | {bl.show(P['XNOR'])} | an **even** number of inputs are 1 (0, 2 or 4) | {sum(out('XNOR', c) for c in combos)} |

*The trap:* a 4-input XOR is **not** "1 when the inputs differ". With 1, 1, 1, 1 all inputs are the same, but the count of 1s is 4 (even), so XOR gives 0. Always count the 1s.

## 2. The symbols

The shape does not change: the gate simply has four input lines.

| | | |
|:-:|:-:|:-:|
| {pics['AND']} | {pics['OR']} | {pics['XOR']} |
| {pics['NAND']} | {pics['NOR']} | {pics['XNOR']} |

## 3. The full truth table

Each row gives the four inputs A, B, C, D in order (0 1 0 1 means A = 0, B = 1, C = 0, D = 1). The column "1s" counts the inputs that are 1: it makes the XOR and XNOR columns easy to check.

{chr(10).join(rows)}

*Reading the table:* AND has one 1 (the last row); OR has one 0 (the first row); NAND and NOR are those two turned round; XOR and XNOR follow the "1s" column: odd gives XOR = 1, even gives XNOR = 1.

## 4. Building a 4-input gate from 2-input gates

- **AND, OR, XOR:** join the inputs in pairs, then join the two results: Y = (A·B)·(C·D), Y = (A + B) + (C + D), Y = (A ⊕ B) ⊕ (C ⊕ D). Three 2-input gates in each case.
- **NAND, NOR, XNOR:** build the AND, OR or XOR first, then put **one NOT at the very end**: Y = ((A·B)·(C·D))'.
- *Trap:* three 2-input NAND gates joined in pairs do **not** make a 4-input NAND. ((A·B)'·(C·D)')' works out to A·B + C·D (De Morgan), a different expression.

## 5. Practice

{qs}""", encoding='utf-8')
print('page written:', PAGE.name)
