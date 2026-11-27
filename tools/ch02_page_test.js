// Run from the repository root:  node tools/ch02_page_test.js
// Runs the compiler-vs-interpreter page's script on a fake page: every example, Compile, every Interpret step,
// Start again; reports any error or empty message.
const fs = require('fs'), path = require('path');
const md = fs.readFileSync('book/unit-1/002-ch02-software-and-os/see-it-compiler-interpreter.md', 'utf8');
const data = JSON.parse(/<script id="tr-data" type="application\/json">([\s\S]*?)<\/script>/.exec(md)[1]);
const els = {};
global.document = { getElementById(id) { return els[id] || (els[id] = { id, value: '', innerHTML: '', onclick: null, onchange: null }); } };
global.window = global;
const Ch02 = require(path.resolve('book/assets/javascripts/ch02-translate.js'));
const ids = { select: 's', code: 'c', compile: 'cp', step: 'st', reset: 'r', message: 'm', listing: 'l', output: 'o' };
document.getElementById('s').value = 'book';
Ch02.page(data, ids);
let bad = 0;
for (const k of Object.keys(data)) {
  els.s.value = k; els.s.onchange();
  if (els.c.value !== data[k].code.join('\n')) { console.log('code not loaded', k); bad++; }
  els.cp.onclick();
  if (!/Compiler:/.test(els.m.innerHTML) || !/<div/.test(els.l.innerHTML)) { console.log('compile shows nothing', k); bad++; }
  for (let i = 0; i < 12; i++) els.st.onclick();
  if (!/Interpreter:/.test(els.m.innerHTML)) { console.log('interpret shows nothing', k); bad++; }
  els.r.onclick();
  if (!/nothing shown yet/.test(els.o.innerHTML)) { console.log('reset', k); bad++; }
}
els.s.value = 'book'; els.s.onchange(); els.cp.onclick();
if (!/2 errors/.test(els.m.innerHTML)) { console.log('book: 2 errors not reported'); bad++; }
els.st.onclick(); els.st.onclick(); els.st.onclick();
if (!/stopped at line 3/.test(els.m.innerHTML) || !/10/.test(els.o.innerHTML)) { console.log('book: interpreter'); bad++; }
console.log(JSON.stringify({ examples: Object.keys(data).length, bad }));
process.exit(bad ? 1 : 0);
