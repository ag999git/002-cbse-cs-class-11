"""Chapter 6: the four Colab notebooks (QR 0620) and their page (28 Nov 2026; online plan v2, plan v1 section 9).
  notebooks/ch06-1-first-steps.ipynb        cells vs the shell vs a script, print(), comments
  notebooks/ch06-2-tokens-lab.ipynb         tokens of any line, the 35 keywords, a name checker, literal types
  notebooks/ch06-3-names-and-objects.ipynb  id() and type(), re-assignment, two names one object, swaps, L-value errors
  notebooks/ch06-4-practice.ipynb           25 tasks with self-check cells
Pattern (plan v1 §9): Learn cells, Predict-first cells, Modify tasks, self-check cells ("Well done" or a hint), practice.
Every notebook is RUN here twice before it is written: (1) as published, with the blanks a student fills: every
check must answer "not yet" without crashing; (2) with the model answers put in the blanks: every check must say
"Well done". Cells meant to show an error must raise exactly that error.
Run from the repository root:  python tools/ch06_notebooks.py"""
import contextlib
import hashlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NB = ROOT / 'notebooks'
D = ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python'
COLAB = 'https://colab.research.google.com/github/ag999git/002-cbse-cs-class-11/blob/main/notebooks/'
PYV = sys.version.split()[0]
checks = 0


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def h(s):
    """The short fingerprint a self-check compares (so the answer is not printed in the notebook)."""
    return hashlib.sha256(str(s).strip().encode()).hexdigest()[:12]


HEAD = ('*Computer Science with Python, CBSE Class XI · Chapter 6 online notebook.* Click a cell and press **Shift + Enter** '
        'to run it. Change anything and run it again: nothing can break. **Predict first** means: write what you expect in '
        'the comment at the top of the cell, then run it and compare.')

CHECKER = '''# Run this cell first. It makes the self-check helpers; you do not need to understand it yet.
import hashlib

def check(task, answer, code):
    """Compare your answer with the right one without showing the right one."""
    given = str(answer).strip() if answer is not None else ''
    if given == '':
        print(f'Task {task}: not answered yet.')
    elif hashlib.sha256(given.encode()).hexdigest()[:12] == code:
        print(f'Task {task}: Well done!')
    else:
        print(f'Task {task}: Not yet. Run the code again and look carefully.')

def check_that(task, test, hint):
    """Run a small test of your code."""
    try:
        passed = test()
    except Exception:
        passed = False
    print(f'Task {task}: Well done!' if passed else f'Task {task}: Not yet. Hint: {hint}')'''


# ================================================================= 6-1 first steps
NB1 = ('ch06-1-first-steps.ipynb', 'Notebook 6-1: First steps', [
    ('md', '# Notebook 6-1: First steps in Python\n\n' + HEAD),
    ('md', '## 1. A cell is like the shell\n\nIn a notebook cell, the value of the **last line** is shown, as in the shell. '
           'Run this cell.'),
    ('code', '7 + 5'),
    ('md', 'Only the **last** bare value is shown. Predict first, then run:'),
    ('code', '# My prediction:\n7 + 5\n2 * 10'),
    ('md', 'In a **script** (IDLE, Thonny, VS Code), neither line would show anything: a script shows only what you `print`. '
           'This is **the Colab trap** of section 6.3. Use `print` and both appear, in a cell and in a script:'),
    ('code', 'print(7 + 5)\nprint(2 * 10)'),
    ('md', '## 2. `print()`\n\n`print()` shows what is inside its brackets. Text in quotes appears exactly as typed; a sum '
           'is worked out first; commas separate values with a space.'),
    ('code', 'print("Hello, world!")\nprint("7 + 5")\nprint(7 + 5)\nprint("Total:", 90 + 85)'),
    ('md', '**Modify:** change the last line so that it prints `Total marks: 175`. Run it.'),
    ('code', 'print("Total:", 90 + 85)'),
    ('md', '## 3. Comments\n\nPython skips everything from `#` to the end of the line. Predict first:'),
    ('code', '# My prediction:\nprint("one")      # this note is skipped\n# print("two")\nprint("three")'),
    ('md', '## 4. Notes over several lines\n\nTwo ways (section 6.8). Both are skipped when the program runs:'),
    ('code', '# Line 1\n# Line 2\nprint("Hash notes were skipped")\n\n"""\nLine 1\nLine 2\n"""\nprint("The triple-quoted note was skipped too")'),
    ('md', '## 5. An error message\n\nRun this cell. Read the **last line** of the message, then correct the cell and run it '
           'again (Python is case-sensitive).'),
    ('error', 'Print("Namaste")', 'NameError'),
    ('md', '## Your turn\n\n**Make:** write a cell that prints your name, your class and your school on three lines, with a '
           'comment at the top saying what the program does.'),
    ('code', '# My program: \n'),
])


