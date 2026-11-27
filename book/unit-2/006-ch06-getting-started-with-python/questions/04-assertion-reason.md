# Chapter 6: Getting Started with Python: Assertion and reason (20)

*Chapter 6 · Questions (online). One mark each. Choose: **(a)** both true, R explains A; **(b)** both true, R does not explain A; **(c)** A true, R false; **(d)** A false, R true. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Assertion and reason

**Q1.** **A:** A Python program written on Windows runs on Linux without change. **R:** Python is cross-platform.

**Answer.** (a). *Why:* cross-platform means exactly this.

**Q2.** **A:** Interactive mode is good for testing one statement. **R:** Work in interactive mode is saved in a file.

**Answer.** (c). *Why:* shell work is lost when the shell closes.

**Q3.** **A:** In a script, `7 + 5` on its own line shows nothing. **R:** A script shows a value only when it is printed.

**Answer.** (a). *Why:* the shell is different: it shows bare values.

**Q4.** **A:** Python is an interpreted language. **R:** Python translates and runs one statement at a time.

**Answer.** (a). *Why:* that is what an interpreter does.

**Q5.** **A:** `print "Hi"` fails in Python 3. **R:** In Python 3, print is a function and needs brackets.

**Answer.** (a). *Why:* Python 2's print statement was removed.

**Q6.** **A:** Google Colab needs the internet. **R:** Colab runs your code on Google's computers.

**Answer.** (a). *Why:* your typing must reach them.

**Q7.** **A:** IDLE is used in the practical exam. **R:** IDLE needs an internet connection.

**Answer.** (c). *Why:* IDLE runs on your own computer.

**Q8.** **A:** `my-marks` is not a valid identifier. **R:** `-` is the minus operator.

**Answer.** (a). *Why:* Python would read my minus marks.

**Q9.** **A:** `print` can be used as a variable name. **R:** `print` is not a keyword.

**Answer.** (a). *Why:* legal, but poor style: it hides the function.

**Q10.** **A:** `True` is a keyword. **R:** All keywords begin with a capital letter.

**Answer.** (c). *Why:* only True, False and None do.

**Q11.** **A:** A comment is not a token. **R:** Python skips comments before cutting a line into tokens.

**Answer.** (a). *Why:* a token must mean something to Python.

**Q12.** **A:** `"Asha's"` is a valid string literal. **R:** A single quote may appear inside double quotes.

**Answer.** (a). *Why:* the double quotes mark the start and end.

**Q13.** **A:** `1,234` makes a tuple of two numbers. **R:** A comma separates values.

**Answer.** (a). *Why:* Python reads (1, 234), not one thousand two hundred and thirty-four.

**Q14.** **A:** `x = 10` is not an equation. **R:** `=` gives the value on the right to the name on the left.

**Answer.** (a). *Why:* read `=` as "becomes".

**Q15.** **A:** After `a = 5`, `b = a`, `a = 6`, `b` is still 5. **R:** `a = 6` moves only the tag `a`.

**Answer.** (a). *Why:* the tag `b` stays on 5.

**Q16.** **A:** `x + 1 = 5` is an error. **R:** The left side of `=` must be a name.

**Answer.** (a). *Why:* `x + 1` is an expression, not a name.

**Q17.** **A:** Python is dynamically typed. **R:** In Python the type belongs to the object, not to the name.

**Answer.** (a). *Why:* so a name may be tied to any type.

**Q18.** **A:** `//` starts a comment in Python. **R:** `//` is floor division in Python.

**Answer.** (d). *Why:* a comment starts with `#`.

**Q19.** **A:** A docstring is shown on the screen when the program runs. **R:** A docstring is a triple-quoted string at the top of a program.

**Answer.** (d). *Why:* Python keeps it but does not print it.

**Q20.** **A:** `_total` is a valid identifier. **R:** An underscore counts as a letter in a name.

**Answer.** (a). *Why:* so it may begin a name.

