"""Test the JavaScript of the Chapter 6 "See it" pages (book/assets/javascripts/ch06-seeit.js) against Python
(27 Nov 2026). Token explorer: about 2,000 generated lines through Python's own tokenize; identifier checker: about
5,000 names through str.isidentifier() and keyword.iskeyword(). Rules:
  tokens: Python gives tokens -> the page must give exactly the same tokens and kinds, or "not covered" (only for
          f-strings and a backslash at the end); Python refuses the line -> the page must not give tokens.
  names:  valid / keyword / invalid must agree with Python for every name.
Run from the repository root:  python tools/ch06_js_test.py   (needs node on the PATH)"""
import io
import json
import keyword
import random
import subprocess
import sys
import tempfile
import tokenize
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JS = ROOT / 'book' / 'assets' / 'javascripts' / 'ch06-seeit.js'
R = random.Random(6)
PUNCT = set('()[]{},:.;@')
REAL_OPS = set(tokenize.EXACT_TOKEN_TYPES) - {'!'}     # '!' alone is an operator only inside f-strings


def py_tokens(line):
    """('ok', [(text, kind)]) or ('fstring', None) or ('refused', None), as the book classifies tokens."""
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(line + '\n').readline))
    except (SyntaxError, tokenize.TokenError, IndentationError):
        return 'refused', None
    for a, b in zip(toks, toks[1:]):
        # tokenize splits 012, 09, 5abc, 1.7E into two touching tokens; Python itself refuses them as bad numbers
        if a.type == tokenize.NUMBER and b.type in (tokenize.NUMBER, tokenize.NAME) and a.end == b.start:
            return 'refused', None
    for t in toks:
        if t.type == tokenize.NUMBER:     # tokenize passes 012 and 09 as one number; the compiler refuses them
            try:
                compile(t.string, '<number>', 'eval')
            except SyntaxError:
                return 'refused', None
    out = []
    stack = []
    for t in toks:
        name = tokenize.tok_name[t.type]
        if t.type == tokenize.OP:
            # tokenize lets any symbol through as OP; Python itself refuses symbols that are not operators
            # ($, ?, `, and ! outside an f-string) and brackets that do not match: model the compiler here
            if t.string not in REAL_OPS:
                return 'refused', None
            if t.string in '([{':
                stack.append(')]}'['([{'.index(t.string)])
            elif t.string in ')]}':
                if not stack or stack.pop() != t.string:
                    return 'refused', None
        if name.startswith('FSTRING'):
            return 'fstring', None
        if name == 'ERRORTOKEN':
            return 'refused', None
        if t.type == tokenize.NAME:
            out.append((t.string, 'keyword' if keyword.iskeyword(t.string) else 'identifier'))
        elif t.type in (tokenize.NUMBER, tokenize.STRING):
            out.append((t.string, 'literal'))
        elif t.type == tokenize.OP:
            out.append((t.string, 'punctuator' if t.string in PUNCT else 'operator'))
        elif t.type == tokenize.COMMENT:
            out.append((t.string, 'comment'))
    return 'ok', out


NAMES = ['marks', 'total_2', 'x', 'Total', 'roll_no', 'my_list', 'print', 'len', 'nam', 'PASS_MARK', '_', 'a1']
NUMS = ['0', '7', '42', '3.14', '.5', '7.', '2.5e3', '1e-3', '1_000', '0b101', '0o17', '0x1F', '5j', '2.5j', '00',
        '1.e5', '1E5']
BADNUMS = ['012', '0o28', '0xG1', '1.7E', '5abc', '0b2', '1__0', '1_', '09']
STRS = ['"Pass"', "'A'", '"Asha\'s"', '"""Hi"""', "'''x'''", 'r"C:\\new"', 'b"bytes"', '"a\\"b"', "''", '"#not a comment"']
BADSTRS = ['"open', "'Hi\"", '"""never closed']
OPS = ['+', '-', '*', '/', '//', '%', '**', '=', '==', '!=', '<', '>', '<=', '>=', '+=', '-=', 'and', 'or', 'not', 'in',
       'is', ',', ':', '.', ';', '->', ':=', '...']
KWS = ['if', 'for', 'while', 'True', 'None', 'False', 'else', 'import', 'def', 'return']


