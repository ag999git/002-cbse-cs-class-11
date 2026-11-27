/* Chapter 6: four "See it" pages (27 Nov 2026; online plan v2, O3).
   tokens(line)  cuts one line into tokens and names the kind of each, as the book does (section 6.4): keyword,
                 identifier, literal, operator, punctuator; a comment is shown as skipped. Lines it does not handle
                 (f-strings, a backslash at the end) get a plain "not covered here" note; lines Python would refuse
                 (an unclosed string or bracket, a symbol such as $ or ?) get "Python would refuse this line".
   checkName(s)  says whether a name is a valid identifier, a keyword, or invalid (and which rule), and adds the
                 conventions of PEP 8 (section 6.5).
   Both are tested by tools/ch06_js_test.py against Python's own tokenize, str.isidentifier() and keyword.
   The other two pages (interactive or script; names and objects) only replay data made by real Python when the
   pages are generated (tools/ch06_seeit.py). No eval of typed text.  */
(function (root) {
  'use strict';

  var KEYWORDS = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'];
  var KW = {};
  KEYWORDS.forEach(function (k) { KW[k] = true; });
  var PUNCT = { '(': 1, ')': 1, '[': 1, ']': 1, '{': 1, '}': 1, ',': 1, ':': 1, '.': 1, ';': 1, '@': 1 };
  var OPS = ['**=', '//=', '>>=', '<<=', '...', '->', ':=', '!=', '==', '<=', '>=', '**', '//', '<<', '>>', '+=', '-=',
    '*=', '/=', '%=', '&=', '|=', '^=', '@=', '+', '-', '*', '/', '%', '<', '>', '=', '&', '|', '^', '~', '@',
    '(', ')', '[', ']', '{', '}', ',', ':', '.', ';'];
  var OPEN = { '(': ')', '[': ']', '{': '}' };

  // Python's number grammar (the same as the tokenize module's)
  var D = '[0-9](?:_?[0-9])*';
  var EXP = '[eE][-+]?' + D;
  var POINTFLOAT = '(?:' + D + '\\.(?:' + D + ')?|\\.' + D + ')(?:' + EXP + ')?';
  var EXPFLOAT = D + EXP;
  var FLOAT = '(?:' + POINTFLOAT + '|' + EXPFLOAT + ')';
  var IMAG = '(?:' + D + '[jJ]|' + FLOAT + '[jJ])';
  var INT = '(?:0[xX](?:_?[0-9a-fA-F])+|0[bB](?:_?[01])+|0[oO](?:_?[0-7])+|0(?:_?0)*|[1-9](?:_?[0-9])*)';
  var NUMBER = new RegExp('^(?:' + IMAG + '|' + FLOAT + '|' + INT + ')');
  var NAME_START = /[\p{XID_Start}_]/u;
  var NAME = /^[\p{XID_Start}_][\p{XID_Continue}]*/u;
  var STR_PREFIX = /^(?:[rR][bB]?|[bB][rR]?|[uU])?(?=['"])/;

  function tokens(line) {
    var out = [], i = 0, stack = [], m;
    var s = line.replace(/\s+$/, '');
    if (/\\$/.test(s)) return { status: 'not covered', why: 'a backslash at the end continues the statement on the next line; type the whole statement on one line' };
    while (i < s.length) {
      var c = s[i], rest = s.slice(i);
      if (c === ' ' || c === '\t') { i++; continue; }
      if (c === '#') { out.push({ text: rest, kind: 'comment' }); break; }
      if (/^[fF][rR]?['"]|^[rR][fF]['"]/.test(rest)) return { status: 'not covered', why: 'f-strings are taught in a later chapter' };
      var pm = STR_PREFIX.exec(rest);
      if (pm) {
        var p = pm[0].length, q = rest[p], triple = rest.substr(p, 3) === q + q + q, j = p + (triple ? 3 : 1), closed = false;
        var raw = /[rR]/.test(pm[0]);
        while (j < rest.length) {
          if (rest[j] === '\\' && !raw) { j += 2; continue; }
          if (rest[j] === '\\' && raw) { j += 2; continue; }
          if (triple ? rest.substr(j, 3) === q + q + q : rest[j] === q) { j += triple ? 3 : 1; closed = true; break; }
          j++;
        }
        if (!closed) return { status: 'refused', why: 'a string is opened with ' + (triple ? q + q + q : q) + ' but not closed on this line' };
        out.push({ text: rest.slice(0, j), kind: 'literal', sub: 'string' });
        i += j;
        continue;
      }
      if (/[0-9]/.test(c) || (c === '.' && /[0-9]/.test(s[i + 1] || ''))) {
        m = NUMBER.exec(rest);
        var after = m ? rest[m[0].length] || '' : '';
        if (!m || /[0-9A-Za-z_.]/.test(after)) {
          return { status: 'refused', why: 'this is not a valid number: ' + rest.split(/[\s()\[\]{},:;+\-*\/%=<>!]/)[0] };
        }
        if (/^0+[1-9]/.test(rest.split(/[^0-9]/)[0])) return { status: 'refused', why: 'a whole number may not begin with 0' };
        out.push({ text: m[0], kind: 'literal', sub: 'number' });
        i += m[0].length;
        continue;
      }
      if (NAME_START.test(c)) {
        m = NAME.exec(rest);
        var w = m[0];
        out.push({ text: w, kind: KW[w] ? 'keyword' : 'identifier' });
        i += w.length;
        continue;
      }
      var op = null;
      for (var k = 0; k < OPS.length; k++) if (rest.substr(0, OPS[k].length) === OPS[k]) { op = OPS[k]; break; }
      if (!op) return { status: 'refused', why: 'the symbol ' + c + ' is not part of Python (outside a string or comment)' };
      if (OPEN[op]) stack.push(OPEN[op]);
      else if (op === ')' || op === ']' || op === '}') {
        if (!stack.length || stack.pop() !== op) return { status: 'refused', why: 'the bracket ' + op + ' does not match an open one' };
      }
      out.push({ text: op, kind: PUNCT[op] ? 'punctuator' : 'operator' });
      i += op.length;
    }
    if (stack.length) return { status: 'refused', why: 'a bracket is opened but not closed on this line' };
    return { status: 'ok', tokens: out };
  }

  var BUILTINS = ['print', 'input', 'len', 'int', 'float', 'str', 'list', 'tuple', 'dict', 'set', 'sum', 'max', 'min',
    'type', 'id', 'range', 'abs', 'round', 'bool', 'sorted', 'open', 'eval'];
  var SOFT = { 'match': 1, 'case': 1, 'type': 1, '_': 1 };

  function checkName(s) {
    if (s === '') return { verdict: 'empty', why: 'Type a name.' };
    if (KW[s]) return { verdict: 'keyword', why: '"' + s + '" is a keyword: Python reserves it, so it cannot be a name (rule 3).' };
    if (/^[0-9]/.test(s)) return { verdict: 'invalid', why: 'A name may not begin with a digit (rule 1).' };
    var bad = null;
    for (var i = 0; i < s.length; i++) {
      var ch = s[i];
      if (i === 0 ? !NAME_START.test(ch) : !/[\p{XID_Continue}]/u.test(ch)) { bad = ch; break; }
    }
    if (bad !== null) {
      if (bad === ' ') return { verdict: 'invalid', why: 'A name may not contain a space: Python would read two names (rule 2).' };
      if (/[\uD800-\uDFFF]/.test(bad)) return { verdict: 'invalid', why: 'This character is not allowed in a name (rule 2).' };
      return { verdict: 'invalid', why: 'The character ' + bad + ' is not allowed: a name may have only letters, digits and _ (rule ' + (s.indexOf(bad) === 0 ? '1' : '2') + ').' };
    }
    var notes = [];
    if (s === 'l' || s === 'O' || s === 'I') notes.push('Legal, but avoid it: ' + s + ' looks like the digit ' + (s === 'O' ? '0' : '1') + '.');
    if (BUILTINS.indexOf(s) >= 0) notes.push('Legal, but it hides Python\'s own ' + s + '(): after this, ' + s + '() stops working.');
    if (SOFT[s]) notes.push('Legal: a "soft keyword", a name everywhere except in one special statement (not in your syllabus).');
    if (/[^\x00-\x7F]/.test(s)) notes.push('Legal: Python accepts names in Indian scripts and other languages. In the exam and in shared code, use English names.');
    else if (/^[A-Z0-9_]+$/.test(s) && /[A-Z]/.test(s) && s.length > 1) notes.push('Fine for a constant (a value that never changes); variables use small letters.');
    else if (/[A-Z]/.test(s) && !/^__/.test(s)) notes.push('Legal, but Python\'s convention is snake_case: small letters joined by _ (for example ' + snake(s) + ').');
    if (/^__.*__$/.test(s) && s.length > 4) notes.push('Legal, but names like this are Python\'s own special names: do not make your own.');
    if (s.length === 1 && notes.length === 0) notes.push('Legal, but a meaningful name such as total or count is easier to read.');
    return { verdict: notes.length ? 'style' : 'valid', why: notes.length ? notes.join(' ') : 'A valid name, and a good one.' };
  }

  function snake(s) {
    return s.replace(/([a-z0-9])([A-Z])/g, '$1_$2').toLowerCase();
  }

  function esc(t) {
    return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // ---------------------------------------------------------------- page: token explorer
  function tokenPage(ids) {
    var inp = document.getElementById(ids.input), res = document.getElementById(ids.result);
    function show() {
      var r = tokens(inp.value);
      if (r.status === 'not covered') { res.innerHTML = '<p class="ch06-note">Not covered here: ' + esc(r.why) + '.</p>'; return; }
      if (r.status === 'refused') { res.innerHTML = '<p class="ch06-bad">Python would refuse this line: ' + esc(r.why) + '.</p>'; return; }
      if (!r.tokens.length) { res.innerHTML = '<p class="ch06-note">Type a line of Python.</p>'; return; }
      var n = r.tokens.filter(function (t) { return t.kind !== 'comment'; }).length;
      var html = '<div class="ch06-tokens">';
      r.tokens.forEach(function (t) {
        html += '<span class="ch06-tok ch06-' + t.kind + '"><code>' + esc(t.text) + '</code><small>' +
          (t.kind === 'comment' ? 'comment: skipped, not a token' : t.kind) + '</small></span>';
      });
      html += '</div><p><b>' + n + ' token' + (n === 1 ? '' : 's') + '.</b> ' + counts(r.tokens) + '</p>';
      res.innerHTML = html;
    }
    inp.oninput = show;
    document.querySelectorAll ? document.querySelectorAll('[data-ch06-line]').forEach(function (b) {
      b.onclick = function () { inp.value = b.getAttribute('data-ch06-line'); show(); };
    }) : null;
    show();
    return show;
  }

  function counts(toks) {
    var c = {};
    toks.forEach(function (t) { if (t.kind !== 'comment') c[t.kind] = (c[t.kind] || 0) + 1; });
    return ['keyword', 'identifier', 'literal', 'operator', 'punctuator'].filter(function (k) { return c[k]; })
      .map(function (k) { return c[k] + ' ' + k + (c[k] > 1 ? 's' : ''); }).join(', ') + '.';
  }

  // ---------------------------------------------------------------- page: identifier checker
  function namePage(ids) {
    var inp = document.getElementById(ids.input), res = document.getElementById(ids.result);
    var label = { valid: 'Valid', style: 'Valid, but see the note', keyword: 'Not allowed: a keyword', invalid: 'Not allowed', empty: '' };
    function show() {
      var r = checkName(inp.value);
      res.innerHTML = r.verdict === 'empty' ? '<p class="ch06-note">' + r.why + '</p>' :
        '<p class="ch06-' + (r.verdict === 'valid' || r.verdict === 'style' ? 'good' : 'bad') + '"><b>' + label[r.verdict] +
        '.</b> ' + esc(r.why) + '</p>';
    }
    inp.oninput = show;
    show();
    return show;
  }

  // ---------------------------------------------------------------- page: interactive or script (replay)
  function modesPage(data, ids) {
    var sel = document.getElementById(ids.select), src = document.getElementById(ids.source),
      shell = document.getElementById(ids.shell), script = document.getElementById(ids.script),
      next = document.getElementById(ids.next), all = document.getElementById(ids.all), note = document.getElementById(ids.note);
    var prog, step;
    function render() {
      var h = '';
      for (var k = 0; k < step; k++) {
        h += '<span class="ch06-prompt">&gt;&gt;&gt; </span>' + esc(prog.lines[k]) + '\n';
        if (prog.shell[k]) h += '<span class="ch06-out">' + esc(prog.shell[k]) + '</span>\n';
      }
      if (step < prog.lines.length) h += '<span class="ch06-prompt">&gt;&gt;&gt; </span>';
      shell.innerHTML = h;
      script.innerHTML = step >= prog.lines.length ? (prog.script ? '<span class="ch06-out">' + esc(prog.script) + '</span>' : '<i>(nothing is shown)</i>') : '<i>press "Next line" or "Run all"</i>';
      note.innerHTML = step >= prog.lines.length ? esc(prog.note) : '';
    }
    function choose() {
      prog = data[sel.value];
      src.innerHTML = prog.lines.map(function (l, k) { return '<span class="ch06-ln">' + (k + 1) + '</span> ' + esc(l); }).join('\n');
      step = 0;
      render();
    }
    next.onclick = function () { if (step < prog.lines.length) step++; render(); };
    all.onclick = function () { step = prog.lines.length; render(); };
    sel.onchange = choose;
    choose();
  }

  // ---------------------------------------------------------------- page: names and objects (replay)
  function objectsPage(data, ids) {
    var sel = document.getElementById(ids.select), src = document.getElementById(ids.source),
      pic = document.getElementById(ids.picture), next = document.getElementById(ids.next),
      back = document.getElementById(ids.back), note = document.getElementById(ids.note), tutor = document.getElementById(ids.tutor);
    var prog, step;
    function draw(st) {
      var objs = st.objects, names = st.names, H = Math.max(objs.length, names.length, 1) * 56 + 20;
      var svg = '<svg viewBox="0 0 420 ' + H + '" width="420" height="' + H + '" role="img" aria-label="names and objects">';
      objs.forEach(function (o, k) {
        var y = 14 + k * 56, cls = o.orphan ? 'ch06-orphan' : 'ch06-obj';
        svg += '<rect class="' + cls + '" x="250" y="' + y + '" width="150" height="32" rx="6"/>' +
          '<text class="ch06-objtext" x="325" y="' + (y + 21) + '" text-anchor="middle">' + esc(o.repr) + '</text>' +
          '<text class="ch06-type" x="325" y="' + (y + 43) + '" text-anchor="middle">' + esc(o.orphan ? 'no tag now' : o.type) + '</text>';
      });
      names.forEach(function (n, k) {
        var y = 14 + k * 56, ty = 14 + n.obj * 56 + 16;
        svg += '<rect class="ch06-tag" x="10" y="' + y + '" width="110" height="32" rx="4"/>' +
          '<text class="ch06-tagtext" x="65" y="' + (y + 21) + '" text-anchor="middle">' + esc(n.name) + '</text>' +
          '<line class="ch06-arrow" x1="122" y1="' + (y + 16) + '" x2="246" y2="' + ty + '" marker-end="url(#ch06-head)"/>';
      });
      svg += '<defs><marker id="ch06-head" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" class="ch06-head"/></marker></defs></svg>';
      return svg;
    }
    function render() {
      src.innerHTML = prog.lines.map(function (l, k) {
        return '<span class="' + (k === step - 1 ? 'ch06-now' : '') + '"><span class="ch06-ln">' + (k + 1) + '</span> ' + esc(l) + '</span>';
      }).join('\n');
      var st = prog.states[step];
      pic.innerHTML = step === 0 ? '<p class="ch06-note">Press "Next line" to run line 1.</p>' : draw(st);
      note.innerHTML = step === 0 ? '' : '<b>After line ' + step + ':</b> ' + esc(st.note) + (st.output ? ' <b>Output:</b> <code>' + esc(st.output) + '</code>' : '');
    }
    function choose() {
      prog = data[sel.value];
      step = 0;
      if (tutor) tutor.href = prog.tutor;
      render();
    }
    next.onclick = function () { if (step < prog.lines.length) step++; render(); };
    back.onclick = function () { if (step > 0) step--; render(); };
    sel.onchange = choose;
    choose();
  }

  var api = { tokens: tokens, checkName: checkName, tokenPage: tokenPage, namePage: namePage, modesPage: modesPage,
    objectsPage: objectsPage, KEYWORDS: KEYWORDS };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.Ch06 = api;
})(typeof window !== 'undefined' ? window : globalThis);
