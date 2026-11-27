// Run from the repository root:  node tools/ch06_page_test.js
// Runs the four Chapter 6 "See it" pages' scripts on a fake page: every example line and name, every program with
// Next line / Run all / Back; reports any error, empty result, or a shown output that differs from Python's.
const fs = require('fs'), path = require('path');
const DIR = 'book/unit-2/006-ch06-getting-started-with-python/';
const els = {};
let buttons = [];
global.document = {
  getElementById(id) { return els[id] || (els[id] = { id, value: '', innerHTML: '', href: '', onclick: null, onchange: null, oninput: null }); },
  querySelectorAll() { return buttons; },
};
global.window = global;
const Ch06 = require(path.resolve('book/assets/javascripts/ch06-seeit.js'));
let bad = 0;
const fail = (m) => { console.log('FAIL', m); bad++; };
const data = (file, id) => JSON.parse(new RegExp('<script id="' + id + '" type="application/json">([\\s\\S]*?)</script>')
  .exec(fs.readFileSync(DIR + file, 'utf8'))[1]);

// token explorer: every example button
const tmd = fs.readFileSync(DIR + 'see-it-token-explorer.md', 'utf8');
const lines = [...tmd.matchAll(/data-ch06-line="([^"]*)"/g)].map((m) => m[1].replace(/&quot;/g, '"'));
buttons = lines.map((l) => ({ getAttribute: () => l, onclick: null }));
els['tk-input'] = { value: lines[0], oninput: null };
Ch06.tokenPage({ input: 'tk-input', result: 'tk-result' });
buttons.forEach((b, k) => {
  b.onclick();
  const h = els['tk-result'].innerHTML;
  if (!h) fail('token example ' + k);
  if (/\$250/.test(lines[k]) && !/refuse/.test(h)) fail('$ not refused');
  if (/print\("Hi"$/.test(lines[k]) && !/refuse/.test(h)) fail('open bracket not refused');
  if (/^if marks/.test(lines[k]) && !/9 tokens/.test(h)) fail('book line: 9 tokens');
});
els['tk-input'].value = ''; els['tk-input'].oninput();
if (!/Type a line/.test(els['tk-result'].innerHTML)) fail('empty line');

// identifier checker: every example, and a few typed names
buttons = [];
Ch06.namePage({ input: 'id-input', result: 'id-result' });
const nmd = fs.readFileSync(DIR + 'see-it-identifier-checker.md', 'utf8');
const names = [...nmd.matchAll(/data-ch06-name="([^"]*)"/g)].map((m) => m[1]);
const want = { total_marks: /Valid\./, '2nd_rank': /Not allowed/, 'my marks': /space/, 'sum$': /Not allowed/, class: /keyword/,
  TotalMarks: /snake_case/, PASS_MARK: /constant/, print: /hides/, l: /looks like/, 'नाम': /Indian scripts/ };
names.forEach((n) => {
  els['id-input'].value = n; els['id-input'].oninput();
  if (!want[n] || !want[n].test(els['id-input'] && els['id-result'].innerHTML)) fail('name ' + n + ': ' + els['id-result'].innerHTML);
});

// interactive or script: every program, line by line and Run all
const md = data('see-it-interactive-or-script.md', 'md-data');
const mids = { select: 's1', source: 'src1', shell: 'sh1', script: 'sc1', next: 'n1', all: 'a1', note: 'no1' };
els.s1 = { value: Object.keys(md)[0] };
Ch06.modesPage(md, mids);
for (const k of Object.keys(md)) {
  els.s1.value = k; els.s1.onchange();
  if (!/\d/.test(els.src1.innerHTML)) fail('source ' + k);
  for (let i = 0; i < md[k].lines.length; i++) els.n1.onclick();
  md[k].shell.forEach((o) => { if (o && els.sh1.innerHTML.indexOf(o.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')) < 0) fail('shell output ' + k + ' ' + o); });
  if (md[k].script && els.sc1.innerHTML.indexOf(md[k].script.replace(/</g, '&lt;').replace(/>/g, '&gt;')) < 0) fail('script output ' + k);
  if (!md[k].script && !/nothing is shown/.test(els.sc1.innerHTML)) fail('empty script ' + k);
  if (!els.no1.innerHTML) fail('note ' + k);
  els.s1.onchange(); els.a1.onclick();
  if (!els.no1.innerHTML) fail('run all ' + k);
}

// names and objects: every program, forward to the end and back
const od = data('see-it-names-and-objects.md', 'ob-data');
const oids = { select: 's2', source: 'src2', picture: 'p2', next: 'n2', back: 'b2', note: 'no2', tutor: 't2' };
els.s2 = { value: Object.keys(od)[0] };
Ch06.objectsPage(od, oids);
for (const k of Object.keys(od)) {
  els.s2.value = k; els.s2.onchange();
  if (!/pythontutor\.com/.test(els.t2.href)) fail('tutor link ' + k);
  for (let i = 0; i < od[k].lines.length; i++) {
    els.n2.onclick();
    const st = od[k].states[i + 1];
    if (!/<svg/.test(els.p2.innerHTML)) fail('picture ' + k + ' ' + i);
    st.names.forEach((n) => { if (els.p2.innerHTML.indexOf('>' + n.name + '<') < 0) fail('tag ' + n.name + ' in ' + k); });
    if (els.no2.innerHTML.indexOf('After line ' + (i + 1)) < 0) fail('note ' + k + ' ' + i);
  }
  els.b2.onclick();
  if (od[k].lines.length > 1 && els.no2.innerHTML.indexOf('After line ' + (od[k].lines.length - 1)) < 0) fail('back ' + k);
  if (od[k].lines.length === 1 && !/Next line/.test(els.p2.innerHTML)) fail('back to the start ' + k);
}
console.log(JSON.stringify({ tokenExamples: lines.length, names: names.length, modes: Object.keys(md).length, objects: Object.keys(od).length, bad }));
process.exit(bad ? 1 : 0);
