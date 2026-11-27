"""Chapter 5, QR 0507: the dry-run player page, and its test (27 Nov 2026; decision D5: free inputs, with tests).

1. Export W1-W10 (the printed descriptions, via algo_lib) to the page as JSON: boxes, what each box does, where each
   box is on the printed picture (so the page can frame the box being run), the pseudocode of each step.
2. Write book/unit-2/005-ch05-problem-solving/see-it-dry-run-player.md.
3. Test: node runs book/assets/javascripts/ch05-dryrun.js on hundreds of inputs; every step number, every
   "What happens" text, every output and every error must be exactly what algo_lib gives.
Run from the repository root:  python tools/ch05_player.py"""
import copy
import json
import random
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ch05_pages as P1  # noqa: E402
from ch05_pages import ok, write, IMG, REL  # noqa: E402
from ch05_pages2 import W, WTITLE  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
JS = ROOT / 'book' / 'assets' / 'javascripts' / 'ch05-dryrun.js'
EXAMPLE = {'W1': '2, 3', 'W2': '5, 3', 'W3': '7, 12', 'W4': '7', 'W5': '9, 9, 4', 'W6': '80, 75, 70, 72, 78',
           'W7': '6, 9, 0', 'W8': '30, 21', 'W9': '2, 3', 'W10': '4'}
HINT = {'W1': 'Type a and b.', 'W2': 'Type the length and the breadth.', 'W3': 'Type a and b. Try two equal numbers too.',
        'W4': 'Type one whole number.', 'W5': 'Type a, b and c. Try two equal numbers.',
        'W6': 'Type the five marks. Try 33 and 32 in one subject.',
        'W7': 'Type the numbers, then 0 (the 0 ends the list). What happens if 0 comes first?',
        'W8': 'Type a and b. Try 1071, 462, or the smaller first: 12, 18.', 'W9': 'Type x and n.',
        'W10': 'Type n (try 0, and 20).'}


def no_fstring(expr):
    """f'{a} {lcm}' -> str(a) + ' ' + str(lcm): the page's reader knows str() but not f-strings."""
    m = re.fullmatch(r"f'(.*)'", expr)
    if not m:
        return expr
    parts = re.split(r'(\{[^}]+\})', m.group(1))
    out = [f'str({p[1:-1]})' if p.startswith('{') else repr(p) for p in parts if p]
    return ' + '.join(out)


def export():
    data = {}
    for key, algo in W.items():
        a = copy.copy(algo)
        a.name = f'c05-player-{key}'
        a.draw(IMG)
        x0, x1, y0, y1 = a.bounds
        wd, ht = x1 - x0, y1 - y0
        code = {}
        for n, line in algo.pseudo:
            if n and n not in code:
                code[n] = line.strip().split('  ')[0].strip()
        nodes, box = {}, {}
        for x in algo.nodes:
            cx, cy = x.at
            w, h = x.wh
            nodes[str(x.num)] = dict(num=x.num, kind=x.kind, text=x.text, reads=x.reads, do=x.do, test=x.test,
                                     show=no_fstring(x.show), next=x.next, yes=x.yes, no=x.no)
            box[str(x.num)] = [round((cx - w / 2 - 0.04 - x0) / wd * 100, 3), round((y1 - cy - h / 2 - 0.04) / ht * 100, 3),
                               round((w + 0.08) / wd * 100, 3), round((h + 0.08) / ht * 100, 3)]
        data[key] = dict(title=f'{key}. {WTITLE[key]}', img=f'../../../assets/images/ch05/c05-player-{key}.png', nodes=nodes,
                         box=box, code={str(k): v for k, v in code.items()}, example=EXAMPLE[key], hint=HINT[key])
        for s in [EXAMPLE[key]]:
            vals = [int(v) for v in s.split(',')]
            ok(algo.run(vals)[0] == algo.run_python(vals))
    return data


def page(data):
    opts = '\n'.join(f'<option value="{k}">{v["title"]}</option>' for k, v in data.items())
    t = P1.head('The dry-run player', 'See it',
                'Choose a worked example, type your own inputs and press Next step: the box being run is framed on '
                'the flowchart, and the walk-through table of the printed book grows one row at a time.',
                src='tools/ch05_player.py')
    t += f'''<div class="dryrun" markdown="0">
<p><label>Worked example: <select id="dr-select">
{opts}
</select></label></p>
<p><label>Inputs, separated by commas: <input id="dr-inputs" type="text" size="28"></label></p>
<p><button id="dr-next" class="md-button md-button--primary">Next step</button>
<button id="dr-all" class="md-button">Run to the end</button>
<button id="dr-reset" class="md-button">Start again</button></p>
<p id="dr-message"></p>
<div class="dryrun-grid">
<div id="dr-picture"></div>
<div>
<p><b>Variables now:</b><br><span id="dr-vars"></span></p>
<p><b>Output:</b><br><span id="dr-output"></span></p>
<div id="dr-table"></div>
</div>
</div>
</div>
<script id="dr-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>
<script>
document.addEventListener('DOMContentLoaded', function () {{   /* the site's scripts load after this page's text */
  Ch05.player(JSON.parse(document.getElementById('dr-data').textContent),
    {{select: 'dr-select', inputs: 'dr-inputs', picture: 'dr-picture', message: 'dr-message', table: 'dr-table',
     vars: 'dr-vars', output: 'dr-output', next: 'dr-next', all: 'dr-all', reset: 'dr-reset'}});
}});
</script>

## How to use it

1. Choose a worked example. Its usual inputs are typed for you; change them if you like.
2. Press **Next step** again and again. The **framed** box is the one that runs next; the boxes already run are shaded.
3. Read the new row of the walk-through: the step number, its pseudocode and what happened.
4. **Run to the end** does every step at once; **Start again** goes back to Start with the inputs in the box.

## Things to try

- **W3** with 7, 7: the two numbers are equal. Which one is printed, and why is that still right?
- **W5** with 9, 9, 4, then with 4, 9, 9: is the answer right both times?
- **W6** with 33, 60, 65, 70, 62 and then with 32, 60, 65, 70, 62: one mark changes the whole result.
- **W7** with 0 alone: the loop never runs and count stays 0. The player stops with "division by zero" at box 7.
  A careful algorithm would check count before dividing.
- **W8** with 12, 18: the smaller number first. Watch round 1 swap the numbers.
- **W10** with 20: the answer has 19 digits; the player keeps every digit, as Python does.

*The player runs the same flowcharts as the printed book, and it was tested on hundreds of inputs: every step, every
value and every output is what the book's own program gives.*
'''
    write('see-it-dry-run-player.md', t)


