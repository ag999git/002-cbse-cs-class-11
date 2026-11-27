"""Chapter 6 online pages, part 2: the four "See it" pages (27 Nov 2026; online plan v2, O3).
0609 interactive or script? · 0612 token explorer · 0614 identifier checker + variable vs identifier ·
0617 names and objects, step by step.
The data of 0609 and 0617 is made here by running real Python (the shell with code.InteractiveConsole, the script in a
fresh interpreter, names and objects with id() and type() after every line); the pages only replay it. The logic of
0612 and 0614 is in book/assets/javascripts/ch06-seeit.js, tested by tools/ch06_js_test.py against Python.
Run from the repository root:  python tools/ch06_seeit.py"""
import code
import contextlib
import io
import json
import keyword
import subprocess
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python'
PYV = sys.version.split()[0]
checks = 0


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def head(title, label, intro):
    return f'# {label}: {title}\n\n*Chapter 6 · {label}. {intro}*\n\n'


def write(name, text):
    (D / name).write_text(text, encoding='utf-8')
    print('wrote', name)


# ================================================================= 0609 interactive or script
MODES = [
    ('sum', 'A sum, with and without print', ['7 + 5', 'print(7 + 5)'],
     'In the shell both lines show 12. In a script, line 1 shows nothing: a value is shown only when you print it.'),
    ('name', 'A name, with and without print', ['marks = 92', 'marks', 'print(marks)'],
     'An assignment shows nothing anywhere. A bare name shows its value only in the shell.'),
    ('quotes', 'Text: why the shell shows quotes', ['"Hello"', 'print("Hello")'],
     'The shell shows the value as you would type it, with quotes: \'Hello\'. print() shows the text itself, without quotes.'),
    ('double', 'Working with a name', ['x = 10', 'x * 2', 'y = x * 2', 'y'],
     'x * 2 is worked out but not kept or shown in a script. y = x * 2 keeps the result in y.'),
    ('calc', 'The shell as a calculator', ['2 ** 10', '7 / 2', '7 // 2', '7 % 2'],
     'A quick way to check sums. A script would show nothing at all here: every line is a bare expression.'),
    ('two', 'Two values in one print', ['a = 5', 'b = 3', 'a + b', 'print(a, b, a + b)'],
     'print() can show several values, separated by spaces.'),
    ('comment', 'Comments are skipped in both', ['# a note for people', '10 + 1   # eleven'],
     'A comment is never run. In the shell the sum still shows 11; in a script nothing shows.'),
    ('length', 'A built-in function', ['len("Asha")', 'print(len("Asha"))'],
     'len() gives the number of characters (Chapter 11). Again: shown in the shell, printed in a script.'),
    ('total', 'Changing a value', ['total = 0', 'total = total + 5', 'total = total + 5', 'total'],
     'Each line uses the old value of total and ties total to a new one. Only the last line shows anything, and only in the shell.'),
    ('repeat', 'Text times a number', ['"Py" * 3', 'print("Py" * 3)'],
     '"Py" * 3 repeats the text. The shell shows \'PyPyPy\' with quotes; print shows PyPyPy.'),
    ('compare', 'A comparison', ['5 > 3', 'print(5 > 3)'],
     'A comparison gives True or False (Chapter 7).'),
    ('none', 'A value that shows nothing', ['result = None', 'result', 'print(result)'],
     'The shell shows nothing for None, but print() shows the word None.'),
]


def shell_outputs(lines):
    """Run lines one by one as the interactive shell does; return what is shown after each."""
    con = code.InteractiveConsole({})
    outs = []
    for ln in lines:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            more = con.push(ln)
        ok(not more, ln)
        outs.append(buf.getvalue().rstrip('\n'))
    return outs


def script_output(lines):
    r = subprocess.run([sys.executable, '-I', '-c', '\n'.join(lines)], capture_output=True, text=True, encoding='utf-8')
    ok(r.returncode == 0 and not r.stderr, r.stderr)
    return r.stdout.rstrip('\n')