# ================================================================= 6-2 tokens lab
NB2 = ('ch06-2-tokens-lab.ipynb', 'Notebook 6-2: Tokens lab', [
    ('md', '# Notebook 6-2: Tokens lab\n\n' + HEAD),
    ('md', '## 1. See the tokens of any line\n\nPython\'s own `tokenize` module cuts a line into tokens. The small '
           'function below names each one as the book does (section 6.4). Run it, then change `line` and run again.'),
    ('code', '''import io, keyword, tokenize

def show_tokens(line):
    count = 0
    for t in tokenize.generate_tokens(io.StringIO(line + "\\n").readline):
        if t.type == tokenize.NAME:
            kind = "keyword" if keyword.iskeyword(t.string) else "identifier"
        elif t.type in (tokenize.NUMBER, tokenize.STRING):
            kind = "literal"
        elif t.type == tokenize.OP:
            kind = "punctuator" if t.string in "()[]{},:.;@" else "operator"
        elif t.type == tokenize.COMMENT:
            print(f"{t.string:<12} comment: skipped, not a token")
            continue
        else:
            continue
        count += 1
        print(f"{t.string:<12} {kind}")
    print(count, "tokens")

line = 'if marks >= 33: print("Pass")   # result'
show_tokens(line)'''),
    ('md', '**Predict first:** how many tokens are in `total = price * 2 + tax`? Then run.'),
    ('code', '# My prediction:\nshow_tokens("total = price * 2 + tax")'),
    ('md', '## 2. The keywords\n\nPython lists its own keywords. Count them, and find the three with capital letters.'),
    ('code', 'import keyword\nprint(len(keyword.kwlist))\nprint(keyword.kwlist)\nprint([k for k in keyword.kwlist if k[0].isupper()])'),
    ('md', '## 3. Is this a valid name?\n\n`str.isidentifier()` checks the rules for the characters; `keyword.iskeyword()` '
           'checks the reserved words. A valid name needs both.'),
    ('code', '''def valid_name(name):
    return name.isidentifier() and not keyword.iskeyword(name)

for name in ["marks", "2nd_rank", "my marks", "for", "For", "_total", "sum$", "नाम"]:
    print(f"{name!r:<12} {valid_name(name)}")'''),
    ('md', '**Modify:** add three names of your own to the list, predict, and run.'),
    ('md', '## 4. Literals and their types\n\n`type()` tells the type of each value.'),
    ('code', 'for value in [33, 3.5, "33", True, None, 2+3j, 0b101, 0o17, 0x1F, 2.5e3]:\n    print(repr(value), type(value))'),
    ('md', '## 5. Escape sequences\n\nPredict the output and the length, then run.'),
    ('code', '# My prediction:\ntext = "Name:\\tAsha\\nClass:\\tXI"\nprint(text)\nprint(len(text))'),
    ('md', '## Your turn\n\n**Make:** use `show_tokens` on three lines from your own programs. Which kind of token is most '
           'common?'),
    ('code', 'show_tokens("x, y = y, x")'),
])


