"""Test the JavaScript of the Chapter 4 interactive pages (book/assets/javascripts/ch04-numbase.js) against
numbase_lib.py and Python's own encoders (26 Nov 2026). Makes several hundred cases, runs them through node, and
compares every answer. Run from the repository root:  python tools/ch04_js_test.py   (needs node on the PATH)"""
import json
import random
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numbase_lib as nb  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
JS = ROOT / 'book' / 'assets' / 'javascripts' / 'ch04-numbase.js'
R = random.Random(11)


def ref(text, a, b, places):
    """What the converter must answer: exact digits, or the first `places` digits of a fraction that does not end."""
    v = nb.value(text, a)
    if a != 10:
        places = 200          # between binary, octal and hex every fraction ends: all its digits are exact
    w = int(v)
    f = v - w
    wd = nb.to_base(w, b)
    digits = ''
    while f and len(digits) < places:
        p = f * b
        d = int(p)
        digits += nb.DIGITS[d]
        f = p - d
    if b != 10 and a != 10:
        digits = digits.rstrip('0')
    if b == 10:                                   # to decimal: always exact here (denominators are powers of 2)
        digits, f2 = '', v - w
        while f2:
            p = f2 * 10
            d = int(p)
            digits += str(d)
            f2 = p - d
    return wd + ('.' + digits if digits else ''), f == 0 or b == 10


cases = []
for _ in range(600):
    a, b = R.choice([(10, 2), (10, 8), (10, 16), (2, 10), (8, 10), (16, 10), (2, 8), (2, 16), (8, 2), (16, 2), (8, 16), (16, 8)])
    whole = R.choice([0, R.randint(1, 20), R.randint(21, 5000), R.randint(5001, 10 ** 9)])
    text = nb.to_base(whole, a)
    if R.random() < 0.45:
        if a == 10:
            text += '.' + R.choice(['5', '25', '375', '1', '3', '6875', '7', '45', '05', '828125'])
        else:
            text += '.' + ''.join(R.choice(nb.DIGITS[:a]) for _ in range(R.randint(1, 5)))
    places = R.choice([6, 8, 10])
    want, exact = ref(text, a, b, places)
    cases.append({'text': text, 'from': a, 'to': b, 'places': places, 'want': want, 'exact': exact})
bad_inputs = [('1021', 2), ('19', 8), ('G1', 16), ('1.2.3', 10), ('', 10), ('12a', 10)]
texts = ['A', 'a', '₹', 'अ', '😀', 'हम सब एक', 'नमस्ते', 'é', 'India भारत', '\U0001F468‍\U0001F469‍\U0001F467']
enc = [{'text': t, 'cps': [ord(c) for c in t], 'u8': len(t.encode('utf-8')), 'u32': len(t.encode('utf-32-le')),
        'u8hex': [c.encode('utf-8').hex().upper() for c in t]} for t in texts]

runner = r"""
const C = require(process.argv[2]);
const data = JSON.parse(require('fs').readFileSync(process.argv[3], 'utf8'));
const out = {conv: [], bad: [], enc: []};
for (const c of data.cases) {
  const r = C.convert(c.text, c.from, c.to, c.places);
  out.conv.push({ok: r.ok, answer: r.answer, exact: r.exact, same: r.same, err: r.error || ''});
}
for (const [t, b] of data.bad) out.bad.push(C.convert(t, b, 2, 8).ok);
const te = new TextEncoder();
for (const e of data.enc) {
  const cps = Array.from(e.text).map(ch => ch.codePointAt(0));
  const u8 = Array.from(e.text).map(ch => Array.from(te.encode(ch)).map(x => x.toString(16).toUpperCase().padStart(2, '0')).join(''));
  out.enc.push({cps, u8, total8: te.encode(e.text).length, total32: cps.length * 4});
}
console.log(JSON.stringify(out));
"""
with tempfile.TemporaryDirectory() as td:
    (Path(td) / 'run.js').write_text(runner, encoding='utf-8')
    (Path(td) / 'data.json').write_text(json.dumps({'cases': cases, 'bad': bad_inputs, 'enc': enc}, ensure_ascii=False), encoding='utf-8')
    res = subprocess.run(['node', str(Path(td) / 'run.js'), str(JS), str(Path(td) / 'data.json')], capture_output=True, text=True, encoding='utf-8')
if res.returncode:
    print(res.stderr)
    sys.exit(1)
out = json.loads(res.stdout)
fails = 0
for c, r in zip(cases, out['conv']):
    if not r['ok'] or r['answer'] != c['want'] or (c['exact'] and not r['same']):
        fails += 1
        if fails <= 10:
            print('FAIL', c, r)
for (t, b), okk in zip(bad_inputs, out['bad']):
    if okk:
        fails += 1
        print('FAIL bad input accepted', t, b)
for e, r in zip(enc, out['enc']):
    if r['cps'] != e['cps'] or r['u8'] != e['u8hex'] or r['total8'] != e['u8'] or r['total32'] != e['u32']:
        fails += 1
        print('FAIL encoding', e['text'], r)
print(f'{len(cases)} conversions, {len(bad_inputs)} wrong inputs, {len(enc)} texts: {fails} failures')
sys.exit(1 if fails else 0)