def modes():
    data = {}
    for key, title, lines, note in MODES:
        data[key] = {'title': title, 'lines': lines, 'shell': shell_outputs(lines), 'script': script_output(lines), 'note': note}
    ok(data['sum']['shell'] == ['12', '12'] and data['sum']['script'] == '12')
    ok(data['quotes']['shell'] == ["'Hello'", 'Hello'] and data['none']['shell'][1] == '' and data['none']['script'] == 'None')
    ok(data['calc']['script'] == '' and data['calc']['shell'] == ['1024', '3.5', '3', '1'])
    opts = ''.join(f'<option value="{k}">{v["title"]}</option>' for k, v in data.items())
    t = head('Interactive or script?', 'See it',
             'Section 6.3 says: the shell shows the value of a bare expression; a script shows only what you print. '
             'Choose a program, then press **Next line** to type it into the shell one line at a time, or **Run all**. '
             'The script\'s output appears when every line has run.')
    t += f'''<div class="c6box" markdown="0">
<p><label>Program: <select id="md-select">{opts}</select></label>
<button id="md-next">Next line</button> <button id="md-all" class="c6light">Run all</button></p>
<p><b>The program</b></p>
<div id="md-source" class="ch06-pre"></div>
<div class="ch06-twocol">
<div><p><b>Interactive mode: the shell</b></p><div id="md-shell" class="ch06-pre"></div></div>
<div><p><b>Script mode: the same lines saved and run (F5)</b></p><div id="md-script" class="ch06-pre"></div></div>
</div>
<p id="md-note"></p>
</div>
<script id="md-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  Ch06.modesPage(JSON.parse(document.getElementById('md-data').textContent),
    {{select: 'md-select', source: 'md-source', shell: 'md-shell', script: 'md-script', next: 'md-next', all: 'md-all', note: 'md-note'}});
}});
</script>

## What to notice

1. **A bare expression** (`7 + 5`, `marks`, `"Hello"`) shows its value in the shell, and **nothing** in a script.
2. **The shell shows text with quotes** (`'Hello'`), the way you would type it; `print()` shows the text itself.
3. **An assignment** (`marks = 92`) shows nothing in either mode: it only ties a name to a value.
4. **A notebook cell** (Colab, Jupyter) behaves like the shell for its **last** line: a bare expression there shows its
   value. That is "the Colab trap" of section 6.3.

*Every output on this page was made by Python {PYV}: the shell column by Python's own interactive console, the script
column by running the lines as a file.*
'''
    write('see-it-interactive-or-script.md', t)


# ================================================================= 0612 token explorer
TOKEN_EXAMPLES = ['if marks >= 33: print("Pass")   # result', 'total = price * 2', 'area = 22 / 7 * radius * radius',
                  'x, y = y, x', 'print("Total:", 90 + 85)', 'is_ok = not (a == b) and c in d',
                  'x = 0o17 + 0x1F + 2.5e3', 'class = "XI-A"', 'price = $250', 'print("Hi"']


