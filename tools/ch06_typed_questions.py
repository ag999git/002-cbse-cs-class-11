"""Chapter 6 questions by type, online (QR 0622), and the practice page 0618 (27-28 Nov 2026; online plan v2, O2).

Pages 01-07 are written here by hand (answers with the reason; none repeats a printed question of Chapter 6 v6).
Pages 08-11 are generated or decided by Python itself: valid / invalid by str.isidentifier(), keyword and Python's own
parser; every output, error message, type and string size by RUNNING the code. Page 0618 (tricky assignments and
None) is written to the chapter folder.
Run from the repository root:  python tools/ch06_typed_questions.py"""
import ast
import code
import contextlib
import io
import keyword
import subprocess
import tokenize
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch06_pages import literal_answer  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python'
Q = D / 'questions'
TOOL = 'tools/ch06_typed_questions.py'
PYV = sys.version.split()[0]
checks = 0
TOKS = (tokenize.NAME, tokenize.NUMBER, tokenize.STRING, tokenize.OP)
total = {}


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def run(src):
    """Run a script in a fresh Python; return (stdout, last line of stderr)."""
    r = subprocess.run([sys.executable, '-I', '-c', src], capture_output=True, text=True, encoding='utf-8')
    err = r.stderr.strip().splitlines()
    return r.stdout.rstrip('\n'), (err[-1] if err else '')


def out(src):
    o, e = run(src)
    ok(e == '', f'{src!r}: {e}')
    return o


def err(src):
    o, e = run(src)
    ok(e != '', f'{src!r} gave no error')
    return o, e


def shell(lines):
    con = code.InteractiveConsole({})
    res = []
    for ln in lines:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            con.push(ln)
        res.append(buf.getvalue().rstrip('\n'))
    return res


def blk(src, lang='python'):
    return f'\n\n```{lang}\n{src}\n```\n'


def tag(d, s):
    return f' *({d} · {s})*'


def page(fname, title, intro, sections, count, folder=Q, head=None):
    t = head or (f'# Chapter 6: Getting Started with Python: {title} ({count})\n\n*Chapter 6 · Questions (online). '
                 f'{intro} Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are '
                 f'given in brackets. Every output and error message on this page was made by running Python {PYV} '
                 f'(`{TOOL}`).*\n\n')
    n = 0
    for h, items in sections:
        t += f'## {h}\n\n'
        for q, a in items:
            n += 1
            t += f'**Q{n}.** {q}\n\n**Answer.** {a}\n\n'
    ok(n == count, (fname, n, count))
    (folder / fname).write_text(t, encoding='utf-8')
    if folder == Q:
        total[fname] = (title, n)
    print('wrote', fname, n)


