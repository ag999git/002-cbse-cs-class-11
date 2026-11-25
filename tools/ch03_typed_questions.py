"""Chapter 3 online question pages 01-07 (by type of question): every question of the printed chapter (v7) plus new
ones, each with its answer below it. Every Boolean claim in an answer is checked here by boolean_lib.py before a page
is written (equal laws, truth-table outputs, complements, duals, values); circuits are drawn from their expressions.

Run from the repository root:  python tools/ch03_typed_questions.py"""
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import boolean_lib as bl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
QD = ROOT / 'book' / 'unit-1' / '003-ch03-boolean-logic' / 'questions'
IMG = ROOT / 'book' / 'assets' / 'circuits' / 'ch03'
P = bl.parse
checks = 0


# ------------------------------------------------------------------ checks
def same(a, b):
    global checks
    assert bl.equal(P(a), P(b)), f'not equal: {a} | {b}'
    checks += 1


def differ(a, b):
    global checks
    assert not bl.equal(P(a), P(b)), f'equal but claimed different: {a} | {b}'
    checks += 1


def outs(e, want, order=None):
    """Outputs in counting order must be `want` (a string such as '0110')."""
    global checks
    got = ''.join(str(v) for _, v in bl.rows(P(e), order))
    assert got == want, f'{e}: {got} != {want}'
    checks += 1


def val(e, env, want):
    global checks
    got = bl.ev(P(e), env)
    assert got == want, f'{e} at {env}: {got} != {want}'
    checks += 1


def const(e, want):
    outs(e, str(want) * (2 ** len(bl.names(P(e)))))


def dual_is(e, want):
    global checks
    assert bl.show(bl.dual(P(e))) == bl.show(P(want)), (bl.show(bl.dual(P(e))), want)
    checks += 1


def table(cols, inputs, heads=None):
    """Markdown truth table; every column computed."""
    heads = heads or cols
    lines = ['| ' + ' | '.join(inputs + heads) + ' |', '|' + ':-:|' * (len(inputs) + len(cols))]
    for combo in itertools.product((0, 1), repeat=len(inputs)):
        env = dict(zip(inputs, combo))
        lines.append('| ' + ' | '.join([str(c) for c in combo] + [str(bl.ev(P(c), env)) for c in cols]) + ' |')
    return '\n'.join(lines)


def gate_then_not(kind, name, width=330):
    """An AND or OR gate followed by a separate NOT gate (Schemdraw's parser would merge them into NAND/NOR)."""
    import matplotlib
    matplotlib.use('Agg')
    import schemdraw
    from schemdraw import logic
    IMG.mkdir(parents=True, exist_ok=True)
    schemdraw.config(fontsize=14, lw=1.6)
    with schemdraw.Drawing(show=False) as d:
        g = (logic.And if kind == 'AND' else logic.Or)()
        logic.Line().at(g.in1).left(0.6).label('A', 'left')
        logic.Line().at(g.in2).left(0.6).label('B', 'left')
        logic.Line().at(g.out).right(0.8)
        logic.Not()
        logic.Line().right(0.5).label('Y', 'right')
        d.save(str(IMG / f'typed-{name}.png'), dpi=300)
    return f'![A circuit to identify](../../../assets/circuits/ch03/typed-{name}.png){{ width="{width}" }}'


def circuit(expr, name, label='Y', reveal=True, width=420):
    """reveal=False: the drawing shows only the output name, not the expression (for 'which gate is this?')."""
    IMG.mkdir(parents=True, exist_ok=True)
    path = IMG / f'typed-{name}.png'
    bl.draw(P(expr), str(path), out_label=label, reveal=reveal)
    alt = f'Circuit for {label} = {bl.show(P(expr))}' if reveal else 'A circuit to identify'
    return f'![{alt}](../../../assets/circuits/ch03/typed-{name}.png){{ width="{width}" }}'


HEAD = ('*Chapter 3 · Questions (online). The questions of the printed chapter and many more, each followed by its '
        'answer and the reason. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the '
        'book are given in brackets. Every Boolean answer on this page was checked by a program '
        '(`tools/ch03_typed_questions.py`).*')


def write(fname, title, body):
    (QD / fname).write_text(f'# Chapter 3: Boolean Logic and Logic Circuits: {title}\n\n{HEAD}\n\n{body.strip()}\n',
                            encoding='utf-8')


def qblock(items, start=1, opts_break=True):
    out, n = [], start
    for q, a in items:
        sep = '\n\n' if a.startswith('|') else ' '      # a table must start on its own line
        out.append(f'**Q{n}.** {q}\n\n**Answer.**{sep}{a}\n')
        n += 1
    return '\n'.join(out), n