def gen_line():
    r = R.random()
    if r < 0.10:
        return R.choice(['x = $5', 'a ? b', 'print(`x`)', 'total = (1 + 2', 'x = 5)', 'a = [1, 2}', 'y = "abc',
                         'x = 012', 'n = 0o28 + 1', 's = f"hi {x}"', 'total = 1 + \\', '!x', 'x = 1 ! 2'])
    parts = []
    for _ in range(R.randint(1, 7)):
        k = R.random()
        if k < 0.3:
            parts.append(R.choice(NAMES))
        elif k < 0.45:
            parts.append(R.choice(NUMS) if R.random() > 0.08 else R.choice(BADNUMS))
        elif k < 0.58:
            parts.append(R.choice(STRS) if R.random() > 0.06 else R.choice(BADSTRS))
        elif k < 0.85:
            parts.append(R.choice(OPS))
        else:
            parts.append(R.choice(KWS))
    line = ' '.join(parts)
    if R.random() < 0.25:
        line = R.choice(NAMES) + '(' + line + ')'
    if R.random() < 0.15:
        line += '  # ' + R.choice(['total', 'why', 'is "this" a token?'])
    if R.random() < 0.1:
        line = '    ' + line
    return line


BOOK_LINES = ['if marks >= 33: print("Pass")   # result', 'total = price * 2', 'print("Hello, world!")',
              'x, y = y, x', 'area = 22 / 7 * radius * radius', 'import keyword', 'print(len(keyword.kwlist))',
              'marks = "A+"', 'a = b = c = 0', 'class = "XI-A"']

ALPHA = list('abcxyzABCXYZ_019') + [' ', '$', '-', '.', '@', 'न', 'ा', 'म', 'த', 'மி', '२']


def gen_name():
    r = R.random()
    if r < 0.08:
        return R.choice(keyword.kwlist + ['print', 'match', 'type', 'l', 'O', 'I', '__init__', 'TotalMarks', 'PASS'])
    return ''.join(R.choice(ALPHA) for _ in range(R.randint(1, 8)))


def main():
    lines = BOOK_LINES + [gen_line() for _ in range(2000)]
    names = [gen_name() for _ in range(5000)] + ['नाम', 'मान1', 'தமிழ்', 'marks', '2nd', 'my marks', 'sum$']
    names = [n for n in names if n]
    with tempfile.TemporaryDirectory() as td:
        cases = Path(td) / 'cases.json'
        cases.write_text(json.dumps({'lines': lines, 'names': names}), encoding='utf-8')
        runner = Path(td) / 'run.js'
        runner.write_text(
            "const C = require(" + json.dumps(str(JS)) + ");\n"
            "const d = JSON.parse(require('fs').readFileSync(" + json.dumps(str(cases)) + ", 'utf8'));\n"
            "const out = {lines: d.lines.map(l => C.tokens(l)), names: d.names.map(n => C.checkName(n).verdict)};\n"
            "process.stdout.write(JSON.stringify(out));\n", encoding='utf-8')
        res = subprocess.run(['node', str(runner)], capture_output=True, text=True, encoding='utf-8')
        if res.returncode:
            print(res.stderr)
            sys.exit(1)
        js = json.loads(res.stdout)
    bad = 0
    stats = {'same tokens': 0, 'refused by both': 0, 'not covered (f-string, backslash)': 0}
    for line, j in zip(lines, js['lines']):
        status, toks = py_tokens(line)
        if status == 'ok':
            if j['status'] == 'ok':
                got = [(t['text'], t['kind']) for t in j['tokens']]
                if got != toks:
                    bad += 1
                    if bad < 15:
                        print('DIFFERENT', repr(line), got, toks)
                else:
                    stats['same tokens'] += 1
            elif j['status'] == 'not covered' and line.rstrip().endswith('\\'):
                stats['not covered (f-string, backslash)'] += 1
            else:
                bad += 1
                if bad < 15:
                    print('PAGE REFUSES A GOOD LINE', repr(line), j)
        elif status == 'fstring':
            if j['status'] == 'ok':
                bad += 1
                print('F-STRING GIVEN TOKENS', repr(line))
            else:
                stats['not covered (f-string, backslash)'] += 1
        else:
            if j['status'] == 'ok':
                bad += 1
                if bad < 15:
                    print('PAGE GIVES TOKENS FOR A REFUSED LINE', repr(line), j['tokens'])
            else:
                stats['refused by both'] += 1
    nbad = 0
    for n, v in zip(names, js['names']):
        want = 'keyword' if keyword.iskeyword(n) else ('valid' if n.isidentifier() else 'invalid')
        got = 'valid' if v in ('valid', 'style') else v
        if got != want:
            nbad += 1
            if nbad < 15:
                print('NAME', repr(n), 'page:', v, 'python:', want)
    print(json.dumps({'lines': len(lines), **stats, 'line failures': bad, 'names': len(names),
                      'valid': sum(1 for n in names if n.isidentifier() and not keyword.iskeyword(n)),
                      'name failures': nbad}))
    sys.exit(1 if bad or nbad else 0)


if __name__ == '__main__':
    main()