# ================================================================= 01 MCQ
def mcq():
    o_print2 = run('print "Hi"')[1]
    ok(o_print2.startswith('SyntaxError'))
    ok(run('a = 5\nb = a\na = 7\nprint(b)')[0] == '5')
    ok(eval('0o17') == 15 and eval('2.5e3') == 2500.0)
    ok(len([t for t in __import__('tokenize').generate_tokens(io.StringIO('print("Hi", 5)\n').readline)
            if t.type in TOKS]) == 6)
    ok(not keyword.iskeyword('print') and keyword.iskeyword('None') and keyword.iskeyword('elif'))
    ok('_count'.isidentifier() and not 'my-name'.isidentifier() and not 'total 1'.isidentifier())
    ok(run('x = 5\n  y = 6')[1].startswith('IndentationError'))
    raw = {
        'Meet Python (6.1)': [
            ('Python is named after:', ['a snake', 'a British comedy show', 'a Greek god', 'its first computer'], 1, 'Guido van Rossum liked *Monty Python\'s Flying Circus*.', 'E', '6.1'),
            ('Python 2 was retired on:', ['1 Jan 2008', '1 Jan 2015', '1 Jan 2020', '1 Jan 2024'], 2, 'no fixes at all since then, even for security.', 'E', '6.1'),
            ('Which is NOT a feature of Python?', ['interpreted', 'case-sensitive', 'every variable\'s type must be declared', 'cross-platform'], 2, 'Python is dynamically typed: no declarations.', 'E', '6.1'),
            ('A language whose statements are translated and run one at a time is:', ['compiled', 'interpreted', 'assembled', 'machine language'], 1, 'this is what Python\'s interpreter does (Chapter 2).', 'E', '6.1'),
            ('"Free and open source" means the software is:', ['free for 30 days', 'free to use, and its source code is open to all', 'free but secret', 'paid but shared'], 1, 'freeware is free without its source code; shareware is a trial.', 'M', '6.1'),
            ('Python 3.0, the big clean-up, came in:', ['1991', '2000', '2008', '2020'], 2, 'December 2008.', 'E', '6.1'),
            ('"Cross-platform" means a Python program:', ['runs on Windows, Linux and macOS without change', 'needs the internet', 'runs only on phones', 'can be shared'], 0, 'the same .py file runs everywhere Python is installed.', 'E', '6.1'),
            ('In Python 3, `print "Hi"` gives:', ['Hi', '"Hi"', 'a SyntaxError', 'nothing'], 2, f'Python 3 says: `{o_print2}`', 'M', '6.1'),
        ],
        'Your Python workshop (6.2)': [
            ('IDE stands for:', ['Internet Development Engine', 'Integrated Development Environment', 'Interpreted Data Editor', 'Internal Design Environment'], 1, 'one program to write, run and correct programs.', 'E', '6.2'),
            ('Which tool runs your code on Google\'s computers?', ['IDLE', 'Thonny', 'Google Colab', 'VS Code'], 2, 'Colab is a cloud tool: it needs the internet.', 'E', '6.2'),
            ('Which tool comes with Python itself?', ['IDLE', 'VS Code', 'Jupyter', 'Colab'], 0, 'IDLE is installed with Python.', 'E', '6.2'),
            ('Jupyter Notebook runs your code:', ['on Google\'s computers', 'on a server on your own computer', 'in the browser only, without Python', 'only on phones'], 1, 'the browser only shows the cells; a local Jupyter server runs Python.', 'M', '6.2'),
            ('Which of these needs no installation?', ['IDLE', 'Thonny', 'VS Code', 'Google Colab'], 3, 'only a browser and a Google sign-in.', 'E', '6.2'),
            ('The tool used in most school labs and the practical exam is:', ['IDLE', 'Colab', 'Jupyter', 'PyCharm'], 0, 'it comes with Python and needs no internet.', 'E', '6.2'),
            ('A notebook (Colab, Jupyter) is made of:', ['pages', 'cells', 'shells', 'scripts'], 1, 'each cell holds code or text and is run on its own.', 'E', '6.2'),
        ],
        'First program and the two modes (6.3)': [
            ('In IDLE\'s shell window you work in:', ['script mode', 'interactive mode', 'compile mode', 'debug mode'], 1, 'one statement at a time, answered at once.', 'E', '6.3'),
            ('Which line of a SCRIPT shows something on the screen?', ['`7 + 5`', '`print(7 + 5)`', '`x = 7 + 5`', '`# 7 + 5`'], 1, 'a script shows a value only through print().', 'E', '6.3'),
            ('The `= RESTART: …` line in the shell means:', ['an error', 'IDLE cleared the shell\'s memory before running the file', 'the computer restarted', 'the program ended'], 1, 'it is IDLE\'s own line, not your output.', 'M', '6.3'),
            ('The last line of an error message tells you:', ['the time', 'the kind of error and its cause', 'the file size', 'the Python version'], 1, 'read it first, then go to the line number.', 'E', '6.3'),
            ('A line that begins with spaces for no reason gives:', ['NameError', 'IndentationError', 'TypeError', 'no error'], 1, 'Python uses the spaces at the start of a line to mark blocks.', 'E', '6.3'),
            ('The prompt `>>>` means:', ['an error', 'Python is waiting for a statement', 'the program has ended', 'a comment'], 1, 'type a statement and press Enter.', 'E', '6.3'),
            ('The better way to write one long statement over two lines is:', ['inside brackets', 'with a `;`', 'with `#`', 'it is not possible'], 0, 'Python does not end a statement while a bracket is open; `\\` also works but breaks easily.', 'M', '6.3'),
            ('Work typed in the shell is lost when:', ['you press Enter', 'the shell is closed', 'you use print', 'you type a comment'], 1, 'save programs as scripts to keep them.', 'E', '6.3'),
        ],
        'Character set and tokens (6.4)': [
            ('Which is a white-space character?', ['`_`', 'tab', '`#`', '`@`'], 1, 'space, tab and new line are white space.', 'E', '6.4'),
            ('How many tokens are in `print("Hi", 5)`?', ['4', '5', '6', '7'], 2, '`print`, `(`, `"Hi"`, `,`, `5`, `)`: counted by Python\'s tokenizer.', 'M', '6.4'),
            ('In `x = 5  # five`, the part `# five` is:', ['a literal', 'a comment, which is not a token', 'an operator', 'a keyword'], 1, 'Python skips it before cutting the line into tokens.', 'E', '6.4'),
            ('In `if a >= b:`, the token `>=` is:', ['a punctuator', 'an operator', 'a keyword', 'a literal'], 1, 'it does work on two values: a comparison.', 'E', '6.4'),
            ('In `if a >= b:`, the token `:` is:', ['an operator', 'a punctuator', 'a literal', 'an identifier'], 1, 'it ends a line that starts a block.', 'E', '6.4'),
            ('`"33"` is:', ['an integer literal', 'a string literal', 'an identifier', 'a keyword'], 1, 'quotes make it text.', 'E', '6.4'),
            ('Hindi or Tamil letters may appear in a Python program in:', ['nowhere', 'strings and comments (and even names)', 'only in keywords', 'only in numbers'], 1, 'Python uses Unicode (Chapter 4).', 'M', '6.4'),
        ],
        'Keywords and identifiers (6.5)': [
            ('Which is a keyword?', ['`print`', '`input`', '`None`', '`main`'], 2, '`print` and `input` are names of functions, not keywords.', 'M', '6.5'),
            ('Which is NOT a keyword?', ['`elif`', '`lambda`', '`print`', '`pass`'], 2, '`print` is a built-in function.', 'M', '6.5'),
            ('Which is a valid identifier?', ['`my-name`', '`_count`', '`3rd`', '`for`'], 1, '`-` is not allowed; a digit cannot come first; `for` is a keyword.', 'E', '6.5'),
            ('Which is NOT a valid identifier?', ['`Total_1`', '`total1`', '`total 1`', '`TOTAL`'], 2, 'a space makes two names.', 'E', '6.5'),
            ('Python\'s convention for variable names is:', ['camelCase', 'snake_case', 'ALL CAPITALS', 'any style'], 1, 'small letters joined by `_` (PEP 8).', 'E', '6.5'),
            ('A name in capitals, like `PASS_MARK`, is meant for:', ['a keyword', 'a constant', 'a function', 'a comment'], 1, 'a value that never changes.', 'E', '6.5'),
            ('Which pair are BOTH keywords?', ['`True` and `False`', '`true` and `false`', '`print` and `input`', '`If` and `Else`'], 0, 'keywords are written exactly: `true` and `If` are ordinary names.', 'M', '6.5'),
            ('How long may an identifier be?', ['8 characters', '32 characters', '79 characters', 'any length'], 3, 'PEP 8 limits a LINE to 79 characters, not a name.', 'M', '6.5'),
            ('Which name hides one of Python\'s own functions?', ['`length`', '`len`', '`size`', '`count1`'], 1, 'after `len = 5`, `len("abc")` stops working.', 'M', '6.5'),
        ],
        'Literals, operators, punctuators (6.6)': [
            ('The value of `0o17` is:', ['17', '15', '0', '1.7'], 1, '`0o` means octal: 1 × 8 + 7 = 15.', 'M', '6.6'),
            ('Which is a floating-point literal?', ['`25`', '`2.5e3`', '`"2.5"`', '`0x25`'], 1, '2.5e3 = 2500.0.', 'E', '6.6'),
            ('`None` stands for:', ['zero', 'an empty string', 'no value', 'False'], 2, 'it is the special literal.', 'E', '6.6'),
            ('In `print(a, b)`, the comma is:', ['an operator', 'a punctuator', 'a literal', 'a keyword'], 1, 'it separates items.', 'E', '6.6'),
            ('`=` in `x = 5` is called the:', ['equality operator', 'assignment operator', 'comparison', 'punctuator only'], 1, 'equality is tested with `==` (Chapter 7).', 'E', '6.6'),
        ],
        'Variables (6.7)': [
            ('In Python, a variable is best described as:', ['a box of fixed type', 'a name tied to an object', 'a memory address you type', 'a keyword'], 1, 'the price-tag picture of section 6.7.', 'E', '6.7'),
            ('After `a = 5`, `b = a`, `a = 7`, the value of `b` is:', ['5', '7', '12', 'an error'], 0, '`a = 7` moves only the tag `a`.', 'M', '6.7'),
            ('`type(x)` gives the type of:', ['the name x', 'the object x is tied to', 'the line', 'the keyword'], 1, 'a name has no type of its own.', 'M', '6.7'),
            ('Which statement is an error?', ['`x = 10`', '`x + 1 = 5`', '`x = x + 1`', '`x = y = 0`'], 1, 'the left side of `=` must be a name, not an expression.', 'M', '6.7'),
            ('Python is:', ['statically typed', 'dynamically typed', 'untyped', 'weakly typed'], 1, 'names have no fixed type; values are never mixed quietly (strongly typed).', 'M', '6.7'),
        ],
        'Comments (6.8)': [
            ('A docstring is:', ['a comment starting with //', 'a triple-quoted note as the first statement of a program or function', 'any string', 'an error message'], 1, 'it tells the user what the program does.', 'M', '6.8'),
        ],
    }
    secs, n = [], 0
    for h, items in raw.items():
        o = []
        for stem, opts, k, why, d, s in items:
            ok(0 <= k < 4 and len(opts) == 4)
            op = ' '.join(f'({chr(97 + i)}) {x}' for i, x in enumerate(opts))
            o.append((f'{stem} {op}{tag(d, s)}', f'({chr(97 + k)}) {opts[k]}. *Why:* {why}'))
        secs.append((h, o))
        n += len(o)
    page('01-mcq.md', 'Multiple-choice questions', 'One mark each.', secs, 50)