# ================================================================== 01 MCQ (40)
mcq = [
    ('3.2–3.3 The gates', [
        ('Which gate gives output 1 only when all its inputs are 1? *(E · 3.2)*  \n(a) OR (b) AND (c) NOR (d) XOR',
         '(b) AND. *How to answer:* write the letter **and** the name.'),
        ('The gate that gives 1 when its two inputs are the same: *(E · 3.4)*  \n(a) XOR (b) XNOR (c) NAND (d) OR',
         '(b) XNOR. *Why:* it is XOR turned round.'),
        ('Which gate gives 1 when all inputs are 0? *(E · 3.3)*  \n(a) AND (b) OR (c) NOR (d) XOR',
         '(c) NOR. *Why:* OR gives 0 then, and NOR turns it round.'),
        ('Which gate gives 0 only when all its inputs are 1? *(E · 3.3)*  \n(a) AND (b) OR (c) NAND (d) NOR',
         '(c) NAND. *Why:* AND gives 1 only then, and NAND turns it round.'),
        ('The output of a NOR gate when A = 0 and B = 1 is *(E · 3.3)*  \n(a) 0 (b) 1 (c) 01 (d) cannot be found',
         '(a) 0. *Why:* one input is 1, so OR gives 1 and NOR turns it to 0.'),
        ('NAND is *(E · 3.3)*  \n(a) NOT then AND (b) AND then NOT (c) OR then NOT (d) AND then OR',
         '(b). *Why:* the bubble is at the output.'),
        ('An OR symbol with a bubble at its output is the *(E · 3.3)*  \n(a) NAND gate (b) XNOR gate (c) NOR gate (d) NOT gate',
         '(c) NOR gate: Y = (A + B)\'.'),
        ('Which is the expression of the XOR gate? *(M · 3.4)*  \n(a) A·B + A\'·B\' (b) A\'·B + A·B\' (c) A + B (d) (A·B)\'',
         '(b). *Why:* each term is 1 in one of the two rows where A and B differ. (a) is XNOR.'),
        ('1 ⊕ 1 ⊕ 1 = ? *(M · 3.5)*  \n(a) 0 (b) 1 (c) 3 (d) 2',
         '(b) 1. *Why:* an odd number of 1s.'),
        ('Which is NOT a universal gate? *(E · 3.3)*  \n(a) NAND (b) NOR (c) XOR (d) none',
         '(c) XOR. *Why:* only NAND and NOR can build every gate.'),
        ('Joining both inputs of a NOR gate gives *(M · 3.3)*  \n(a) AND (b) OR (c) NOT (d) XOR',
         '(c) NOT. *Why:* (A + A)\' = A\' (idempotent law).'),
        ('How many NAND gates are needed to make an AND gate? *(M · 3.3)*  \n(a) 1 (b) 2 (c) 3 (d) 4',
         '(b) 2. *Why:* one NAND gives (A·B)\'; a second NAND with its inputs joined turns it round: ((A·B)\')\' = A·B.'),
        ('How many NOR gates are needed to make an OR gate? *(M · 3.3)*  \n(a) 1 (b) 2 (c) 3 (d) 4',
         '(b) 2. *Why:* one NOR gives (A + B)\'; a second NOR with joined inputs turns it round.'),
        ('Switches in parallel make *(E · 3.4)*  \n(a) AND (b) OR (c) NOT (d) XOR',
         '(b) OR. *Why:* one closed switch is enough.'),
        ('A staircase light that can be switched from either end works like the *(M · 3.4)*  \n(a) AND gate (b) OR gate (c) XOR gate (d) NAND gate',
         '(c) XOR gate. *Why:* flipping either switch changes the light (section 3.4).'),
        ('In a Venn diagram, shading only the overlap of circles A and B shows *(E · 3.2)*  \n(a) A + B (b) A·B (c) A\' (d) A ⊕ B',
         '(b) A·B (AND): only the part that is in both.'),
    ]),
    ('3.1 and 3.5 Truth tables', [
        ('How many rows has the truth table of a 4-input AND gate? *(E · 3.1)*  \n(a) 4 (b) 8 (c) 16 (d) 32',
         '(c) 16. *Why:* 2⁴.'),
        ('How many rows has the truth table of an expression in A, B and C? *(E · 3.1)*  \n(a) 3 (b) 6 (c) 8 (d) 9',
         '(c) 8. *Why:* 2³; each input doubles the rows. *Trap:* not 2 × 3 = 6.'),
        ('In a truth table of A, B, C written in counting order, the 6th row is *(M · 3.1)*  \n(a) 1 0 1 (b) 1 1 0 (c) 1 0 0 (d) 0 1 1',
         '(a) 1 0 1. *Why:* the rows count 0 to 7, so the 6th row is 5 = 101 in binary.'),
        ('The value of Y = (A + B)\'·C when A = 0, B = 0, C = 1 is *(M · 3.5)*  \n(a) 0 (b) 1 (c) 2 (d) C\'',
         '(b) 1. *Why:* A + B = 0, so (A + B)\' = 1, and 1·1 = 1.'),
    ]),
    ('3.6–3.7 Laws, De Morgan, duality', [
        ('A + 1 = ? *(E · 3.7)*  \n(a) A (b) 1 (c) 0 (d) A\'', '(b) 1. *Why:* null law: one 1 is enough for OR.'),
        ('A · 0 = ? *(E · 3.7)*  \n(a) A (b) 1 (c) 0 (d) A\'', '(c) 0. *Why:* null law: one 0 keeps AND at 0.'),
        ('A · 1 = ? *(E · 3.7)*  \n(a) 0 (b) 1 (c) A (d) A\'', '(c) A. *Why:* identity law: a 1 does not change an AND.'),
        ('A + A = ? *(E · 3.7)*  \n(a) 2A (b) A (c) 1 (d) 0', '(b) A. *Why:* idempotent law; there is no "2" in Boolean algebra.'),
        ('A · A\' = ? *(E · 3.7)*  \n(a) 1 (b) A (c) 0 (d) A\'', '(c) 0. *Why:* complement law: A and A\' are never both 1.'),
        ('(A\')\' = ? *(E · 3.7)*  \n(a) A\' (b) A (c) 1 (d) 0', '(b) A. *Why:* involution: *ulta* of *ulta* is *seedha*.'),
        ('The law A·B = B·A is the *(E · 3.7)*  \n(a) associative law (b) commutative law (c) distributive law (d) absorption law',
         '(b) commutative law: only the order changes.'),
        ('The law A·(B + C) = A·B + A·C is the *(E · 3.7)*  \n(a) distributive law (b) associative law (c) idempotent law (d) involution law',
         '(a) distributive law.'),
        ('A + A·B = ? *(E · 3.7)*  \n(a) A·B (b) B (c) A (d) 1', '(c) A. *Why:* absorption: if A = 1 the answer is 1; if A = 0 both terms are 0.'),
        ('A + A\'·B = ? *(M · 3.7)*  \n(a) A (b) B (c) A + B (d) A·B', '(c) A + B. *Why:* the redundant-literal law.'),
        ('(P · Q)\' is equal to *(E · 3.6)*  \n(a) P\' · Q\' (b) P\' + Q\' (c) P + Q (d) (P + Q)\'',
         '(b) P\' + Q\'. *Why:* De Morgan\'s second law: open the bracket, flip the sign, prime each letter. *Trap:* (a) forgets to flip the sign.'),
        ('The complement of A·B is *(E · 3.6)*  \n(a) A\'·B\' (b) A\' + B\' (c) A + B (d) (A + B)\'', '(b) A\' + B\'. *Why:* De Morgan\'s second law.'),
        ('The complement of A + B\' is *(M · 3.6)*  \n(a) A\'·B (b) A\' + B (c) A·B\' (d) A\'·B\'',
         '(a) A\'·B. *Why:* first law: (A + B\')\' = A\'·(B\')\' = A\'·B.'),
        ('Bubble pushing shows that a NOR gate is the same as *(H · 3.6)*  \n(a) an AND gate with bubbles on its inputs (b) an OR gate with bubbles on its inputs (c) a NAND gate (d) an AND gate',
         '(a). *Why:* (A + B)\' = A\'·B\' (De Morgan\'s first law): the NOTs move to the inputs and OR becomes AND.'),
        ('The dual of A + 0 = A is *(E · 3.7)*  \n(a) A·1 = A (b) A·0 = 0 (c) A + 1 = 1 (d) A\' + 1 = A\'',
         '(a). *Why:* swap + with · and 0 with 1.'),
        ('The dual of A·(B + C) is *(M · 3.7)*  \n(a) A + B·C (b) A\'·(B\' + C\') (c) A·B + C (d) (A + B)·C',
         '(a) A + B·C. *Why:* swap · and +; letters keep their primes. (b) is a complement, not a dual.'),
        ('A + A\' is a *(E · 3.7)*  \n(a) fallacy (b) tautology (c) dual (d) complement', '(b) tautology. *Why:* it is 1 in every row.'),
        ('Which expression is a fallacy? *(E · 3.7)*  \n(a) A + A\' (b) A·A\' (c) A + 1 (d) A·1', '(b) A·A\'. *Why:* it is 0 in every row.'),
    ]),
    ('3.8 Circuits and history', [
        ('The order in which an expression is worked out is *(E · 3.8)*  \n(a) AND, OR, NOT, brackets (b) brackets, NOT, AND, OR (c) OR, AND, NOT, brackets (d) left to right only',
         '(b): B-N-A-O.'),
        ('Boolean algebra was developed by *(E · 3.1)*  \n(a) Claude Shannon (b) George Boole (c) Charles Babbage (d) Alan Turing',
         '(b) George Boole, an English mathematician, in 1854. Claude Shannon later (1938) used it for switch circuits.'),
    ]),
]
same("A + 1", "1"); same("A·0", "0"); same("A·1", "A"); same("A + A", "A"); const("A·A'", 0); same("(A')'", "A")
same("A + A·B", "A"); same("A + A'·B", "A + B"); same("(P·Q)'", "P' + Q'"); differ("(P·Q)'", "P'·Q'")
same("(A + B')'", "A'·B"); same("(A + B)'", "A'·B'"); same("A'·B + A·B'", "A ⊕ B"); differ("A·B + A'·B'", "A ⊕ B")
val("A ⊕ B ⊕ C", {'A': 1, 'B': 1, 'C': 1}, 1); val("(A + B)'", {'A': 0, 'B': 1}, 0); val("(A + B)'·C", {'A': 0, 'B': 0, 'C': 1}, 1)
dual_is("A + 0", "A·1"); dual_is("A·(B + C)", "A + B·C"); const("A + A'", 1); same("((A·B)')'", "A·B")
assert sum(len(x[1]) for x in mcq) == 40

