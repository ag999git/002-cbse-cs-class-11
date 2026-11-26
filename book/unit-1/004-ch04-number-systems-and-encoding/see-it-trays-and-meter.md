# See it: cake trays and the meter

*Chapter 4 · Helps you understand. Two pictures of the printed book that you can play with: the cake trays (section 4.2 and 4.4) and the auto-rickshaw meter (section 4.2).*

## 1. The cake trays

Click a tray to fill it or empty it. Each tray holds twice as many cakes as the tray to its right; after the point the plates hold ½, ¼ and ⅛ of a cake. A full tray is 1, an empty tray is 0.

<div class="c4box" markdown="0">
<div class="c4trays" id="c4trays"></div>
<p class="c4ans" id="c4tv"></p>
<p><button id="c4clear" class="c4light">Empty all</button> <button id="c4rand" class="c4light">A surprise number</button>
<label>or type a decimal number (0 to 255.875) <input id="c4tn" size="8"></label> <button id="c4tset">Fill the trays</button></p>
<p class="c4err" id="c4terr"></p>
</div>

## 2. The meter

Press **+1** and watch the wheels. A wheel that passes its top digit rolls over to 0 and pushes the next wheel: the orange wheels are the ones that changed.

<div class="c4box" markdown="0">
<p><label>Base <select id="c4mb"><option value="2">binary (wheels 0–1)</option><option value="8">octal (wheels 0–7)</option><option value="10" selected>decimal (wheels 0–9)</option><option value="16">hexadecimal (wheels 0–F)</option></select></label>
<button id="c4plus">+1</button> <button id="c4minus" class="c4light">−1</button> <button id="c4zero" class="c4light">Back to 0</button></p>
<p id="c4wheels"></p>
<p class="c4ans" id="c4mv"></p>
</div>

<script>
(function () {
  function $(id) { return document.getElementById(id); }
  /* ---- trays: 128 … 1, then ½ ¼ ⅛ ---- */
  var W = [128, 64, 32, 16, 8, 4, 2, 1], F = ['½', '¼', '⅛'], on = new Array(11).fill(false);
  function cols(n) { return n >= 64 ? 16 : n >= 16 ? 8 : n >= 4 ? 4 : n >= 2 ? 2 : 1; }
  function draw() {
    var h = '';
    W.forEach(function (w, i) {
      var c = cols(w), dots = '';
      for (var k = 0; k < w; k++) dots += '<span class="c4dot"></span>';
      h += '<div class="c4tray' + (on[i] ? ' on' : '') + '" data-i="' + i + '"><b>' + w + '</b><div class="c4dots" style="grid-template-columns:repeat(' + c + ',.45rem)">' + dots + '</div>' + (on[i] ? '1' : '0') + '</div>';
    });
    h += '<div style="font:bold 2rem sans-serif;align-self:center">.</div>';
    F.forEach(function (f, j) {
      var i = 8 + j;
      h += '<div class="c4tray' + (on[i] ? ' on' : '') + '" data-i="' + i + '"><b>' + f + '</b><div style="font-size:1.4rem">' + (on[i] ? '◔' : '○') + '</div>' + (on[i] ? '1' : '0') + '</div>';
    });
    $('c4trays').innerHTML = h;
    Array.prototype.forEach.call(document.querySelectorAll('#c4trays .c4tray'), function (el) {
      el.onclick = function () { var i = +el.getAttribute('data-i'); on[i] = !on[i]; draw(); };
    });
    var whole = 0, eighths = 0;
    W.forEach(function (w, i) { if (on[i]) whole += w; });
    [4, 2, 1].forEach(function (e, j) { if (on[8 + j]) eighths += e; });
    var bits = on.slice(0, 8).map(function (x) { return x ? 1 : 0; }).join('').replace(/^0+(?=.)/, '');
    var fb = on.slice(8).map(function (x) { return x ? 1 : 0; }).join('').replace(/0+$/, '');
    var dec = whole + (eighths ? '.' + String(eighths * 125).padStart(3, '0').replace(/0+$/, '') : '');
    var parts = W.filter(function (w, i) { return on[i]; }).map(String).concat(F.filter(function (f, j) { return on[8 + j]; }));
    $('c4tv').innerHTML = '(' + bits + (fb ? '.' + fb : '') + ')₂ = ' + (parts.length ? parts.join(' + ') : '0') + ' = <b>(' + dec + ')₁₀</b> cakes';
  }
  $('c4clear').onclick = function () { on.fill(false); draw(); };
  $('c4rand').onclick = function () { for (var i = 0; i < 11; i++) on[i] = Math.random() < 0.45; draw(); };
  $('c4tset').onclick = function () {
    $('c4terr').textContent = '';
    var v = parseFloat($('c4tn').value);
    var e8 = Math.round(v * 8);
    if (isNaN(v) || v < 0 || v > 255.875 || Math.abs(e8 - v * 8) > 1e-9) {
      $('c4terr').textContent = 'Type a number from 0 to 255.875 that is a whole number of eighths (for example 22, 2.625 or 100.5).';
      return;
    }
    for (var i = 0; i < 8; i++) on[i] = (Math.floor(e8 / 8) & W[i]) !== 0;
    [4, 2, 1].forEach(function (b, j) { on[8 + j] = (e8 % 8 & b) !== 0; });
    draw();
  };
  draw();
  /* ---- meter ---- */
  var DIG = '0123456789ABCDEF', val = 0, prev = 0;
  function show() {
    var b = +$('c4mb').value, max = Math.pow(b, 4);
    val = ((val % max) + max) % max;
    var s = val.toString(b).toUpperCase().padStart(4, '0'), p = ((prev % max) + max) % max;
    var ps = p.toString(b).toUpperCase().padStart(4, '0');
    $('c4wheels').innerHTML = s.split('').map(function (c, i) { return '<span class="c4wheel' + (c !== ps[i] ? ' changed' : '') + '">' + c + '</span>'; }).join('');
    $('c4mv').innerHTML = '(' + s + ')' + (b === 10 ? '₁₀' : b === 2 ? '₂' : b === 8 ? '₈' : '₁₆') + ' = <b>' + val + '</b> in decimal' +
      (val === max - 1 ? ': every wheel is at its top digit; one more and all four roll over.' : '');
  }
  $('c4plus').onclick = function () { prev = val; val += 1; show(); };
  $('c4minus').onclick = function () { prev = val; val -= 1; show(); };
  $('c4zero').onclick = function () { prev = val; val = 0; show(); };
  $('c4mb').onchange = function () { prev = val = Math.pow(+$('c4mb').value, 2) - 1; show(); };
  prev = val = 99; show();
})();
</script>

## Things to try

- Fill the trays for 22 (16, 4, 2) and for 2.625 (2, ½, ⅛), the examples of the book.
- Fill every tray: what is the largest number eight trays can make? (255 = 2⁸ − 1, the largest byte.)
- On the binary meter, start at 0 and press +1 sixteen times: you get the counting table of section 4.2.
- On the hexadecimal meter, go from 00FF to 0100: two wheels roll over at once.