# ================================================================= 02 fill in
def fill():
    ok(eval('2.5e3') == 2500.0 and eval('0b101') == 5 and len('ab\ncd') == 5)
    ok(run('x, y = 5, 7\nx, y = y, x\nprint(x)')[0] == '7')
    items = [
        ('Python was first released in ______.', '1991 (version 0.9.0, February 1991).', 'E', '6.1'),
        ('Python\'s name comes from the British TV show ______.', '*Monty Python\'s Flying Circus*.', 'E', '6.1'),
        ('A program that translates and runs one statement at a time is an ______.', 'interpreter.', 'E', '6.1'),
        ('IDE stands for ______.', 'Integrated Development Environment.', 'E', '6.2'),
        ('IDLE\'s window for interactive mode is the ______.', 'shell.', 'E', '6.2'),
        ('In Google Colab, your code runs on ______ computers.', 'Google\'s (the cloud).', 'E', '6.2'),
        ('A Jupyter or Colab notebook is made of ______.', 'cells.', 'E', '6.2'),
        ('In a script, a value is shown on the screen only by ______.', '`print()`.', 'E', '6.3'),
        ('The IDLE menu command that runs a script is Run → ______.', 'Run Module.', 'E', '6.3'),
        ('The keyboard shortcut to save a file in IDLE is ______.', 'Ctrl+S.', 'E', '6.3'),
        ('The ______ line of an error message names the error and its cause.', 'last.', 'E', '6.3'),
        ('The set of characters that Python accepts is its ______.', 'character set.', 'E', '6.4'),
        ('The five kinds of token are keyword, identifier, literal, operator and ______.', 'punctuator.', 'E', '6.4'),
        ('A word that Python reserves for its own use is a ______.', 'keyword.', 'E', '6.5'),
        ('A name chosen by the programmer is an ______.', 'identifier.', 'E', '6.5'),
        ('The keywords `async` and `await` were added in Python ______.', '3.7 (2018).', 'M', '6.5'),
        ('An identifier must not begin with a ______.', 'digit.', 'E', '6.5'),
        ('The only special character allowed in an identifier is ______.', '`_` (the underscore).', 'E', '6.5'),
        ('In snake_case, words are joined by ______.', '`_`: for example `bus_fare`.', 'E', '6.5'),
        ('Java and JavaScript name variables in ______ style, like `rollNo`.', 'camelCase.', 'M', '6.5'),
        ('The value of the literal `2.5e3` is ______.', '2500.0 (2.5 × 10³).', 'M', '6.6'),
        ('The value of the literal `0b101` is ______.', '5 (binary 101).', 'M', '6.6'),
        ('The special literal that means "no value" is ______.', '`None`.', 'E', '6.6'),
        ('A symbol or word that does work on values is an ______.', 'operator.', 'E', '6.6'),
        ('A value that an operator works on is an ______.', 'operand.', 'E', '6.6'),
        ('The name on the left of `=` is the ______.', 'L-value.', 'E', '6.7'),
        ('`id()` gives an object\'s ______.', 'identity number (unique while the object exists).', 'M', '6.7'),
        ('`type(x)` gives the type of the ______ that `x` is tied to.', 'object.', 'M', '6.7'),
        ('Tying one name to values of different types at different times is called ______ typing.', 'dynamic.', 'E', '6.7'),
        ('In C++ and Java a variable\'s type is fixed before the program runs: ______ typing.', 'static.', 'M', '6.7'),
        ('After `x, y = 5, 7` and then `x, y = y, x`, the value of `x` is ______.', '7.', 'M', '6.7'),
        ('A comment written after a statement on the same line is an ______ comment.', 'inline.', 'E', '6.8'),
        ('A triple-quoted note as the first statement of a program is called a ______.', 'docstring.', 'M', '6.8'),
        ('`print(len("ab\\ncd"))` prints ______.', '5: `\\n` is one character.', 'H', '6.6'),
        ('PEP stands for Python ______ Proposal.', 'Enhancement.', 'E', '6.5'),
    ]
    o = [(f'{q}{tag(d, s)}', a) for q, a, d, s in items]
    page('02-fill-in.md', 'Fill in the blanks', 'One mark each.', [('Fill in the blanks', o)], 35)


# ================================================================= 03 true or false
def true_false():
    ok(shell(['"Hi"'])[0] == "'Hi'")
    ok(run('print(1)\nprint("x"')[0] == '')                       # a SyntaxError: nothing runs
    ok(run('a = 5\nb = a\na = 9\nprint(b)')[0] == '5')
    ok(run('x = y = 0\nprint(id(x) == id(y))')[0] == 'True')
    ok(run('print(totl)')[1].startswith('NameError'))
    ok(run('print(type(3.0))')[0] == "<class 'float'>")
    ok(keyword.iskeyword('None') and not keyword.iskeyword('print') and '_'.isidentifier() and 'class_11'.isidentifier())
    ok(('x' * 100).isidentifier())
    try:
        eval('0o9'); valid = True
    except SyntaxError:
        valid = False
    ok(not valid)
    items = [
        ('Python is a compiled language.', False, 'it is interpreted: one statement at a time.'),
        ('Python 3 runs every Python 2 program without change.', False, 'for example `print "Hi"` fails in Python 3.'),
        ('Python is free and open source.', True, 'free to use, and its source code is open to all.'),
        ('IDLE is installed together with Python.', True, 'it comes with Python from python.org.'),
        ('Google Colab needs Python to be installed on your computer.', False, 'it runs on Google\'s computers; you need only a browser.'),
        ('Work typed in the shell is saved automatically.', False, 'it is lost when the shell closes.'),
        ('IDLE asks you to save a new script before it runs it.', True, 'Run Module (F5) runs the saved file.'),
        ('In the shell, typing `"Hi"` shows `\'Hi\'`, with quotes.', True, 'the shell shows the value as you would type it; print() shows Hi.'),
        ('`print()` can show several values in one call.', True, '`print(a, b, c)` separates them with spaces.'),
        ('If line 2 of a script has a SyntaxError, line 1 still runs.', False, 'Python checks the grammar of the whole file first; nothing runs.'),
        ('`a=5` and `a = 5` mean different things.', False, 'spaces inside a line do not change the meaning; they help reading.'),
        ('A space at the start of a line can stop a program.', True, '`IndentationError: unexpected indent`.'),
        ('Python skips blank lines in a script.', True, 'they only help people read the program.'),
        ('`print` is a keyword.', False, 'it is the name of a built-in function.'),
        ('`True` and `true` are the same in Python.', False, 'Python is case-sensitive: only `True` is a keyword.'),
        ('An identifier may contain a hyphen, as in `roll-no`.', False, '`-` is the minus operator.'),
        ('`_` on its own is a valid identifier.', True, 'an underscore counts as a letter.'),
        ('An identifier may be 100 characters long.', True, 'any length is allowed (but keep it sensible).'),
        ('`class_11` is a valid identifier.', True, 'it is not the keyword `class`.'),
        ('`None` is a keyword.', True, 'one of the three keywords with a capital letter.'),
        ('`"5"` and `5` are the same value.', False, 'a string and an integer.'),
        ('`0o9` is a valid octal literal.', False, 'octal digits are 0 to 7 only.'),
        ('`=` tests whether two values are equal.', False, '`=` assigns; `==` tests equality (Chapter 7).'),
        ('After `b = a`, giving `a` a new value also changes `b`.', False, 'only the tag `a` moves; `b` stays on the old object.'),
        ('`x = y = 0` ties both names to one object.', True, '`id(x) == id(y)` is True.'),
        ('In Python a variable must be declared before it is used.', False, 'it is created when it is first assigned.'),
        ('Using a name before giving it a value gives `NameError`.', True, 'the name does not exist yet.'),
        ('Python is weakly typed.', False, 'it is dynamically but strongly typed: `"5" + 3` is a TypeError.'),
        ('`x, y = y, x` swaps two values.', True, 'the right side is worked out first.'),
        ('A triple-quoted string on its own line does nothing.', True, 'Python makes the string and throws it away.'),
        ('`//` starts a comment in Python.', False, 'it is floor division (Chapter 7); a comment starts with `#`.'),
        ('A docstring is the first statement of a program or function.', True, 'a triple-quoted note there.'),
        ('Python refuses to run a program that breaks PEP 8.', False, 'PEP 8 is about style; Python does not check it.'),
        ('The L-value of an assignment must be a name.', True, 'a value cannot be tied to anything.'),
        ('`print(type(3.0))` prints `<class \'float\'>`.', True, '3.0 has a decimal point.'),
    ]
    o = [(q, f'**{"True" if v else "False"}.** {w}') for q, v, w in items]
    page('03-true-false.md', 'True or false', 'One mark each.', [('True or false', o)], 35)