body, n = [], 1
for head, items in mcq:
    b, n = qblock(items, n)
    body.append(f'## {head}\n\n{b}')
write('01-mcq.md', 'Multiple-choice questions (40)', '\n'.join(body))

# ================================================================== 02 fill in (25)
fill = [
    ('The operation done by a NOT gate is called ______. *(E · 3.2)*', 'complementation (inversion).'),
    ('The NOT gate is also called an ______. *(E · 3.2)*', 'inverter.'),
    ('An OR gate gives 0 only when all its inputs are ______. *(E · 3.2)*', '0.'),
    ('An AND gate gives 1 only when all its inputs are ______. *(E · 3.2)*', '1.'),
    ('A NOR gate is an OR gate followed by a ______ gate. *(E · 3.3)*', 'NOT.'),
    ('The two universal gates are ______ and ______. *(E · 3.3)*', 'NAND and NOR.'),
    ('The XOR gate is also called the ______ OR gate. *(E · 3.4)*', 'exclusive.'),
    ('The XOR gate gives 1 when an ______ number of inputs are 1. *(M · 3.5)*', 'odd.'),
    ('A 2-input XNOR gate gives 1 when its inputs are ______. *(E · 3.4)*', 'the same (both 0 or both 1).'),
    ('Switches joined one after the other are in ______, and they make an ______ gate. *(E · 3.4)*', 'series; AND.'),
    ('A truth table of n inputs has ______ rows. *(E · 3.1)*', '2ⁿ.'),
    ('A truth table with 5 inputs has ______ rows. *(E · 3.1)*', '32 (2⁵).'),
    ('The inputs of a 3-input truth table run from 000 to ______. *(E · 3.1)*', '111 (0 to 7 in binary).'),
    ('In Boolean algebra, + stands for ______ and · stands for ______. *(E · 3.1)*', 'OR; AND.'),
    ('A · A = ______ (idempotent law). *(E · 3.7)*', 'A.'),
    ('A · 0 = ______ (null law). *(E · 3.7)*', '0.'),
    ('A + 0 = ______ (identity law). *(E · 3.7)*', 'A.'),
    ('A + A·B = ______ (absorption law). *(E · 3.7)*', 'A.'),
    ('A + A\'·B = ______. *(M · 3.7)*', 'A + B (redundant-literal law).'),
    ('De Morgan\'s first law: (A + B)\' = ______. *(E · 3.6)*', 'A\' · B\'.'),
    ('De Morgan\'s second law: (A · B)\' = ______. *(E · 3.6)*', 'A\' + B\'.'),
    ('The dual of A + 0 = A is ______. *(E · 3.7)*', 'A · 1 = A.'),
    ('An expression that is 1 for every combination of inputs is a ______. *(E · 3.7)*', 'tautology.'),
    ('An expression that is 0 in every row is a ______. *(E · 3.7)*', 'fallacy.'),
    ('In 1938 ______ applied Boolean algebra to switching circuits. *(E · 3.4)*', 'Claude Shannon.'),
]
same("A·A", "A"); same("A + 0", "A"); same("A·B + A'·B'", "(A ⊕ B)'")
assert len(fill) == 25
write('02-fill-in.md', 'Fill in the blanks (25)', qblock(fill)[0])