def token_explorer():
    import tokenize
    toks = [t for t in tokenize.generate_tokens(io.StringIO(TOKEN_EXAMPLES[0] + '\n').readline)
            if t.type in (tokenize.NAME, tokenize.NUMBER, tokenize.STRING, tokenize.OP)]
    ok(len(toks) == 9, 'the book line has 9 tokens')
    btns = ''.join(f'<button class="c6light" data-ch06-line="{e.replace(chr(34), "&quot;")}">{e.split("#")[0].strip()}</button> '
                   for e in TOKEN_EXAMPLES)
    t = head('Token explorer', 'See it',
             'Section 6.4 cuts one line into its tokens. Type any line of Python (or press an example) and see it cut into '
             'tokens, each named by its kind. Comments and spaces are skipped: they are not tokens.')
    t += f'''<div class="c6box" markdown="0">
<p><label>A line of Python: <input id="tk-input" size="48" spellcheck="false" value="{TOKEN_EXAMPLES[0].replace(chr(34), '&quot;')}"></label></p>
<p>Examples: {btns}</p>
<div id="tk-result"></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  Ch06.tokenPage({{input: 'tk-input', result: 'tk-result'}});
}});
</script>

## The five kinds, and their colours

| Kind | What it is | Examples |
|---|---|---|
| keyword | a word Python reserves | `if`, `for`, `True`, `and` |
| identifier | a name you choose | `marks`, `price`, `print` |
| literal | a fixed value written in the line | `33`, `"Pass"`, `2.5e3` |
| operator | does work on values | `+`, `>=`, `=`, `//` |
| punctuator | groups or separates | `(` `)` `,` `:` `.` |

## What to notice

1. `print` is an **identifier**, not a keyword: it is the name of a function, and you could (but should not) use it as a
   name for something else.
2. `True`, `False` and `None` come out as **keywords**: in exam answers they are called Boolean literals and the special
   literal (section 6.6).
3. `and`, `or`, `not`, `in`, `is` are **keywords** that work as operators.
4. Try `price = $250` or an unclosed bracket: Python would refuse the line, and the page says why.

*The page was tested on 2,010 lines against Python's own tokenizer: for every line it gives exactly Python's tokens, or
says that Python would refuse the line. Lines it does not handle (f-strings, a backslash at the end) get a "not covered
here" note.*
'''
    write('see-it-token-explorer.md', t)


# ================================================================= 0614 identifier checker
NAME_EXAMPLES = ['total_marks', '2nd_rank', 'my marks', 'sum$', 'class', 'TotalMarks', 'PASS_MARK', 'print', 'l', 'नाम']


def identifier_checker():
    ok(all((n.isidentifier() and not keyword.iskeyword(n)) == want for n, want in
           [('total_marks', True), ('2nd_rank', False), ('my marks', False), ('sum$', False), ('class', False),
            ('TotalMarks', True), ('PASS_MARK', True), ('print', True), ('l', True), ('नाम', True)]))
    btns = ''.join(f'<button class="c6light" data-ch06-name="{n}">{n}</button> ' for n in NAME_EXAMPLES)
    t = head('Identifier checker', 'See it',
             'Section 6.5 has the rules Python enforces and the conventions good programmers follow. Type a name (or press '
             'an example) to see whether Python accepts it, and whether it follows the conventions.')
    t += f'''<div class="c6box" markdown="0">
<p><label>A name: <input id="id-input" size="24" spellcheck="false" value="total_marks"></label></p>
<p>Examples: {btns}</p>
<div id="id-result"></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  var show = Ch06.namePage({{input: 'id-input', result: 'id-result'}});
  document.querySelectorAll('[data-ch06-name]').forEach(function (b) {{
    b.onclick = function () {{ document.getElementById('id-input').value = b.getAttribute('data-ch06-name'); show(); }};
  }});
}});
</script>

## The rules and the conventions

| Rules Python enforces (break one: the program does not run) | Conventions (break one: it runs, but reads badly) |
|---|---|
| 1. Begin with a letter or `_`, never a digit | meaningful names: `total_marks`, not `tm` |
| 2. Then only letters, digits and `_`: no space, `$`, `-`, `.`, `@` | snake_case: small letters joined by `_` |
| 3. Not a keyword | CAPITALS only for constants: `PASS_MARK` |
| 4. Capital and small letters differ | never `l`, `O`, `I` as one-letter names |
| 5. Any length | do not reuse Python's own names: `print`, `len`, `sum` |

**Names in Indian scripts.** Python accepts letters of every language, so `नाम = "Asha"` is legal. In the exam and in
code you share, use English names: everyone can type and read them.

## Variable vs identifier

The two words are often mixed up. An **identifier** is a **name**; a **variable** is a name **tied to an object**.

| Basis of difference | Identifier | Variable |
|---|---|---|
| What it is | a name, made by the rules above | a name tied to an object (section 6.7) |
| Names what? | anything with a name: a variable, a function, a module | a value the program keeps and uses |
| Examples | `marks`, `print` (a function), `math` (a module) | `marks` after `marks = 92` |
| Has a value? | not by itself | yes: through its object |
| Has a type? | no | **no**: in Python the **object** has the type, not the name (box or tag, section 6.7) |

- Every variable has an identifier (its name); not every identifier is a variable (`print` names a function, `math` a
  module).
- In C++ and Java a variable is a box with a fixed type, so books for those languages describe a variable as "a name, a
  value and a type". In Python the type belongs to the object; the name only points to it.
- A name also has a **scope**, the part of the program where it can be used; you meet scope with functions in Class XII.

*The checker was tested on 5,007 names against Python's own `str.isidentifier()` and `keyword.iskeyword()`, including
names in Devanagari and Tamil: it agrees with Python on every one.*
'''
    write('see-it-identifier-checker.md', t)