# ================================================================= 04 assertion and reason
def assertion_reason():
    ok(run('a = 5\nb = a\na = 6\nprint(b)')[0] == '5' and run('x = 1,234\nprint(type(x).__name__)')[0] == 'tuple')
    items = [
        ('A Python program written on Windows runs on Linux without change.', 'Python is cross-platform.', 'a', 'cross-platform means exactly this.'),
        ('Interactive mode is good for testing one statement.', 'Work in interactive mode is saved in a file.', 'c', 'shell work is lost when the shell closes.'),
        ('In a script, `7 + 5` on its own line shows nothing.', 'A script shows a value only when it is printed.', 'a', 'the shell is different: it shows bare values.'),
        ('Python is an interpreted language.', 'Python translates and runs one statement at a time.', 'a', 'that is what an interpreter does.'),
        ('`print "Hi"` fails in Python 3.', 'In Python 3, print is a function and needs brackets.', 'a', 'Python 2\'s print statement was removed.'),
        ('Google Colab needs the internet.', 'Colab runs your code on Google\'s computers.', 'a', 'your typing must reach them.'),
        ('IDLE is used in the practical exam.', 'IDLE needs an internet connection.', 'c', 'IDLE runs on your own computer.'),
        ('`my-marks` is not a valid identifier.', '`-` is the minus operator.', 'a', 'Python would read my minus marks.'),
        ('`print` can be used as a variable name.', '`print` is not a keyword.', 'a', 'legal, but poor style: it hides the function.'),
        ('`True` is a keyword.', 'All keywords begin with a capital letter.', 'c', 'only True, False and None do.'),
        ('A comment is not a token.', 'Python skips comments before cutting a line into tokens.', 'a', 'a token must mean something to Python.'),
        ('`"Asha\'s"` is a valid string literal.', 'A single quote may appear inside double quotes.', 'a', 'the double quotes mark the start and end.'),
        ('`1,234` makes a tuple of two numbers.', 'A comma separates values.', 'a', 'Python reads (1, 234), not one thousand two hundred and thirty-four.'),
        ('`x = 10` is not an equation.', '`=` gives the value on the right to the name on the left.', 'a', 'read `=` as "becomes".'),
        ('After `a = 5`, `b = a`, `a = 6`, `b` is still 5.', '`a = 6` moves only the tag `a`.', 'a', 'the tag `b` stays on 5.'),
        ('`x + 1 = 5` is an error.', 'The left side of `=` must be a name.', 'a', '`x + 1` is an expression, not a name.'),
        ('Python is dynamically typed.', 'In Python the type belongs to the object, not to the name.', 'a', 'so a name may be tied to any type.'),
        ('`//` starts a comment in Python.', '`//` is floor division in Python.', 'd', 'a comment starts with `#`.'),
        ('A docstring is shown on the screen when the program runs.', 'A docstring is a triple-quoted string at the top of a program.', 'd', 'Python keeps it but does not print it.'),
        ('`_total` is a valid identifier.', 'An underscore counts as a letter in a name.', 'a', 'so it may begin a name.'),
    ]
    intro = ('One mark each. Choose: **(a)** both true, R explains A; **(b)** both true, R does not explain A; **(c)** A true, '
             'R false; **(d)** A false, R true.')
    o = [(f'**A:** {a} **R:** {r}', f'({k}). *Why:* {w}') for a, r, k, w in items]
    ok(all(k in 'abcd' for _, _, k, _ in items))
    page('04-assertion-reason.md', 'Assertion and reason', intro, [('Assertion and reason', o)], 20)


# ================================================================= 05 short answer
def short():
    toks = [t for t in __import__('tokenize').generate_tokens(io.StringIO('x = y + 10\n').readline) if t.type in TOKS]
    ok([t.string for t in toks] == ['x', '=', 'y', '+', '10'])
    names = ['roll-no', 'Roll_No', 'roll no', '2roll', '_roll']
    bad = [n for n in names if not n.isidentifier()]
    ok(bad == ['roll-no', 'roll no', '2roll'])
    ok([type(eval(v)).__name__ for v in ('5', '"5"', '5.0')] == ['int', 'str', 'float'] and len('a\tb') == 3)
    ok(run('a = [1]\nb = a\nprint(id(a) == id(b))')[0] == 'True')
    items = [
        ('Why is Python called an interpreted language?', 'Its interpreter translates and runs one statement at a time, while the program runs, and stops at the first error it meets; there is no separate translation of the whole program first.', 'E', '6.1'),
        ('Give two differences between Python 2 and Python 3.', '(1) `print` is a statement in Python 2 (`print "Hi"`) and a function in Python 3 (`print("Hi")`). (2) `7 / 2` gives 3 in Python 2 and 3.5 in Python 3. (Also: Python 3 uses Unicode text by default; Python 2 is no longer supported.)', 'M', '6.1'),
        ('Write two advantages and two limits of Python.', 'Advantages: easy to read; free and open source (also: cross-platform, large library). Limits: slower than C/C++ for heavy calculation; types are not fixed on names, so some mistakes appear only when a line runs.', 'M', '6.1'),
        ('What is an IDE? Name two IDEs for Python.', 'An Integrated Development Environment: one program to write, run and correct programs (editor, Run button, error messages, debugger). IDLE and Thonny (also VS Code, PyCharm).', 'E', '6.2'),
        ('Differentiate between IDLE and Google Colab (two points).', '(1) *Where the code runs:* IDLE on your own computer; Colab on Google\'s computers. (2) *Needs:* IDLE needs Python installed; Colab needs only a browser, the internet and a Google sign-in.', 'M', '6.2'),
        ('What is the Python shell? What does its prompt `>>>` mean?', 'The window of interactive mode, where each statement is run as soon as you press Enter. `>>>` means Python is waiting for the next statement.', 'E', '6.3'),
        ('Give two reasons to write a program as a script.', 'A script is saved and can be run again; it can be long; it can be given to others (any two).', 'E', '6.3'),
        ('List the steps to write and run a script in IDLE.', '(1) File → New File; (2) type the program; (3) save it with a `.py` name; (4) Run → Run Module (F5); (5) read the output (or the error) in the shell.', 'E', '6.3'),
        ('What is "the Colab trap"?', 'In a Colab or Jupyter cell (and in the shell) a bare expression on the last line shows its value; in a script it shows nothing. A program that "worked" in Colab may print less as a script: use print().', 'M', '6.3'),
        ('What does the `= RESTART: …` line mean in IDLE\'s shell?', 'IDLE cleared the shell\'s memory before running the file, so earlier shell work cannot disturb it, and it names the file that ran. It is not part of the output.', 'M', '6.3'),
        ('How should you read an error message?', 'Read the last line first (the kind of error and its cause), then go to the line number it gives; correct one error, save and run again.', 'E', '6.3'),
        ('What is Python\'s character set? Name its groups.', 'The characters Python accepts: letters (A–Z, a–z), digits (0–9), special symbols (`+ - * / ( ) [ ] { } , : . # …`), white space (space, tab, new line) and any Unicode character inside strings and comments.', 'E', '6.4'),
        ('Name the kind of each token in `x = y + 10`.', '`x` identifier; `=` operator (assignment); `y` identifier; `+` operator; `10` literal: 5 tokens.', 'E', '6.4'),
        ('Why can a keyword not be used as a name?', 'A keyword already has a fixed meaning to Python; if it were also a name, Python could not tell which meaning you want (like a reserved seat).', 'M', '6.5'),
        ('Which are invalid identifiers, and why: `roll-no`, `Roll_No`, `roll no`, `2roll`, `_roll`?', 'Invalid: `roll-no` (`-` not allowed), `roll no` (space), `2roll` (begins with a digit). `Roll_No` and `_roll` are valid.', 'E', '6.5'),
        ('Differentiate between a naming rule and a naming convention, with one example of each.', 'A rule is enforced by Python: break it and the program does not run (a name cannot begin with a digit). A convention is followed by programmers: break it and the program runs but reads badly (snake_case for variables).', 'M', '6.5'),
        ('What are snake_case and camelCase? Which does Python prefer?', 'snake_case: small letters joined by `_` (`roll_no`). camelCase: words joined with a capital at each new word (`rollNo`). Python prefers snake_case (PEP 8).', 'E', '6.5'),
        ('Why should `l`, `O` and `I` not be used as one-letter names?', 'They are legal but look like the digits 1 and 0; `l1` may be read as "one-one".', 'E', '6.5'),
        ('What are literals? Name four kinds, with an example of each.', 'Fixed values written in a program: string `"Pass"`, integer `33`, float `3.14`, Boolean `True` (also complex `2+3j`, special `None`).', 'E', '6.6'),
        ('How are `5`, `"5"` and `5.0` different?', '`5` is an integer (`int`), `"5"` is a string (`str`, text), `5.0` is a floating-point number (`float`).', 'E', '6.6'),
        ('What are an operator and an operand? Give an example.', 'An operator does work on values; the values it works on are operands. In `price * 2`, `*` is the operator; `price` and `2` are the operands.', 'E', '6.6'),
        ('What are punctuators? Name four.', 'Symbols that group or separate parts of a statement: `( )`, `[ ]`, `,`, `:` (also `.`, `{ }`, `;`).', 'E', '6.6'),
        ('What is an escape sequence? Give two. What is the length of `"a\\tb"`?', 'A backslash and a character that together stand for one character you cannot type directly: `\\n` (new line), `\\t` (tab). `len("a\\tb")` is 3.', 'M', '6.6'),
        ('What is a variable in Python?', 'A name tied to an object in memory; the object carries the value and its type. The name can later be tied to another object.', 'E', '6.7'),
        ('What happens in the three steps of `marks = 92`?', '(1) Python makes the object 92 (an int) in memory; (2) it makes the name `marks`, if new; (3) it ties the name to the object.', 'M', '6.7'),
        ('Show with an example that two names can refer to one object.', '`a = [1]` then `b = a`: `id(a) == id(b)` prints True; one object, two tags.', 'M', '6.7'),
        ('Give two differences between static and dynamic typing.', '(1) *Who has the type:* static (C++, Java): the variable (box); dynamic (Python): only the object. (2) *When types are checked:* static: before the program runs; dynamic: while it runs.', 'M', '6.7'),
        ('Why is it wrong to call Python "weakly typed"?', 'Python never mixes types quietly: `"5" + 3` stops with TypeError. It is dynamically typed (names have no type) but strongly typed (values are not mixed).', 'H', '6.7'),
        ('What is swapping? Why does it usually need a third variable?', 'Exchanging the values of two variables. Writing `x = y` first would wipe out the old value of x, so it is first saved in a third variable: `t = x`, `x = y`, `y = t`.', 'M', '6.7'),
        ('Why is `x = x + 1` correct in Python but impossible in mathematics?', 'In Python `=` is an assignment: work out x + 1, then tie x to the result. In mathematics `=` says both sides are equal, and no number equals itself plus 1.', 'M', '6.7'),
        ('What are an expression and a statement? Give one example of each.', 'An expression gives a value: `price * 2`. A statement is an instruction that does something: `total = price * 2`.', 'E', '6.3'),
        ('Differentiate between a `#` comment and a triple-quoted note.', 'A `#` comment runs to the end of the line and is skipped by Python. A triple-quoted note is a string that may run over many lines; on its own line it is made and thrown away.', 'M', '6.8'),
        ('What is a docstring?', 'A triple-quoted note as the first statement of a program (or function), telling a user what it does and how to use it.', 'E', '6.8'),
        ('What are physical and logical lines?', 'A physical line is a line as you see it; a logical line is one whole statement as Python reads it. One logical line may run over several physical lines inside brackets or after `\\`.', 'M', '6.3'),
        ('What is PEP 8? Give two of its rules.', 'Python\'s style guide (PEP = Python Enhancement Proposal). Rules: snake_case names; 4 spaces per indent; lines of at most 79 characters; one statement per line (any two).', 'E', '6.5'),
    ]
    o = [(f'{q}{tag(d, s)}', a) for q, a, d, s in items]
    page('05-short-answer.md', 'Short-answer questions', 'Two or three marks each.', [('Short answers', o)], 35)


