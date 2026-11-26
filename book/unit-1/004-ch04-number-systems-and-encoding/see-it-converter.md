# See it: the step-by-step converter

*Chapter 4 · Helps you understand. Type a number, choose the two bases, and the page shows every step, exactly as in the printed book (sections 4.3 and 4.4). Use it to check your homework and to see where a mistake came in.*

*Every answer is exact. The program was tested on 600 conversions against the book's own checking program (`tools/ch04_js_test.py`).*

<div class="c4box" markdown="0">
<p>
  <label>Number <input id="c4n" value="156" size="16"></label>
  <label>from <select id="c4f"><option value="10" selected>decimal (10)</option><option value="2">binary (2)</option><option value="8">octal (8)</option><option value="16">hexadecimal (16)</option></select></label>
  <label>to <select id="c4t"><option value="2">binary (2)</option><option value="8" selected>octal (8)</option><option value="10">decimal (10)</option><option value="16">hexadecimal (16)</option></select></label>
  <label>places after the point <select id="c4p"><option>4</option><option>6</option><option selected>8</option><option>12</option></select></label>
</p>
<p><button id="c4go">Show the steps</button> <button id="c4back" class="c4light">Check by the return road</button></p>
<div id="c4out"></div>
<div id="c4chk"></div>
</div>

<script>
(function () {
  var last = null;
  function $(id) { return document.getElementById(id); }
  function run() {
    var r = Ch04.convert($('c4n').value, +$('c4f').value, +$('c4t').value, +$('c4p').value);
    $('c4chk').innerHTML = '';
    if (!r.ok) { $('c4out').innerHTML = '<p class="c4err">' + Ch04.esc(r.error) + '</p>'; last = null; return; }
    $('c4out').innerHTML = r.html; last = r;
  }
  $('c4go').onclick = run;
  $('c4n').onkeydown = function (e) { if (e.key === 'Enter') run(); };
  $('c4back').onclick = function () { if (!last) run(); if (last) $('c4chk').innerHTML = last.backHtml; };
  run();
})();
</script>

## Try these

| Type | From | To | What to notice |
|---|:-:|:-:|---|
| 156 | 10 | 16 | the remainder 12 is written as C |
| 11010110 | 2 | 8 | a 0 is added on the left to fill the first group |
| 5A | 16 | 8 | octal and hex go through binary |
| 12.375 | 10 | 2 | the fraction ends after three steps |
| 0.1 | 10 | 2 | a fraction comes back: 0.1 never ends in binary |
| 1021 | 2 | 10 | the page explains why this is not a binary number |