# ================================================================== 03 true or false (25)
tf = [
    ('A NOT gate can have two inputs. *(E · 3.2)*', 'False. *Why:* it has exactly one.'),
    ('An OR gate gives 1 when both its inputs are 1. *(E · 3.2)*', 'True. *Why:* at least one input is 1.'),
    ('An OR gate gives 0 in only one row of its truth table. *(E · 3.2)*', 'True. *Why:* only when all inputs are 0.'),
    ('An XOR gate gives 1 when both its inputs are 1. *(E · 3.4)*', 'False. *Why:* XOR gives 0 when the inputs are the same; "exclusive" excludes the both-1 row.'),
    ('XNOR is XOR followed by NOT. *(E · 3.4)*', 'True.'),
    ('A 2-input NOR gate gives 1 in only one row of its truth table. *(E · 3.3)*', 'True. *Why:* only when both inputs are 0.'),
    ('Every other gate can be built from NAND gates alone. *(E · 3.3)*', 'True. *Why:* NAND is a universal gate.'),
    ('Two push-to-break switches in series make a NOR gate. *(M · 3.4)*', 'True. *Why:* the bulb lights only when neither is pressed.'),
    ('Two switches in parallel make an AND gate. *(E · 3.4)*', 'False. *Why:* in parallel one closed switch is enough: that is OR.'),
    ('The truth table of a NOT gate has two rows. *(E · 3.1)*', 'True. *Why:* one input: 2¹ = 2 rows.'),
    ('"Shut the door" is a logical statement. *(E · 3.1)*', 'False. *Why:* an order is neither true nor false.'),
    ('In Boolean algebra 1 + 1 = 10. *(E · 3.1)*', 'False. *Why:* + is OR, so 1 + 1 = 1. 1 + 1 = 10 is binary addition (Chapter 4).'),
    ('A · A = A². *(E · 3.7)*', 'False. *Why:* A · A = A (idempotent law); Boolean algebra has no powers.'),
    ('A · A\' = 1. *(E · 3.7)*', 'False. *Why:* A and A\' are never both 1: A·A\' = 0.'),
    ('A · (A + B) = A. *(M · 3.7)*', 'True. *Why:* absorption law (the dual of A + A·B = A).'),
    ('A·B + A·B\' = A. *(M · 3.7)*', 'True. *Why:* A·(B + B\') = A·1 = A.'),
    ('A + B·C = (A + B)·C. *(M · 3.7)*', 'False. *Why:* AND comes first, so A + B·C = A + (B·C). With A = 1, B = 0, C = 0 the left side is 1 and the right side is 0.'),
    ('(A + B)\' = A\'·B\'. *(E · 3.6)*', 'True. *Why:* De Morgan\'s first law.'),
    ('(A · B)\' = A\' · B\'. *(E · 3.6)*', 'False. *Why:* the sign must flip: (A · B)\' = A\' + B\'. With A = 1, B = 0 the left side is 1 and A\'·B\' is 0.'),
    ('The dual of an expression is the same as its complement. *(M · 3.7)*', 'False. *Why:* the dual does not prime the letters.'),
    ('The dual is found by swapping + with · and 0 with 1, without priming the letters. *(E · 3.7)*', 'True.'),
    ('If a Boolean law is true, its dual is also true. *(E · 3.7)*', 'True. *Why:* the principle of duality.'),
    ('A tautology is 0 in every row. *(E · 3.7)*', 'False. *Why:* a tautology is 1 in every row; 0 in every row is a fallacy.'),
    ('XNOR is the complement of XOR. *(E · 3.4)*', 'True. *Why:* XNOR = (A ⊕ B)\'.'),
    ('NOT has the highest priority among NOT, AND and OR. *(E · 3.8)*', 'True. *Why:* the order is brackets, NOT, AND, OR.'),
]
same("A·(A + B)", "A"); same("A·B + A·B'", "A"); differ("A + B·C", "(A + B)·C")
val("A + B·C", {'A': 1, 'B': 0, 'C': 0}, 1); val("(A + B)·C", {'A': 1, 'B': 0, 'C': 0}, 0)
differ("(A·B)'", "A'·B'"); val("(A·B)'", {'A': 1, 'B': 0}, 1); val("A'·B'", {'A': 1, 'B': 0}, 0); outs("(A + B)'", '1000')
assert len(tf) == 25
write('03-true-false.md', 'True or false (25)', qblock(tf)[0])

# ================================================================== 04 assertion and reason (15)
ar = [
    ('A: An OR gate gives 1 when A = 1 and B = 1. R: An OR gate gives 1 when at least one input is 1. *(E · 3.2)*',
     '(a). *Why:* R is the rule of OR, and it covers the case in A.'),
    ('A: NAND is a universal gate. R: NAND gives 0 only when all inputs are 1. *(M · 3.3)*',
     '(b). *Why:* both are true, but R only describes NAND; it does not say why every gate can be built from it.'),
    ('A: NOR is a universal gate. R: The output of a NOR gate is 1 only when all inputs are 0. *(M · 3.3)*',
     '(b). *Why:* both true, but R is only NOR\'s truth table, not the reason it can build every gate. *Exam tip:* ask "does R tell **why** A is true?"'),
    ('A: A NAND gate gives 1 when A = 0 and B = 0. R: NAND is an AND gate followed by NOT. *(E · 3.3)*',
     '(a). *Why:* AND gives 0, and the NOT turns it into 1: R explains A.'),
    ('A: XOR is a universal gate. R: XOR gives 1 when its inputs differ. *(M · 3.4)*',
     '(d). *Why:* A is false (only NAND and NOR are universal); R is true.'),
    ('A: A NOT gate has one input. R: NOT is the only universal gate. *(E · 3.3)*',
     '(c). *Why:* A is true; R is false (NAND and NOR are the universal gates).'),
    ('A: A truth table with 3 inputs has 8 rows. R: Each input doubles the number of rows. *(E · 3.1)*',
     '(a). *Why:* 2 × 2 × 2 = 8: R is the reason.'),
    ('A: A · A\' = 0. R: A and A\' can never both be 1. *(E · 3.7)*', '(a). *Why:* AND needs both to be 1.'),
    ('A: A + A\' is a tautology. R: A and A\' are opposites, so one of them is always 1. *(E · 3.7)*',
     '(a). *Why:* R is exactly why the OR is always 1.'),
    ('A: An expression that is always 1 is a fallacy. R: A + A\' is always 1. *(E · 3.7)*',
     '(d). *Why:* A is false (that is a tautology); R is true.'),
    ('A: The dual of A + A\' = 1 is A · A\' = 0. R: Duality swaps + with · and 1 with 0. *(E · 3.7)*',
     '(a). *Why:* R is the rule that gives A.'),
    ('A: The complement of A + B is A\' + B\'. R: De Morgan\'s law changes + into ·. *(M · 3.6)*',
     '(d). *Why:* A is false (it is A\'·B\'); R is true.'),
    ('A: (A + B)\' = A\' · B\'. R: A prime over a bracket primes each letter but keeps the sign. *(M · 3.6)*',
     '(c). *Why:* A is true (first law); R is false: the sign flips too.'),
    ('A: Bubble pushing turns a NAND gate into an OR gate with NOT on its inputs. R: (A·B)\' = A\' + B\'. *(H · 3.6)*',
     '(a). *Why:* the picture is De Morgan\'s second law.'),
    ('A: A + B·C and (A + B)·C are different expressions. R: AND is worked out before OR. *(M · 3.8)*',
     '(a). *Why:* because AND comes first, A + B·C means A + (B·C), which differs from (A + B)·C.'),
]
same("A + A'", "1"); dual_is("A + A'", "A·A'"); same("(A·B)'", "A' + B'"); differ("(A + B)'", "A' + B'")
outs("(A·B)'", '1110')
assert len(ar) == 15
write('04-assertion-reason.md', 'Assertion and reason (15)',
      'For each question choose: (a) both A and R are true, and R explains A; (b) both are true, but R does not '
      'explain A; (c) A is true, R is false; (d) A is false, R is true.\n\n' + qblock(ar)[0])