# ================================================================= 06 long answer
def long_():
    toks = [(t.string, t.type) for t in __import__('tokenize').generate_tokens(io.StringIO('area = 3.14 * r * r  # circle\n').readline)
            if t.type in TOKS]
    ok(len(toks) == 7, toks)
    p10 = ('# Shopping bill: 3 notebooks and 2 pens\nNOTEBOOK_PRICE = 45   # rupees each\nPEN_PRICE = 10\n'
           'notebooks = 3\npens = 2\ntotal = notebooks * NOTEBOOK_PRICE + pens * PEN_PRICE\nprint("Total bill:", total, "rupees")')
    o10 = out(p10)
    ok(o10 == 'Total bill: 155 rupees')
    p11 = 'a, b, c = 1, 2, 3\nt = a      # with a third variable\na = b\nb = c\nc = t\nprint(a, b, c)\na, b, c = c, a, b   # back again, in one line\nprint(a, b, c)'
    o11 = out(p11)
    ok(o11 == '2 3 1\n1 2 3', o11)
    p7 = 'marks = 92\ntotal = marks\nprint(id(marks) == id(total))\nmarks = 95\nprint(marks, total, id(marks) == id(total))'
    o7 = out(p7)
    ok(o7 == 'True\n95 92 False')
    p6 = 'for v in [33, 3.5, "33", True, None, 2+3j]:\n    print(repr(v), type(v))'
    o6 = out(p6)
    p12 = '"""Average of three test marks.\nAsha, Class XI-A."""\nMAX_MARKS = 25          # each test is out of 25\nt1, t2, t3 = 20, 18, 22\naverage = (t1 + t2 + t3) / 3   # a plain average, no weights\nprint("Average:", round(average, 2), "out of", MAX_MARKS)'
    o12 = out(p12)
    ok(o12 == 'Average: 20.0 out of 25')
    names = ['studentName', 'student_name', '2ndTerm', 'term_2', 'MAX', 'for', 'For', 'total$']
    verdict = {n: ('keyword' if keyword.iskeyword(n) else ('valid' if n.isidentifier() else 'invalid')) for n in names}
    ok(verdict == {'studentName': 'valid', 'student_name': 'valid', '2ndTerm': 'invalid', 'term_2': 'valid', 'MAX': 'valid',
                   'for': 'keyword', 'For': 'valid', 'total$': 'invalid'})
    items = [
        ('Explain five features of Python, and what each means for a student.' + tag('M', '6.1'),
         '(1) **Easy to read:** short, English-like statements: fewer lines, fewer mistakes. (2) **Interpreted:** one statement at a time: try a line and see the answer at once. (3) **Free and open source:** nothing to buy; the source code is open. (4) **Cross-platform:** the same program runs at school (Windows) and at home (Linux, macOS). (5) **Dynamically typed:** no declarations: `marks = 92` is enough. (Also: large standard library, case-sensitive, used everywhere.)'),
        ('Compare interactive mode and script mode in five points, with an example of each.' + tag('M', '6.3'),
         '| Basis | Interactive mode | Script mode |\n|---|---|---|\n| Where | the shell, after `>>>` | the editor, a `.py` file |\n| Runs | one statement at a time, at once | the whole file, line 1 to the end |\n| Saved? | no | yes |\n| Bare expression `7 + 5` | value shown | nothing shown |\n| Best for | trying a statement, quick sums | programs of more than a few lines |\n\nExample: `>>> 2 ** 10` shows 1024 in the shell; a script needs `print(2 ** 10)`.'),
        ('Describe five places to write Python: where the code runs, whether it needs installing, and what each is best for.' + tag('M', '6.2'),
         'IDLE: your computer; comes with Python; learning and the exam. Thonny: your computer; install; beginners (shows values). VS Code: your computer; install + Python extension; bigger projects. Jupyter: a server on your own computer, shown in the browser; install; notebooks without the internet. Google Colab: Google\'s computers (cloud); no install, needs a sign-in and the internet; practice anywhere.'),
        ('Cut `area = 3.14 * r * r  # circle` into tokens. Name the kind of each, and say what happens to the comment.' + tag('M', '6.4'),
         '7 tokens: `area` identifier, `=` operator, `3.14` literal, `*` operator, `r` identifier, `*` operator, `r` identifier. `# circle` is a comment: Python skips it before making tokens, so it is not a token.'),
        ('State the rules for identifiers and two conventions. Then classify: `studentName`, `student_name`, `2ndTerm`, `term_2`, `MAX`, `for`, `For`, `total$`.' + tag('M', '6.5'),
         'Rules: begin with a letter or `_`; then only letters, digits, `_`; not a keyword; case-sensitive; any length. Conventions: snake_case; CAPITALS for constants. Valid: `student_name`, `term_2`, `For`, `studentName` (legal, but camelCase), `MAX` (a constant). Invalid: `2ndTerm` (digit first), `total$` (`$`), `for` (keyword).'),
        ('Explain the kinds of literal with examples, and show their types with a program.' + tag('M', '6.6') + blk(p6),
         'String (`"33"`), integer (`33`), floating point (`3.5`), Boolean (`True`), complex (`2+3j`) and the special literal `None`. Output:' + blk(o6, 'text') + 'Each value carries its own type; `type()` reports it.'),
        ('Explain, with the price-tag picture and a program, how variables work in Python.' + tag('H', '6.7') + blk(p7),
         'A variable is a tag tied to an object. `total = marks` ties a second tag to the same object (`id` equal: True). `marks = 95` makes a new object and moves only the tag `marks`; `total` stays on 92. Output:' + blk(o7, 'text')),
        ('Compare static and dynamic typing in a table of four points, using the box and the tag.' + tag('H', '6.7'),
         '| Basis | Static (C++, Java) | Dynamic (Python) |\n|---|---|---|\n| A variable is | a box with a type | a tag on an object |\n| Declaration | needed: `int marks;` | none |\n| Checked | before running | while running |\n| Another type later? | no | yes: `marks = "A+"` |\n\nPython is still strongly typed: `"5" + 3` is a TypeError.'),
        ('Explain L-value and R-value. Why are `5 = x` and `x + 1 = 5` errors, but `x = x + 1` is correct?' + tag('M', '6.7'),
         'The L-value (left of `=`) says WHERE the result goes: a name. The R-value (right) says WHAT the value is: anything that gives a value. `5 = x` and `x + 1 = 5` have a literal and an expression on the left: nothing can be tied to them. `x = x + 1` works out x + 1 (R-value), then ties the name x (L-value) to it.'),
        ('Write a documented program for a bill: 3 notebooks at ₹45 each and 2 pens at ₹10 each. Use constants for the prices.' + tag('M', '6.7, 6.8'),
         blk(p10) + 'Output:' + blk(o10, 'text') + 'Constants in capitals, snake_case names, a comment at the top and one saying what the numbers mean.'),
        ('Rotate three values so that a gets b\'s value, b gets c\'s and c gets a\'s: (i) with a third variable, (ii) in one line. Then rotate them back.' + tag('H', '6.7'),
         blk(p11) + 'Output:' + blk(o11, 'text') + 'In (ii) the whole right side is worked out first, so no value is lost.'),
        ('Explain the two kinds of note in Python with an example of each, and write a short documented program.' + tag('M', '6.8'),
         '`#` comments (to the end of the line, for readers of the code) and a triple-quoted docstring at the top (for users).' + blk(p12) + 'Output:' + blk(o12, 'text')),
    ]
    page('06-long-answer.md', 'Long-answer questions', 'Four or five marks each.', [('Long answers', items)], 12)


