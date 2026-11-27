/* Chapter 5: the dry-run player (27 Nov 2026).
   Runs the flowcharts of worked examples W1-W10 box by box, exactly as 50-tools/algo_lib.py runs them for the printed
   book: the same steps, the same values (whole numbers exact, as in Python; floats printed as Python prints them),
   and the same "What happens" text. The work in each box is read by a small expression reader (no eval of typed text).
   Tested against algo_lib by tools/ch05_js_test.py (node), for hundreds of inputs.
   Used by: see-it-dry-run-player. */
(function (root) {
  'use strict';

  /* ---------------------------------------------------------------- values as Python has them */
  function isInt(v) { return typeof v === 'bigint'; }
  function isNum(v) { return typeof v === 'bigint' || typeof v === 'number'; }
  function fmt(v) {
    if (typeof v === 'bigint') return v.toString();
    if (typeof v === 'boolean') return v ? 'True' : 'False';
    if (typeof v === 'number') {
      if (!isFinite(v)) return isNaN(v) ? 'nan' : (v > 0 ? 'inf' : '-inf');
      var a = Math.abs(v);
      if (a !== 0 && (a >= 1e16 || a < 1e-4)) {
        return v.toExponential().replace(/e([+-])(\d)$/, 'e$10$2');
      }
      if (Number.isInteger(v)) return v.toFixed(1);
      return String(v);
    }
    return String(v);
  }
  function truthy(v) {
    if (typeof v === 'bigint') return v !== 0n;
    if (typeof v === 'string') return v.length > 0;
    return !!v;
  }
  function both(a, b) {                 /* numbers of one kind: both BigInt, or both float */
    if (isInt(a) && isInt(b)) return [a, b, true];
    if (typeof a === 'boolean') a = a ? 1n : 0n;
    if (typeof b === 'boolean') b = b ? 1n : 0n;
    return [Number(a), Number(b), false];
  }
  function err(msg) { var e = new Error(msg); e.py = true; return e; }
  function arith(op, a, b) {
    if (op === '+' && typeof a === 'string' && typeof b === 'string') return a + b;
    if (!isNum(a) || !isNum(b)) throw err('TypeError: cannot use ' + op + ' here');
    var p = both(a, b), x = p[0], y = p[1], ints = p[2];
    switch (op) {
      case '+': return x + y;
      case '-': return x - y;
      case '*': return x * y;
      case '/':
        if (Number(y) === 0) throw err('ZeroDivisionError: division by zero');
        return Number(x) / Number(y);
      case '//':
        if (ints) {
          if (y === 0n) throw err('ZeroDivisionError: division by zero');
          var q = x / y;
          if ((x % y !== 0n) && ((x < 0n) !== (y < 0n))) q -= 1n;
          return q;
        }
        if (y === 0) throw err('ZeroDivisionError: division by zero');
        return Math.floor(x / y);
      case '%':
        if (ints) {
          if (y === 0n) throw err('ZeroDivisionError: division by zero');
          var r = x % y;
          if (r !== 0n && ((r < 0n) !== (y < 0n))) r += y;
          return r;
        }
        if (y === 0) throw err('ZeroDivisionError: division by zero');
        var m = x % y;
        if (m !== 0 && ((m < 0) !== (y < 0))) m += y;
        return m;
    }
    throw err('unknown operator ' + op);
  }
  function compare(op, a, b) {
    var x = a, y = b;
    if (isNum(a) && isNum(b)) { var p = both(a, b); x = p[0]; y = p[1]; }
    switch (op) {
      case '==': return x === y || (isNum(a) && isNum(b) && Number(x) === Number(y));
      case '!=': return !(x === y || (isNum(a) && isNum(b) && Number(x) === Number(y)));
      case '<': return x < y;
      case '<=': return x <= y;
      case '>': return x > y;
      case '>=': return x >= y;
    }
  }

  /* ---------------------------------------------------------------- the expression reader */
  function tokens(s) {
    var out = [], i = 0, m;
    var re = /\s*(?:(\d+\.\d*|\.\d+)|(\d+)|('[^']*'|"[^"]*")|([A-Za-z_]\w*)|(\/\/|==|!=|<=|>=|[-+*\/%<>(),]))/y;
    while (i < s.length) {
      re.lastIndex = i;
      m = re.exec(s);
      if (!m) { if (/^\s*$/.test(s.slice(i))) break; throw err('cannot read: ' + s.slice(i)); }
      i = re.lastIndex;
      if (m[1] !== undefined) out.push({ t: 'num', v: parseFloat(m[1]) });
      else if (m[2] !== undefined) out.push({ t: 'num', v: BigInt(m[2]) });
      else if (m[3] !== undefined) out.push({ t: 'str', v: m[3].slice(1, -1) });
      else if (m[4] !== undefined) out.push({ t: 'name', v: m[4] });
      else out.push({ t: 'op', v: m[5] });
    }
    return out;
  }
  var FUN = {
    min: function (args) { return args.reduce(function (a, b) { return compare('<', b, a) ? b : a; }); },
    max: function (args) { return args.reduce(function (a, b) { return compare('>', b, a) ? b : a; }); },
    abs: function (args) { var v = args[0]; return isInt(v) ? (v < 0n ? -v : v) : Math.abs(v); },
    str: function (args) { return fmt(args[0]); }
  };
  function evaluate(src, env) {
    var tk = tokens(src), pos = 0;
    function peek() { return tk[pos]; }
    function take(v) { var t = tk[pos]; if (!t || (v && t.v !== v)) throw err('cannot read: ' + src); pos++; return t; }
    function isOp(v) { var t = peek(); return t && t.t !== 'str' && t.v === v; }
    function orE() { var a = andE(); while (isOp('or')) { take(); var b = andE(); a = truthy(a) ? a : b; } return a; }
    function andE() { var a = notE(); while (isOp('and')) { take(); var b = notE(); a = truthy(a) ? b : a; } return a; }
    function notE() { if (isOp('not')) { take(); return !truthy(notE()); } return cmpE(); }
    function cmpE() {
      var a = addE(), result = null;
      while (peek() && peek().t === 'op' && ['==', '!=', '<', '<=', '>', '>='].indexOf(peek().v) >= 0) {
        var op = take().v, b = addE();
        var r = compare(op, a, b);
        result = result === null ? r : (result && r);
        a = b;
      }
      return result === null ? a : result;
    }
    function addE() {
      var a = mulE();
      while (peek() && peek().t === 'op' && (peek().v === '+' || peek().v === '-')) { var op = take().v; a = arith(op, a, mulE()); }
      return a;
    }
    function mulE() {
      var a = unE();
      while (peek() && peek().t === 'op' && ['*', '/', '//', '%'].indexOf(peek().v) >= 0) { var op = take().v; a = arith(op, a, unE()); }
      return a;
    }
    function unE() {
      if (isOp('-')) { take(); var v = unE(); return isInt(v) ? -v : -v; }
      if (isOp('+')) { take(); return unE(); }
      return atom();
    }
    function atom() {
      var t = take();
      if (t.t === 'num' || t.t === 'str') return t.v;
      if (t.t === 'op' && t.v === '(') { var v = orE(); take(')'); return v; }
      if (t.t === 'name') {
        if (t.v === 'True') return true;
        if (t.v === 'False') return false;
        if (isOp('(')) {
          take('(');
          var args = [];
          if (!isOp(')')) { args.push(orE()); while (isOp(',')) { take(); args.push(orE()); } }
          take(')');
          if (!FUN[t.v]) throw err('unknown function ' + t.v);
          return FUN[t.v](args);
        }
        if (!env.has(t.v)) throw err("NameError: name '" + t.v + "' is not defined");
        return env.get(t.v);
      }
      throw err('cannot read: ' + src);
    }
    var v = orE();
    if (pos !== tk.length) throw err('cannot read: ' + src);
    return v;
  }
  function execute(code, env) {
    code.split(/\n|;/).forEach(function (line) {
      line = line.trim();
      if (!line) return;
      var m = /^([A-Za-z_]\w*)\s*=(?!=)\s*(.+)$/.exec(line);
      if (!m) throw err('cannot read: ' + line);
      env.set(m[1], evaluate(m[2], env));
    });
  }

  /* ---------------------------------------------------------------- inputs typed by the reader */
  function readInputs(text) {
    var parts = String(text).split(',').map(function (s) { return s.trim(); }).filter(function (s) { return s !== ''; });
    var vals = [];
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      if (/^[-+]?\d+$/.test(p)) vals.push(BigInt(p));
      else if (/^[-+]?(\d+\.\d*|\.\d+)$/.test(p)) vals.push(parseFloat(p));
      else return { error: '"' + p + '" is not a number. Type numbers separated by commas, for example 7, 12.' };
    }
    return { values: vals };
  }

  /* ---------------------------------------------------------------- the machine: one box at a time */
  function Machine(algo, inputs) {
    this.a = algo; this.stream = inputs.slice(); this.env = new Map(); this.out = []; this.rows = [];
    this.n = 1; this.done = false; this.error = null; this.count = 0;
  }
  Machine.prototype.node = function (n) { return this.a.nodes[String(n)]; };
  Machine.prototype.explain = function (x, before, after, result) {
    function sub(s) {
      return s.replace(/\b([A-Za-z_]\w*)\b/g, function (w) { return before.has(w) ? fmt(before.get(w)) : w; });
    }
    if (x.kind === 'start') return 'begin';
    if (x.kind === 'stop') return 'end';
    if (x.kind === 'decision') return sub(x.text.replace(/\n/g, ' ').replace(/\?+$/, '')) + '? ' + result;
    if (x.kind === 'process' && x.text.indexOf('\n') < 0 && x.text.split('=').length === 2 && x.text.indexOf(',') < 0) {
      var parts = x.text.split('=').map(function (s) { return s.trim(); });
      var v = parts[0], shown = sub(parts[1]);
      var nv = after.has(v) ? after.get(v) : undefined;
      if (nv === undefined) after.forEach(function (val, k) { if (nv === undefined && k.toLowerCase() === v.toLowerCase()) nv = val; });
      return shown.trim() === fmt(nv) ? v + ' = ' + fmt(nv) : shown + ' = ' + fmt(nv);
    }
    return result;
  };
  Machine.prototype.step = function () {
    if (this.done) return null;
    if (++this.count > 2000) { this.done = true; this.error = 'More than 2,000 steps: the loop does not end with these inputs.'; return null; }
    var x = this.node(this.n), env = this.env, before = new Map(env), result = '', next = x.next;
    try {
      if (x.kind === 'stop') { this.done = true; }
      else if (x.kind === 'input') {
        var got = [];
        for (var i = 0; i < x.reads.length; i++) {
          if (!this.stream.length) throw err('Box ' + x.num + ' asks for ' + x.reads[i] + ', but no input is left. Type more values.');
          env.set(x.reads[i], this.stream.shift());
          got.push(x.reads[i] + ' = ' + fmt(env.get(x.reads[i])));
        }
        result = got.join(', ');
      } else if (x.kind === 'process') {
        execute(x.do, env);
        var ch = [];
        env.forEach(function (v, k) { if (!before.has(k) || before.get(k) !== v) ch.push(k + ' = ' + fmt(v)); });
        result = ch.join(', ');
      } else if (x.kind === 'output') {
        var val = fmt(evaluate(x.show, env));
        this.out.push(val);
        result = 'prints ' + val;
      } else if (x.kind === 'decision') {
        var yes = truthy(evaluate(x.test, env));
        result = yes ? 'Yes' : 'No';
        next = yes ? x.yes : x.no;
      }
    } catch (e) {
      this.done = true; this.error = (e && e.py) ? e.message : String(e);
      return null;
    }
    var row = { step: x.num, code: x.kind === 'start' ? 'START' : x.kind === 'stop' ? 'STOP' : (this.a.code[String(x.num)] || x.text),
                what: this.explain(x, before, env, result), result: result };
    this.rows.push(row);
    if (!this.done) this.n = next;
    return row;
  };
  Machine.prototype.runAll = function () { while (!this.done) this.step(); return this; };

  /* ---------------------------------------------------------------- the page */
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function player(data, ids) {
    var sel = document.getElementById(ids.select), box = document.getElementById(ids.inputs);
    var pic = document.getElementById(ids.picture), msg = document.getElementById(ids.message);
    var table = document.getElementById(ids.table), vars = document.getElementById(ids.vars), out = document.getElementById(ids.output);
    var m = null;
    function algo() { return data[sel.value]; }
    function draw() {
      var a = algo(), html = '<img src="' + a.img + '" alt="Flowchart of ' + esc(a.title) + '" style="width:100%;display:block">';
      var cur = m && !m.done ? m.n : (m && m.rows.length ? m.rows[m.rows.length - 1].step : null);
      var seen = {};
      if (m) m.rows.forEach(function (r) { seen[r.step] = true; });
      Object.keys(a.nodes).forEach(function (k) {
        var x = a.nodes[k], b = a.box[k];
        var style = 'position:absolute;left:' + b[0] + '%;top:' + b[1] + '%;width:' + b[2] + '%;height:' + b[3] + '%;border-radius:6px;pointer-events:none;';
        if (String(cur) === k) html += '<div style="' + style + 'border:4px solid #C55A11;box-shadow:0 0 0 4px rgba(197,90,17,.25)"></div>';
        else if (seen[k]) html += '<div style="' + style + 'background:rgba(197,90,17,.13)"></div>';
      });
      pic.innerHTML = '<div style="position:relative">' + html + '</div>';
      var rows = m ? m.rows : [];
      table.innerHTML = '<table><thead><tr><th>No.</th><th>Pseudocode</th><th>What happens</th></tr></thead><tbody>' +
        rows.map(function (r, i) {
          return '<tr' + (i === rows.length - 1 ? ' style="background:rgba(197,90,17,.15)"' : '') + '><td>' + r.step +
            '</td><td><code>' + esc(r.code) + '</code></td><td>' + esc(r.what) + '</td></tr>';
        }).join('') + '</tbody></table>';
      var v = [];
      if (m) m.env.forEach(function (val, k) { v.push('<b>' + esc(k) + '</b> = ' + esc(fmt(val))); });
      vars.innerHTML = v.length ? v.join(' &nbsp;·&nbsp; ') : '<i>no variables yet</i>';
      out.innerHTML = m && m.out.length ? m.out.map(esc).join('<br>') : '<i>nothing printed yet</i>';
      if (m && m.error) msg.innerHTML = '<b>Stopped:</b> ' + esc(m.error);
      else if (m && m.done) msg.innerHTML = '<b>Stop reached</b> after ' + m.rows.length + ' steps.';
      else if (m) msg.innerHTML = 'Next box: <b>' + m.n + '</b>. Press <b>Next step</b>.';
    }
    function start() {
      var r = readInputs(box.value);
      if (r.error) { m = null; draw(); msg.innerHTML = esc(r.error); return false; }
      m = new Machine(algo(), r.values); return true;
    }
    function choose() { box.value = algo().example; m = null; draw(); msg.innerHTML = esc(algo().hint); }
    sel.onchange = choose;
    document.getElementById(ids.next).onclick = function () { if (!m || m.done) { if (!start()) return; } m.step(); draw(); };
    document.getElementById(ids.all).onclick = function () { if (!m || m.done) { if (!start()) return; } m.runAll(); draw(); };
    document.getElementById(ids.reset).onclick = function () { if (start()) draw(); };
    choose();
  }

  var api = { fmt: fmt, evaluate: evaluate, execute: execute, readInputs: readInputs, Machine: Machine, player: player };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.Ch05 = api;
})(typeof window !== 'undefined' ? window : globalThis);
