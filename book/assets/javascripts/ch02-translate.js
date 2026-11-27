/* Chapter 2: compiler vs interpreter, step by step (27 Nov 2026).
   A tiny teaching language with three kinds of line:  name = expression  ·  PRINT expression  ·  (a blank line).
   An expression is whole numbers and names joined by + - * /  (/ gives the whole-number part, as // in Python;
   * and / are done before + and -). Grammar errors are found by checking a line; "no value yet" and "division by 0"
   only while running. The same rules are written in Python in tools/ch02_translate.py, and tools/ch02_js_test.py
   checks that both give exactly the same result for hundreds of programs. No eval of typed text.
   Used by: see-it-compiler-interpreter. */
(function (root) {
  'use strict';

  var NAME = /^[A-Za-z_][A-Za-z0-9_]*$/;

  /* ---------------------------------------------------------------- checking one line (grammar only) */
  function tokens(text) {
    var out = [], i = 0, m;
    var re = /\s*(?:(\d+)|([A-Za-z_][A-Za-z0-9_]*)|([-+*\/]))/y;
    text = String(text);
    while (i < text.length) {
      if (/^\s*$/.test(text.slice(i))) break;
      re.lastIndex = i;
      m = re.exec(text);
      if (!m) return { error: 'unknown symbol "' + text.slice(i).trim()[0] + '"' };
      i = re.lastIndex;
      if (m[1] !== undefined) out.push({ t: 'num', v: m[1] });
      else if (m[2] !== undefined) out.push({ t: 'name', v: m[2] });
      else out.push({ t: 'op', v: m[3] });
    }
    return { tokens: out };
  }

  function checkExpr(text) {
    var r = tokens(text);
    if (r.error) return r.error;
    var tk = r.tokens;
    if (!tk.length) return 'incomplete expression';
    for (var i = 0; i < tk.length; i++) {
      var wantOperand = (i % 2 === 0);
      if (wantOperand && tk[i].t === 'op') return 'incomplete expression';
      if (!wantOperand && tk[i].t !== 'op') return 'missing operator';
    }
    if (tk[tk.length - 1].t === 'op') return 'incomplete expression';
    return null;
  }

  /* returns null for a blank line, {kind, name, expr} for a correct line, or {error} */
  function parse(line) {
    var s = String(line).trim();
    if (s === '') return null;
    var m = /^PRINT(\s+(.*))?$/.exec(s);
    if (m) {
      var e = checkExpr(m[2] || '');
      return e ? { error: e } : { kind: 'print', expr: m[2] };
    }
    m = /^([^=]*)=(.*)$/.exec(s);
    if (m && m[2].indexOf('=') < 0) {
      var name = m[1].trim();
      if (!NAME.test(name) || name === 'PRINT') return { error: 'bad name "' + name + '"' };
      var e2 = checkExpr(m[2]);
      return e2 ? { error: e2 } : { kind: 'set', name: name, expr: m[2] };
    }
    return { error: 'unknown command' };
  }

  /* ---------------------------------------------------------------- running (whole numbers, exact) */
  function floordiv(a, b) {
    var q = a / b;
    if ((a % b !== 0n) && ((a < 0n) !== (b < 0n))) q -= 1n;
    return q;
  }
  function evaluate(text, vars) {
    var tk = tokens(text).tokens;
    var vals = [], ops = [];
    for (var i = 0; i < tk.length; i++) {
      var x = tk[i];
      if (x.t === 'num') vals.push(BigInt(x.v));
      else if (x.t === 'name') {
        if (!Object.prototype.hasOwnProperty.call(vars, x.v)) throw new Error("name '" + x.v + "' has no value yet");
        vals.push(vars[x.v]);
      } else ops.push(x.v);
    }
    // * and / first, left to right
    var v2 = [vals[0]], o2 = [];
    for (var j = 0; j < ops.length; j++) {
      var b = vals[j + 1];
      if (ops[j] === '*') v2[v2.length - 1] = v2[v2.length - 1] * b;
      else if (ops[j] === '/') {
        if (b === 0n) throw new Error('division by 0');
        v2[v2.length - 1] = floordiv(v2[v2.length - 1], b);
      } else { o2.push(ops[j]); v2.push(b); }
    }
    var r = v2[0];
    for (var k = 0; k < o2.length; k++) r = o2[k] === '+' ? r + v2[k + 1] : r - v2[k + 1];
    return r;
  }

  /* ---------------------------------------------------------------- the two translators */
  function compile(lines) {
    var errors = [];
    lines.forEach(function (ln, i) {
      var p = parse(ln);
      if (p && p.error) errors.push({ line: i + 1, error: p.error });
    });
    return errors;      // empty: the object file can be made
  }

  function runAll(lines) {
    /* run a program that has passed compile(): returns {out, error, line} */
    var vars = {}, out = [];
    for (var i = 0; i < lines.length; i++) {
      var p = parse(lines[i]);
      if (!p) continue;
      try {
        var v = evaluate(p.expr, vars);
        if (p.kind === 'set') vars[p.name] = v; else out.push(String(v));
      } catch (e) { return { out: out, error: e.message, line: i + 1 }; }
    }
    return { out: out, error: null, line: null };
  }

  function Interpreter(lines) { this.lines = lines; this.i = 0; this.vars = {}; this.out = []; this.done = false;
                                this.error = null; this.line = null; this.log = []; }
  Interpreter.prototype.step = function () {
    while (!this.done) {
      if (this.i >= this.lines.length) { this.done = true; this.log.push({ line: null, text: 'no line left: stop' }); return; }
      var n = this.i + 1, p = parse(this.lines[this.i]);
      this.i++;
      if (!p) continue;                         // a blank line: go on to the next
      if (p.error) { this.done = true; this.error = p.error; this.line = n; this.log.push({ line: n, text: 'error: ' + p.error }); return; }
      try {
        var v = evaluate(p.expr, this.vars);
        if (p.kind === 'set') { this.vars[p.name] = v; this.log.push({ line: n, text: p.name + ' = ' + v }); }
        else { this.out.push(String(v)); this.log.push({ line: n, text: 'shows ' + v }); }
      } catch (e) { this.done = true; this.error = e.message; this.line = n; this.log.push({ line: n, text: 'error: ' + e.message }); }
      return;
    }
  };
  Interpreter.prototype.runAll = function () { while (!this.done) this.step(); return this; };

  /* ---------------------------------------------------------------- the page */
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function page(examples, ids) {
    var $ = function (id) { return document.getElementById(id); };
    var sel = $(ids.select), box = $(ids.code), out = $(ids.output), msg = $(ids.message), listing = $(ids.listing);
    var it = null;
    function lines() { return box.value.split('\n'); }
    function show(marked, kinds) {
      listing.innerHTML = lines().map(function (ln, i) {
        var k = kinds[i + 1] || '';
        var bg = k === 'err' ? 'rgba(200,0,0,.15)' : k === 'run' ? 'rgba(197,90,17,.18)' : k === 'next' ? 'rgba(197,90,17,.06)' : '';
        return '<div style="font-family:monospace;padding:1px 6px;' + (bg ? 'background:' + bg : '') + '"><b>' + (i + 1) +
          '</b>&nbsp; ' + esc(ln || ' ') + (marked[i + 1] ? ' <span style="color:#C55A11">← ' + esc(marked[i + 1]) + '</span>' : '') + '</div>';
      }).join('');
    }
    function choose() { box.value = examples[sel.value].code.join('\n'); it = null; reset(); msg.innerHTML = esc(examples[sel.value].hint); }
    function reset() { out.innerHTML = '<i>nothing shown yet</i>'; show({}, {}); }
    $(ids.compile).onclick = function () {
      it = null;
      var errs = compile(lines()), marked = {}, kinds = {};
      if (errs.length) {
        errs.forEach(function (e) { marked[e.line] = e.error; kinds[e.line] = 'err'; });
        show(marked, kinds);
        out.innerHTML = '<i>nothing runs</i>';
        msg.innerHTML = '<b>Compiler:</b> read all ' + lines().length + ' lines and found <b>' + errs.length + ' error' +
          (errs.length > 1 ? 's' : '') + '</b> (lines ' + errs.map(function (e) { return e.line; }).join(', ') +
          '). No object file is made; nothing runs. Fix them all, then compile again.';
        return;
      }
      var r = runAll(lines());
      if (r.error) { marked[r.line] = r.error; kinds[r.line] = 'err'; }
      show(marked, kinds);
      out.innerHTML = r.out.length ? r.out.map(esc).join('<br>') : '<i>nothing shown</i>';
      msg.innerHTML = '<b>Compiler:</b> no grammar errors, so the <b>object file is made</b> and runs without the compiler. ' +
        (r.error ? 'While running, line ' + r.line + ' stops it: <b>' + esc(r.error) + '</b> (no translator can find this before running).' :
          'It ran to the end, and can run again and again.');
    };
    $(ids.step).onclick = function () {
      if (!it || it.done) it = new Interpreter(lines());
      it.step();
      var marked = {}, kinds = {};
      it.log.forEach(function (l) { if (l.line) { marked[l.line] = l.text; kinds[l.line] = 'run'; } });
      if (it.error) kinds[it.line] = 'err';
      else if (!it.done && it.i < it.lines.length) kinds[it.i + 1] = 'next';
      show(marked, kinds);
      out.innerHTML = it.out.length ? it.out.map(esc).join('<br>') : '<i>nothing shown yet</i>';
      msg.innerHTML = it.error ? '<b>Interpreter:</b> stopped at line ' + it.line + ': <b>' + esc(it.error) + '</b>. The lines before it have already run; the lines after it are never read.'
        : it.done ? '<b>Interpreter:</b> every line ran, one at a time. Run it again and it translates everything again.'
          : '<b>Interpreter:</b> translated and ran line ' + it.log[it.log.length - 1].line + ' at once. Press again for the next line.';
    };
    $(ids.reset).onclick = function () { it = null; reset(); msg.innerHTML = ''; };
    sel.onchange = choose;
    choose();
  }

  var api = { parse: parse, compile: compile, runAll: runAll, Interpreter: Interpreter, page: page };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.Ch02 = api;
})(typeof window !== 'undefined' ? window : globalThis);
