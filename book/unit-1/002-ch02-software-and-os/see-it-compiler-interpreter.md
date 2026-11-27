# See it: Compiler vs interpreter, step by step

*Chapter 2 · See it. Choose a small program (or type your own), then press **Compile** or **Interpret: next line**,
and watch how each translator meets the errors. The program is written in a tiny teaching language, so that the two
ways can be shown exactly.*

<div class="ch02tr" markdown="0">
<p><label>Program: <select id="tr-select">
<option value="book">The book's program (errors in lines 3 and 5)</option>
<option value="marks">A correct program: total and average of two marks</option>
<option value="zero">An error only running can find: dividing by 0</option>
<option value="both">A name with no value, and a spelling error later</option>
</select></label></p>
<p><textarea id="tr-code" rows="7" cols="40" spellcheck="false"></textarea></p>
<p><button id="tr-compile" class="md-button md-button--primary">Compile</button>
<button id="tr-step" class="md-button md-button--primary">Interpret: next line</button>
<button id="tr-reset" class="md-button">Start again</button></p>
<p id="tr-message"></p>
<div id="tr-listing"></div>
<p><b>Output:</b><br><span id="tr-output"></span></p>
</div>
<script id="tr-data" type="application/json">{"book": {"title": "The book's program (errors in lines 3 and 5)", "code": ["a = 10", "PRINT a", "PRNT a + 5", "b = a * 2", "PRINT b +"], "hint": "The program of section 2.4. Press Compile, then press Interpret line by line."}, "marks": {"title": "A correct program: total and average of two marks", "code": ["m1 = 80", "m2 = 75", "total = m1 + m2", "PRINT total", "avg = total / 2", "PRINT avg"], "hint": "No errors: both give the same output. The difference is when the translating is done."}, "zero": {"title": "An error only running can find: dividing by 0", "code": ["a = 10", "b = 0", "PRINT a", "c = a / b", "PRINT c"], "hint": "The grammar is correct, so the compiler makes the object file; the error appears only when line 4 runs."}, "both": {"title": "A name with no value, and a spelling error later", "code": ["x = 5", "PRINT y", "z = x * 3", "PRNT z"], "hint": "The compiler finds the spelling error in line 4 and runs nothing. The interpreter stops at line 2 and never reaches line 4."}}</script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  Ch02.page(JSON.parse(document.getElementById('tr-data').textContent),
    {select: 'tr-select', code: 'tr-code', compile: 'tr-compile', step: 'tr-step', reset: 'tr-reset',
     message: 'tr-message', listing: 'tr-listing', output: 'tr-output'});
});
</script>

## The teaching language

| You write | It means |
|---|---|
| `x = 5` | put 5 in x |
| `total = m1 + m2` | work it out and put the answer in total (`+ - * /`; `/` keeps the whole-number part) |
| `PRINT total` | show the value |

## What to notice

1. **The book's program.** *Compile* lists **both** errors (lines 3 and 5) and runs nothing. *Interpret* shows 10, then
   stops at line 3; it has not even read line 5.
2. **A correct program.** Both give the same output. The compiler translated once and made a file that runs again and
   again; the interpreter translates every time.
3. **Dividing by 0.** The grammar is correct, so the compiler cannot see a problem; the error appears only when line 4
   runs, in both. Such errors are called **run-time errors** (Chapter 8).
4. **A name with no value.** The compiler reports the spelling error in line 4 and runs nothing; the interpreter stops at
   line 2 and never sees line 4.
5. **Memory.** After compiling, the compiler is not needed to run the file; the interpreter must stay in memory the
   whole time the program runs.

*The page was tested on hundreds of programs: for every one, it gives exactly what a separate Python model of the same
rules gives.*
