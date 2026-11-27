"""Chapter 5 online pages, part 2 (27 Nov 2026; Euclid sample approved by Anurag the same day).

Pages, in the approved order: the ATM (0503), testing and debugging (0502), halving search (0511), the four prime
tests (0512), pseudocode to Python (0509), trace tables (0510), more symbols (0505), more decompositions (0513),
five-step practice (0506), the 22 practical charts (0508), the card game, and the index (0501).

Every number is computed here and checked (ok(...)); every flowchart is drawn, checked and run by algo_lib (the
printed ones come from the chapter's own descriptions, the new ones from 50-tools/flow_layout.py, each tested against
a separate reference). Run from the repository root:  python tools/ch05_pages2.py"""
import copy
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle, Wedge, FancyArrowPatch  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ch05_pages as P1  # noqa: E402  (helpers, folders, Euclid page)
from ch05_pages import ok, ind, write, IMG, REL, D, CH, INK, OR, OR2, OR3  # noqa: E402
import figures_v1 as F  # noqa: E402
import figures_v2 as F2  # noqa: E402
from flow_layout import make, nice  # noqa: E402
import ch05_practicals as PR  # noqa: E402

W = {'W1': F.SUM2, 'W2': F2.RECT2, 'W3': F.LARGER, 'W4': F.EVEN, 'W5': F.GREAT, 'W6': F.GRADE, 'W7': F.AVG,
     'W8': F.GCD, 'W9': F2.SER2, 'W10': F2.FAC2}
WTITLE = {'W1': 'Sum of two numbers', 'W2': 'Area and perimeter of a rectangle', 'W3': 'The larger of two numbers',
          'W4': 'Even or odd', 'W5': 'The greatest of three numbers', 'W6': 'Report card: result and grade',
          'W7': 'Average of numbers until 0 is typed', 'W8': 'GCD and LCM by Euclid\'s method',
          'W9': 'The series 1 + x + x² + … + xⁿ', 'W10': 'The factorial of n'}
ATM = F2.ATM2
GREY = '#9A9A9A'


# ================================================================= helpers
def head(title, label, intro):
    return P1.head(title, label, intro, src='tools/ch05_pages2.py')


def pic(name, alt, scale=1.25, cap=720):
    """A picture at `scale` times its natural size (a 300 dpi file), never wider than the page."""
    from PIL import Image
    import shutil
    if (CH / 'images' / name).exists():          # a printed figure: always the chapter's current file
        shutil.copy(CH / 'images' / name, IMG / name)
    w = min(cap, int(Image.open(IMG / name).width * 96 * scale / 300))
    return f'![{alt}]({REL}/{name}){{ width="{w}" }}'


def drawn(algo, name=None, path=None):
    """Draw a flowchart (optionally with one run highlighted) into the site's picture folder; returns the file name."""
    a = copy.copy(algo)
    if name:
        a.name = name
    p, _, _ = a.draw(IMG, path=path)
    return p.name


def run_path(algo, stream):
    out, trace = algo.run(stream)
    return out, [r['step'] for r in trace]


def walk_md(algo, stream, telling=False, head_row=('Step', 'Pseudocode', 'What happens')):
    rows = algo.walkthrough_rows(stream, telling=telling)
    t = f'| {head_row[0]} | {head_row[1]} | {head_row[2]} |\n|:-:|---|---|\n'
    for s, p, e in rows:
        t += f'| {s} | `{p}` | {e} |\n'
    return t


def trace_md(algo, stream, show_vars=None):
    """The classic trace table: one row for every box that changes a value, asks a question or prints."""
    out, trace = algo.run(stream)
    names = show_vars or [k for k in trace[-1]['before']]
    t = '| Step | Box | ' + ' | '.join(names) + ' | Output |\n|:-:|---|' + ':-:|' * len(names) + '---|\n'
    for r in trace:
        nd = algo.node(r['step'])
        if nd.kind in ('start', 'stop'):
            continue
        after = r.get('after', r['before'])
        cells = []
        for v in names:
            val = after.get(v, '')
            changed = v in after and r['before'].get(v, object()) != after[v]
            cells.append(f'**{val}**' if changed else (str(val) if val != '' else ''))
        res = r['result'] if nd.kind == 'decision' else ''
        box = r['box'].replace('|', '/')
        if nd.kind == 'decision':
            box = f'{box} → {res}'
        outc = r['result'][7:] if nd.kind == 'output' else ''
        t += f"| {r['step']} | {box} | " + ' | '.join(cells) + f' | {outc} |\n'
    return t, out


def grid2(left, right):
    return f'<div class="grid2" markdown>\n<div markdown>\n\n{left}\n\n</div>\n<div markdown>\n\n{right}\n\n</div>\n</div>\n'


def canvas(w, h):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis('off')
    return fig, ax


def save(fig, name):
    p = IMG / f'{name}.png'
    fig.savefig(p, dpi=300, facecolor='white'); plt.close(fig)
    return p.name


def rbox(ax, x, y, w, h, text, fc=OR3, fs=8.5, weight='normal', color=INK):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0,rounding_size=0.06', fc=fc, ec=INK,
                                lw=1.2))
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, weight=weight, color=color, linespacing=1.05)


def arr(ax, p, q, color=INK):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=9, color=color, lw=1.2, shrinkA=0, shrinkB=0))


def answer(text):
    """A collapsible answer (Material 'details')."""
    body = '\n'.join('    ' + line if line else '' for line in text.strip('\n').split('\n'))
    return f'??? success "Answer"\n{body}\n\n'


