# See it: from a letter to bytes

*Chapter 4 · Helps you understand. Type any text: English, Hindi or any Indian script, ₹, an emoji. The page shows each character's code point and the bytes it takes in UTF-8 and in UTF-32, like the हम सब एक picture of the printed book (section 4.5).*

*Tested against Python's own encoders (`tools/ch04_js_test.py`).*

<div class="c4box" markdown="0">
<p><label>Text <input id="c4s" value="हम सब एक" size="28"></label> <button id="c4sgo">Show the bytes</button>
<span> or try: </span><button class="c4light c4ex">A</button><button class="c4light c4ex">₹</button><button class="c4light c4ex">नमस्ते</button><button class="c4light c4ex">India</button><button class="c4light c4ex">😀</button></p>
<div id="c4sout"></div>
</div>

<script>
(function () {
  function $(id) { return document.getElementById(id); }
  var te = new TextEncoder();
  function hex(n, w) { return n.toString(16).toUpperCase().padStart(w, '0'); }
  function run() {
    var text = $('c4s').value, chars = Array.from(text);
    if (!chars.length) { $('c4sout').innerHTML = '<p class="c4err">Type some text first.</p>'; return; }
    if (chars.length > 60) chars = chars.slice(0, 60);
    var h = ['<table class="c4"><tr><th>Character</th><th>Code point</th><th>Decimal</th><th>UTF-8 bytes</th><th>UTF-32 bytes</th></tr>'];
    var t8 = 0;
    chars.forEach(function (ch) {
      var cp = ch.codePointAt(0), b8 = Array.from(te.encode(ch)), c32 = hex(cp, 8);
      t8 += b8.length;
      var show = ch === ' ' ? 'space' : /\p{M}/u.test(ch) ? '◌' + ch : Ch04.esc(ch);
      h.push('<tr><td style="font-size:1.2rem">' + show + '</td><td>U+' + hex(cp, 4) + '</td><td>' + cp + '</td><td>' +
        b8.map(function (b) { return '<span class="c4byte">' + hex(b, 2) + '</span>'; }).join('') + ' ' + b8.length + '</td><td>' +
        [0, 2, 4, 6].map(function (i) { var b = c32.slice(i, i + 2); return '<span class="c4byte' + (b === '00' ? ' zero' : '') + '">' + b + '</span>'; }).join('') + ' 4</td></tr>');
    });
    h.push('</table>');
    h.push('<p class="c4ans">' + chars.length + (chars.length === 1 ? ' code point' : ' code points') + ': <b>UTF-8 ' + t8 + (t8 === 1 ? ' byte' : ' bytes') + '</b>, <b>UTF-32 ' + chars.length * 4 + ' bytes</b>.' +
      (Array.from($('c4s').value).length > 60 ? ' (Only the first 60 characters are shown.)' : '') + '</p>');
    h.push('<p>A grey 00 in UTF-32 holds only zeros. A character shown with ◌ is a sign that joins the letter before it.</p>');
    $('c4sout').innerHTML = h.join('');
  }
  $('c4sgo').onclick = run;
  $('c4s').onkeydown = function (e) { if (e.key === 'Enter') run(); };
  Array.prototype.forEach.call(document.querySelectorAll('.c4ex'), function (b) { b.onclick = function () { $('c4s').value = b.textContent; run(); }; });
  run();
})();
</script>

## What to notice

- English letters, digits and the space: **1 byte** in UTF-8, the same as ASCII.
- Hindi and the other Indian scripts, and ₹: **3 bytes** in UTF-8.
- Emojis: **4 bytes** in UTF-8.
- In UTF-32, every character takes **4 bytes**, whatever it is.
- Type नमस्ते: it shows **6** code points, because the halant (्) and the vowel sign (े) are characters of their own (see "Characters that join").
