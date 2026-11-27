"""Chapter 2, QR 0207: the "compiler vs interpreter, step by step" page, its Python model and its test (27 Nov 2026).

The teaching language (same rules as book/assets/javascripts/ch02-translate.js):
    name = expression      PRINT expression      (blank lines are skipped)
    expression: whole numbers and names joined by + - * /  (/ is the whole-number part, as // in Python; * / first)
Grammar errors: "unknown command", "incomplete expression", "missing operator", 'bad name "…"', 'unknown symbol "…"'.
Errors found only while running: "name 'x' has no value yet", "division by 0".
The test runs node on hundreds of random programs and requires the JavaScript to give exactly the model's results
(compile errors, output, run-time error and its line; the interpreter's step log).
Run from the repository root:  python tools/ch02_translate.py"""
import json
import random
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JS = ROOT / 'book' / 'assets' / 'javascripts' / 'ch02-translate.js'
D = ROOT / 'book' / 'unit-1' / '002-ch02-software-and-os'
NAME = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')
TOK = re.compile(r'\s*(?:(\d+)|([A-Za-z_][A-Za-z0-9_]*)|([-+*/]))')


# ------------------------------------------------------------------ the model
def tokens(text):
    out, i = [], 0
    while i < len(text):
        if text[i:].strip() == '':
            break
        m = TOK.match(text, i)
        if not m:
            return None, f'unknown symbol "{text[i:].strip()[0]}"'
        i = m.end()
        if m.group(1) is not None:
            out.append(('num', m.group(1)))
        elif m.group(2) is not None:
            out.append(('name', m.group(2)))
        else:
            out.append(('op', m.group(3)))
    return out, None


def check_expr(text):
    tk, err = tokens(text)
    if err:
        return err
    if not tk:
        return 'incomplete expression'
    for i, (t, _) in enumerate(tk):
        if i % 2 == 0 and t == 'op':
            return 'incomplete expression'
        if i % 2 == 1 and t != 'op':
            return 'missing operator'
    if tk[-1][0] == 'op':
        return 'incomplete expression'
    return None


def parse(line):
    s = line.strip()
    if s == '':
        return None
    m = re.match(r'^PRINT(\s+(.*))?$', s)
    if m:
        e = check_expr(m.group(2) or '')
        return {'error': e} if e else {'kind': 'print', 'expr': m.group(2)}
    m = re.match(r'^([^=]*)=(.*)$', s)
    if m and '=' not in m.group(2):
        name = m.group(1).strip()
        if not NAME.match(name) or name == 'PRINT':
            return {'error': f'bad name "{name}"'}
        e = check_expr(m.group(2))
        return {'error': e} if e else {'kind': 'set', 'name': name, 'expr': m.group(2)}
    return {'error': 'unknown command'}


class RunError(Exception):
    pass


def evaluate(text, env):
    tk, _ = tokens(text)
    vals, ops = [], []
    for t, v in tk:
        if t == 'num':
            vals.append(int(v))
        elif t == 'name':
            if v not in env:
                raise RunError(f"name '{v}' has no value yet")
            vals.append(env[v])
        else:
            ops.append(v)
    v2, o2 = [vals[0]], []
    for j, op in enumerate(ops):
        b = vals[j + 1]
        if op == '*':
            v2[-1] = v2[-1] * b
        elif op == '/':
            if b == 0:
                raise RunError('division by 0')
            v2[-1] = v2[-1] // b
        else:
            o2.append(op); v2.append(b)
    r = v2[0]
    for k, op in enumerate(o2):
        r = r + v2[k + 1] if op == '+' else r - v2[k + 1]
    return r


def compile_(lines):
    return [{'line': i + 1, 'error': p['error']} for i, ln in enumerate(lines) if (p := parse(ln)) and 'error' in p]


def run_all(lines):
    env, out = {}, []
    for i, ln in enumerate(lines):
        p = parse(ln)
        if not p:
            continue
        try:
            v = evaluate(p['expr'], env)
        except RunError as e:
            return {'out': out, 'error': str(e), 'line': i + 1}
        if p['kind'] == 'set':
            env[p['name']] = v
        else:
            out.append(str(v))
    return {'out': out, 'error': None, 'line': None}