# ================================================================== 05 short answer (25)
nand_tab = table(["(A·B)'"], ['A', 'B'], ["Y = (A·B)'"])
outs("(A·B)'", '1110')
short = [
    ('1 mark', [
        ('Which gate has only one input? *(E · 3.2)* *[1 mark]*',
         'The NOT gate (inverter). *Why:* "the opposite" is the opposite of one value; every other gate combines two or more inputs.'),
        ('A door alarm must ring when either the front door or the back door is open (open = 1). Which gate is needed? *(M · 3.2)* *[1 mark]*',
         'The OR gate. *Why:* one open door is enough. *Exam tip:* the word "either" usually points to OR.'),
        ('A circuit must give 1 only when its two inputs are different. Which gate? *(E · 3.4)* *[1 mark]*',
         'The XOR gate, the "difference detector".'),
        ('How many rows does the truth table of an expression with 4 variables have? *(E · 3.1)* *[1 mark]*',
         '2⁴ = 16 rows. *Trap:* not 4 × 2 = 8.'),
        ('Which law does A + (B + C) = (A + B) + C show? *(E · 3.7)* *[1 mark]*',
         'The associative law. *Why:* only the grouping changes. If the order changed (A + B = B + A), it would be the commutative law.'),
        ('State the principle of duality. *(E · 3.7)* *[1 mark]*',
         'If a Boolean law is true, the law made by swapping + with · and 0 with 1 (keeping every letter and prime) is also true.'),
        ('A 3-input XOR gate gets A = 1, B = 0, C = 1. What is its output? Explain. *(M · 3.5)* *[1 mark]*',
         '0. *Why:* two inputs are 1, an even number. (1 ⊕ 0 = 1, then 1 ⊕ 1 = 0.)'),
    ]),
    ('2 marks', [
        ('What is a logic gate? Name the three basic gates. *(E · 3.1)* *[2 marks]*',
         'A logic gate is a tiny circuit that turns one or more inputs (each 0 or 1) into one output by a fixed rule. The basic gates are NOT, AND and OR.'),
        ('Why are NAND and NOR called universal gates? Show how NAND makes a NOT gate. *(M · 3.3)* *[2 marks]*',
         'Because any other gate (NOT, AND, OR, and so any circuit) can be built using only NAND gates, or only NOR gates. '
         'NOT from NAND: join both inputs and feed A into them: Y = (A · A)\' = A\'. *Why it works:* A · A = A (idempotent law). '
         '*Exam tip:* draw a NAND with its two inputs joined.'),
        ('Write the truth table of a 2-input NAND gate and give its expression. *(E · 3.3)* *[2 marks]*',
         'Y = (A·B)\'.\n\n' + nand_tab + '\n\n*Why:* the AND column turned round: 0 only in the last row.'),
        ('Complete and name each law: (i) A + A = ___ (ii) A · A\' = ___ (iii) (A\')\' = ___ (iv) A + A·B = ___ *(E · 3.7)* *[2 marks]*',
         '(i) A, idempotent (ii) 0, complement (iii) A, involution (iv) A, absorption. *Exam tip:* half a mark for the value, half for the name.'),
        ('Find the complement of F = A·B\' + C·D using De Morgan\'s laws. *(M · 3.6)* *[2 marks]*',
         'F\' = (A·B\' + C·D)\' = (A·B\')\'·(C·D)\' = **(A\' + B)·(C\' + D\')**. *Why:* De Morgan on the +, then on each ·; (B\')\' = B. *Exam tip:* keep the brackets in the last line.'),
        ('Find the complement of F = (A + B)·(C + D\'). *(M · 3.6)* *[2 marks]*',
         'F\' = ((A + B)·(C + D\'))\' = (A + B)\' + (C + D\')\' = **A\'·B\' + C\'·D**. *Why:* the · between the brackets becomes +, and each bracket is opened with the first law.'),
        ('Write the dual of: (i) A + A·B = A (ii) (A + B)·(A + C) = A + B·C. *(E · 3.7)* *[2 marks]*',
         '(i) A·(A + B) = A (ii) A·B + A·C = A·(B + C). *Why:* swap + and ·; letters and primes stay.'),
        ('Define tautology and fallacy, with one example of each. *(E · 3.7)* *[2 marks]*',
         'A tautology is 1 for every combination of inputs, e.g. A + A\'. A fallacy is 0 for every combination, e.g. A·A\'. *Exam tip:* "every combination" is the key phrase.'),
        ('Prove algebraically that A + A\'·B = A + B. *(M · 3.7)* *[2 marks]*',
         'A + A\'·B = (A + A\')·(A + B) (distributive) = 1·(A + B) (complement) = A + B (identity). *Exam tip:* name the law at every step.'),
        ('Make the truth table of Y = A\'·B + A·B\' and say which single gate it is. *(M · 3.5)* *[2 marks]*',
         'Outputs for A, B = 00, 01, 10, 11: **0, 1, 1, 0**. It is the **XOR** gate: Y is 1 exactly when A and B differ.'),
        ('Show how to make an AND gate using only NOR gates. *(M · 3.3)* *[2 marks]*',
         'Feed A into a NOR with both inputs joined (gives A\'), and B the same way (gives B\'); feed A\' and B\' into a third NOR: (A\' + B\')\' = A·B (De Morgan). Three NOR gates in all.'),
        ('Write the XNOR truth table for two inputs, and its expression. *(E · 3.4)* *[2 marks]*',
         'Outputs for 00, 01, 10, 11: **1, 0, 0, 1**. Y = (A ⊕ B)\' = A·B + A\'·B\'. *Why:* 1 when the inputs are the same.'),
        ('How many NAND gates are needed to make an OR gate? Show the circuit in words. *(M · 3.3)* *[2 marks]*',
         'Three: two NANDs with joined inputs make A\' and B\'; a third NAND gives (A\'·B\')\' = A + B.'),
        ('Draw the Venn diagrams of A + B and A·B, and say which one shows an OR gate. *(E · 3.2)* *[2 marks]*',
         'A + B: both circles fully shaded; A·B: only the overlap shaded (section 3.2). The first, A + B, is OR.'),
        ('Why are there 2ⁿ rows in the truth table of n inputs? *(M · 3.1)* *[2 marks]*',
         'Each input can be 0 or 1. The first input gives 2 rows; every new input can be 0 or 1 in each of those rows, so it doubles them: 2 × 2 × … × 2 (n times) = 2ⁿ.'),
    ]),
    ('Drawing circuits (2 and 3 marks)', [
        ('Draw the logic circuit for Y = A\'·B + A·C. *(M · 3.8)* *[2 marks]*',
         'A NOT gate for A\'; an AND gate for A\'·B; an AND gate for A·C; an OR gate joining the two AND outputs.\n\n'
         + circuit("A'·B + A·C", 'ec-draw') + '\n\n*How to answer:* inputs on the left, output on the right, label every line.'),
        ('Draw the logic circuit for F = (P + Q)\' · R. *(M · 3.8)* *[2 marks]*',
         'P and Q go into a NOR gate (or an OR gate followed by NOT), giving (P + Q)\'; that output and R go into an AND gate.\n\n'
         + circuit("(P + Q)'·R", 'q10', 'F') + '\n\n*Exam tip:* label the output of every gate, not only F.'),
        ('Explain the order of operations in a Boolean expression, with an example. *(E · 3.8)* *[2 marks]*',
         'Brackets first, then NOT, then AND, then OR (B-N-A-O). Example: in A + B·C\', first C\', then B·C\', then the OR with A.'),
    ]),
    ('Which gate is this circuit? (1 mark)', [
        ('Which single gate does this circuit behave like? Give its name and expression. *(M · 3.3)* *[1 mark]*\n\n'
         + gate_then_not('AND', 'which-nand'),
         'A **NAND** gate: Y = (A·B)\'. *Why:* the AND gives A·B and the NOT turns it round; "AND, then NOT" is exactly NAND. '
         '*Check:* its outputs for 00, 01, 10, 11 are 1, 1, 1, 0.'),
        ('Which single gate does this circuit behave like? Give its name and expression. *(M · 3.3)* *[1 mark]*\n\n'
         + gate_then_not('OR', 'which-nor'),
         'A **NOR** gate: Y = (A + B)\'. *Why:* "OR, then NOT" is NOR. *Check:* its outputs for 00, 01, 10, 11 are 1, 0, 0, 0.'),
    ]),
]
outs("(A·B)'", '1110'); outs("(A + B)'", '1000')
for e, w in [("A + A", "A"), ("A·A'", "0"), ("(A')'", "A"), ("A + A·B", "A"), ("A + (B + C)", "(A + B) + C")]:
    same(e, w)