# ================================================================= 07 case studies
def cases():
    riya = '7 * 24\n60 * 60\nprint("Done")'
    ok(out(riya) == 'Done' and shell(riya.split('\n'))[:2] == ['168', '3600'])
    sneha = 'a, b = 3, 8\na = b\nb = a\nprint(a, b)'
    ok(out(sneha) == '8 8')
    arjun = '1 marks = 90\n2 print(marks)'
    ok(err(arjun)[1].startswith('SyntaxError'))
    neha = 'price = 120\nquantity = 3\nprint(price * quantity)\nprice = 100\nprint(price * quantity)'
    ok(out(neha) == '360\n300')
    rohit = 'total = 450\nprint(Total)'
    ok(err(rohit)[1].startswith('NameError'))
    items = [
        ('**Riya\'s script.** Riya tested these lines in the shell and saw 168 and 3600. She saved them as a script, ran it, and saw only "Done".' + blk(riya) + '(a) Why do the numbers not appear? (b) Correct the script. (c) Where else would the numbers appear without print?',
         '(a) In a script a bare expression shows nothing; only print() shows output. (b) `print(7 * 24)` and `print(60 * 60)`. (c) In the shell and in the last line of a Colab or Jupyter cell.'),
        ('**Arjun copies code from a PDF.** He pasted this from a book page:' + blk(arjun) + '(a) What goes wrong? (b) Why? (c) What habit prevents it?',
         f'(a) `{err(arjun)[1]}`. (b) The line numbers of the book were copied into the program. (c) Copy code from the website or the notebooks, not from a PDF; delete line numbers and `>>>` signs.'),
        ('**A lab without the internet.** The school\'s internet fails on the day of a practical.' + ' (a) Which tools still work: IDLE, Colab, Jupyter? (b) Why? (c) Which one is used in the exam?',
         '(a) IDLE and Jupyter. (b) They run Python on the computer itself (Jupyter through a local server); Colab runs on Google\'s computers through the internet. (c) IDLE.'),
        ('**Names in a marks program.** A student used the names `a`, `b`, `l`, `Total-Marks`, `print` and `PASS`.' + ' (a) Which name stops the program? (b) Which names are legal but poor, and why? (c) Suggest better names.',
         '(a) `Total-Marks` (`-` is not allowed). (b) `a`, `b` (meaningless), `l` (looks like 1), `print` (hides the function), `PASS` is fine only if it is a constant. (c) `maths_marks`, `science_marks`, `count`, `total_marks`, `PASS_MARK`.'),
        ('**Kunal\'s token homework.** He must cut `if total >= 33 and attendance >= 75:` into tokens.' + ' (a) How many tokens? (b) Name the kinds. (c) Is `and` an operator or a keyword?',
         '(a) 8: `if`, `total`, `>=`, `33`, `and`, `attendance`, `>=`, `75`, `:` makes **9**. (b) keywords `if`, `and`; identifiers `total`, `attendance`; operators `>=` (twice); literals `33`, `75`; punctuator `:`. (c) Both: a keyword that works as a (logical) operator.'),
        ('**The shopkeeper\'s price tags.** Neha models her shop:' + blk(neha) + '(a) What is printed? (b) Draw what happens to the tag `price`. (c) Why does the first answer not change?',
         f'(a)' + blk(out(neha), 'text') + '(b) `price` is first tied to 120, then moved to a new object 100; 120 has no tag now. (c) The first product was worked out and printed before the tag moved; nothing remembers the expression.'),
        ('**Sneha\'s swap.** She wants to swap a and b:' + blk(sneha) + '(a) What is printed? (b) What went wrong? (c) Correct it in two ways.',
         f'(a) `{out(sneha)}`. (b) `a = b` wiped out the old value of a before it was saved. (c) `t = a`, `a = b`, `b = t`; or `a, b = b, a`.'),
        ('**Rohit\'s error message.**' + blk(rohit) + '(a) Which error is shown? (b) What is its cause? (c) Which feature of Python explains it?',
         f'(a) `{err(rohit)[1]}`. (b) The name was created as `total` but used as `Total`. (c) Python is case-sensitive.'),
    ]
    ok(len([t for t in __import__('tokenize').generate_tokens(io.StringIO('if total >= 33 and attendance >= 75:\n').readline) if t.type in TOKS]) == 9)
    items[4] = (items[4][0], '(a) **9** tokens. (b) keywords `if`, `and`; identifiers `total`, `attendance`; operators `>=` (twice); literals `33`, `75`; punctuator `:`. (c) Both: a keyword that works as a (logical) operator.')
    page('07-case-study.md', 'Case studies', 'Each case has three parts.', [('Case studies', items)], 8)


# ================================================================= 08 valid or invalid
ID_DRILL = ['first_name', 'firstName', '1st_name', 'name1', 'first-name', 'first name', '_', '__name', 'Name', 'NAME',
            'elif', 'Elif', 'import', 'imports', 'try_2', 'try', 'class2', 'my.name', 'rate%', 'pin@code']
LIT_DRILL = ['100', '-3.5', '0b11', '0b12', '0o7', '0o8', '0xff', '0xfg', '1.5e2', '1.5e', '3e-2', '4_000', '4__000',
             '"Delhi"', "'Mumbai\"", '"""Chennai"""', 'False', 'false', '7j', '0']