def cases():
    R = random.Random(27)
    C = {}
    ints = lambda k, lo=-50, hi=50: [R.randint(lo, hi) for _ in range(k)]
    C['W1'] = [ints(2) for _ in range(40)] + [[2.5, 3], [0.1, 0.2], [10 ** 20, 1]]
    C['W2'] = [ints(2, 0, 99) for _ in range(40)] + [[2.5, 4], [7, 7]]
    C['W3'] = [ints(2) for _ in range(40)] + [[7, 7]]
    C['W4'] = [[v] for v in range(-20, 21)]
    C['W5'] = [ints(3, -5, 5) for _ in range(80)] + [[9, 9, 4], [4, 9, 9], [5, 5, 5]]
    C['W6'] = [ints(5, 0, 100) for _ in range(80)] + [[33] * 5, [32, 90, 90, 90, 90], [90] * 5, [75, 75, 75, 75, 74],
                                                      [80.5, 75, 70, 72, 78]]
    C['W7'] = [ints(R.randint(0, 6), 1, 99) + [0] for _ in range(40)] + [[0], [2.5, 0], [-5, 5, 3, 0], [1, 2]]
    C['W8'] = [ints(2, 1, 5000) for _ in range(60)] + [[12, 18], [8, 8], [0, 5], [5, 0], [0, 0], [987, 610]]
    C['W9'] = [[R.randint(-4, 6), R.randint(0, 12)] for _ in range(40)] + [[2, 60], [10, 20], [0.5, 3]]
    C['W10'] = [[v] for v in range(0, 26)] + [[-3]]
    return C


def expected(algo, stream):
    try:
        out, trace = algo.run(stream, limit=2000)
    except ZeroDivisionError:
        return {'error': 'ZeroDivisionError'}
    except IndexError:
        return {'error': 'no input'}
    rows = algo.walkthrough_rows(stream, telling=False)
    return {'steps': [int(r[0]) for r in rows], 'what': [r[2] for r in rows], 'out': out}


def js_value(v):
    return {'i': str(v)} if isinstance(v, int) else {'f': v}


def test(data):
    C = cases()
    jobs = []
    for key, streams in C.items():
        for s in streams:
            jobs.append({'key': key, 'inputs': [js_value(v) for v in s], 'want': expected(W[key], s)})
    runner = '''
const Ch05 = require(process.argv[2]);
const data = JSON.parse(require('fs').readFileSync(process.argv[3], 'utf8'));
const jobs = JSON.parse(require('fs').readFileSync(process.argv[4], 'utf8'));
let bad = 0;
for (const j of jobs) {
  const vals = j.inputs.map(v => ('i' in v) ? BigInt(v.i) : v.f);
  const m = new Ch05.Machine(data[j.key], vals).runAll();
  let ok;
  if (j.want.error) {
    ok = !!m.error && (j.want.error === 'no input' ? /no input is left/.test(m.error) : /ZeroDivisionError/.test(m.error));
  } else {
    const steps = m.rows.map(r => r.step), what = m.rows.map(r => r.what);
    ok = !m.error && JSON.stringify(steps) === JSON.stringify(j.want.steps) && JSON.stringify(what) === JSON.stringify(j.want.what)
         && JSON.stringify(m.out) === JSON.stringify(j.want.out);
    if (!ok && bad < 5) console.log(JSON.stringify({key: j.key, inputs: j.inputs, err: m.error, got: {steps, what, out: m.out}, want: j.want}));
  }
  if (!ok) bad++;
}
// wrong inputs give a message, not a crash
for (const s of ['seven', '7,,x', '1.2.3']) { if (!Ch05.readInputs(s).error) { console.log('accepted', s); bad++; } }
if (!Ch05.readInputs(' 7 , 12 ').values || Ch05.readInputs('').values.length !== 0) { console.log('readInputs'); bad++; }
console.log(JSON.stringify({jobs: jobs.length, bad}));
'''
    tmp = Path(__file__).resolve().parent / '__pycache__'
    tmp.mkdir(exist_ok=True)
    (tmp / 'ch05_runner.js').write_text(runner, encoding='utf-8')
    (tmp / 'ch05_data.json').write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    (tmp / 'ch05_jobs.json').write_text(json.dumps(jobs), encoding='utf-8')
    r = subprocess.run(['node', str(tmp / 'ch05_runner.js'), str(JS), str(tmp / 'ch05_data.json'), str(tmp / 'ch05_jobs.json')],
                       capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-3000:], r.stderr[-2000:])
    res = json.loads(r.stdout.strip().split('\n')[-1])
    ok(res['bad'] == 0, res)
    return res


if __name__ == '__main__':
    d = export()
    page(d)
    print(test(d), P1.checks, 'checks passed')