same("(A·B' + C·D)'", "(A' + B)·(C' + D')"); same("((A + B)·(C + D'))'", "A'·B' + C'·D")
dual_is("A + A·B", "A·(A + B)"); dual_is("(A + B)·(A + C)", "A·B + A·C"); dual_is("A + B·C", "A·(B + C)")
same("A + A'·B", "A + B"); outs("A'·B + A·B'", '0110'); same("(A' + B')'", "A·B"); outs("(A ⊕ B)'", '1001')
same("(A ⊕ B)'", "A·B + A'·B'"); same("(A'·B')'", "A + B"); same("(A·A)'", "A'"); val("A ⊕ B ⊕ C", {'A': 1, 'B': 0, 'C': 1}, 0)
assert sum(len(x[1]) for x in short) == 27
body, n = [], 1
for head, items in short:
    b, n = qblock(items, n)
    body.append(f'## {head}\n\n{b}')
write('05-short-answer.md', 'Short-answer questions (27)', '\n'.join(body))

# ================================================================== 06 long answer (10)
long_q = [
    ('Draw the symbols of the AND, OR and NOT gates and write the truth table of each. *(E · 3.2)* *[3 marks]*',
     'Symbols: AND is a D shape (flat back, round front); OR is a shield (curved back, pointed front); NOT is a triangle with a bubble at its tip (figures of section 3.2).\n\n'
     + table(["A'"], ['A'], ["NOT: A'"]) + '\n\n' + table(["A·B", "A + B"], ['A', 'B'], ["AND: A·B", "OR: A + B"])
     + '\n\n*Exam tip:* NOT has one input, so it gets its own two-row table.'),
    ('Explain the XOR gate with its symbol, expression and truth table for two inputs. *(M · 3.4)* *[3 marks]*',
     'The XOR (exclusive OR) gate gives 1 when its two inputs are **different** and 0 when they are the same. Expression: Y = A ⊕ B = A\'·B + A·B\'. '
     'Symbol: the OR shape with an extra curved line at the input side.\n\n' + table(["A ⊕ B"], ['A', 'B'], ["Y = A ⊕ B"])
     + '\n\n*Why "exclusive":* it excludes the row where both inputs are 1, which ordinary OR includes.'),
    ('State De Morgan\'s first law and prove it using a truth table. *(M · 3.6)* *[3 marks]*',
     'First law: **(A + B)\' = A\' · B\'**.\n\n'
     + table(["A + B", "(A + B)'", "A'", "B'", "A'·B'"], ['A', 'B'])
     + '\n\nThe columns (A + B)\' and A\'·B\' are identical in all rows; hence proved. *How to answer:* formula + table + one closing line. Never only the name.'),
    ('State De Morgan\'s second law and prove it with a truth table. *(M · 3.6)* *[3 marks]*',
     'Second law: **(A · B)\' = A\' + B\'**.\n\n'
     + table(["A·B", "(A·B)'", "A'", "B'", "A' + B'"], ['A', 'B'])
     + '\n\nThe columns (A·B)\' and A\' + B\' are identical in all four rows; hence proved. *Exam tip:* some examiners number the laws the other way, so the formula protects your marks.'),
    ('Make the truth table of Y = (A + B)\' · C. *(M · 3.5)* *[3 marks]*',
     'Three inputs, so 2³ = 8 rows. Steps, inside out: A + B, then (A + B)\', then Y.\n\n'
     + table(["A + B", "(A + B)'", "(A + B)'·C"], ['A', 'B', 'C'], ["A + B", "(A + B)'", "Y = (A + B)'·C"])
     + '\n\n*Why only one 1:* Y needs A = 0, B = 0 **and** C = 1. *Exam tip:* a column for each step earns the method marks.'),
    ('Name the law X + Y·Z = (X + Y)·(X + Z) and verify it with a truth table. *(M · 3.7)* *[3 marks]*',
     'The distributive law (second form: OR over AND).\n\n'
     + table(["Y·Z", "X + Y·Z", "X + Y", "X + Z", "(X + Y)·(X + Z)"], ['X', 'Y', 'Z'])
     + '\n\nThe columns X + Y·Z and (X + Y)·(X + Z) are identical in all eight rows; hence verified. *Why it surprises:* ordinary arithmetic has no such rule (1 + 2 × 3 = 7, but (1 + 2) × (1 + 3) = 12).'),
    ('Simplify: (i) A·B + A·B\' (ii) A·(A + B) (iii) (A + B)\'·A. *(M · 3.7)* *[3 marks]*',
     '(i) A·(B + B\') = A·1 = **A**. (ii) **A** (absorption). (iii) A\'·B\'·A = (A·A\')·B\' = 0·B\' = **0**. *Why (iii):* A and A\' cannot both be 1.'),
    ('Draw the circuit for Y = (A + B)·(A\' + C). *(M · 3.8)* *[3 marks]*',
     'One NOT gate for A\'; one OR gate for A + B; one OR gate for A\' + C; one AND gate joining the two OR outputs.\n\n'
     + circuit("(A + B)·(A' + C)", 'q25') + '\n\n*Exam tip:* in a product of sums the OR gates come first and the AND is last.'),
    ('Draw the logic circuit for F = A\'·B\'·C + A·B. *(M · 3.8)* *[3 marks]*',
     'NOT gates for A\' and B\'; a 3-input AND for A\'·B\'·C; a 2-input AND for A·B; an OR gate joining the two AND outputs.\n\n'
     + circuit("A'·B'·C + A·B", 'q26', 'F') + '\n\n*Exam tip:* a 3-input AND is allowed; or use two 2-input ANDs one after the other.'),
    ('Verify using a truth table that A·B + A\'·C + B·C = A·B + A\'·C (consensus). Then complement X·Y + X\'·Z and check your answer for X = 1, Y = 1, Z = 0. *(H · 3.6–3.7)* *[4 marks]*',
     table(["A·B + A'·C + B·C", "A·B + A'·C"], ['A', 'B', 'C'])
     + '\n\nThe two columns are equal in all eight rows. *Why the B·C term adds nothing:* when B·C = 1, either A = 1 (then A·B = 1) or A = 0 (then A\'·C = 1).\n\n'
     'Complement: (X·Y + X\'·Z)\' = (X·Y)\'·(X\'·Z)\' = **(X\' + Y\')·(X + Z\')**. Check: original 1·1 + 0·0 = 1; complement (0 + 0)·(1 + 1) = 0. Opposite, as it must be.'),
]
same("(A + B)'", "A'·B'"); same("(A·B)'", "A' + B'"); outs("(A + B)'·C", '01000000')
same("X + Y·Z", "(X + Y)·(X + Z)"); same("A·B + A·B'", "A"); same("A·(A + B)", "A"); const("(A + B)'·A", 0)
same("A·B + A'·C + B·C", "A·B + A'·C"); same("(X·Y + X'·Z)'", "(X' + Y')·(X + Z')")
val("X·Y + X'·Z", {'X': 1, 'Y': 1, 'Z': 0}, 1); val("(X' + Y')·(X + Z')", {'X': 1, 'Y': 1, 'Z': 0}, 0)
assert len(long_q) == 10
write('06-long-answer.md', 'Long-answer questions (10)', qblock(long_q)[0])

