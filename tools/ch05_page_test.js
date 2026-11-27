// Run from the repository root:  node tools/ch05_page_test.js
// Run the dry-run player page's own script against a small fake page: choose every worked example, press
// Next step, Run to the end and Start again, type a wrong input, and report any error or empty output.
const fs = require('fs');
const path = require('path');
const md = fs.readFileSync(path.join('book/unit-2/005-ch05-problem-solving/see-it-dry-run-player.md'), 'utf8');
const data = JSON.parse(/<script id="dr-data" type="application\/json">([\s\S]*?)<\/script>/.exec(md)[1]);
const els = {};
const doc = { getElementById(id) { return els[id] || (els[id] = { id, value: '', innerHTML: '', textContent: '', onclick: null, onchange: null }); } };
global.document = doc;
global.window = global;
const Ch05 = require(path.resolve('book/assets/javascripts/ch05-dryrun.js'));
const ids = { select: 's', inputs: 'i', picture: 'p', message: 'm', table: 't', vars: 'v', output: 'o', next: 'n', all: 'a', reset: 'r' };
doc.getElementById('s').value = 'W1';
Ch05.player(data, ids);
let bad = 0;
for (const k of Object.keys(data)) {
  els.s.value = k; els.s.onchange();
  if (els.i.value !== data[k].example) { console.log('example not typed', k); bad++; }
  els.n.onclick(); els.n.onclick();
  if (!/<td>/.test(els.t.innerHTML) || !/border:4px/.test(els.p.innerHTML)) { console.log('no row or frame', k); bad++; }
  els.a.onclick();
  if (!/Stop reached/.test(els.m.innerHTML) || /nothing printed/.test(els.o.innerHTML)) { console.log('not finished', k, els.m.innerHTML); bad++; }
  els.r.onclick();
  if (/<td>/.test(els.t.innerHTML)) { console.log('reset left rows', k); bad++; }
}
els.s.value = 'W3'; els.s.onchange(); els.i.value = 'seven'; els.n.onclick();
if (!/not a number/.test(els.m.innerHTML)) { console.log('wrong input not refused'); bad++; }
els.s.value = 'W7'; els.s.onchange(); els.i.value = '0'; els.a.onclick();
if (!/ZeroDivisionError/.test(els.m.innerHTML)) { console.log('no division message'); bad++; }
console.log(JSON.stringify({ examples: Object.keys(data).length, bad }));
process.exit(bad ? 1 : 0);
