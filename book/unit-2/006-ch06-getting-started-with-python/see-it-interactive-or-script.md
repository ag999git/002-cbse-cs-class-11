# See it: Interactive or script?

*Chapter 6 · See it. Section 6.3 says: the shell shows the value of a bare expression; a script shows only what you print. Choose a program, then press **Next line** to type it into the shell one line at a time, or **Run all**. The script's output appears when every line has run.*

<div class="c6box" markdown="0">
<p><label>Program: <select id="md-select"><option value="sum">A sum, with and without print</option><option value="name">A name, with and without print</option><option value="quotes">Text: why the shell shows quotes</option><option value="double">Working with a name</option><option value="calc">The shell as a calculator</option><option value="two">Two values in one print</option><option value="comment">Comments are skipped in both</option><option value="length">A built-in function</option><option value="total">Changing a value</option><option value="repeat">Text times a number</option><option value="compare">A comparison</option><option value="none">A value that shows nothing</option></select></label>
<button id="md-next">Next line</button> <button id="md-all" class="c6light">Run all</button></p>
<p><b>The program</b></p>
<div id="md-source" class="ch06-pre"></div>
<div class="ch06-twocol">
<div><p><b>Interactive mode: the shell</b></p><div id="md-shell" class="ch06-pre"></div></div>
<div><p><b>Script mode: the same lines saved and run (F5)</b></p><div id="md-script" class="ch06-pre"></div></div>
</div>
<p id="md-note"></p>
</div>
<script id="md-data" type="application/json">{"sum": {"title": "A sum, with and without print", "lines": ["7 + 5", "print(7 + 5)"], "shell": ["12", "12"], "script": "12", "note": "In the shell both lines show 12. In a script, line 1 shows nothing: a value is shown only when you print it."}, "name": {"title": "A name, with and without print", "lines": ["marks = 92", "marks", "print(marks)"], "shell": ["", "92", "92"], "script": "92", "note": "An assignment shows nothing anywhere. A bare name shows its value only in the shell."}, "quotes": {"title": "Text: why the shell shows quotes", "lines": ["\"Hello\"", "print(\"Hello\")"], "shell": ["'Hello'", "Hello"], "script": "Hello", "note": "The shell shows the value as you would type it, with quotes: 'Hello'. print() shows the text itself, without quotes."}, "double": {"title": "Working with a name", "lines": ["x = 10", "x * 2", "y = x * 2", "y"], "shell": ["", "20", "", "20"], "script": "", "note": "x * 2 is worked out but not kept or shown in a script. y = x * 2 keeps the result in y."}, "calc": {"title": "The shell as a calculator", "lines": ["2 ** 10", "7 / 2", "7 // 2", "7 % 2"], "shell": ["1024", "3.5", "3", "1"], "script": "", "note": "A quick way to check sums. A script would show nothing at all here: every line is a bare expression."}, "two": {"title": "Two values in one print", "lines": ["a = 5", "b = 3", "a + b", "print(a, b, a + b)"], "shell": ["", "", "8", "5 3 8"], "script": "5 3 8", "note": "print() can show several values, separated by spaces."}, "comment": {"title": "Comments are skipped in both", "lines": ["# a note for people", "10 + 1   # eleven"], "shell": ["", "11"], "script": "", "note": "A comment is never run. In the shell the sum still shows 11; in a script nothing shows."}, "length": {"title": "A built-in function", "lines": ["len(\"Asha\")", "print(len(\"Asha\"))"], "shell": ["4", "4"], "script": "4", "note": "len() gives the number of characters (Chapter 11). Again: shown in the shell, printed in a script."}, "total": {"title": "Changing a value", "lines": ["total = 0", "total = total + 5", "total = total + 5", "total"], "shell": ["", "", "", "10"], "script": "", "note": "Each line uses the old value of total and ties total to a new one. Only the last line shows anything, and only in the shell."}, "repeat": {"title": "Text times a number", "lines": ["\"Py\" * 3", "print(\"Py\" * 3)"], "shell": ["'PyPyPy'", "PyPyPy"], "script": "PyPyPy", "note": "\"Py\" * 3 repeats the text. The shell shows 'PyPyPy' with quotes; print shows PyPyPy."}, "compare": {"title": "A comparison", "lines": ["5 > 3", "print(5 > 3)"], "shell": ["True", "True"], "script": "True", "note": "A comparison gives True or False (Chapter 7)."}, "none": {"title": "A value that shows nothing", "lines": ["result = None", "result", "print(result)"], "shell": ["", "", "None"], "script": "None", "note": "The shell shows nothing for None, but print() shows the word None."}}</script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  Ch06.modesPage(JSON.parse(document.getElementById('md-data').textContent),
    {select: 'md-select', source: 'md-source', shell: 'md-shell', script: 'md-script', next: 'md-next', all: 'md-all', note: 'md-note'});
});
</script>

## What to notice

1. **A bare expression** (`7 + 5`, `marks`, `"Hello"`) shows its value in the shell, and **nothing** in a script.
2. **The shell shows text with quotes** (`'Hello'`), the way you would type it; `print()` shows the text itself.
3. **An assignment** (`marks = 92`) shows nothing in either mode: it only ties a name to a value.
4. **A notebook cell** (Colab, Jupyter) behaves like the shell for its **last** line: a bare expression there shows its
   value. That is "the Colab trap" of section 6.3.

*Every output on this page was made by Python 3.12.7: the shell column by Python's own interactive console, the script
column by running the lines as a file.*