# ================================================================== 07 case studies (6 cases, 26 questions)
cases = [
    ('Case 1: A circuit in three stages',
     'A circuit has three stages: stage 1 = A AND B; stage 2 = NOT C; stage 3 = stage 1 NOR stage 2.',
     [('Output of stage 1 when A = 1, B = 1? *[1 mark]*', '1.'),
      ('Output of stage 2 when C = 0? *[1 mark]*', '1.'),
      ('Write the final expression. *[1 mark]*', 'Y = (A·B + C\')\'.'),
      ('Final output when A = 1, B = 1, C = 0? *[1 mark]*', '(1 + 1)\' = 1\' = **0**.'),
      ('How many rows has its truth table? *[1 mark]*', '2³ = 8.')]),
    ('Case 2: AND, NOT and NOR',
     'In a circuit, A and B go into an AND gate; C goes into a NOT gate; the two outputs go into a NOR gate whose output is Y.',
     [('Write the expression for Y. *[1 mark]*', 'Y = (A·B + C\')\'.'),
      ('Simplify it using De Morgan\'s laws. *[1 mark]*',
       'First law: Y = (A·B)\' · (C\')\' = (A·B)\' · C. Second law on (A·B)\': **Y = (A\' + B\') · C**.'),
      ('Find Y when A = 0, B = 1, C = 1. *[1 mark]*', 'A·B = 0 and C\' = 0, so Y = (0 + 0)\' = **1**. Check with the simplified form: (1 + 0) · 1 = 1.'),
      ('How many rows does its truth table have? *[1 mark]*', '2³ = 8.'),
      ('Find Y when A = 1, B = 1, C = 1 from both expressions. *[1 mark]*',
       'Original: (1 + 0)\' = 0. Simplified: (0 + 0) · 1 = 0. Both give **Y = 0**, which shows the simplification is right.')]),
    ('Case 3: The school fire alarm',
     'A school\'s science lab has a fire alarm that must ring when the smoke sensor (S) gives 1 **or** both the heat sensor (H) **and** the gas sensor (G) give 1.',
     [('Write the Boolean expression. *[1 mark]*', 'Y = S + H·G.'),
      ('Describe the circuit. *[1 mark]*', 'H and G into an AND gate; its output and S into an OR gate.'),
      ('How many rows has its truth table? *[1 mark]*', '2³ = 8.'),
      ('Find the output when S = 0, H = 1, G = 0. *[1 mark]*', 'Y = 0 + 1·0 = **0**: the alarm stays silent.')]),
    ('Case 4: The bank locker',
     'A bank locker opens (Y = 1) only when the manager\'s key (M) **and** the customer\'s key (K) are both turned, **and** the alarm switch (S) is **not** on.',
     [('Write the Boolean expression. *[1 mark]*', 'Y = M·K·S\'.'),
      ('Which gates are needed? *[1 mark]*', 'One NOT gate (for S\') and one 3-input AND gate (or two 2-input AND gates).'),
      ('Find Y when M = 1, K = 1, S = 1. *[1 mark]*', 'Y = 1·1·0 = **0**: with the alarm on, the locker stays shut.'),
      ('In how many of the 8 rows of its truth table does the locker open? *[1 mark]*', '**One**: M = 1, K = 1, S = 0. *Why:* an AND gives 1 in only one row.')]),
    ('Case 5: Can Riya go out to play?',
     'Riya may go out to play (Y = 1) only when her homework is **not** pending (H = 0) and it is **not** raining (R = 0).',
     [('Which single gate gives Y from H and R? *[1 mark]*', 'The **NOR** gate: Y = (H + R)\'.'),
      ('Write Y another way using De Morgan\'s law. *[1 mark]*', 'Y = H\' · R\' (first law): "no homework **and** no rain".'),
      ('Find Y when H = 0 and R = 1. *[1 mark]*', 'Y = (0 + 1)\' = **0**: it is raining, so she stays in.'),
      ('Write the truth table. *[1 mark]*', table(["(H + R)'"], ['H', 'R'], ["Y = (H + R)'"]))]),
    ('Case 6: Three judges',
     'In a quiz, three judges A, B and C each press 1 (yes) or 0 (no). A team goes through (Y = 1) when **at least two** judges say yes.',
     [('Write the Boolean expression. *[1 mark]*', 'Y = A·B + B·C + A·C: any pair saying yes is enough.'),
      ('How many rows has its truth table? *[1 mark]*', '2³ = 8.'),
      ('Find Y when A = 1, B = 0, C = 1. *[1 mark]*', 'Y = 0 + 0 + 1 = **1**: two judges said yes.'),
      ('In how many rows is Y = 1? *[1 mark]*', '**4**: 011, 101, 110 and 111.\n\n' + table(["A·B + B·C + A·C"], ['A', 'B', 'C'], ["Y"]))]),
]
val("(A·B + C')'", {'A': 1, 'B': 1, 'C': 0}, 0); same("(A·B + C')'", "(A' + B')·C")
val("(A·B + C')'", {'A': 0, 'B': 1, 'C': 1}, 1); val("(A' + B')·C", {'A': 0, 'B': 1, 'C': 1}, 1)
val("(A·B + C')'", {'A': 1, 'B': 1, 'C': 1}, 0); val("S + H·G", {'S': 0, 'H': 1, 'G': 0}, 0)
val("M·K·S'", {'M': 1, 'K': 1, 'S': 1}, 0); outs("M·K·S'", '00000010', ['M', 'K', 'S'])
same("(H + R)'", "H'·R'"); val("(H + R)'", {'H': 0, 'R': 1}, 0)
outs("A·B + B·C + A·C", '00010111'); val("A·B + B·C + A·C", {'A': 1, 'B': 0, 'C': 1}, 1)
nq = sum(len(c[2]) for c in cases)
body = []
for i, (head, story, qs) in enumerate(cases, 1):
    body.append(f'## {head}\n\n{story}\n')
    for j, (q, a) in enumerate(qs, 1):
        sep = '\n\n' if a.startswith('|') else ' '
        body.append(f'**{i}.{j}** {q}\n\n**Answer.**{sep}{a}\n')