# ================================================================= 6-3 names and objects
NB3 = ('ch06-3-names-and-objects.ipynb', 'Notebook 6-3: Names and objects lab', [
    ('md', '# Notebook 6-3: Names and objects lab\n\n' + HEAD + '\n\nA variable is a **name tied to an object** (section 6.7). '
           '`id()` gives an object\'s identity number; `type()` gives its type.'),
    ('md', '## 1. Two names, one object'),
    ('code', 'marks = 95\ntotal = marks\nprint(id(marks) == id(total))\nprint(type(marks), type(total))'),
    ('md', '## 2. Re-assigning moves only one tag\n\nPredict first: what are `x` and `y` at the end?'),
    ('code', '# My prediction:\nx = 3\ny = x\nx = x + 2\nprint(x, y)\nprint(id(x) == id(y))'),
    ('md', '## 3. Dynamic typing\n\nThe same name, tied to objects of different types:'),
    ('code', 'marks = 92\nprint(type(marks))\nmarks = "A+"\nprint(type(marks))\nmarks = 9.2\nprint(type(marks))'),
    ('md', 'Python is still **strongly** typed: it never mixes types quietly. Run this and read the last line of the error.'),
    ('error', 'print("5" + 3)', 'TypeError'),
    ('md', '## 4. Swapping\n\nWith a third variable (the empty third glass), and Python\'s way:'),
    ('code', 'x, y = 5, 7\nt = x\nx = y\ny = t\nprint(x, y)\n\nx, y = y, x\nprint(x, y)'),
    ('md', '**Modify:** rotate three values so that `a` gets `b`\'s value, `b` gets `c`\'s and `c` gets `a`\'s, in one line.'),
    ('code', 'a, b, c = 1, 2, 3\n# your line here\nprint(a, b, c)'),
    ('md', '## 5. The L-value must be a name\n\nRun this cell. Why is it an error? (Section 6.7: `=` is an assignment, not '
           'an equation.)'),
    ('error', '10 = x', 'SyntaxError'),
    ('md', '## 6. A name used before it has a value'),
    ('error', 'print(totl)', 'NameError'),
    ('md', '## Your turn\n\n**Make:** a shop sells pens at ₹10. Tie `price` to 10 and `bill` to `price * 3`. Then change '
           '`price` to 12 and print `bill`. Predict first: does the bill change? Why?'),
    ('code', '# My prediction:\n'),
])


# ================================================================= 6-4 practice with self-checks
PRED = [  # (task, program); the answer is the program's output, which Python makes here
    (1, 'print(7 + 5, 7 * 5)'), (2, 'print("7" + "5")'), (3, 'x = 10\nx = x + 5\nprint(x)'),
    (4, 'a = 3\nb = a\na = 4\nprint(a, b)'), (5, 'x, y = 2, 9\nx, y = y, x\nprint(x, y)'),
    (6, 'print(len("a b c"))'), (7, 'print(0b11 + 0x11)'), (8, 'x = 5\ny = x * 2\nx = 100\nprint(y)'),
    (9, 'print(type(7.0))'), (10, 'a = b = 7\nb = b + 1\nprint(a, b)'),
]


