# See it: Token explorer

*Chapter 6 · See it. Section 6.4 cuts one line into its tokens. Type any line of Python (or press an example) and see it cut into tokens, each named by its kind. Comments and spaces are skipped: they are not tokens.*

<div class="c6box" markdown="0">
<p><label>A line of Python: <input id="tk-input" size="48" spellcheck="false" value="if marks >= 33: print(&quot;Pass&quot;)   # result"></label></p>
<p>Examples: <button class="c6light" data-ch06-line="if marks >= 33: print(&quot;Pass&quot;)   # result">if marks >= 33: print("Pass")</button> <button class="c6light" data-ch06-line="total = price * 2">total = price * 2</button> <button class="c6light" data-ch06-line="area = 22 / 7 * radius * radius">area = 22 / 7 * radius * radius</button> <button class="c6light" data-ch06-line="x, y = y, x">x, y = y, x</button> <button class="c6light" data-ch06-line="print(&quot;Total:&quot;, 90 + 85)">print("Total:", 90 + 85)</button> <button class="c6light" data-ch06-line="is_ok = not (a == b) and c in d">is_ok = not (a == b) and c in d</button> <button class="c6light" data-ch06-line="x = 0o17 + 0x1F + 2.5e3">x = 0o17 + 0x1F + 2.5e3</button> <button class="c6light" data-ch06-line="class = &quot;XI-A&quot;">class = "XI-A"</button> <button class="c6light" data-ch06-line="price = $250">price = $250</button> <button class="c6light" data-ch06-line="print(&quot;Hi&quot;">print("Hi"</button> </p>
<div id="tk-result"></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function () {
  Ch06.tokenPage({input: 'tk-input', result: 'tk-result'});
});
</script>

## The five kinds, and their colours

| Kind | What it is | Examples |
|---|---|---|
| keyword | a word Python reserves | `if`, `for`, `True`, `and` |
| identifier | a name you choose | `marks`, `price`, `print` |
| literal | a fixed value written in the line | `33`, `"Pass"`, `2.5e3` |
| operator | does work on values | `+`, `>=`, `=`, `//` |
| punctuator | groups or separates | `(` `)` `,` `:` `.` |

## What to notice

1. `print` is an **identifier**, not a keyword: it is the name of a function, and you could (but should not) use it as a
   name for something else.
2. `True`, `False` and `None` come out as **keywords**: in exam answers they are called Boolean literals and the special
   literal (section 6.6).
3. `and`, `or`, `not`, `in`, `is` are **keywords** that work as operators.
4. Try `price = $250` or an unclosed bracket: Python would refuse the line, and the page says why.

*The page was tested on 2,010 lines against Python's own tokenizer: for every line it gives exactly Python's tokens, or
says that Python would refuse the line. Lines it does not handle (f-strings, a backslash at the end) get a "not covered
here" note.*
