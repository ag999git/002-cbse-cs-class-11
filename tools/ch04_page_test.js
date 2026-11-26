// Run from the repository root after "mkdocs build -d <site>":  node tools/ch04_page_test.js <site>
// Run the inline scripts of the three Chapter 4 interactive pages (as built by MkDocs) against a small fake page,
// press every button, and report any error or empty output.
const fs = require('fs');
const path = require('path');
const site = process.argv[2];
global.Ch04 = require(path.join(site, 'assets/javascripts/ch04-numbase.js'));
global.TextEncoder = require('util').TextEncoder;

function fakePage(html) {
  const els = {};
  const re = /<(input|select|div|p|span|button)([^>]*)>/g;
  let m;
  const all = [];
  while ((m = re.exec(html))) {
    const idm = /id="([^"]+)"/.exec(m[2]);
    const cls = (/class="([^"]+)"/.exec(m[2]) || [, ''])[1];
    const valm = /value="([^"]*)"/.exec(m[2]);
    const el = { tag: m[1], id: idm && idm[1], className: cls, innerHTML: '', textContent: '', value: valm ? valm[1] : '',
                 attrs: {}, getAttribute(k) { return this.attrs[k]; }, onclick: null, onchange: null, onkeydown: null };
    if (m[1] === 'select') {                       // selected option
      const rest = html.slice(m.index);
      const sel = rest.slice(0, rest.indexOf('</select>'));
      const s = /<option value="([^"]+)" selected>/.exec(sel) || /<option value="([^"]+)">/.exec(sel) || /<option selected>([^<]+)</.exec(sel) || /<option>([^<]+)</.exec(sel);
      el.value = s ? s[1] : '';
    }
    if (m[1] === 'button') { const t = html.slice(re.lastIndex, html.indexOf('</button>', re.lastIndex)); el.textContent = t; }
    if (el.id) els[el.id] = el;
    all.push(el);
  }
  return {
    els, all,
    getElementById: id => { if (!els[id]) throw new Error('no element #' + id); return els[id]; },
    querySelectorAll: q => {
      if (q === '.c4ex') return all.filter(e => / c4ex|c4ex /.test(' ' + e.className + ' '));
      if (q === '#c4trays .c4tray') {               // made from the drawn HTML
        const h = els.c4trays.innerHTML, out = [];
        const r2 = /data-i="(\d+)"/g; let k;
        while ((k = r2.exec(h))) out.push({ attrs: { 'data-i': k[1] }, getAttribute(a) { return this.attrs[a]; }, onclick: null });
        global.__trays = out;
        return out;
      }
      return [];
    },
  };
}

const pages = ['see-it-converter', 'see-it-trays-and-meter', 'see-it-letters-to-bytes'];
let problems = 0;
for (const p of pages) {
  const html = fs.readFileSync(path.join(site, 'unit-1/004-ch04-number-systems-and-encoding', p, 'index.html'), 'utf8');
  const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(x => x[1]).filter(s => s.includes("$('c4") || s.includes('Ch04'));
  if (!scripts.length) { console.log(p, 'NO INLINE SCRIPT'); problems++; continue; }
  const doc = fakePage(html);
  global.document = doc;
  try {
    scripts.forEach(s => new Function(s)());
    const E = doc.els;
    if (p === 'see-it-converter') {
      const cases = [['156', '10', '8'], ['11010110', '2', '16'], ['5A', '16', '8'], ['12.375', '10', '2'], ['0.1', '10', '2'], ['1021', '2', '10'], ['2F.8', '16', '10']];
      for (const [n, f, t] of cases) {
        E.c4n.value = n; E.c4f.value = f; E.c4t.value = t; E.c4go.onclick(); E.c4back.onclick();
        const ans = (E.c4out.innerHTML.match(/class="c4ans">([\s\S]*?)<\/p>/) || [, ''])[1].replace(/<[^>]+>/g, '');
        console.log(' ', n, f, '→', t, ':', ans || E.c4out.innerHTML.replace(/<[^>]+>/g, '').slice(0, 90), '|', E.c4chk.innerHTML.replace(/<[^>]+>/g, '').slice(0, 70));
        if (!E.c4out.innerHTML) problems++;
      }
    } else if (p === 'see-it-trays-and-meter') {
      console.log('  start:', E.c4tv.innerHTML.replace(/<[^>]+>/g, ''));
      E.c4tn.value = '2.625'; E.c4tset.onclick(); console.log('  2.625:', E.c4tv.innerHTML.replace(/<[^>]+>/g, ''));
      E.c4tn.value = '22'; E.c4tset.onclick(); console.log('  22:', E.c4tv.innerHTML.replace(/<[^>]+>/g, ''));
      E.c4tn.value = '300'; E.c4tset.onclick(); console.log('  300:', E.c4terr.textContent.slice(0, 60));
      doc.querySelectorAll('#c4trays .c4tray');
      E.c4mb.value = '2'; E.c4mb.onchange(); for (let i = 0; i < 13; i++) E.c4plus.onclick();
      console.log('  binary meter:', E.c4mv.innerHTML.replace(/<[^>]+>/g, ''));
      E.c4mb.value = '16'; E.c4mb.onchange(); E.c4plus.onclick();
      console.log('  hex meter:', E.c4wheels.innerHTML.replace(/<span class="c4wheel( changed)?">/g, (a, c) => c ? '[' : '').replace(/<\/span>/g, ' ').trim(), E.c4mv.innerHTML.replace(/<[^>]+>/g, ''));
      E.c4clear.onclick(); E.c4rand.onclick(); E.c4zero.onclick(); E.c4minus.onclick();
      console.log('  after −1 from 0:', E.c4mv.innerHTML.replace(/<[^>]+>/g, '').slice(0, 60));
    } else {
      for (const s of ['हम सब एक', 'A', '😀', 'नमस्ते', '']) {
        E.c4s.value = s; E.c4sgo.onclick();
        console.log(' ', JSON.stringify(s), (E.c4sout.innerHTML.match(/class="c4ans">([\s\S]*?)<\/p>/) || [, E.c4sout.innerHTML])[1].replace(/<[^>]+>/g, ''));
      }
      doc.querySelectorAll('.c4ex').forEach(b => b.onclick());
    }
    console.log(p, 'OK');
  } catch (e) {
    console.log(p, 'ERROR', e.stack);
    problems++;
  }
}
console.log('problems:', problems);
process.exit(problems ? 1 : 0);