# ================================================================= 0503 the ATM
def atm_page():
    steps = [
        (1, 'User', 'Start: the user comes to the machine.', 'sequence'),
        (2, 'User → Machine', 'The user inserts the card; the machine reads it and finds the balance.', 'sequence'),
        (3, 'Machine', 'Set the number of wrong tries to 0.', 'sequence'),
        (4, 'User', 'Enter the PIN.', 'repetition (steps 4–7)'),
        (5, 'Machine', 'Is the PIN right? Yes: go to 9. No: go to 6.', 'selection'),
        (6, 'Machine', 'Add 1 to the wrong tries.', 'repetition'),
        (7, 'Machine', 'Are the wrong tries now 3? Yes: go to 8. No: back to 4.', 'selection, ends the loop'),
        (8, 'Machine', 'Show "Card blocked" and keep the card; go to 13.', 'sequence'),
        (9, 'User', 'Enter the amount.', 'sequence'),
        (10, 'Machine', 'Is the amount a multiple of ₹100 and not more than the balance?', 'selection'),
        (11, 'Machine', 'Give the cash; go to 13.', 'sequence'),
        (12, 'Machine', 'Show "Cannot pay this amount".', 'sequence'),
        (13, '—', 'Stop.', '—')]
    ok(len(steps) == len(ATM.nodes) == 13)
    t = head('The ATM algorithm, run by run', 'Explained',
             'The printed book (section 5.3) gives the 13 steps of taking cash from an ATM, and section 5.5 its '
             'flowchart. This page runs the algorithm four times, with different PINs and amounts, and colours the '
             'path each run takes through the flowchart.')
    t += '## 1. The 13 steps, who does each, and which building block it is\n\n'
    t += '| Step | Who | What happens | Building block |\n|:-:|---|---|---|\n'
    for n, who, what, blk in steps:
        t += f'| {n} | {who} | {what} | {blk} |\n'
    t += ('\nThe machine knows the right PIN of the card (in these runs it is **4321**) and the balance of the account '
          '(₹5,000).\n\n## 2. The flowchart\n\n')
    t += pic('c05-flow-atm-v2.png', 'The ATM flowchart', 1.15) + '\n\n'
    runs = [
        ('Run 1: the right PIN at once, ₹2,800', [5000, 4321, 2800], ['Cash 2800'],
         'The shortest path that pays: the PIN loop is never entered, because box 5 says Yes at the first try.'),
        ('Run 2: one wrong PIN, then the right one; ₹2,850', [5000, 1111, 4321, 2850], ['Cannot pay this amount'],
         'The loop 4 → 5 → 6 → 7 → 4 runs once. Then 2,850 is not a multiple of 100 (2,850 ÷ 100 leaves 50), so box '
         '10 says No and the machine refuses.'),
        ('Run 3: three wrong PINs', [5000, 1111, 2222, 3333], ['Card blocked'],
         'The loop runs three times; at the third wrong PIN, tries = 3, box 7 says Yes and the card is blocked. '
         'The amount is never asked.'),
        ('Run 4: the right PIN, but more than the balance: ₹6,000', [5000, 4321, 6000], ['Cannot pay this amount'],
         '6,000 IS a multiple of 100, but it is more than 5,000: one half of the AND is No, so the whole question is '
         'No.')]
    for k, (title, stream, expect, why) in enumerate(runs, 1):
        out, path = run_path(ATM, stream)
        ok(out == expect, (out, expect))
        ok(ATM.run_python(stream) == [o.replace('Cash ', 'Cash ') for o in expect])
        t += f'## {k + 2}. {title}\n\n'
        pins = stream[1:] if 'Card' in expect[0] else stream[1:-1]
        amt = '' if 'Card' in expect[0] else f'; amount ₹{ind(stream[-1])}'
        t += f'*Inputs:* balance ₹5,000; PIN{"s" if len(pins) > 1 else ""} typed: {", ".join(map(str, pins))}{amt}.\n\n'
        t += pic(drawn(ATM, f'c05-atm-run{k}', path), f'The path of run {k}', 1.15) + '\n\n'
        t += f'*The path:* boxes {" → ".join(map(str, path))}. ' + why + '\n\n'
        t += walk_md(ATM, stream) + '\n'
        t += f'**The machine shows:** {expect[0]}.\n\n'
    t += '''## 7. Why the algorithm always stops

There are only two ways round the loop, and both end:

- a right PIN leaves the loop at box 5 (Yes), and then the machine pays or refuses: either way it reaches Stop;
- every wrong PIN adds 1 to *tries*, so after at most **three** wrong PINs box 7 says Yes and the card is blocked.

So the loop runs **at most 3 times**, whatever the user types. This is **finiteness**, one of the five
characteristics of an algorithm. Without box 6 (tries = tries + 1), *tries* would stay 0, box 7 would always say No,
and a thief could go on trying PINs for ever.

'''
    a, notes = 2800, []
    for n in (500, 200, 100):
        notes.append(a // n); a %= n
    ok(notes == [5, 1, 1])
    t += f'''## 8. The notes for ₹2,800

The machine holds ₹500, ₹200 and ₹100 notes. Taking the **largest note first**, again and again, gives the fewest
notes: 2,800 ÷ 500 = **5** notes, leaving 300; 300 ÷ 200 = **1** note, leaving 100; 100 ÷ 100 = **1** note.
So ₹2,800 = 5 × ₹500 + 1 × ₹200 + 1 × ₹100: **{sum(notes)} notes**. This "largest first" rule is itself a small
algorithm (it is called a *greedy* algorithm).

## 9. Try it yourself

'''
    qs = [([5000, 2222, 4321, 500], 'The PINs 2222 and then 4321 are typed, and the amount ₹500. Which boxes run, '
           'in order, and what does the machine do?'),
          ([5000, 4321, 5000], 'The right PIN is typed and the amount is ₹5,000, exactly the balance. What happens, '
           'and which sign in box 10 decides it?')]
    for stream, q in qs:
        out, path = run_path(ATM, stream)
        extra = (' "Not more than the balance" means ≤: 5,000 ≤ 5,000 is Yes.' if stream[-1] == 5000 else '')
        t += f'**{q}**\n\n' + answer(f'Boxes {" → ".join(map(str, path))}. The machine shows **{out[0]}**.{extra}')
    write('explained-atm-algorithm.md', t)


# ================================================================= 0502 testing and debugging
def variant(algo, name, **changes):
    """A copy of an algorithm with some boxes changed: {box number: dict(test=..., do=..., text=...)}."""
    a = copy.deepcopy(algo)
    a.name = name
    for n, ch in changes.items():
        nd = a.node(int(n[1:]))
        for k, v in ch.items():
            setattr(nd, k, v)
    return a


def testing_page():
    G = F.GRADE
    t = head('Testing and debugging the report-card program', 'Explained',
             'The printed book (section 5.2) explains testing and debugging in a few lines. Here the report-card '
             'program (worked example W6) is tested with the four kinds of test data, three bugs are found, and each '
             'is traced to its cause and fixed.')
    t += '## 1. The program under test\n\n'
    t += ('The class teacher types the marks of five subjects (each 0 to 100). The program prints **Fail** if any mark '
          'is below 33; otherwise the grade: 90% and above **A**, 75% and above **B**, 60% and above **C**, below 60% '
          '**D**.\n\n')
    t += pic('c05-flow-grade.png', 'W6: the report-card flowchart', 1.2) + '\n\n'
    t += '## 2. Test data: choose marks whose answers you already know\n\n'
    tests = [('Normal', [80, 75, 70, 72, 78], 'Grade B', 'usual marks must work'),
             ('Normal', [95, 92, 88, 91, 94], 'Grade A', 'each grade at least once'),
             ('Extreme', [100, 100, 100, 100, 100], 'Grade A', 'the largest marks allowed'),
             ('Extreme', [0, 0, 0, 0, 0], 'Fail', 'the smallest marks allowed'),
             ('Boundary', [33, 33, 33, 33, 33], 'Grade D', 'exactly the pass mark passes'),
             ('Boundary', [32, 90, 90, 90, 90], 'Fail', 'one mark just below 33 fails the student'),
             ('Boundary', [90, 90, 90, 90, 90], 'Grade A', 'exactly 90% is an A'),
             ('Boundary', [75, 75, 75, 75, 74], 'Grade C', '74.8% is just below a B')]
    t += '| Kind | Marks | Expected | The program gives | Why this test |\n|---|---|---|---|---|\n'
    for kind, m, exp, why in tests:
        out, _ = G.run(m)
        ok(out == [exp], (m, out, exp))
        ok(G.run_python(m) == [exp])
        t += f'| {kind} | {", ".join(map(str, m))} | {exp} | {out[0]} ✓ | {why} |\n'
    ok(sum([75, 75, 75, 75, 74]) / 5 == 74.8)
    t += ('\n**Abnormal data** (−5, 105, "sixty") is not a mark at all. The program of W6 does not check for it: given '
          '−5, 100, 100, 100, 100 it ')
    out, _ = G.run([-5, 100, 100, 100, 100])
    ok(out == ['Fail'])
    out2, _ = G.run([105, 105, 105, 105, 105])
    ok(out2 == ['Grade A'])
    t += (f'says **{out[0]}**, and given 105 in every subject it says **{out2[0]}**, as if nothing were wrong. A real '
          'report-card program must refuse such marks *before* using them. That check is one more decision at the '
          'start: "is every mark from 0 to 100?". Its No path asks for the marks again.\n\n')
    t += '## 3. Three bugs, found by testing and removed by debugging\n\n'
    bugs = [
        ('Bug 1: "more than 33" instead of "33 or more"',
         variant(G, 'bug1', n4=dict(test='low > 33', text='low > 33?')), [33, 33, 33, 33, 33],
         'Grade D', 'Box 4 asks "low > 33?". For a lowest mark of exactly 33, 33 > 33 is No, so a student who passed is '
         'told Fail.', 'Change the question to **low ≥ 33**. The pass mark itself passes.'),
        ('Bug 2: dividing by 4', variant(G, 'bug2', n3=dict(do='total = m1 + m2 + m3 + m4 + m5\nper = total / 4\n'
                                                              'low = min(m1, m2, m3, m4, m5)')),
         [80, 75, 70, 72, 78], 'Grade B', 'Box 3 computes per = total ÷ 4. Five subjects need ÷ 5: the program found '
         '93.75% instead of 75%.', 'Divide by the number of subjects, **5**.'),
        ('Bug 3: the grade questions in the wrong order',
         variant(G, 'bug3', n6=dict(test='per >= 60'), n7=dict(show="'Grade C'"), n10=dict(test='per >= 90'),
                 n11=dict(show="'Grade A'")),
         [95, 92, 88, 91, 94], 'Grade A', 'The ladder asks "% ≥ 60?" first. 92% is ≥ 60, so the first Yes prints the '
         'first grade on the ladder and the other questions are never asked.', 'Ask the **highest** limit first: '
         '90, then 75, then 60. In a ladder, the first Yes wins.'),
    ]
    for title, bad, marks, exp, cause, fix in bugs:
        got, _ = bad.run(marks)
        right, _ = G.run(marks)
        ok(right == [exp] and got != right, (title, got, right))
        t += f'### {title}\n\n'
        t += (f'- **Test:** marks {", ".join(map(str, marks))}. Expected: **{exp}**. The program printed: '
              f'**{got[0]}**. *Testing has found a bug:* the answer is wrong, but testing does not say why.\n')
        t += f'- **Debugging, the cause:** {cause}\n- **The fix:** {fix}\n'
        t += f'- **Test again:** with the fix, the same marks give **{right[0]}** ✓, and every test of section 2 still passes.\n\n'
    pct = sum([80, 75, 70, 72, 78]) / 4
    ok(pct == 93.75)
    t += '''*Why "test again" after every fix?* A fix can break something that worked before. Running all the old tests
again after each change is called **regression testing** (beyond the syllabus).

## 4. Four kinds of testing, in the report-card program

| Kind | What is tested | In the report-card program |
|---|---|---|
| **Unit** testing | one part alone | the part that works out the percentage: give it 375, it must give 75 |
| **Integration** testing | parts joined together | the marks-entry part joined to the grade part: do the marks reach the grade part correctly? |
| **System** testing | the whole program | type real marks, check the printed report card from start to end |
| **Acceptance** testing | by the user, before delivery | the class teacher tries last year's report cards and says "yes, this is what I wanted" |

## 5. Testing vs debugging, once more

| | Testing | Debugging |
|---|---|---|
| Question | **Is** something wrong? | **Where** and **why** is it wrong? |
| Tool | test data with known answers | the program text, a dry run (section 5.7), printing values |
| Result | a list of faults | a corrected program, tested again |

## 6. Try it yourself

'''
    q = [('A program finds the average of 3 marks as (m1 + m2 + m3) ÷ 2. Which test finds the bug: 60, 60, 60 or '
          '0, 0, 0?', '60, 60, 60: the program says 90 instead of 60. With 0, 0, 0 both give 0, so that test hides '
          'the bug: a test whose answer is the same for the right and the wrong program finds nothing.'),
         ('Choose boundary test data for "a person may vote at 18 or more".', '17 (just below), 18 (exactly the '
          'limit) and 19 (just above). Most faults hide at the limit: > instead of ≥ fails only for 18.')]
    for qq, a in q:
        t += f'**{qq}**\n\n' + answer(a)
    write('explained-testing-and-debugging.md', t)


# ================================================================= 0511 halving search
def halving(items, target):
    """Binary search as in the book: look at the middle, keep the half the target must be in."""
    lo, hi, looks = 0, len(items) - 1, []
    while lo <= hi:
        mid = (lo + hi) // 2
        looks.append((lo, hi, mid))
        if items[mid] == target:
            return looks, mid
        if target > items[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return looks, None


def halving_picture(items, target, name):
    looks, pos = halving(items, target)
    n = len(items)
    cw, rh = 0.36, 0.55
    fig, ax = canvas(n * cw + 1.35, len(looks) * rh + 0.2)
    for k, (lo, hi, mid) in enumerate(looks):
        y = (len(looks) - 1 - k) * rh + 0.15
        ax.text(0.05, y + 0.17, f'Look {k + 1}', fontsize=9, weight='bold', va='center')
        for i, it in enumerate(items):
            x = 0.75 + i * cw
            inside = lo <= i <= hi
            fc = OR if i == mid else (OR3 if inside else '#EEEEEE')
            ax.add_patch(Rectangle((x, y), cw - 0.04, 0.34, fc=fc, ec=INK if inside else '#BBBBBB', lw=0.9))
            ax.text(x + (cw - 0.04) / 2, y + 0.17, it, ha='center', va='center', fontsize=9,
                    color='white' if i == mid else (INK if inside else '#AAAAAA'), weight='bold' if i == mid else 'normal')
        left = hi - lo + 1
        ax.text(0.75 + n * cw + 0.05, y + 0.17, f'{left} left', fontsize=8.5, va='center', color=OR)
    ok(all(a[0] <= a[2] <= a[1] for a in looks))
    return save(fig, name), looks, pos


def halving_page():
    letters = [chr(65 + i) for i in range(16)]
    t = head('Halving search, step by step', 'Step by step',
             'The printed book (section 5.8) finds M among 16 names in 4 looks by halving. This page draws every look, '
             'shows why 100 contacts need at most 7 looks, and plays the guessing game.')
    t += '''## 1. The rule

> **Open the middle of what is left. If it is the one you want, stop. If what you want comes after it, keep the
> half after it; if before, keep the half before it. Repeat.**

It works only when the list is **in order**, like the contacts in a phone or the words in a dictionary.

## 2. Finding M among A to P

The orange box is the middle, the one opened at that look; the grey boxes have been thrown away.

'''
    name, looks, pos = halving_picture(letters, 'M', 'c05-halving-M')
    ok([letters[m] for _, _, m in looks] == ['H', 'L', 'N', 'M'] and pos == 12)
    t += pic(name, 'Halving search for M among A to P') + '\n\n'
    t += '| Look | Names left | Middle | Compare | Keep |\n|:-:|:-:|:-:|---|---|\n'
    for k, (lo, hi, mid) in enumerate(looks, 1):
        if letters[mid] == 'M':
            cmp_, keep = 'M = M: found', '—'
        elif 'M' > letters[mid]:
            cmp_, keep = f'M comes after {letters[mid]}', f'{letters[mid + 1]} to {letters[hi]}'
        else:
            cmp_, keep = f'M comes before {letters[mid]}', f'{letters[lo]} to {letters[mid - 1]}'
        t += f'| {k} | {letters[lo]} to {letters[hi]} ({hi - lo + 1}) | {letters[mid]} | {cmp_} | {keep} |\n'
    t += '\nOne by one (A, B, C … M), the same search takes **13** looks.\n\n'
    ok(letters.index('M') + 1 == 13)
    t += '## 3. Every letter: one by one vs halving\n\n'
    rows = [(c, letters.index(c) + 1, len(halving(letters, c)[0])) for c in letters]
    t += '| Name | ' + ' | '.join(r[0] for r in rows) + ' |\n|---|' + ':-:|' * 16 + '\n'
    t += '| One by one | ' + ' | '.join(str(r[1]) for r in rows) + ' |\n'
    t += '| Halving | ' + ' | '.join(str(r[2]) for r in rows) + ' |\n\n'
    mx = max(r[2] for r in rows)
    avg1, avg2 = sum(r[1] for r in rows) / 16, sum(r[2] for r in rows) / 16
    ok(mx == 5 and avg1 == 8.5)
    t += (f'Halving never needs more than **{mx}** looks for 16 names; one by one needs up to 16. On average: '
          f'{avg1} looks one by one, {avg2:.4g} by halving. *Why 5 and not 4?* After 4 looks one name is left, '
          'and for some names (P, for example) the 5th look is needed to open it.\n\n')
    name, looksP, _ = halving_picture(letters, 'P', 'c05-halving-P')
    t += pic(name, 'Halving search for P: five looks') + '\n\n'
    t += '## 4. Why 100 contacts need 7 looks, 1,000 need 10, 1,00,000 need 17\n\n'
    t += ('Each look can deal with one name and splits the rest in two halves. So **k looks are enough for '
          '2ᵏ − 1 names**: 1 look for 1 name, 2 looks for 3, 3 looks for 7, and the number almost doubles with every '
          'look.\n\n')
    t += '| Looks k | Names that k looks can always handle (2ᵏ − 1) |\n|:-:|:-:|\n'
    for k in range(1, 18):
        t += f'| {k} | {ind(2 ** k - 1)} |\n'
    for n, k in [(100, 7), (1000, 10), (100000, 17)]:
        ok(math.ceil(math.log2(n + 1)) == k and 2 ** (k - 1) - 1 < n <= 2 ** k - 1)
        worst = max(len(halving(list(range(n)), x)[0]) for x in range(0, n, max(1, n // 2000)))
        ok(worst <= k)
    t += ('\nSo 100 contacts need **7** (6 looks handle only 63), 1,000 need **10** (2¹⁰ − 1 = 1,023), and 1,00,000 '
          'need **17** (2¹⁷ − 1 = 1,31,071). The program also searched for thousands of names in lists of these '
          'sizes: none needed more.\n\n')
    t += '## 5. The guessing game: a number from 1 to 100\n\n'
    t += ('A friend thinks of a number from 1 to 100 and answers only "higher", "lower" or "right". Guess the middle '
          'every time:\n\n| Secret | Guesses | Number of guesses |\n|:-:|---|:-:|\n')
    nums = list(range(1, 101))
    worst = 0
    for sec in [37, 50, 1, 100, 73]:
        looks, _ = halving(nums, sec)
        worst = max(worst, len(looks))
        t += f'| {sec} | {", ".join(str(nums[m]) for _, _, m in looks)} | {len(looks)} |\n'
    allw = max(len(halving(nums, s)[0]) for s in nums)
    ok(allw == 7)
    t += f'\nThe program played all 100 secrets: never more than **{allw}** guesses.\n\n'
    t += '''## 6. Halving needs a list in order

In the list K, B, P, D, A (not in order), look for A: the middle is P; A comes before P, so keep K, B … and A is
thrown away with the other half. **Halving on a list that is not in order can miss a name that is there.** One by
one works on any list.

## 7. Try it yourself

'''
    looks, _ = halving(nums, 81)
    t += '**Guess 81 in 1 to 100 by halving. Write every guess.**\n\n'
    t += answer(f'{", ".join(str(nums[m]) for _, _, m in looks)}: {len(looks)} guesses.')
    ok(math.ceil(math.log2(1000 + 1)) == 10)
    t += '**At most how many looks find a word in a dictionary of 50,000 words?**\n\n'
    k = math.ceil(math.log2(50001))
    ok(2 ** (k - 1) - 1 < 50000 <= 2 ** k - 1)
    t += answer(f'{k}: {k - 1} looks can always handle only {ind(2 ** (k - 1) - 1)} words, which is fewer than '
                f'50,000; {k} looks handle {ind(2 ** k - 1)}.')
    write('step-by-step-halving-search.md', t)


# ================================================================= 0512 prime tests
PRIMES100 = [p for p in range(2, 101) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def prime_method(n, m):
    """Divisions made by method m (1-4) on n, stopping at the first divisor. Returns (divisors tried, verdict)."""
    if m == 1:
        cands = range(2, n)
    elif m == 2:
        cands = range(2, n // 2 + 1)
    elif m == 3:
        cands = range(2, math.isqrt(n) + 1)
    else:
        cands = [p for p in PRIMES100 if p != n]
    tried = []
    for d in cands:
        tried.append(d)
        if n % d == 0:
            return tried, 'not prime'
    return tried, 'prime'


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


def primes_page():
    ok(len(PRIMES100) == 25)
    t = head('The four prime tests, worked', 'Explained',
             'The printed book (section 5.8) compares four ways to test whether a number is prime. Here each method is '
             'worked for 97, 91, 997 and 10,201, with the divisions counted by a program, and the reason why the '
             'shorter methods are still right.')
    t += '''## 1. The four methods

| Method | Divide n by | Stop |
|:-:|---|---|
| (i) | 2, 3, 4 … up to n − 1 | at the first divisor: n is **not prime** |
| (ii) | 2, 3, 4 … up to n ÷ 2 | the same |
| (iii) | 2, 3, 4 … while d × d ≤ n (up to √n) | the same |
| (iv) | the 25 primes up to 100, kept in a list (but never n itself) | the same; works only for n below 10,201 |

If no division leaves remainder 0, n is **prime**.

## 2. Divisions needed

'''
    nums = [97, 91, 997, 10201, 1000003]
    t += '| n | Really prime? | (i) | (ii) | (iii) | (iv) |\n|:-:|:-:|:-:|:-:|:-:|:-:|\n'
    for n in nums:
        cells = []
        for m in (1, 2, 3, 4):
            if m == 4 and n >= 10201 and n != 10201:
                cells.append('not allowed')
                continue
            tried, verdict = prime_method(n, m)
            right = (verdict == 'prime') == is_prime(n)
            cells.append(f'{ind(len(tried))}, says {verdict}' + ('' if right else ' **(wrong!)**'))
        t += f'| {ind(n)} | {"yes" if is_prime(n) else "no"} | ' + ' | '.join(cells) + ' |\n'
    ok([len(prime_method(997, m)[0]) for m in (1, 2, 3, 4)] == [995, 497, 30, 25])
    ok([len(prime_method(1000003, m)[0]) for m in (1, 2, 3)] == [1000001, 500000, 999])
    ok(prime_method(10201, 4)[1] == 'prime' and not is_prime(10201) and 10201 == 101 * 101)
    ok(len(prime_method(91, 3)[0]) == 6 and 91 == 7 * 13)
    t += '''
- For a **prime** the method tries every divisor it allows, so the counts differ hugely: 995, 497, 30, 25 for 997.
- For a number that is **not** prime, every method stops at the first divisor: 91 = 7 × 13 stops at 7 in all four.
- For **10,201** method (iv) is **wrong**: none of the 25 primes up to 100 divides it, so it says "prime", but
  10,201 = 101 × 101. That is the limit of method (iv).

## 3. Method (iii) for 97, every division

'''
    tried, verdict = prime_method(97, 3)
    t += '| d | d × d | 97 ÷ d | Remainder |\n|:-:|:-:|:-:|:-:|\n'
    for d in tried:
        t += f'| {d} | {d * d} | {97 // d} | {97 % d} |\n'
    nxt = tried[-1] + 1
    ok(nxt * nxt > 97 and verdict == 'prime' and len(tried) == 8)
    t += (f'\nThe next d would be {nxt}, but {nxt} × {nxt} = {nxt * nxt} is more than 97, so we stop: no remainder was '
          '0, so **97 is prime**, after only **8** divisions (method (i) needs 95).\n\n')
    t += '## 4. 91, by all four methods\n\n| Method | Divisions made | Remainders |\n|:-:|:-:|---|\n'
    for m in (1, 2, 3, 4):
        tried, verdict = prime_method(91, m)
        t += f'| ({"i" * m if m < 4 else "iv"}) | {len(tried)} | ' + ', '.join(f'91 ÷ {d} r {91 % d}' for d in tried) + ' |\n'
    t += '\nAll four stop at 7: 91 ÷ 7 = 13 remainder **0**, so 91 is **not prime**. *Trap:* 91 looks prime; always test it.\n\n'
    t += '## 5. Why n ÷ 2 is enough (method ii)\n\n'
    t += ('Any divisor of n other than n itself is **at most n ÷ 2**, because the smallest other factor is 2, and '
          'n = 2 × (n ÷ 2). For 100 the divisors are ' + ', '.join(str(d) for d in range(1, 101) if 100 % d == 0) +
          ': after 50 the next is 100 itself.\n\n')
    ok(max(d for d in range(1, 100) if 100 % d == 0) == 50)
    t += '## 6. Why √n is enough (method iii)\n\nFactors come in **pairs** whose product is n:\n\n'
    for n in (100, 36):
        pairs = [(a, n // a) for a in range(1, math.isqrt(n) + 1) if n % a == 0]
        t += f'- {n} = ' + ' = '.join(f'{a} × {b}' for a, b in pairs) + f'; √{n} = {math.isqrt(n)}.\n'
        ok(all(a <= math.isqrt(n) <= b for a, b in pairs))
    t += ('\nIn every pair the smaller factor is at most √n. So if no number up to √n divides n, no number above √n can '
          'either: its partner would have been found already.\n\n')
    t += '''## 7. Why method (iv) works below 10,201, and its two limits

- A number that is not prime has a factor ≤ its square root (section 6), and so a **prime** factor ≤ its square root.
  Below 10,201 = 101 × 101 the square root is below 101, so that prime factor is one of the 25 primes up to 100.
- **Limit 1:** do not divide n by itself. 7 is in the list and 7 ÷ 7 leaves 0, yet 7 is prime.
- **Limit 2:** from 10,201 on, a number can have all its prime factors above 100: 10,201 = 101 × 101 slips through.
- Its price is **memory**: the list of 25 primes must be stored. That is time against space (section 5.8).

## 8. Try it yourself

'''
    for n in (221, 113):
        tried, verdict = prime_method(n, 3)
        ok((verdict == 'prime') == is_prime(n))
        t += f'**Test {n} by method (iii). How many divisions?**\n\n'
        why = (f'{n} ÷ {tried[-1]} leaves 0 ({n} = {tried[-1]} × {n // tried[-1]}), so {n} is not prime.'
               if verdict != 'prime' else f'{tried[-1] + 1} × {tried[-1] + 1} = {(tried[-1] + 1) ** 2} is more than {n}, '
               f'and no remainder was 0, so {n} is prime.')
        t += answer(f'{len(tried)} divisions (d = 2 to {tried[-1]}). {why}')
    write('explained-prime-tests.md', t)


# ================================================================= 0509 pseudocode to Python
def pseudo_python_page():
    t = head('Pseudocode to Python, line for line', 'Explained',
             'The printed book (section 5.6) writes every algorithm in pseudocode. Here each pseudocode of the chapter '
             'stands beside its Python program, so you can see which line becomes which. You will learn the Python '
             'from Chapter 6 on; for now, just notice how close the two are.')
    t += '''## 1. The keywords and their Python

| Pseudocode | Python | Example |
|---|---|---|
| INPUT a | `a = int(input())` | a whole number typed by the user |
| PRINT sum | `print(sum)` | |
| COMPUTE, SET x = … | `x = …` | `area = length * breadth` |
| IF … THEN … ELSE … END IF | `if …:` … `else:` … | indentation instead of END IF |
| ELSE IF | `elif …:` | |
| WHILE … END WHILE | `while …:` | |
| FOR i = 1 TO n | `for i in range(1, n + 1):` | range stops just before its end |
| INCREMENT i | `i = i + 1` or `i += 1` | |
| × ÷ ≤ ≥ ≠ = (in a test) | `* / <= >= != ==` | `==` asks, `=` gives a value |
| remainder of a ÷ b | `a % b` | |

'''
    t += '## 2. Every algorithm of the chapter\n\nEach Python program was run on the test inputs of the book and gave the same answers as the flowchart.\n\n'
    items = list(W.items()) + [('ATM', ATM)]
    for k, (key, algo) in enumerate(items, 1):
        n = algo.test()
        ok(n >= 1)
        title = WTITLE.get(key, 'Cash from an ATM')
        t += f'### {key}. {title}\n\n'
        t += grid2(f'**Pseudocode**\n\n```text\n{algo.pseudocode_md()}\n```',
                   f'**Python**\n\n```python\n{algo.python.rstrip()}\n```')
        t += '\n'
    t += ('*Notice:* in W6 the five marks are kept together as one list, `m`; in the ATM, Python leaves the loop with '
          '`break`. These are ways of writing the same steps that you will meet in Chapters 9 and 10.\n\n')
    t += '''## 3. The same algorithm in three styles

There is no single standard for pseudocode. Books and teachers write it in different styles; all are accepted if the
steps are exact and in order. Here is W3, the larger of two numbers, three ways:

'''
    s1 = 'INPUT a, b\nIF a > b THEN\n    PRINT a\nELSE\n    PRINT b\nEND IF'
    s2 = 'Step 1: Start\nStep 2: Read a, b\nStep 3: If a > b then\n            Display a\n        Else\n            Display b\n        Endif\nStep 4: Stop'
    s3 = 'BEGIN\n    READ a, b\n    IF a > b\n        big ← a\n    ELSE\n        big ← b\n    ENDIF\n    WRITE big\nEND'
    t += grid2(f'**Style 1: this book (as NCERT)**\n\n```text\n{s1}\n```', f'**Style 2: numbered steps**\n\n```text\n{s2}\n```')
    t += f'\n**Style 3: BEGIN … END, with ←**\n\n```text\n{s3}\n```\n\n'
    t += ('*What stays the same in every style:* one step on a line, the IF with both of its paths, the closing END IF, '
          'and the indentation. ← and = both mean "put the value into".\n')
    write('explained-pseudocode-to-python.md', t)


# ================================================================= 0510 trace tables
def time_adders():
    bug = make('c05-time-adder-bug', 'Adding two times (with the bug)',
               [('in', ['h1', 'm1', 'h2', 'm2']), ('do', 'h = h1 + h2; m = m1 + m2'),
                ('out', "str(h) + ' h ' + str(m) + ' min'", {'text': 'Print h, m'})],
               [([4, 50, 2, 20], ['6 h 70 min']), ([5, 20, 7, 30], ['12 h 50 min'])])
    fix = make('c05-time-adder', 'Adding two times (fixed)',
               [('in', ['h1', 'm1', 'h2', 'm2']), ('do', 'h = h1 + h2; m = m1 + m2'),
                ('if', 'm >= 60', [('do', 'h = h + 1; m = m - 60')]),
                ('out', "str(h) + ' h ' + str(m) + ' min'", {'text': 'Print h, m'})],
               [([4, 50, 2, 20], ['7 h 10 min']), ([5, 20, 7, 30], ['12 h 50 min']), ([0, 59, 0, 1], ['1 h 0 min'])])
    return bug, fix


def trace_page():
    t = head('Trace tables, with more to fill in', 'Practice',
             'The printed book (section 5.7) shows one classic trace table. Here are full trace tables for W6 to W10, '
             'the bug in the time adder found by a dry run, and ten trace tables to fill in yourself, with the '
             'answers behind a click.')
    t += '''## 1. How to make a trace table

1. Draw one column for **each variable**, one for the **question** and one for the **output**.
2. Follow the flowchart from Start. Each time a box **changes** a value, **asks** a question or **prints**, write a row.
3. Write a value **only when it changes** (here it is in bold); the others stay as they were.
4. At Stop, the output column holds the answer. Check it by hand if you can.

'''
    cases = [('W6', [80, 75, 70, 72, 78], ['m1', 'm2', 'm3', 'm4', 'm5', 'total', 'per', 'low']),
             ('W7', [6, 9, 0], ['x', 'sum', 'count', 'avg']),
             ('W8', [30, 21], ['a', 'b', 'x', 'y', 'r', 'lcm']),
             ('W9', [2, 3], ['x', 'n', 'sum', 'term', 'i']),
             ('W10', [4], ['n', 'fact', 'i'])]
    for k, (key, stream, vars_) in enumerate(cases, 2):
        algo = W[key]
        tab, out = trace_md(algo, stream, vars_)
        ok(out == algo.run_python(stream) or key in ('W8',), (key, out))
        t += f'## {k}. {key}: {WTITLE[key]}, for {", ".join(map(str, stream))}\n\n{tab}\n**Output:** {", ".join(out)}.\n\n'
    bug, fix = time_adders()
    t += '## 7. The bug in the time adder, found by a dry run\n\n'
    tb, ob = trace_md(bug, [4, 50, 2, 20], ['h1', 'm1', 'h2', 'm2', 'h', 'm'])
    tf, of = trace_md(fix, [4, 50, 2, 20], ['h1', 'm1', 'h2', 'm2', 'h', 'm'])
    ok(ob == ['6 h 70 min'] and of == ['7 h 10 min'])
    t += ('Journey J1 takes 4 h 50 min and J2 takes 2 h 20 min. The first algorithm adds hours to hours and minutes to '
          'minutes:\n\n' + tb + f'\nIt prints **{ob[0]}**: 70 minutes is more than an hour. The fix adds one '
          'question: if the minutes are 60 or more, add 1 to the hours and take 60 from the minutes.\n\n')
    t += pic(drawn(fix), 'The time adder, fixed', 1.2) + '\n\n' + tf + f'\nNow it prints **{of[0]}** ✓.\n\n'
    t += '## 8. Ten to fill in\n\nMake the trace table on paper first; then open the answer.\n\n'
    P = {p[1]: p[4] for p in PR.P}
    todo = [('W7', W['W7'], [4, 8, 6, 0], ['x', 'sum', 'count', 'avg']),
            ('W9', W['W9'], [3, 4], ['sum', 'term', 'i']),
            ('W10', W['W10'], [5], ['fact', 'i']),
            ('W8', W['W8'], [48, 18], ['a', 'b', 'r']),
            ('Fibonacci (practical 15)', P['fibonacci'], [6], ['a', 'b', 'c', 'i']),
            ('Palindrome number (practical 13)', P['palindrome-number'], [1231], ['rev', 't']),
            ('Armstrong number (practical 12)', P['armstrong'], [370], ['k', 's', 't', 'd']),
            ('Series 1 − x + x² … (practical 8)', P['series-2'], [2, 4], ['total', 'term', 'i']),
            ('Pattern 2 (practical 5)', P['pattern-numbers'], [3], ['i', 'j', 'row']),
            ('Sum of digits (five-step practice)', make('c05-sum-digits-t', 'Sum of digits',
                                                         [('in', ['n']), ('do', 's = 0'),
                                                          ('while', 'n > 0', [('do', 's = s + n % 10'), ('do', 'n = n // 10')]),
                                                          ('out', 's')], [([4096], ['19'])]), [4096], ['n', 's'])]
    ok(len(todo) == 10)
    for k, (label, algo, stream, vars_) in enumerate(todo, 1):
        tab, out = trace_md(algo, stream, vars_)
        ok(out == algo.run_python(stream), (label, out))
        t += f'**T{k}. {label}, for {", ".join(map(str, stream))}.** Columns: {", ".join(vars_)}, output.\n\n'
        t += answer(tab + f'\n**Output:** {", ".join(out)}.')
    write('practice-trace-tables.md', t)


# ================================================================= 0505 more symbols
def symbols_picture():
    syms = ['predefined', 'document', 'manual input', 'display', 'preparation', 'off-page', 'stored data',
            'annotation', 'manual op', 'merge', 'extract', 'delay']
    cols = 4
    cw, ch = 1.7, 1.15
    fig, ax = canvas(cols * cw, 3 * ch)
    names = {'predefined': 'Predefined process', 'document': 'Document', 'manual input': 'Manual input',
             'display': 'Display', 'preparation': 'Preparation', 'off-page': 'Off-page connector',
             'stored data': 'Stored data', 'annotation': 'Annotation', 'manual op': 'Manual operation',
             'merge': 'Merge', 'extract': 'Extract', 'delay': 'Delay'}
    for i, s in enumerate(syms):
        cx = (i % cols) * cw + cw / 2
        cy = (2 - i // cols) * ch + 0.68
        w, h = 1.0, 0.5
        x0, y0 = cx - w / 2, cy - h / 2
        kw = dict(fc=OR3, ec=INK, lw=1.2)
        if s == 'predefined':
            ax.add_patch(Rectangle((x0, y0), w, h, **kw))
            for dx in (0.1, w - 0.1):
                ax.plot([x0 + dx, x0 + dx], [y0, y0 + h], color=INK, lw=1.2)
        elif s == 'document':
            import numpy as np
            xs = np.linspace(x0, x0 + w, 50)
            ys = y0 + 0.06 * np.sin((xs - x0) / w * 2 * np.pi)
            ax.add_patch(Polygon(list(zip(xs, ys)) + [(x0 + w, y0 + h), (x0, y0 + h)], closed=True, **kw))
        elif s == 'manual input':
            ax.add_patch(Polygon([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h * 0.6)], closed=True, **kw))
        elif s == 'display':                        # pointed left side, rounded right side (ISO 5807)
            import numpy as np
            th = np.linspace(-np.pi / 2, np.pi / 2, 40)
            arc = [(x0 + w - h / 2 + h / 2 * np.cos(a_), cy + h / 2 * np.sin(a_)) for a_ in th]
            ax.add_patch(Polygon([(x0, cy), (x0 + 0.2, y0)] + arc + [(x0 + 0.2, y0 + h)], closed=True, **kw))
        elif s == 'preparation':
            ax.add_patch(Polygon([(x0 + 0.15, y0), (x0 + w - 0.15, y0), (x0 + w, cy), (x0 + w - 0.15, y0 + h),
                                  (x0 + 0.15, y0 + h), (x0, cy)], closed=True, **kw))
        elif s == 'off-page':
            ax.add_patch(Polygon([(cx - 0.25, y0 + h), (cx + 0.25, y0 + h), (cx + 0.25, y0 + 0.15), (cx, y0 - 0.05),
                                  (cx - 0.25, y0 + 0.15)], closed=True, **kw))
            ax.text(cx, cy + 0.06, 'A', ha='center', va='center', fontsize=10, weight='bold')
        elif s == 'stored data':
            ax.add_patch(Polygon([(x0 + 0.15, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0 + 0.15, y0 + h)], closed=True, **kw))
            ax.add_patch(Wedge((x0 + 0.15, cy), h / 2, 90, 270, fc=OR3, ec=INK, lw=1.2))
            ax.add_patch(Wedge((x0 + w, cy), h / 2, 90, 270, fc='white', ec=INK, lw=1.2))
        elif s == 'annotation':
            ax.plot([x0 + 0.25, x0, x0, x0 + 0.25], [y0 + h, y0 + h, y0, y0], color=INK, lw=1.2)
            ax.plot([x0 - 0.3, x0], [cy, cy], color=INK, lw=1.0, ls='--')
            ax.text(x0 + 0.1, cy, 'a note', fontsize=8, va='center', style='italic')
        elif s == 'manual op':
            ax.add_patch(Polygon([(x0, y0 + h), (x0 + w, y0 + h), (x0 + w - 0.15, y0), (x0 + 0.15, y0)], closed=True, **kw))
        elif s == 'merge':
            ax.add_patch(Polygon([(cx - 0.3, y0 + h), (cx + 0.3, y0 + h), (cx, y0)], closed=True, **kw))
        elif s == 'extract':
            ax.add_patch(Polygon([(cx - 0.3, y0), (cx + 0.3, y0), (cx, y0 + h)], closed=True, **kw))
        elif s == 'delay':
            ax.add_patch(Polygon([(x0, y0), (x0 + w - h / 2, y0), (x0 + w - h / 2, y0 + h), (x0, y0 + h)], closed=True, **kw))
            ax.add_patch(Wedge((x0 + w - h / 2, cy), h / 2, 270, 90, fc=OR3, ec=INK, lw=1.2))
            ax.plot([x0 + w - h / 2, x0 + w - h / 2], [y0 + 0.01, y0 + h - 0.01], color=OR3, lw=2)
        ax.text(cx, cy - 0.47, names[s], ha='center', va='center', fontsize=8.5, weight='bold')
    return save(fig, 'c05-symbols-more'), [names[s] for s in syms]


def symbols_page():
    name, names = symbols_picture()
    ok(len(names) == 12)
    t = head('More flowchart symbols', 'Sometimes asked',
             'The printed book (section 5.4) teaches the six symbols the syllabus needs. The international standard '
             'ISO 5807 has more. A few of them turn up in some school papers and books; none is needed to answer a '
             'CBSE question.')
    t += pic(name, 'Twelve more flowchart symbols', 1.15) + '\n\n'
    t += '''| Symbol | Used for | Example |
|---|---|---|
| Predefined process | a step whose details are written somewhere else (a sub-program) | "Find the grade (see chart 2)" |
| Document | a printed report or slip | "Print the receipt" |
| Manual input | data typed by hand at that moment | "Enter the PIN" |
| Display | a result shown on a screen | "Show the balance" |
| Preparation | setting up a counted loop | "i = 1 to 10" (some books draw FOR loops with it) |
| Off-page connector | the chart goes on to another page | (A) on page 1 → (A) on page 2 |
| Stored data | data kept in a file or a database | "Bank accounts" |
| Annotation | a note that explains a box; not a step | "PIN: 4 digits" |
| Manual operation | a step done by a person, not the computer | "Count the cash by hand" |
| Merge | several lists or flows joined into one | joining two class lists |
| Extract | taking some items out of a set | "Pick the students above 75" |
| Delay | waiting | "Wait 30 seconds for the card" |

**In the exam:** draw only the six symbols of the syllabus (terminal, input/output, process, decision, flow line,
connector). Input and output are both the parallelogram there, even when the input is typed by hand and the output
is shown on a screen.

## Connectors: when a flowchart does not fit

A long flowchart can be cut into pieces joined by **connectors**: a small circle with the same letter at the end of
one piece and the start of the next. An **on-page** connector (circle) joins pieces on the same page; an
**off-page** connector (the five-sided shape above) joins pieces on different pages. Each letter is used for one
join only.

## Why the shapes are what they are

- The **parallelogram** leans, like data sliding in or out.
- The **diamond** has corners for the ways out: one way in, Yes and No out.
- The **terminal** is rounded, so it can never be mistaken for a step.
- The **document** has a torn, wavy bottom, like a sheet torn off a printer.
'''
    write('sometimes-asked-more-symbols.md', t)


# ================================================================= 0513 more decompositions
def tree_picture(name, root, parts):
    """A structure diagram in the printed book's style: the root, its parts, and each part's sub-parts."""
    n = len(parts)
    cw = 1.32
    W_ = max(n * cw + 0.2, 3.0)
    fig, ax = canvas(W_, 2.25)
    xs = [0.1 + cw / 2 + i * cw for i in range(n)]
    mid = (xs[0] + xs[-1]) / 2
    rbox(ax, mid, 1.98, min(2.6, W_ - 0.2), 0.36, root, fc=OR, fs=9, weight='bold', color='white')
    ax.plot([xs[0], xs[-1]], [1.58, 1.58], color=INK, lw=1.2)
    ax.plot([mid, mid], [1.8, 1.58], color=INK, lw=1.2)
    for x, (head_, sub) in zip(xs, parts):
        arr(ax, (x, 1.58), (x, 1.42))
        rbox(ax, x, 1.23, cw - 0.1, 0.36, head_, fc=OR2, fs=8.5, weight='bold')
        arr(ax, (x, 1.05), (x, 0.92))
        rbox(ax, x, 0.5, cw - 0.1, 0.8, sub, fc=OR3, fs=8)
    return save(fig, name)


def decomposition_page():
    t = head('More systems, decomposed', 'Explained',
             'The printed book (section 5.9) decomposes a food-delivery app and a railway reservation system. Here '
             'are four more, each with its structure diagram, what each part does, and what the parts must agree '
             'on; then the report-card algorithm refined step by step.')
    systems = [
        ('c05-tree-school', 'A school management system',
         [('Admissions', 'forms\nfees\nclass and\nsection'), ('Attendance', 'daily register\nSMS to parents\nmonthly %'),
          ('Exams', 'timetable\nmarks entry\nreport cards'), ('Fees', 'fee slips\nUPI or bank\nreceipts'),
          ('Library', 'issue, return\nfines\ncatalogue')],
         'The roll number of a student: attendance, exams, fees and the library all use the same one.',
         'The report-card part (Exams) is the program of W6; it can be tested alone with sample marks before it is '
         'joined to the marks-entry screens.'),
        ('c05-tree-hospital', 'A hospital system',
         [('Registration', 'patient ID\nappointment\ntoken'), ('Doctors', 'consultation\nprescription\nreferral'),
          ('Laboratory', 'samples\nreports'), ('Pharmacy', 'medicines\nstock\nexpiry'), ('Billing', 'bill\ninsurance\nreceipt')],
         'The patient ID: the lab report and the medicines must reach the right patient.',
         'If the pharmacy part is changed (a new supplier), registration and billing need not change: this is why '
         'parts are kept separate.'),
        ('c05-tree-cricket', 'A school cricket tournament',
         [('Teams', 'register teams\nplayers\ncaptains'), ('Fixtures', 'groups\nmatch dates\ngrounds'),
          ('Scoring', 'ball by ball\nscorecard'), ('Points table', 'win 2, tie 1\nnet run rate'),
          ('Results', 'semi-finals\nfinal\nawards')],
         'The match result: scoring hands it to the points table, which decides the semi-finalists.',
         'Pattern recognition: every match has the same steps (toss, two innings, result), so one scoring part serves '
         'all the matches.'),
        ('c05-tree-upi', 'A UPI payment',
         [('Payer app', 'scan QR or\nenter UPI ID\namount'), ('Check', 'UPI PIN\nbalance\nlimits'),
          ('Transfer', 'payer\'s bank\nto payee\'s bank'), ('Confirm', 'messages to\nboth phones\nreceipt'),
          ('Safety', 'block fraud\ncomplaints\nrefunds')],
         'The transaction ID: every part writes it down, so a payment can be traced and a refund can find it.',
         'Abstraction: the payer sees only "Paid ✓"; the banks, the network and the checks stay hidden.')]
    for k, (name, title, parts, agree, note) in enumerate(systems, 1):
        ok(len(parts) == 5)
        t += f'## {k}. {title}\n\n'
        t += pic(tree_picture(name, title, parts), f'Structure diagram of {title.lower()}', 1.2) + '\n\n'
        t += '| Part | What it does |\n|---|---|\n'
        for h, sub in parts:
            t += f'| {h} | {sub.replace(chr(10), "; ")} |\n'
        t += f'\n- **The parts must agree on:** {agree}\n- {note}\n\n'
    G = F.GRADE
    out, _ = G.run([80, 75, 70, 72, 78])
    ok(out == ['Grade B'])
    t += '''## 5. Stepwise refinement: the report card, from one line to boxes

**Level 1** (the whole problem, in one line):

1. Make the report card.

**Level 2** (each line broken into steps):

1. Take the marks.
2. Work out the result.
3. Print the result.

**Level 3** (until each step can be one box of a flowchart):

1. Take the marks → *Input m1, m2, m3, m4, m5* (box 2 of W6).
2. Work out the result →
    1. total = m1 + … + m5; per = total ÷ 5; low = the lowest mark (box 3);
    2. Is low ≥ 33? No: the result is Fail (boxes 4, 5);
    3. Yes: is per ≥ 90? ≥ 75? ≥ 60? → the grade (boxes 6 to 12).
3. Print the result → the Print boxes 5, 7, 9, 11, 12.

This is **top-down design**: start from the whole and break it down. Its opposite, **bottom-up design**, starts from
small ready parts (a part that finds the lowest of five numbers, a part that prints) and joins them.

## 6. Try it yourself

**Decompose a school canteen app into five parts.**

'''
    t += answer('Menu (items, prices, today\'s specials); orders (cart, pre-order for the break); payment (UPI, '
                'canteen card, cash); kitchen (orders in the queue, ready alert); feedback (ratings, complaints). '
                'They must agree on the order number.')
    write('explained-more-decompositions.md', t)


# ================================================================= 0506 five-step practice
def five_step_page():
    worked = [
        dict(q='A bank pays simple interest. Input the principal, the rate (% per year) and the time (years), and '
             'print the interest SI = P × R × T ÷ 100.',
             read='Given P, R, T. Asked: SI.', mark='input (input) · print (output) · "SI = …" (a formula: process).',
             list_=['Input P, R, T.', 'Compute SI = P × R × T ÷ 100.', 'Print SI.'],
             steps=[('in', ['p', 'r', 't']), ('do', 'si = p * r * t / 100'), ('out', 'si')],
             ref=lambda p, r, t: [str(p * r * t / 100)], tests=[(1000, 5, 2), (2500, 8, 3), (100, 0, 5)],
             runs=[(1000, 5, 2), (100, 0, 5)], pattern='sequence'),
        dict(q='Input the age of a person and print whether the person can vote (18 or more).',
             read='Given age. Asked: "Can vote" or "Cannot vote yet".', mark='input · whether (decision) · print (output).',
             list_=['Input age.', 'Is age ≥ 18? Yes: print "Can vote". No: print "Cannot vote yet".'],
             steps=[('in', ['age']), ('if', 'age >= 18', [('out', "'Can vote'")], [('out', "'Cannot vote yet'")])],
             ref=lambda a: ['Can vote' if a >= 18 else 'Cannot vote yet'], tests=[(18,), (17,), (45,)],
             runs=[(18,), (17,)], pattern='one choice'),
        dict(q='An electricity board charges ₹5 a unit for the first 100 units and ₹7 a unit after that. Input the '
             'units and print the bill.',
             read='Given units. Asked: the bill.', mark='input · "for the first 100 … after that" (a hidden decision) · '
             'charges (process) · print.',
             list_=['Input units.', 'Is units ≤ 100? Yes: bill = units × 5. No: bill = 500 + (units − 100) × 7.',
                    'Print bill.'],
             steps=[('in', ['units']), ('if', 'units <= 100', [('do', 'bill = units * 5')],
                                        [('do', 'bill = 500 + (units - 100) * 7')]), ('out', 'bill')],
             ref=lambda u: [str(u * 5 if u <= 100 else 500 + (u - 100) * 7)], tests=[(80,), (100,), (101,), (250,)],
             runs=[(250,), (100,)], pattern='one choice'),
        dict(q='A cinema charges ₹100 for children under 12, ₹120 for people of 60 or more, and ₹200 for others. '
             'Input the age and print the price.',
             read='Given age. Asked: the price.', mark='input · "under 12", "60 or more", "others" (a ladder of '
             'decisions) · print.',
             list_=['Input age.', 'Is age < 12? Yes: price 100.', 'No: is age ≥ 60? Yes: price 120. No: price 200.',
                    'Print price.'],
             steps=[('in', ['age']), ('if', 'age < 12', [('do', 'price = 100')],
                                      [('if', 'age >= 60', [('do', 'price = 120')], [('do', 'price = 200')])]),
                    ('out', 'price')],
             ref=lambda a: [str(100 if a < 12 else 120 if a >= 60 else 200)], tests=[(11,), (12,), (59,), (60,), (75,)],
             runs=[(12,), (60,)], pattern='a ladder (nested choice)'),
        dict(q='Input a year and print whether it is a leap year. (A year divisible by 400 is leap; otherwise one '
             'divisible by 100 is not; otherwise one divisible by 4 is.)',
             read='Given year. Asked: "Leap" or "Not leap".', mark='input · "divisible", "otherwise" (decisions, in '
             'order) · print.',
             list_=['Input y.', 'Divisible by 400? Yes: Leap.', 'No: divisible by 100? Yes: Not leap.',
                    'No: divisible by 4? Yes: Leap. No: Not leap.'],
             steps=[('in', ['y']), ('if', 'y % 400 == 0', [('out', "'Leap'")],
                                    [('if', 'y % 100 == 0', [('out', "'Not leap'")],
                                      [('if', 'y % 4 == 0', [('out', "'Leap'")], [('out', "'Not leap'")])])])],
             ref=lambda y: ['Leap' if (y % 400 == 0 or (y % 4 == 0 and y % 100)) else 'Not leap'],
             tests=[(2000,), (1900,), (2024,), (2023,), (2100,)], runs=[(1900,), (2024,)], pattern='a ladder'),
        dict(q='Input n and print its multiplication table up to 10 (n × 1 = …, n × 2 = …).',
             read='Given n. Asked: 10 lines.', mark='input · "up to 10" (a counted loop) · print.',
             list_=['Input n; set i = 1.', 'While i ≤ 10: print "n × i = n·i"; increase i by 1.'],
             steps=[('in', ['n']), ('do', 'i = 1'),
                    ('while', 'i <= 10', [('out', "str(n) + ' x ' + str(i) + ' = ' + str(n * i)",
                                           {'text': 'Print n × i = n·i'}), ('do', 'i = i + 1')])],
             ref=lambda n: [f'{n} x {i} = {n * i}' for i in range(1, 11)], tests=[(7,), (1,)], runs=[(7,)],
             pattern='counted loop'),
        dict(q='Input a whole number and print the sum of its digits (for 4096: 4 + 0 + 9 + 6 = 19).',
             read='Given n. Asked: the sum of the digits.', mark='input · "each digit" (a loop until nothing is '
             'left) · sum (process) · print.',
             list_=['Input n; set s = 0.', 'While n > 0: add the last digit (n mod 10) to s; drop the last digit '
                    '(n div 10).', 'Print s.'],
             steps=[('in', ['n']), ('do', 's = 0'),
                    ('while', 'n > 0', [('do', 's = s + n % 10', {'text': 's = s + last digit\n(n mod 10)'}),
                                        ('do', 'n = n // 10', {'text': 'n = n div 10'})]),
                    ('out', 's')],
             ref=lambda n: [str(sum(int(c) for c in str(n)))], tests=[(4096,), (7,), (0,), (1001,)],
             runs=[(4096,), (0,)], pattern='loop until a condition'),
        dict(q='Marks are typed one at a time; −1 ends the list. Count how many students passed (33 or more).',
             read='Given marks, then −1. Asked: how many passed.', mark='"one at a time", "ends" (a loop until −1) · '
             '"passed" (a decision inside the loop) · count (process) · print.',
             list_=['Set c = 0; input m.', 'While m ≠ −1: if m ≥ 33, add 1 to c; input the next m.', 'Print c.'],
             steps=[('do', 'c = 0'), ('in', ['m']),
                    ('while', 'm != -1', [('if', 'm >= 33', [('do', 'c = c + 1')]), ('in', ['m'])]),
                    ('out', 'c')],
             ref=lambda *ms: [str(sum(1 for m in ms[:ms.index(-1)] if m >= 33))],
             tests=[(45, 20, 33, 90, -1), (-1,), (10, 32, -1)], runs=[(45, 20, 33, -1), (-1,)],
             pattern='a loop with a choice inside')]
    t = head('The five-step method, practised', 'Practice',
             'The printed book (section 5.5) gives the five steps Read, Mark, List, Draw, Check, worked on the ATM. '
             'Here are eight more questions worked the same way, from easy to hard, and six to try.')
    t += '''Each worked question shows: **Read** (what is given, what is asked), **Mark** (the signal words and their
shapes), **List** (the steps in plain words), **Draw** (the flowchart) and **Check** (two dry runs, a normal value
and a boundary value).

'''
    for k, wq in enumerate(worked, 1):
        algo = make(f'c05-five-{k}', f'Five-step {k}', wq['steps'], [(list(c), wq['ref'](*c)) for c in wq['tests']])
        t += f'## {k}. {wq["q"]}\n\n*Pattern: {wq["pattern"]}.*\n\n'
        t += f'- **Read.** {wq["read"]}\n- **Mark.** {wq["mark"]}\n- **List.**\n'
        for i, s in enumerate(wq['list_'], 1):
            t += f'    {i}. {s}\n'
        t += '- **Draw.**\n\n' + pic(drawn(algo), f'Flowchart for question {k}', 1.15) + '\n\n- **Check.**\n\n'
        for c in wq['runs']:
            out, path = run_path(algo, list(c))
            ok(out == wq['ref'](*c))
            shown = ', '.join(out) if len(out) <= 3 else f'{out[0]} … {out[-1]} ({len(out)} lines)'
            t += f'    - Input {", ".join(map(str, c))}: boxes {" → ".join(map(str, path)) if len(path) <= 16 else " → ".join(map(str, path[:12])) + " → …"}; prints **{shown}**.\n'
        t += '\n'
    tries = [
        ('Input a temperature in Celsius and print it in Fahrenheit (F = C × 9 ÷ 5 + 32).',
         [('in', ['c']), ('do', 'f = c * 9 / 5 + 32'), ('out', 'f')], lambda c: [str(c * 9 / 5 + 32)], [(100,), (0,), (37,)]),
        ('Input a number and print "Positive", "Negative" or "Zero".',
         [('in', ['n']), ('if', 'n > 0', [('out', "'Positive'")], [('if', 'n < 0', [('out', "'Negative'")], [('out', "'Zero'")])])],
         lambda n: ['Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'], [(5,), (-3,), (0,)]),
        ('A shop gives 10% off on a bill above ₹5,000 and 5% off otherwise. Input the bill and print the amount to pay.',
         [('in', ['bill']), ('if', 'bill > 5000', [('do', 'pay = bill - bill * 10 / 100')], [('do', 'pay = bill - bill * 5 / 100')]),
          ('out', 'pay')], lambda b: [str(b - b * 10 / 100 if b > 5000 else b - b * 5 / 100)], [(6000,), (5000,), (100,)]),
        ('Input n and print the sum 1 + 2 + … + n using a loop.',
         [('in', ['n']), ('do', 's = 0; i = 1'), ('while', 'i <= n', [('do', 's = s + i'), ('do', 'i = i + 1')]), ('out', 's')],
         lambda n: [str(n * (n + 1) // 2)], [(10,), (1,), (0,)]),
        ('Input a whole number and print how many digits it has (0 has 1 digit).',
         [('in', ['n']), ('do', 'd = 1'), ('while', 'n >= 10', [('do', 'n = n // 10', {'text': 'n = n div 10'}), ('do', 'd = d + 1')]),
          ('out', 'd')], lambda n: [str(len(str(n)))], [(0,), (7,), (4096,), (100,)]),
        ('Numbers are typed until 0. Print the largest of them (the first number is not 0).',
         [('in', ['x']), ('do', 'big = x'), ('while', 'x != 0', [('if', 'x > big', [('do', 'big = x')]), ('in', ['x'])]), ('out', 'big')],
         lambda *xs: [str(max(xs[:xs.index(0)]))], [(4, 9, 2, 0), (5, 0), (-3, -1, -8, 0)])]
    t += '## Try these\n\nWork the five steps on paper; then open the answer: the list and the flowchart, tested.\n\n'
    for k, (q, steps, ref, tests) in enumerate(tries, 1):
        algo = make(f'c05-five-try-{k}', f'Try {k}', steps, [(list(c), ref(*c)) for c in tests])
        runs = '; '.join(f'{", ".join(map(str, c))} → {", ".join(algo.run(list(c))[0])}' for c in tests)
        code = algo.pseudocode_md()
        t += f'**{k}. {q}**\n\n'
        t += answer(f'```text\n{code}\n```\n\n' + pic(drawn(algo), f'Flowchart for try {k}', 1.1) +
                    f'\n\nTested: {runs}.')
    write('practice-five-step-method.md', t)


# ================================================================= 0508 the 22 practical charts
def practicals_page():
    t = head('The 22 practical programs as flowcharts', 'Practical',
             'The CBSE practical list for Class XI asks for these programs. For each: the flowchart (the numbers on '
             'the boxes are the step numbers), the pseudocode, the Python program and a walk-through. Every flowchart '
             'and every program was run on many inputs and compared with a separate check.')
    t += '| No. | Program | Pattern |\n|:-:|---|---|\n'
    pat = {1: 'sequence', 2: 'one choice', 3: 'choices in a row', 4: 'loop inside a loop', 5: 'loop inside a loop',
           6: 'loop inside a loop', 7: 'counted loop', 8: 'counted loop', 9: 'counted loop', 10: 'counted loop',
           11: 'loop, then one choice', 12: 'loop, then one choice', 13: 'loop, then one choice',
           14: 'loop with an early stop', 15: 'counted loop', 16: 'loop until the remainder is 0',
           17: 'loop over the characters, choices inside', 18: 'loop over the characters', 19: 'loop over the items',
           20: 'loop over the items, two at a time', 21: 'loop with an early stop', 22: 'two loops'}
    for num, slug, title, words, algo, walk, note in PR.P:
        t += f'| {num} | [{title}](#{num}-{slug}) | {pat[num]} |\n'
    t += '\n*Chapters 11, 12 and 14 print the string, list and dictionary programs (17 to 22) beside their Python again, when you learn them.*\n\n'
    for num, slug, title, words, algo, walk, note in PR.P:
        t += f'## {num}. {title} {{ #{num}-{slug} }}\n\n*The syllabus:* {words}\n\n'
        t += pic(drawn(algo), f'Flowchart of practical {num}', 1.15, cap=640) + '\n\n'
        t += grid2(f'**Pseudocode**\n\n```text\n{algo.pseudocode_md()}\n```',
                   f'**Python**\n\n```python\n{algo.python.rstrip()}\n```')
        out, _ = algo.run(walk)
        ok(out == algo.run_python(walk))
        shown = ', '.join(map(str, walk))
        t += f'\n**Walk-through for the input {shown}**\n\n' + walk_md(algo, walk, telling=True) + '\n'
        t += f'**Output:** {" / ".join(out)}\n\n'
        if note:
            t += f'*Note:* {note}\n\n'
        t += f'*Tested on {len(algo.tests)} inputs: the flowchart and the Python gave the expected answer every time.*\n\n'
    write('practical-flowcharts.md', t)


# ================================================================= the card game (print Q13)
def card_game_page():
    def ref(suit, value):
        if suit in ('diamond', 'club'):
            return ['TIGERS']
        if suit == 'heart' and value.isdigit():
            return ['LIONS']
        if suit == 'heart':
            return ['TIGERS']
        return ['LIONS']
    suits = ['diamond', 'club', 'heart', 'spade']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    algo = make('c05-card-game', 'The card game',
                [('in', ['suit', 'value']),
                 ('if', "suit == 'diamond' or suit == 'club'", [('out', "'TIGERS'")],
                  [('if', "suit == 'heart' and value.isdigit()", [('out', "'LIONS'")],
                    [('if', "suit == 'heart'", [('out', "'TIGERS'")], [('out', "'LIONS'")])],
                    {'text': 'heart AND\na number?'})],
                  {'text': 'diamond OR\nclub?'})],
                [([s, v], ref(s, v)) for s in suits for v in values], types={'suit': 'str', 'value': 'str'})
    ok(len(algo.tests) == 52)
    tally = {'TIGERS': 0, 'LIONS': 0}
    for s in suits:
        for v in values:
            tally[algo.run([s, v])[0][0]] += 1
    ok(tally == {'TIGERS': 30, 'LIONS': 22})
    t = head('The card game, in full', 'Explained',
             'Question 13 of the printed chapter: two teams, TIGERS and LIONS, and a card drawn from a pack. Here is '
             'the whole algorithm as a flowchart, run for all 52 cards.')
    t += '''**The rules.** If the card is a diamond or a club, TIGERS get a point. If it is a heart with a number
(2 to 10), LIONS get a point. If it is a heart without a number (ace, jack, queen, king), TIGERS get a point.
Any other card (a spade) gives LIONS a point.

'''
    t += pic(drawn(algo), 'The card game flowchart', 1.15) + '\n\n'
    t += f'```text\n{algo.pseudocode_md()}\n```\n\n'
    t += '## Every card\n\n| Suit | ' + ' | '.join(values) + ' |\n|---|' + ':-:|' * 13 + '\n'
    for s in suits:
        t += f'| {s}s | ' + ' | '.join('T' if algo.run([s, v])[0][0] == 'TIGERS' else 'L' for v in values) + ' |\n'
    t += (f'\nT = TIGERS, L = LIONS. Over the whole pack TIGERS win **{tally["TIGERS"]}** cards and LIONS '
          f'**{tally["LIONS"]}**: 13 diamonds + 13 clubs + 4 hearts without a number = 30 for TIGERS.\n\n')
    for s, v in [('heart', '7'), ('spade', 'K')]:
        out, path = run_path(algo, [s, v])
        t += f'- **{v} of {s}s:** boxes {" → ".join(map(str, path))}: **{out[0]}**.\n'
    t += '\n*Why AND, why OR?* "a diamond **or** a club" is Yes if either is true; "a heart **and** a number" needs both.\n'
    write('explained-card-game.md', t)


# ================================================================= 0501 the index
def index_page():
    t = '''# Chapter 5: Problem Solving

The online pages of Chapter 5 of *Computer Science with Python, CBSE Class XI*. The label under each QR code in the
printed book says what you will find:

- **Explained**: a topic of the book explained more fully, with more examples;
- **Step by step**: one algorithm, every step drawn;
- **Practical**: the CBSE practical programs;
- **See it**: interactive: type the inputs, and watch;
- **Sometimes asked**: beyond the syllabus wording, but set now and then in school papers;
- **Practice**, **Revise**: questions with answers, flashcards and the glossary.

| Page | Label | Section of the book |
|---|---|---|
| [Testing and debugging the report-card program](explained-testing-and-debugging.md) | Explained | 5.2 |
| [The ATM algorithm, run by run](explained-atm-algorithm.md) | Explained | 5.3 |
| [Euclid's GCD, step by step](step-by-step-euclid-gcd.md) | Step by step | 5.3 |
| [More flowchart symbols](sometimes-asked-more-symbols.md) | Sometimes asked | 5.4 |
| [The five-step method, practised](practice-five-step-method.md) | Practice | 5.5 |
| [The dry-run player: W1 to W10](see-it-dry-run-player.md) | See it | 5.5 |
| [The 22 practical programs as flowcharts](practical-flowcharts.md) | Practical | 5.5 |
| [Pseudocode to Python, line for line](explained-pseudocode-to-python.md) | Explained | 5.6 |
| [Trace tables, with more to fill in](practice-trace-tables.md) | Practice | 5.7 |
| [Halving search, step by step](step-by-step-halving-search.md) | Step by step | 5.8 |
| [The four prime tests, worked](explained-prime-tests.md) | Explained | 5.8 |
| [More systems, decomposed](explained-more-decompositions.md) | Explained | 5.9 |
| [The card game, in full](explained-card-game.md) | Explained | Question 13 |
| [Questions with answers, by type](questions/index.md) | Practice | the whole chapter |
| [Flashcards](flashcards.md) and [glossary](glossary.md) | Revise | the whole chapter |

The Python programs of this chapter can be run in Google Colab with Chapter 6, when you start Python.

## Full-colour pictures

Large full-colour versions of the pictures of the printed chapter.

**The report-card program** (section 5.2): the class teacher checks the program's result against a printed report card.

![The class teacher checks the report-card program](../../assets/images/ch05/colour-reportcard.jpg)

**Cash from an ATM** (section 5.3): the card in one hand, the PIN typed with the other.

![A student at an ATM](../../assets/images/ch05/colour-atm.jpg)

**A food-delivery app** (section 5.9): many parts of the app worked together so that the parcel changes hands.

![The parcel changes hands at the gate](../../assets/images/ch05/colour-delivery.jpg)
'''
    write('index.md', t)


ALL = [atm_page, testing_page, halving_page, primes_page, pseudo_python_page, trace_page, symbols_page,
       decomposition_page, five_step_page, practicals_page, card_game_page, index_page]

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for f in ALL:
        if not only or f.__name__ in only:
            f()
    print(P1.checks, 'checks passed')