def practice_cells():
    cells = [('md', '# Notebook 6-4: Practice and self-check\n\n' + HEAD + '\n\nFirst run the helper cell. Then, for '
                    'each task, type your answer where it says `None`, run the cell, and run its check. A check says '
                    '**Well done!** or **Not yet**, without showing the answer.'),
             ('code', CHECKER),
             ('md', '## Part A: Predict the output (tasks 1–10)\n\nRead the program, **do not run it**, and type the output '
                    'you expect as text, for example `answer_1 = "12 35"`. Then run the check. If it says *Not yet*, '
                    'run the program and find out why.')]
    sol = {}
    for k, prog in PRED:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(prog, {})
        o = buf.getvalue().strip()
        ok('\n' not in o, prog)
        cells += [('md', f'**Task {k}.**'), ('code', f'# The program (do not run it yet):\n# ' + prog.replace('\n', '\n# ')),
                  ('task', f'answer_{k} = None   # type the output here, in quotes', f'answer_{k} = {o!r}'),
                  ('check', f'check({k}, answer_{k}, "{h(o)}")')]
        sol[k] = o
    cells.append(('md', '## Part B: Names (tasks 11–15)\n\nType a name in quotes.'))
    names = [(11, 'a valid Python name, in snake_case, for "number of students"',
              'lambda: answer_11.isidentifier() and answer_11 == answer_11.lower() and "_" in answer_11 and not __import__("keyword").iskeyword(answer_11)',
              'small letters joined by _', '"number_of_students"'),
             (12, 'a name for the constant "pass mark"',
              'lambda: answer_12.isidentifier() and answer_12.isupper()', 'CAPITALS joined by _', '"PASS_MARK"'),
             (13, 'a keyword that begins with a capital letter, other than True',
              'lambda: answer_13 in ("False", "None")', 'there are only three such keywords', '"None"'),
             (14, 'a name that LOOKS like a keyword but is not one',
              'lambda: answer_14.isidentifier() and not __import__("keyword").iskeyword(answer_14) and any(k.lower() == answer_14.lower() for k in __import__("keyword").kwlist)',
              'change one letter to a capital: For, Pass, IF ...', '"Pass"'),
             (15, 'an INVALID name (any reason)', 'lambda: not answer_15.isidentifier() or __import__("keyword").iskeyword(answer_15)',
              'begin with a digit, or use a space, -, $', '"2nd_rank"')]
    for k, what, test, hint, model in names:
        cells += [('md', f'**Task {k}.** Type {what}.'), ('task', f'answer_{k} = None', f'answer_{k} = {model}'),
                  ('check', f'check_that({k}, {test}, "{hint}")')]
    cells.append(('md', '## Part C: Write the code (tasks 16–20)'))
    writes = [(16, 'Tie `bus_fare` to 25 and `days` to 22, and `monthly_fare` to their product.',
               'bus_fare = None\ndays = None\nmonthly_fare = None', 'bus_fare = 25\ndays = 22\nmonthly_fare = bus_fare * days',
               'lambda: monthly_fare == 550 and bus_fare == 25', 'monthly_fare = bus_fare * days'),
              (17, 'Swap `left` and `right` in ONE line.', 'left, right = "L", "R"\n# your line here',
               'left, right = "L", "R"\nleft, right = right, left', 'lambda: (left, right) == ("R", "L")', 'left, right = right, left'),
              (18, 'Tie `three_lines` to ONE string that prints on three lines: Delhi, Mumbai, Chennai.',
               'three_lines = None', 'three_lines = """Delhi\nMumbai\nChennai"""',
               'lambda: three_lines.split("\\n") == ["Delhi", "Mumbai", "Chennai"]', 'use triple quotes, or \\n'),
              (19, 'Tie `a`, `b` and `c` to the SAME object 0 in one line.', 'a = b = c = None', 'a = b = c = 0',
               'lambda: a == 0 and id(a) == id(b) == id(c)', 'a = b = c = 0'),
              (20, 'Tie `x` to 5, then tie it to the text "five" (dynamic typing).', 'x = None', 'x = 5\nx = "five"',
               'lambda: x == "five"', 'the same name can be tied to a str')]
    for k, what, blank, model, test, hint in writes:
        cells += [('md', f'**Task {k}.** {what}'), ('task', blank, model), ('check', f'check_that({k}, {test}, "{hint}")')]
    cells.append(('md', '## Part D: Find and correct the error (tasks 21–25)\n\nRun each cell: it stops with an error. '
                        'Read the last line, correct the cell, run it again, then run the check.'))
    fixes = [(21, 'marks = 90\ntotal_21 = Marks + 5', 'marks = 90\ntotal_21 = marks + 5', 'lambda: total_21 == 95', 'Python is case-sensitive'),
             (22, 'roll-no = 12', 'roll_no = 12', 'lambda: roll_no == 12', 'use _ instead of -'),
             (23, 'total marks = 450', 'total_marks = 450', 'lambda: total_marks == 450', 'no space in a name'),
             (24, "city = 'Pune\"", 'city = "Pune"', 'lambda: city == "Pune"', 'the opening and closing quotes must be the same'),
             (25, 'class = "XI-A"', 'section = "XI-A"', 'lambda: section == "XI-A"', 'class is a keyword: call it section')]
    for k, bad, good, test, hint in fixes:
        cells += [('md', f'**Task {k}.**'), ('fix', bad, good), ('check', f'check_that({k}, {test}, "{hint}")')]
    cells.append(('md', '**Finished?** Run every check again from the top (Runtime → Run all) to see all 25 answers.'))
    return cells


NB4 = ('ch06-4-practice.ipynb', 'Notebook 6-4: Practice and self-check', practice_cells())