def id_reason(n):
    if keyword.iskeyword(n):
        return 'invalid', 'a keyword'
    if n.isidentifier():
        if keyword.iskeyword(n.lower()) or keyword.iskeyword(n.capitalize()):
            kw = n.lower() if keyword.iskeyword(n.lower()) else n.capitalize()
            return 'valid', f'it is not the keyword `{kw}`: capital and small letters differ'
        if n == '_' or n.startswith('__'):
            return 'valid', 'begins with `_`, which counts as a letter'
        if any(c.isupper() for c in n) and not n.isupper():
            return 'valid', 'legal; Python\'s convention would be snake_case' if any(c.islower() for c in n[1:]) and n[0].islower() else 'legal (capital and small letters are allowed)'
        return 'valid', 'letters, digits and `_` only, not beginning with a digit'
    if n[0].isdigit():
        return 'invalid', 'begins with a digit'
    bad = next(c for c in n if not (c.isalnum() or c == '_'))
    return 'invalid', 'a space is not allowed' if bad == ' ' else f'`{bad}` is not allowed'


def valid_invalid():
    ids = [(f'Is `{n}` a valid identifier?{tag("E", "6.5")}', f'**{id_reason(n)[0].capitalize()}:** {id_reason(n)[1]}.') for n in ID_DRILL]
    for n in ID_DRILL:
        ok((id_reason(n)[0] == 'valid') == (n.isidentifier() and not keyword.iskeyword(n)), n)
    lits = []
    for lit in LIT_DRILL:
        reasons = {'0b12': '2 is not a binary digit', '0o8': '8 is not an octal digit', '0xfg': 'g is not a hexadecimal digit',
                   '1.5e': 'no digits after e', '4__000': 'only single underscores between digits', "'Mumbai\"": 'the quotes do not match'}
        try:
            ast.parse(lit, mode='eval')                  # Python's own parser decides valid or invalid
            a, why = literal_answer(lit)
            ok(lit not in reasons, lit)
        except SyntaxError:
            a, why = 'invalid', reasons[lit]
        lits.append((f'Is `{lit}` a valid literal? If so, of what type?{tag("M", "6.6")}', f'**{a}**' + (f': {why}.' if why else '.')))
    head = ('Is it valid? (identifiers)', ids), ('Is it valid? (literals)', lits)
    page('08-valid-or-invalid.md', 'Valid or invalid?', 'Generated drills: every answer was decided by Python itself '
         '(`str.isidentifier()`, `keyword` and Python\'s own parser). None repeats a name or literal printed in the book or '
         'on the "Literals up close" page.', list(head), 40)


# ================================================================= 09 predict the output
PREDICT = [
    'print("Hello", "Class", 11)',
    'print(7 + 5, 7 * 5)',
    'print("7" + "5")',
    'print("ab" * 3)',
    'x = 10\nx = x + 5\nprint(x)',
    'a = 3\nb = a\na = 4\nprint(a, b)',
    'name = "Asha"\nName = "Ravi"\nprint(name, Name)',
    'x, y = 2, 9\nprint(y, x)',
    'a = b = 7\nb = b + 1\nprint(a, b)',
    'p, q = 4, 6\np, q = q, p\nprint(p - q)',
    'print(type(7), type(7.0))',
    'print(type("7"), type(True))',
    'x = 5\nprint(type(x))\nx = "five"\nprint(type(x))',
    'print(0b11 + 0o11 + 0x11)',
    'print(1e3)',
    'print(len("Python"))',
    'print(len("a b c"))',
    'print("Line1\\nLine2")',
    'print("Tab\\tend")',
    'print(len("\\n\\t"))',
    'print(5, end=" ")\nprint(6)',
    'print("A", "B", sep="-")',
    '# print("hidden")\nprint("shown")',
    'x = 3   # x = 4\nprint(x)',
    '"""A docstring\nover two lines"""\nprint("after the note")',
    's = """one\ntwo"""\nprint(s)',
    'total = (10 +\n         20 +\n         30)\nprint(total)',
    'a = 1; b = 2; print(a + b)',
    'x = 5\ny = x * 2\nx = 100\nprint(y)',
    'count = 0\ncount = count + 1\ncount = count + 1\nprint(count)',
    'price = 50\nprice = price * 2\nprice = price - 10\nprint(price)',
    'x = None\nprint(x)',
    'first, second = "Hi", "there"\nprint(second, first)',
    'a, b, c = 1, 2, 3\na, b, c = c, a, b\nprint(a, b, c)',
    'x = 10\ny = 3\nprint(x // y, x % y)',
    'print(2 ** 3 ** 0)',
    'print(10 / 4)',
    'print(True + True)',
    'marks = 92\nprint("Marks:", marks)',
    'x = 7\nx = "seven"\nx = 7.0\nprint(x, type(x))',
]
PRED_NOTES = {2: 'two strings joined, not added', 3: 'a string repeated', 13: '3 + 9 + 17', 14: 'a float: 1000.0',
              16: 'spaces count as characters', 19: 'each escape sequence is one character', 20: 'end=" " stops the new line',
              21: 'sep sets the separator', 26: 'one statement over three lines, inside brackets', 28: 'y was worked out when x was 5',
              35: '`**` is worked out from the right: `3 ** 0` = 1, then `2 ** 1` = 2', 37: 'True counts as 1 (Chapter 7)'}


def predict():
    ok(len(PREDICT) == 40)
    items = []
    for k, p in enumerate(PREDICT):
        o = out(p)
        note = PRED_NOTES.get(k, '')
        items.append((f'Predict the output.{tag("E" if k < 20 else "M", "6.3–6.8")}' + blk(p),
                      blk(o, 'text') + (f'*Why:* {note}.' if note else '')))
    ok(out(PREDICT[35]) == '2' and out(PREDICT[13]) == '29' and out(PREDICT[2]) == '75')
    page('09-predict-the-output.md', 'Predict the output', 'Each program was run by Python; the answer box is its real '
         'output. Some use things you meet fully in Chapter 7 (`//`, `%`, `**`, `end`, `sep`).', [('Predict the output', items)], 40)


# ================================================================= 10 find the error
FIND = [
    ('Print("Welcome")', 'print("Welcome")', '`print` is written in small letters; Python is case-sensitive'),
    ('print("Welcome)', 'print("Welcome")', 'the string is not closed'),
    ('print "Welcome"', 'print("Welcome")', 'Python 3 needs brackets'),
    ('print("Total:", total)', 'total = 0\nprint("Total:", total)', 'the name is used before it is given a value'),
    ('marks = 90\nprint(Marks)', 'marks = 90\nprint(marks)', 'the name was created with a small m'),
    ('roll-no = 12\nprint(roll-no)', 'roll_no = 12\nprint(roll_no)', '`-` is not allowed in a name'),
    ('2nd_term = 80', 'term_2 = 80', 'a name may not begin with a digit'),
    ('total marks = 450', 'total_marks = 450', 'a name may not contain a space'),
    ('for = 5', 'count = 5', '`for` is a keyword'),
    ('10 = x', 'x = 10', 'the value goes on the right'),
    ('x + y = 15', 'x, y = 7, 8\ntotal = x + y', 'the left side of `=` must be a name'),
    ('x = 5\n  print(x)', 'x = 5\nprint(x)', 'the second line starts with spaces for no reason'),
    ('print("Marks: " + 92)', 'print("Marks:", 92)', 'text and a number cannot be joined with `+`'),
    ('print(10 / 0)', 'print(10 / 2)', 'division by zero'),
    ('x = 012', 'x = 12', 'a whole number may not begin with 0'),
    ('x = 0b102', 'x = 0b101', '2 is not a binary digit'),
    ('pin = 0o189', 'pin = 0o17', '8 and 9 are not octal digits'),
    ('name = \'Asha"', 'name = "Asha"', 'the opening and closing quotes differ'),
    ('// my program\nprint(1)', '# my program\nprint(1)', 'a comment starts with `#`, not `//`'),
    ('print("A")\nprint("B"', 'print("A")\nprint("B")', 'a bracket is not closed; even line 1 does not run'),
    ('a, b = 1, 2, 3', 'a, b, c = 1, 2, 3', 'three values cannot go into two names'),
    ('a, b, c = 1, 2', 'a, b = 1, 2', 'two values cannot go into three names'),
    ('price = 50$', 'price = 50', '`$` is not part of Python'),
    ('print(len(5))', 'print(len("5"))', 'a number has no length; text does'),
    ('class = "XI"\nprint(class)', 'section = "XI"\nprint(section)', '`class` is a keyword'),
]