def interpret(lines):
    env, out, log = {}, [], []
    for i, ln in enumerate(lines):
        n = i + 1
        p = parse(ln)
        if not p:
            continue
        if 'error' in p:
            log.append({'line': n, 'text': 'error: ' + p['error']})
            return {'out': out, 'error': p['error'], 'line': n, 'log': log}
        try:
            v = evaluate(p['expr'], env)
        except RunError as e:
            log.append({'line': n, 'text': 'error: ' + str(e)})
            return {'out': out, 'error': str(e), 'line': n, 'log': log}
        if p['kind'] == 'set':
            env[p['name']] = v; log.append({'line': n, 'text': f"{p['name']} = {v}"})
        else:
            out.append(str(v)); log.append({'line': n, 'text': f'shows {v}'})
    log.append({'line': None, 'text': 'no line left: stop'})
    return {'out': out, 'error': None, 'line': None, 'log': log}


# ------------------------------------------------------------------ the examples on the page
EXAMPLES = {
    'book': {'title': 'The book\'s program (errors in lines 3 and 5)',
             'code': ['a = 10', 'PRINT a', 'PRNT a + 5', 'b = a * 2', 'PRINT b +'],
             'hint': 'The program of section 2.4. Press Compile, then press Interpret line by line.'},
    'marks': {'title': 'A correct program: total and average of two marks',
              'code': ['m1 = 80', 'm2 = 75', 'total = m1 + m2', 'PRINT total', 'avg = total / 2', 'PRINT avg'],
              'hint': 'No errors: both give the same output. The difference is when the translating is done.'},
    'zero': {'title': 'An error only running can find: dividing by 0',
             'code': ['a = 10', 'b = 0', 'PRINT a', 'c = a / b', 'PRINT c'],
             'hint': 'The grammar is correct, so the compiler makes the object file; the error appears only when line 4 runs.'},
    'both': {'title': 'A name with no value, and a spelling error later',
             'code': ['x = 5', 'PRINT y', 'z = x * 3', 'PRNT z'],
             'hint': 'The compiler finds the spelling error in line 4 and runs nothing. The interpreter stops at line 2 and never reaches line 4.'},
}


def check_examples():
    b = EXAMPLES['book']['code']
    assert compile_(b) == [{'line': 3, 'error': 'unknown command'}, {'line': 5, 'error': 'incomplete expression'}]
    r = interpret(b)
    assert r['out'] == ['10'] and r['line'] == 3
    m = EXAMPLES['marks']['code']
    assert compile_(m) == [] and run_all(m)['out'] == ['155', '77'] and interpret(m)['out'] == ['155', '77']
    z = EXAMPLES['zero']['code']
    assert compile_(z) == [] and run_all(z) == {'out': ['10'], 'error': 'division by 0', 'line': 4}
    w = EXAMPLES['both']['code']
    assert compile_(w) == [{'line': 4, 'error': 'unknown command'}]
    assert interpret(w)['line'] == 2 and interpret(w)['error'] == "name 'y' has no value yet"
    return 4


def page():
    opts = '\n'.join(f'<option value="{k}">{v["title"]}</option>' for k, v in EXAMPLES.items())
    t = '''# See it: Compiler vs interpreter, step by step

*Chapter 2 · See it. Choose a small program (or type your own), then press **Compile** or **Interpret: next line**,
and watch how each translator meets the errors. The program is written in a tiny teaching language, so that the two
ways can be shown exactly.*

'''
    t += f'''<div class="ch02tr" markdown="0">
<p><label>Program: <select id="tr-select">
{opts}
</select></label></p>
<p><textarea id="tr-code" rows="7" cols="40" spellcheck="false"></textarea></p>
<p><button id="tr-compile" class="md-button md-button--primary">Compile</button>
<button id="tr-step" class="md-button md-button--primary">Interpret: next line</button>
<button id="tr-reset" class="md-button">Start again</button></p>
<p id="tr-message"></p>
<div id="tr-listing"></div>
<p><b>Output:</b><br><span id="tr-output"></span></p>
</div>
<script id="tr-data" type="application/json">{json.dumps(EXAMPLES, ensure_ascii=False)}</script>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  Ch02.page(JSON.parse(document.getElementById('tr-data').textContent),
    {{select: 'tr-select', code: 'tr-code', compile: 'tr-compile', step: 'tr-step', reset: 'tr-reset',
     message: 'tr-message', listing: 'tr-listing', output: 'tr-output'}});
}});
</script>

## The teaching language

| You write | It means |
|---|---|
| `x = 5` | put 5 in x |
| `total = m1 + m2` | work it out and put the answer in total (`+ - * /`; `/` keeps the whole-number part) |
| `PRINT total` | show the value |

## What to notice

1. **The book's program.** *Compile* lists **both** errors (lines 3 and 5) and runs nothing. *Interpret* shows 10, then
   stops at line 3; it has not even read line 5.
2. **A correct program.** Both give the same output. The compiler translated once and made a file that runs again and
   again; the interpreter translates every time.
3. **Dividing by 0.** The grammar is correct, so the compiler cannot see a problem; the error appears only when line 4
   runs, in both. Such errors are called **run-time errors** (Chapter 8).
4. **A name with no value.** The compiler reports the spelling error in line 4 and runs nothing; the interpreter stops at
   line 2 and never sees line 4.
5. **Memory.** After compiling, the compiler is not needed to run the file; the interpreter must stay in memory the
   whole time the program runs.

*The page was tested on hundreds of programs: for every one, it gives exactly what a separate Python model of the same
rules gives.*
'''
    (D / 'see-it-compiler-interpreter.md').write_text(t, encoding='utf-8')
    print('wrote see-it-compiler-interpreter.md')


