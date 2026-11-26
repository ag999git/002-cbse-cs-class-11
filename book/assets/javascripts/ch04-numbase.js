/* Chapter 4 interactive pages: number-system logic (26 Nov 2026).
   Exact arithmetic with BigInt fractions, the same methods as the printed book and as tools/numbase_lib.py:
   division ladder (Road 1), place values (Road 2), grouping (Roads 3-4), through binary (Road 5), multiplication
   ladder for fractions (Road 6). Tested against numbase_lib.py by tools/ch04_js_test.py (node).
   Used by: see-it-converter, see-it-trays-and-meter, see-it-letters-to-bytes. */
(function (root) {
  'use strict';
  var DIG = '0123456789ABCDEF';
  var SUBS = '₀₁₂₃₄₅₆₇₈₉';

  function sub(n) { return String(n).split('').map(function (c) { return SUBS[+c]; }).join(''); }
  function num(s, b) { return '(' + s + ')' + sub(b); }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function gcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { var t = a % b; a = b; b = t; } return a; }
  function frac(n, d) { var g = gcd(n, d) || 1n; return { n: n / g, d: d / g }; }
  function fracStr(f) { return f.d === 1n ? String(f.n) : f.n + '/' + f.d; }

  /* check and read a numeral: returns {whole: '1011', frac: '01'} or an error message */
  function parse(text, b) {
    var t = String(text).trim().toUpperCase().replace(/\s+/g, '');
    if (!t) return { error: 'Type a number first.' };
    if (!/^[0-9A-F]*(\.[0-9A-F]*)?$/.test(t) || t === '.') return { error: 'Use only digits, the letters A–F and one point.' };
    var parts = t.split('.');
    var all = parts.join('');
    for (var i = 0; i < all.length; i++) {
      if (DIG.indexOf(all[i]) >= b) {
        return { error: '"' + all[i] + '" is not a digit of base ' + b + ': base ' + b + ' has the digits 0 to ' + DIG[b - 1] + '.' };
      }
    }
    var whole = parts[0].replace(/^0+(?=.)/, '') || '0';
    return { whole: whole, frac: parts.length > 1 ? parts[1] : '' };
  }

  function value(p, b) {               /* exact value of a parsed numeral, as a fraction */
    var B = BigInt(b), n = 0n, d = 1n, i;
    for (i = 0; i < p.whole.length; i++) n = n * B + BigInt(DIG.indexOf(p.whole[i]));
    var fn = 0n;
    for (i = 0; i < p.frac.length; i++) { fn = fn * B + BigInt(DIG.indexOf(p.frac[i])); d *= B; }
    return frac(n * d + fn, d);
  }

  function toBaseWhole(n, b) {
    if (n === 0n) return '0';
    var B = BigInt(b), s = '';
    while (n > 0n) { s = DIG[Number(n % B)] + s; n /= B; }
    return s;
  }

  function divLadder(n, b) {           /* rows [dividend, quotient, remainder] */
    var B = BigInt(b), rows = [];
    while (n > 0n) { rows.push([n, n / B, Number(n % B)]); n /= B; }
    return rows;
  }

  function mulLadder(f, b, places) {   /* f = {n, d} with n < d; rows [fraction, product, digit]; why: zero | repeats | limit */
    var B = BigInt(b), rows = [], seen = {}, why = 'limit', digits = '', cycleFrom = -1;
    while (digits.length < places) {
      if (f.n === 0n) { why = 'zero'; break; }
      var key = f.n + '/' + f.d;
      if (key in seen && cycleFrom < 0) { cycleFrom = seen[key]; why = 'repeats'; }
      if (!(key in seen)) seen[key] = rows.length;
      var p = f.n * B;
      var dgt = Number(p / f.d);
      var nf = frac(p - BigInt(dgt) * f.d, f.d);
      rows.push([f, frac(p, f.d), dgt]);
      digits += DIG[dgt];
      f = nf;
    }
    if (why === 'limit' && f.n === 0n) why = 'zero';
    return { rows: rows, digits: digits, why: why, cycleFrom: cycleFrom };
  }

  function decimalOf(f) {              /* fraction with denominator 2^a 5^b -> exact decimal text; otherwise 12 places */
    var w = f.n / f.d, r = frac(f.n - w * f.d, f.d);
    if (r.n === 0n) return String(w);
    var m = mulLadder(r, 10, 40);
    return String(w) + '.' + (m.why === 'zero' ? m.digits : m.digits.slice(0, 12) + '…');
  }

  function bitsOf(p, b) {              /* octal or hex numeral -> binary, digit by digit */
    var k = b === 8 ? 3 : 4, wb = '', fb = '', pairs = [];
    p.whole.split('').forEach(function (c) { var s = DIG.indexOf(c).toString(2).padStart(k, '0'); pairs.push([c, s]); wb += s; });
    var fp = [];
    p.frac.split('').forEach(function (c) { var s = DIG.indexOf(c).toString(2).padStart(k, '0'); fp.push([c, s]); fb += s; });
    return { whole: wb.replace(/^0+(?=.)/, '') || '0', frac: fb.replace(/0+$/, ''), pairs: pairs, fpairs: fp };
  }

  function group(p, b) {               /* binary -> octal or hex by grouping away from the point */
    var k = b === 8 ? 3 : 4;
    var w = p.whole, f = p.frac;
    var wpad = (k - w.length % k) % k, fpad = (k - f.length % k) % k;
    var W = '0'.repeat(wpad) + w, F = f + '0'.repeat(fpad);
    var wg = [], fg = [], i;
    for (i = 0; i < W.length; i += k) wg.push(W.slice(i, i + k));
    for (i = 0; i < F.length; i += k) fg.push(F.slice(i, i + k));
    var wd = wg.map(function (g) { return DIG[parseInt(g, 2)]; }).join('').replace(/^0+(?=.)/, '') || '0';
    var fd = fg.map(function (g) { return DIG[parseInt(g, 2)]; }).join('').replace(/0+$/, '');
    return { wg: wg, fg: fg, wpad: wpad, fpad: fpad, whole: wd, frac: fd };
  }

  function join(whole, f) { return f ? whole + '.' + f : whole; }

  /* the whole converter: returns {ok, error, answer, exact, html} */
  function convert(text, from, to, places) {
    places = places || 8;
    var p = parse(text, from);
    if (p.error) return { ok: false, error: p.error };
    var v = value(p, from), h = [], answer, exact = true;
    var shown = num(join(p.whole, p.frac), from);
    if (from === to) {
      return { ok: true, answer: join(p.whole, p.frac), exact: true, html: '<p>Both bases are the same: nothing to convert.</p>' };
    }
    if (from === 10) {
      var w = v.n / v.d, r = frac(v.n - w * v.d, v.d);
      h.push('<p><b>Road 1: divide.</b> Whole part ' + w + ': divide by ' + to + ' again and again; read the remainders <b>upward</b>.</p>');
      var rows = divLadder(w, to);
      if (rows.length) {
        h.push('<table class="c4"><tr><th>Divide</th><th>Quotient</th><th>Remainder</th></tr>');
        rows.forEach(function (x) {
          h.push('<tr><td>' + x[0] + ' ÷ ' + to + '</td><td>' + x[1] + '</td><td><b>' + DIG[x[2]] + '</b>' + (x[2] > 9 ? ' (' + x[2] + ')' : '') + '</td></tr>');
        });
        h.push('</table>');
      } else h.push('<p>The whole part is 0.</p>');
      var wd = toBaseWhole(w, to);
      h.push('<p>Read upward: whole part = <b>' + wd + '</b></p>');
      var fd = '';
      if (r.n !== 0n) {
        h.push('<p><b>Fraction ' + decimalOf(r) + ': multiply</b> by ' + to + ' again and again; the whole part of each answer is the next digit; read <b>downward</b>.</p>');
        var m = mulLadder(r, to, places);
        h.push('<table class="c4"><tr><th>Fraction × ' + to + '</th><th>Digit</th></tr>');
        m.rows.forEach(function (x) { h.push('<tr><td>' + decimalOf(x[0]) + ' × ' + to + ' = ' + decimalOf(x[1]) + '</td><td><b>' + DIG[x[2]] + '</b></td></tr>'); });
        h.push('</table>');
        fd = m.digits;
        if (m.why === 'zero') h.push('<p>The fraction is now 0: the answer is exact.</p>');
        else {
          exact = false;
          h.push('<p>' + (m.why === 'repeats' ? 'A fraction came back: the digits repeat for ever. ' : 'It has not ended. ') +
                 'Shown to ' + places + ' places.</p>');
        }
      }
      answer = join(wd, fd);
    } else if (to === 10) {
      h.push('<p><b>Road 2: place values.</b> Multiply each digit by ' + from + ' to the power of its position, then add.</p>');
      h.push('<table class="c4"><tr><th>Digit</th><th>Position</th><th>Place value</th><th>Digit × place value</th></tr>');
      var digs = (p.whole + p.frac).split(''), L = p.whole.length;
      digs.forEach(function (c, i) {
        var pos = L - 1 - i, dv = DIG.indexOf(c);
        var pv = pos >= 0 ? frac(BigInt(from) ** BigInt(pos), 1n) : frac(1n, BigInt(from) ** BigInt(-pos));
        var prod = frac(pv.n * BigInt(dv), pv.d);
        h.push('<tr><td>' + c + (dv > 9 ? ' (' + dv + ')' : '') + '</td><td>' + pos + '</td><td>' + fracStr(pv) +
               '</td><td>' + decimalOf(prod) + '</td></tr>');
      });
      h.push('</table>');
      answer = decimalOf(v);
      if (answer.indexOf('…') >= 0) exact = false;
      h.push('<p>Add the last column: <b>' + answer + '</b></p>');
    } else if (from === 2) {
      var g = group(p, to), k = to === 8 ? 3 : 4;
      h.push('<p><b>Roads 3 and 4: group the bits</b> in ' + k + 's, starting at the point: leftward for the whole part, rightward for the fraction. ' +
             'Extra 0s go only at the far ends' + (g.wpad || g.fpad ? ' (shown in orange)' : '') + '.</p>');
      function show(grps, padL, padR) {
        return grps.map(function (s, i) {
          if (i === 0 && padL) s = '<span class="c4pad">' + s.slice(0, padL) + '</span>' + s.slice(padL);
          if (i === grps.length - 1 && padR) s = s.slice(0, s.length - padR) + '<span class="c4pad">' + s.slice(s.length - padR) + '</span>';
          return '<span class="c4grp">' + s + '<br><b>' + DIG[parseInt(s.replace(/<[^>]+>/g, ''), 2)] + '</b></span>';
        }).join(' ');
      }
      h.push('<p class="c4mono">' + show(g.wg, g.wpad, 0) + (g.fg.length ? ' <b>.</b> ' + show(g.fg, 0, g.fpad) : '') + '</p>');
      answer = join(g.whole, g.frac);
    } else if (to === 2) {
      var bt = bitsOf(p, from);
      h.push('<p><b>Each ' + (from === 8 ? 'octal' : 'hex') + ' digit becomes its own ' + (from === 8 ? 3 : 4) + ' bits.</b></p>');
      h.push('<p class="c4mono">' + bt.pairs.concat(bt.fpairs.length ? [['.', '.']] : []).concat(bt.fpairs).map(function (x) {
        return x[0] === '.' ? '<b>.</b>' : '<span class="c4grp"><b>' + x[0] + '</b><br>' + x[1] + '</span>';
      }).join(' ') + '</p>');
      h.push('<p>Leading 0s of the whole part and trailing 0s of the fraction can be dropped.</p>');
      answer = join(bt.whole, bt.frac);
    } else {
      var bt2 = bitsOf(p, from);
      var g2 = group({ whole: bt2.whole, frac: bt2.frac }, to);
      h.push('<p><b>Road 5: through binary.</b> First each digit to its ' + (from === 8 ? 3 : 4) + ' bits: ' +
             esc(bt2.pairs.map(function (x) { return x[0] + ' → ' + x[1]; }).join(', ')) +
             (bt2.fpairs.length ? ' . ' + esc(bt2.fpairs.map(function (x) { return x[0] + ' → ' + x[1]; }).join(', ')) : '') + '.</p>');
      h.push('<p>Binary: <span class="c4mono">' + join(bt2.whole, bt2.frac) + '</span>. Now regroup in ' + (to === 8 ? 3 : 4) + 's from the point: ' +
             '<span class="c4mono">' + g2.wg.join(' ') + (g2.fg.length ? ' . ' + g2.fg.join(' ') : '') + '</span>.</p>');
      answer = join(g2.whole, g2.frac);
    }
    h.push('<p class="c4ans">' + shown + ' ' + (exact ? '=' : '≈') + ' <b>' + num(answer + (exact ? '' : '…'), to) + '</b></p>');
    var back = value(parse(answer, to), to);
    var same = back.n === v.n && back.d === v.d;
    return { ok: true, answer: answer, exact: exact, same: same, html: h.join('\n'),
             backHtml: '<p><b>Check by the return road:</b> ' + num(answer, to) + ' back to decimal = ' + decimalOf(back) +
                       (same ? '. Same number ✓' : '; the number you typed is ' + decimalOf(v) + ' (the difference is only the digits cut off after ' + places + ' places).') + '</p>' };
  }

  var api = { DIG: DIG, parse: parse, value: value, toBaseWhole: toBaseWhole, divLadder: divLadder, mulLadder: mulLadder,
              decimalOf: decimalOf, bitsOf: bitsOf, group: group, convert: convert, num: num, esc: esc };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Ch04 = api;
})(this);
