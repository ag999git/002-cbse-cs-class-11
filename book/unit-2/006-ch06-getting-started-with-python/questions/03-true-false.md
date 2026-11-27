# Chapter 6: Getting Started with Python: True or false (35)

*Chapter 6 · Questions (online). One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## True or false

**Q1.** Python is a compiled language.

**Answer.** **False.** it is interpreted: one statement at a time.

**Q2.** Python 3 runs every Python 2 program without change.

**Answer.** **False.** for example `print "Hi"` fails in Python 3.

**Q3.** Python is free and open source.

**Answer.** **True.** free to use, and its source code is open to all.

**Q4.** IDLE is installed together with Python.

**Answer.** **True.** it comes with Python from python.org.

**Q5.** Google Colab needs Python to be installed on your computer.

**Answer.** **False.** it runs on Google's computers; you need only a browser.

**Q6.** Work typed in the shell is saved automatically.

**Answer.** **False.** it is lost when the shell closes.

**Q7.** IDLE asks you to save a new script before it runs it.

**Answer.** **True.** Run Module (F5) runs the saved file.

**Q8.** In the shell, typing `"Hi"` shows `'Hi'`, with quotes.

**Answer.** **True.** the shell shows the value as you would type it; print() shows Hi.

**Q9.** `print()` can show several values in one call.

**Answer.** **True.** `print(a, b, c)` separates them with spaces.

**Q10.** If line 2 of a script has a SyntaxError, line 1 still runs.

**Answer.** **False.** Python checks the grammar of the whole file first; nothing runs.

**Q11.** `a=5` and `a = 5` mean different things.

**Answer.** **False.** spaces inside a line do not change the meaning; they help reading.

**Q12.** A space at the start of a line can stop a program.

**Answer.** **True.** `IndentationError: unexpected indent`.

**Q13.** Python skips blank lines in a script.

**Answer.** **True.** they only help people read the program.

**Q14.** `print` is a keyword.

**Answer.** **False.** it is the name of a built-in function.

**Q15.** `True` and `true` are the same in Python.

**Answer.** **False.** Python is case-sensitive: only `True` is a keyword.

**Q16.** An identifier may contain a hyphen, as in `roll-no`.

**Answer.** **False.** `-` is the minus operator.

**Q17.** `_` on its own is a valid identifier.

**Answer.** **True.** an underscore counts as a letter.

**Q18.** An identifier may be 100 characters long.

**Answer.** **True.** any length is allowed (but keep it sensible).

**Q19.** `class_11` is a valid identifier.

**Answer.** **True.** it is not the keyword `class`.

**Q20.** `None` is a keyword.

**Answer.** **True.** one of the three keywords with a capital letter.

**Q21.** `"5"` and `5` are the same value.

**Answer.** **False.** a string and an integer.

**Q22.** `0o9` is a valid octal literal.

**Answer.** **False.** octal digits are 0 to 7 only.

**Q23.** `=` tests whether two values are equal.

**Answer.** **False.** `=` assigns; `==` tests equality (Chapter 7).

**Q24.** After `b = a`, giving `a` a new value also changes `b`.

**Answer.** **False.** only the tag `a` moves; `b` stays on the old object.

**Q25.** `x = y = 0` ties both names to one object.

**Answer.** **True.** `id(x) == id(y)` is True.

**Q26.** In Python a variable must be declared before it is used.

**Answer.** **False.** it is created when it is first assigned.

**Q27.** Using a name before giving it a value gives `NameError`.

**Answer.** **True.** the name does not exist yet.

**Q28.** Python is weakly typed.

**Answer.** **False.** it is dynamically but strongly typed: `"5" + 3` is a TypeError.

**Q29.** `x, y = y, x` swaps two values.

**Answer.** **True.** the right side is worked out first.

**Q30.** A triple-quoted string on its own line does nothing.

**Answer.** **True.** Python makes the string and throws it away.

**Q31.** `//` starts a comment in Python.

**Answer.** **False.** it is floor division (Chapter 7); a comment starts with `#`.

**Q32.** A docstring is the first statement of a program or function.

**Answer.** **True.** a triple-quoted note there.

**Q33.** Python refuses to run a program that breaks PEP 8.

**Answer.** **False.** PEP 8 is about style; Python does not check it.

**Q34.** The L-value of an assignment must be a name.

**Answer.** **True.** a value cannot be tied to anything.

**Q35.** `print(type(3.0))` prints `<class 'float'>`.

**Answer.** **True.** 3.0 has a decimal point.