# ------------------------------------------------------------------ the test against the JavaScript
def random_program(R):
    names = ['a', 'b', 'c', 'total', 'x']
    def expr():
        k = R.randint(1, 4)
        parts = [R.choice([str(R.randint(0, 20)), R.choice(names)]) for _ in range(k)]
        s = parts[0]
        for p in parts[1:]:
            s += f' {R.choice("+-*/")} {p}'
        return s
    lines = []
    for _ in range(R.randint(1, 7)):
        r = R.random()
        if r < 0.45:
            lines.append(f'{R.choice(names)} = {expr()}')
        elif r < 0.75:
            lines.append(f'PRINT {expr()}')
        else:
            lines.append(R.choice(['PRNT a', 'b = a +', 'c = 2 3', '= 5', '9x = 1', 'PRINT', 'x = a % 2', '',
                                   'PRINT = 4', 'total = (a)', 'a = b = 1', 'print a', 'x=1', 'PRINT 7*-2']))
    return lines


def test():
    R = random.Random(2)
    progs = [v['code'] for v in EXAMPLES.values()] + [random_program(R) for _ in range(600)]
    want = [{'compile': compile_(p), 'run': run_all(p) if not compile_(p) else None, 'interp': interpret(p)} for p in progs]
    runner = '''
const Ch02 = require(process.argv[2]);
const progs = JSON.parse(require('fs').readFileSync(process.argv[3], 'utf8'));
const out = progs.map(p => {
  const c = Ch02.compile(p);
  const r = c.length ? null : Ch02.runAll(p);
  const it = new Ch02.Interpreter(p).runAll();
  return {compile: c, run: r, interp: {out: it.out, error: it.error, line: it.line, log: it.log}};
});
console.log(JSON.stringify(out));
'''
    tmp = Path(__file__).resolve().parent / '__pycache__'
    tmp.mkdir(exist_ok=True)
    (tmp / 'ch02_runner.js').write_text(runner, encoding='utf-8')
    (tmp / 'ch02_progs.json').write_text(json.dumps(progs), encoding='utf-8')
    r = subprocess.run(['node', str(tmp / 'ch02_runner.js'), str(JS), str(tmp / 'ch02_progs.json')],
                       capture_output=True, text=True, encoding='utf-8')
    if r.returncode:
        print(r.stderr[-2000:]); sys.exit(1)
    got = json.loads(r.stdout)
    bad = 0
    for p, w, g in zip(progs, want, got):
        if w != g:
            bad += 1
            if bad <= 3:
                print('MISMATCH', json.dumps(p), '\n want', json.dumps(w), '\n got ', json.dumps(g))
    kinds = {'compile errors': sum(1 for w in want if w['compile']), 'run-time errors': sum(1 for w in want if w['run'] and w['run']['error']),
             'clean': sum(1 for w in want if not w['compile'] and not w['run']['error'])}
    print({'programs': len(progs), 'mismatches': bad, **kinds})
    assert bad == 0
    return len(progs)


if __name__ == '__main__':
    print(check_examples(), 'examples checked')
    page()
    test()