# ================================================================= 0617 names and objects
OBJ_PROGRAMS = [
    ('assign', 'Assign, then re-assign', ['marks = 92', 'marks = 95']),
    ('share', 'Two names, one object', ['marks = 95', 'total = marks']),
    ('moves', 'Does y change?', ['x = 3', 'y = x', 'x = x + 2', 'print(x, y)']),
    ('three', 'One value, three names', ['a = b = c = 0']),
    ('type', 'A new type: dynamic typing', ['marks = 92', 'marks = "A+"', 'print(type(marks))']),
    ('swap3', 'Swap with a third variable', ['x, y = 5, 7', 't = x', 'x = y', 'y = t', 'print(x, y)']),
    ('swap', "Python's swap", ['x, y = 5, 7', 'x, y = y, x', 'print(x, y)']),
    ('price', 'Changing price does not change total', ['price = 250', 'total = price * 2', 'price = 300', 'print(total)']),
    ('names', 'Text objects', ['name = "Asha"', 'city = name', 'name = "Ravi"', 'print(city)']),
    ('count', 'Counting up', ['count = 0', 'count = count + 1', 'count = count + 1']),
]


def trace(lines):
    """Run the lines one by one; after each, the names and the objects they point to (by id), with orphans."""
    ns = {}
    states = [{'names': [], 'objects': [], 'note': '', 'output': ''}]
    prev_ids = {}
    order = []
    for ln in lines:
        before = dict(ns)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(ln, ns)
        user = {k: v for k, v in ns.items() if k != '__builtins__'}
        for k in user:
            if k not in order:
                order.append(k)
        objs, index = [], {}
        for k in order:
            i = id(user[k])
            if i not in index:
                index[i] = len(objs)
                objs.append({'repr': repr(user[k]), 'type': type(user[k]).__name__, 'orphan': False})
        names = [{'name': k, 'obj': index[id(user[k])]} for k in order]
        for k, v in before.items():                    # objects that lost their last tag on this line
            if k == '__builtins__':
                continue
            if id(v) not in index:
                index[id(v)] = len(objs)
                objs.append({'repr': repr(v), 'type': type(v).__name__, 'orphan': True})
        changed = [k for k in order if k not in before or id(before[k]) != id(user[k])]
        parts = []
        old_ids = {id(v) for k, v in before.items() if k != '__builtins__'}
        done = set()
        for k in changed:
            if k in done:
                continue
            group = [m for m in changed if id(user[m]) == id(user[k])]      # names moved onto one object together
            done.update(group)
            others = [m for m in order if m not in group and id(user[m]) == id(user[k])]
            who = group[0] if len(group) == 1 else ', '.join(group[:-1]) + ' and ' + group[-1]
            s = f'{who} {"is" if len(group) == 1 else "are"} tied to {user[k]!r} ({type(user[k]).__name__})'
            if len(group) > 1:
                s += f': one object, {len(group)} names'
            if others:
                s += ', the same object as ' + ' and '.join(others)
            elif id(user[k]) not in old_ids and before:
                s += ', a new object'
            parts.append(s)
        lost = [o['repr'] for o in objs if o['orphan']]
        if lost:
            parts.append(' and '.join(lost) + (' has' if len(lost) == 1 else ' have') + ' no tag now')
        if not parts:
            parts.append('no name changes; this line only shows something')
        states.append({'names': names, 'objects': objs, 'note': '; '.join(parts) + '.', 'output': buf.getvalue().rstrip('\n')})
    return states