def find_error():
    items = []
    for bad, good, why in FIND:
        o, e = run(bad)
        ok(e != '', bad)
        good_o, good_e = run(good)
        ok(good_e == '', good)
        items.append((f'Find the error and correct it.{tag("M", "6.3–6.7")}' + blk(bad),
                      f'Python says: `{e}`. *Why:* {why}. Corrected:' + blk(good)))
    ok(run(FIND[19][0])[0] == '', 'line 1 does not run')
    page('10-find-the-error.md', 'Find the error', 'Every error message is the real one from Python; every corrected '
         'program was run without error.', [('Find the error', items)], 25)


# ================================================================= 11 expression or statement; size of a string
EXPR = ['7 + 5', 'x = 7 + 5', 'marks >= 33', 'import math', 'a * b - c', 'del x', 'pass', '"Hi" * 2', 'total += 1',
        'x, y = 1, 2']
SIZES = ['"Python"', '"Class XI"', '"a\\nb"', '"\\t\\t"', '"It\'s"', '"C:\\\\data"', '""', '"""ab\ncd"""', '" "', '"\\"Hi\\""']


def expr_size():
    items = []
    for s in EXPR:
        try:
            ast.parse(s, mode='eval')
            kind, why = 'an expression', 'it gives a value'
        except SyntaxError:
            ast.parse(s, mode='exec')
            kind, why = 'a statement', 'it does something (assigns, imports, deletes or does nothing on purpose) and gives no value'
        items.append((f'Is `{s}` an expression or a statement?{tag("M", "6.3")}', f'**{kind.capitalize()}:** {why}.'))
    ok(sum(1 for q, a in items if 'expression' in a.lower()[:20]) == 4)
    sizes = []
    for s in SIZES:
        n = len(eval(s))
        sizes.append((f'What does `len({s.replace(chr(10), "↵")})` give?{tag("M", "6.6")}',
                      f'**{n}**.' + (' An escape sequence counts as one character.' if '\\' in s else '') +
                      (' The Enter inside triple quotes is a new-line character.' if '\n' in s else '') +
                      (' The empty string has no characters.' if n == 0 else '')))
    ok(len(eval('"""ab\ncd"""')) == 5 and len(eval('"\\"Hi\\""')) == 4)
    page('11-expression-or-statement.md', 'Expression or statement? Size of a string?', 'The kinds of question some '
         'school papers ask (written in our own words); every answer was decided by Python (`ast`, `len`).',
         [('Expression or statement?', items), ('Size of a string', sizes)], 20)


# ================================================================= 0618 practice: tricky assignments and None
TRICKY = [
    'x, x = 20, 30\nprint(x)',
    'a, b, c = 5, 10, 7\nb, c, a = a + 1, b + 2, c - 1\nprint(a, b, c)',
    'x, y = 1, 2\nx, y = y + 1, x + 2\nprint(x, y)',
    'p, q = 3, 5\nq, p = p - 2, p + 2\nprint(p, q)',
    'x = 10\ny, y = x + 2, x + 5\nprint(y)',
    'x, x = 20, 30\ny, y = x + 10, x + 20\nprint(x, y)',
    'a = b = c = 5\nb = 6\nprint(a, b, c)',
    'a, b = 2, 3\na = a + b\nb = a - b\na = a - b\nprint(a, b)',
    'a, b = 4, 9\na, b = b, a + b\nprint(a, b)',
    'm, n = 1, 1\nm, n = n, m + n\nm, n = n, m + n\nprint(m, n)',
    'x = 5\nx, y = x * 2, x * 3\nprint(x, y)',
    'i, j = 0, 1\ni, j = j, i\nj, i = i, j\nprint(i, j)',
    'a, b, c = "x", "y", "z"\na, b, c = c, a, b\nprint(a + b + c)',
    'x = y = 0\nx = x + 1\ny = y + 2\nprint(x, y)',
    'n = 5\nn, m = n + 1, n + 2\nprint(n, m)',
    'result = None\nprint(result)',
    'print(None)',
    'x = None\nprint(type(x))',
    'x = None\nx = 5\nprint(x)',
    'x = None\nprint(x is None)',
    'print(print("Hi"))',
    'a = print("A")\nprint(a)',
    'x = None\ny = x\nprint(y)',
    'x = 0\nprint(x is None)',
    'x = ""\nprint(x is None, len(x))',
]
TRICKY_WHY = {0: 'the right side gives (20, 30); x is tied to 20, then to 30', 1: 'the right side (6, 12, 6) is worked out first, then b, c, a are tied in order',
              2: 'the right side uses the OLD x and y: (2 + 1, 1 + 2)', 3: 'the right side is (1, 5): q = 1, p = 5',
              4: 'y is tied to 12, then to 15', 5: 'x ends as 30; then y is tied to 40, then to 50',
              6: 'b = 6 moves only b', 7: 'a swap without a third variable, using + and −', 8: 'right side first: (9, 4 + 9)',
              9: 'each line uses the old m and n (like the Fibonacci numbers)', 10: 'x * 2 and x * 3 both use the old x = 5',
              11: 'swapped, then swapped back', 15: 'print shows the word None', 16: 'print shows the word None',
              17: 'None is the only value of its type', 19: '`is None` is the right way to test for None',
              20: 'print() shows Hi, and gives back None, which the outer print shows', 21: 'print gives back None',
              23: '0 is a value: it is not None', 24: 'an empty string is a value, not None'}


def tricky():
    items = []
    for k, p in enumerate(TRICKY):
        o = out(p)
        items.append((f'Predict the output.{tag("H" if k < 15 else "M", "6.7" if k < 15 else "6.6")}' + blk(p),
                      blk(o, 'text') + (f'*Why:* {TRICKY_WHY[k]}.' if k in TRICKY_WHY else '')))
    ok(out(TRICKY[0]) == '30' and out(TRICKY[1]) == '6 6 12' and out(TRICKY[2]) == '3 3' and out(TRICKY[5]) == '30 50')
    ok(out(TRICKY[20]) == 'Hi\nNone' and shell(['result = None', 'result']) == ['', ''])
    head = ('# Practice: Tricky assignments and `None`\n\n*Chapter 6 · Practice. Section 6.7 swaps two values with '
            '`x, y = y, x`. Here are harder ones: several names on the left, the same name twice, and the special value '
            '`None`. Every output was made by running Python ' + PYV + '.*\n\n**The one rule:** Python works out the '
            '**whole right side first**, from left to right, using the values the names have **before** the line; then it '
            'ties the names on the left, from left to right. If a name appears twice on the left, the last value wins.\n\n'
            '**`None` in the shell:** typing a name tied to `None` shows nothing; `print()` shows the word `None`.\n\n')
    page('practice-tricky-assignments-and-none.md', 'Tricky assignments and None', '', [('Predict the output', items)], 25,
         folder=D, head=head)


def index():
    t = '# Chapter 6: Getting Started with Python: questions\n\n'
    n = sum(v[1] for v in total.values())
    t += (f'**{n} questions**, each with its answer and the reason below it. They are for learning: try each question '
          'first, then read the answer. None repeats a question printed in the book.\n\n**By type of question**\n\n')
    for f in sorted(total)[:7]:
        t += f'- [{total[f][0]}: {total[f][1]}]({f})\n'
    t += '\n**Practice with code**: every answer decided or made by running Python\n\n'
    for f in sorted(total)[7:]:
        t += f'- [{total[f][0]}: {total[f][1]}]({f})\n'
    t += '\nMore: [Tricky assignments and `None` (25)](../practice-tricky-assignments-and-none.md)\n'
    (Q / 'index.md').write_text(t, encoding='utf-8')
    print('total', n)
    return n


if __name__ == '__main__':
    for f in (mcq, fill, true_false, assertion_reason, short, long_, cases, valid_invalid, predict, find_error, expr_size, tricky):
        f()
    n = index()
    ok(n == 320, n)
    print(f'{checks} checks, 0 wrong (Python {PYV})')