# ================================================================= run and write
def run_nb(cells, solutions):
    """Run the code cells in one namespace (like a notebook); return the printed text."""
    env, buf = {}, io.StringIO()
    with contextlib.redirect_stdout(buf):
        for c in cells:
            kind = c[0]
            if kind in ('code', 'check'):
                exec(c[1], env)
            elif kind == 'task':
                exec(c[2] if solutions else c[1], env)
            elif kind == 'fix':
                if solutions:
                    exec(c[2], env)
                else:
                    try:
                        exec(c[1], env)
                        raise AssertionError('a "find the error" cell ran without error: ' + c[1])
                    except SyntaxError:
                        pass
                    except (NameError, TypeError):
                        pass
            elif kind == 'error':
                try:
                    exec(compile(c[1], '<cell>', 'exec'), env)
                    raise AssertionError('no error: ' + c[1])
                except SyntaxError as e:
                    ok(c[2] == 'SyntaxError', (c[1], e))
                except Exception as e:  # noqa: BLE001
                    ok(type(e).__name__ == c[2], (c[1], e))
    return buf.getvalue()


def to_nb(cells):
    out = []
    for c in cells:
        kind = c[0]
        src = c[1]
        lines = src.split('\n')
        source = [l + '\n' for l in lines[:-1]] + [lines[-1]]
        if kind == 'md':
            out.append({'cell_type': 'markdown', 'metadata': {}, 'source': source})
        else:
            out.append({'cell_type': 'code', 'metadata': {}, 'execution_count': None, 'outputs': [], 'source': source})
    return {'cells': out, 'metadata': {'colab': {'provenance': []}, 'kernelspec': {'name': 'python3', 'display_name': 'Python 3'},
                                       'language_info': {'name': 'python'}}, 'nbformat': 4, 'nbformat_minor': 0}


def build(nb):
    fname, title, cells = nb
    blank = run_nb(cells, False)
    full = run_nb(cells, True)
    n_checks = sum(1 for c in cells if c[0] == 'check')
    if n_checks:
        ok(blank.count('Well done') == 0, f'{fname}: a blank answer passed')
        ok(full.count('Well done') == n_checks, f'{fname}: {full.count("Well done")} of {n_checks} model answers passed')
    (NB / fname).write_text(json.dumps(to_nb(cells), ensure_ascii=False, indent=1), encoding='utf-8')
    print('wrote', fname, len(cells), 'cells;', n_checks, 'self-checks')
    return full


def page():
    t = ('# Practice: Four Colab notebooks\n\n*Chapter 6 · Practice. Try the chapter in Python yourself, in your browser. '
         'Each notebook opens in Google Colab (sign in with a Google account); use **File → Save a copy in Drive** to keep '
         'your work. Every cell was run before the notebook was published.*\n\n'
         '| Notebook | What you do | Open |\n|---|---|---|\n')
    rows = [(NB1, 'cells vs the shell vs a script (the Colab trap); `print()`; comments; reading an error message'),
            (NB2, 'see the tokens of any line; the 35 keywords; a name checker; the types of literals; escape sequences'),
            (NB3, 'two names, one object; re-assigning; dynamic typing; swaps; the errors of section 6.7'),
            (NB4, '25 tasks (predict, names, write the code, find the error), each with a self-check: Well done! or Not yet')]
    for (fname, title, _), what in rows:
        t += f'| **{title}** | {what} | [Open in Colab]({COLAB}{fname}) |\n'
    t += ('\n## How to use them\n\n1. Open a notebook; run the first cell with **Shift + Enter**.\n2. **Predict first:** '
          'before running a cell marked *My prediction*, write what you expect.\n3. **Modify:** change the cell and run '
          'it again; nothing can break.\n4. In notebook 6-4, type your answers where it says `None` and run each check.\n\n'
          '*Remember the Colab trap: a cell shows the value of its last line by itself, a script does not. In IDLE, use '
          '`print`.*\n')
    (D / 'practice-colab-notebooks.md').write_text(t, encoding='utf-8')
    print('wrote practice-colab-notebooks.md')


if __name__ == '__main__':
    for nb in (NB1, NB2, NB3, NB4):
        out_text = build(nb)
    full2 = run_nb(NB2[2], True)
    ok('9 tokens' in full2 and '35' in full2 and "['False', 'None', 'True']" in full2)
    full3 = run_nb(NB3[2], True)
    ok('5 3' in full3 and '7 5' in full3)
    ok(len([c for c in NB4[2] if c[0] == 'check']) == 25)
    page()
    print(f'{checks} checks, 0 wrong (Python {PYV})')