write('07-case-study.md', f'Case studies (6 cases, {nq} questions)', '\n'.join(body))

# ================================================================== index
idx = QD / 'index.md'
lines = {
    '01-mcq.md': 'Multiple-choice questions: 40', '02-fill-in.md': 'Fill in the blanks: 25',
    '03-true-false.md': 'True or false: 25', '04-assertion-reason.md': 'Assertion and reason: 15',
    '05-short-answer.md': 'Short-answer questions (1, 2 and 3 marks): 27',
    '06-long-answer.md': 'Long-answer questions (3 and 4 marks): 10',
    '07-case-study.md': f'Case studies: 6 cases, {nq} questions'}
typed = 40 + 25 + 25 + 15 + 27 + 10 + nq
idx.write_text(f"""# Chapter 3: Boolean Logic and Logic Circuits: questions

**{typed + 120} questions**, each with its answer and the reason below it. They are for learning: try each question first, then read the answer.

**By type of question ({typed})**: every question of the printed chapter, and more

""" + '\n'.join(f'- [{v}]({k})' for k, v in lines.items()) + """

**Practice with expressions and circuits (120)**: generated and checked by program

- [Finding the complement: 40 questions](08-complements.md)
- [Truth tables of expressions: 30 questions](09-truth-tables.md)
- [Logic circuits to draw and read: 30 questions](10-circuits.md)
- [NAND only and NOR only: 20 questions](11-nand-nor-only.md)
""", encoding='utf-8')
print('pages written; questions by type:', typed, '; Boolean checks passed:', checks)