def tutor(lines):
    q = urllib.parse.quote('\n'.join(lines))
    return f'https://pythontutor.com/visualize.html#code={q}&cumulative=false&heapPrimitives=nevernest&mode=display&py=3'


def names_objects():
    data = {}
    for key, title, lines in OBJ_PROGRAMS:
        st = trace(lines)
        data[key] = {'title': title, 'lines': lines, 'states': st, 'tutor': tutor(lines)}
        ok(len(st) == len(lines) + 1)
    s = data['moves']['states']
    ok(s[2]['names'][0]['obj'] == s[2]['names'][1]['obj'], 'y = x: one object')
    ok(s[3]['names'][0]['obj'] != s[3]['names'][1]['obj'] and s[4]['output'] == '5 3', 'x moves; y stays')
    ok(len(data['three']['states'][1]['objects']) == 1 and len(data['three']['states'][1]['names']) == 3)
    ok(data['assign']['states'][2]['objects'][-1]['orphan'] and data['assign']['states'][2]['objects'][-1]['repr'] == '92')
    ok(data['swap']['states'][3]['output'] == '7 5' and data['swap3']['states'][5]['output'] == '7 5')
    ok(data['price']['states'][4]['output'] == '500' and data['names']['states'][4]['output'] == 'Asha')
    ok(data['type']['states'][3]['output'] == "<class 'str'>")
    opts = ''.join(f'<option value="{k}">{v["title"]}</option>' for k, v in data.items())
    t = head('Names and objects, step by step', 'See it',
             'Section 6.7 pictures a variable as a price tag tied to an object. Choose a program and press **Next line**: '
             'after every line you see each name (tag) and the object it points to, as Python really has them.')
    t += f'''<div class="c6box" markdown="0">
<p><label>Program: <select id="ob-select">{opts}</select></label>
<button id="ob-back" class="c6light">Back</button> <button id="ob-next">Next line</button></p>
<div class="ch06-twocol">
<div><p><b>The program</b></p><div id="ob-source" class="ch06-pre"></div></div>
<div><p><b>Names (tags) and objects</b></p><div id="ob-picture"></div></div>
</div>
<p id="ob-note"></p>
<p><a id="ob-tutor" href="#" target="_blank" rel="noopener">Open this program in Python Tutor</a> (another site that draws
programs step by step; choose "render all objects on the heap" to see the same tags and objects).</p>
</div>
<script id="ob-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  Ch06.objectsPage(JSON.parse(document.getElementById('ob-data').textContent),
    {{select: 'ob-select', source: 'ob-source', picture: 'ob-picture', next: 'ob-next', back: 'ob-back', note: 'ob-note', tutor: 'ob-tutor'}});
}});
</script>

## What to notice

1. **`total = marks`** adds a second tag to the **same** object; nothing is copied.
2. **`x = x + 2`** makes a **new** object and moves only the tag `x`; `y` stays where it was. Moving one tag never moves
   another.
3. **`marks = "A+"`** ties the same name to an object of another type: **dynamic typing**. The name has no type; each
   object has its own.
4. **The swap.** With a third variable, `t` keeps the old object of `x` safe for a moment (the third glass). In
   `x, y = y, x`, Python works out the right side first and then moves both tags.
5. **"No tag now".** An object that has lost its last tag can no longer be used by the program; Python may clear it away.
   (Python keeps small numbers ready for re-use, so it does not always clear them, but your program cannot reach them
   any more.)

*Every picture on this page was made by running the program in Python {PYV} and asking `id()` and `type()` after every
line.*
'''
    write('see-it-names-and-objects.md', t)


if __name__ == '__main__':
    modes()
    token_explorer()
    identifier_checker()
    names_objects()
    print(f'{checks} checks, 0 wrong (Python {PYV})')
