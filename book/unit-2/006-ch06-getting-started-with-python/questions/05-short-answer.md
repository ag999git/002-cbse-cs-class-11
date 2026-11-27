# Chapter 6: Getting Started with Python: Short-answer questions (35)

*Chapter 6 · Questions (online). Two or three marks each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Short answers

**Q1.** Why is Python called an interpreted language? *(E · 6.1)*

**Answer.** Its interpreter translates and runs one statement at a time, while the program runs, and stops at the first error it meets; there is no separate translation of the whole program first.

**Q2.** Give two differences between Python 2 and Python 3. *(M · 6.1)*

**Answer.** (1) `print` is a statement in Python 2 (`print "Hi"`) and a function in Python 3 (`print("Hi")`). (2) `7 / 2` gives 3 in Python 2 and 3.5 in Python 3. (Also: Python 3 uses Unicode text by default; Python 2 is no longer supported.)

**Q3.** Write two advantages and two limits of Python. *(M · 6.1)*

**Answer.** Advantages: easy to read; free and open source (also: cross-platform, large library). Limits: slower than C/C++ for heavy calculation; types are not fixed on names, so some mistakes appear only when a line runs.

**Q4.** What is an IDE? Name two IDEs for Python. *(E · 6.2)*

**Answer.** An Integrated Development Environment: one program to write, run and correct programs (editor, Run button, error messages, debugger). IDLE and Thonny (also VS Code, PyCharm).

**Q5.** Differentiate between IDLE and Google Colab (two points). *(M · 6.2)*

**Answer.** (1) *Where the code runs:* IDLE on your own computer; Colab on Google's computers. (2) *Needs:* IDLE needs Python installed; Colab needs only a browser, the internet and a Google sign-in.

**Q6.** What is the Python shell? What does its prompt `>>>` mean? *(E · 6.3)*

**Answer.** The window of interactive mode, where each statement is run as soon as you press Enter. `>>>` means Python is waiting for the next statement.

**Q7.** Give two reasons to write a program as a script. *(E · 6.3)*

**Answer.** A script is saved and can be run again; it can be long; it can be given to others (any two).

**Q8.** List the steps to write and run a script in IDLE. *(E · 6.3)*

**Answer.** (1) File → New File; (2) type the program; (3) save it with a `.py` name; (4) Run → Run Module (F5); (5) read the output (or the error) in the shell.

**Q9.** What is "the Colab trap"? *(M · 6.3)*

**Answer.** In a Colab or Jupyter cell (and in the shell) a bare expression on the last line shows its value; in a script it shows nothing. A program that "worked" in Colab may print less as a script: use print().

**Q10.** What does the `= RESTART: …` line mean in IDLE's shell? *(M · 6.3)*

**Answer.** IDLE cleared the shell's memory before running the file, so earlier shell work cannot disturb it, and it names the file that ran. It is not part of the output.

**Q11.** How should you read an error message? *(E · 6.3)*

**Answer.** Read the last line first (the kind of error and its cause), then go to the line number it gives; correct one error, save and run again.

**Q12.** What is Python's character set? Name its groups. *(E · 6.4)*

**Answer.** The characters Python accepts: letters (A–Z, a–z), digits (0–9), special symbols (`+ - * / ( ) [ ] { } , : . # …`), white space (space, tab, new line) and any Unicode character inside strings and comments.

**Q13.** Name the kind of each token in `x = y + 10`. *(E · 6.4)*

**Answer.** `x` identifier; `=` operator (assignment); `y` identifier; `+` operator; `10` literal: 5 tokens.

**Q14.** Why can a keyword not be used as a name? *(M · 6.5)*

**Answer.** A keyword already has a fixed meaning to Python; if it were also a name, Python could not tell which meaning you want (like a reserved seat).

**Q15.** Which are invalid identifiers, and why: `roll-no`, `Roll_No`, `roll no`, `2roll`, `_roll`? *(E · 6.5)*

**Answer.** Invalid: `roll-no` (`-` not allowed), `roll no` (space), `2roll` (begins with a digit). `Roll_No` and `_roll` are valid.

**Q16.** Differentiate between a naming rule and a naming convention, with one example of each. *(M · 6.5)*

**Answer.** A rule is enforced by Python: break it and the program does not run (a name cannot begin with a digit). A convention is followed by programmers: break it and the program runs but reads badly (snake_case for variables).

**Q17.** What are snake_case and camelCase? Which does Python prefer? *(E · 6.5)*

**Answer.** snake_case: small letters joined by `_` (`roll_no`). camelCase: words joined with a capital at each new word (`rollNo`). Python prefers snake_case (PEP 8).

**Q18.** Why should `l`, `O` and `I` not be used as one-letter names? *(E · 6.5)*

**Answer.** They are legal but look like the digits 1 and 0; `l1` may be read as "one-one".

**Q19.** What are literals? Name four kinds, with an example of each. *(E · 6.6)*

**Answer.** Fixed values written in a program: string `"Pass"`, integer `33`, float `3.14`, Boolean `True` (also complex `2+3j`, special `None`).

**Q20.** How are `5`, `"5"` and `5.0` different? *(E · 6.6)*

**Answer.** `5` is an integer (`int`), `"5"` is a string (`str`, text), `5.0` is a floating-point number (`float`).

**Q21.** What are an operator and an operand? Give an example. *(E · 6.6)*

**Answer.** An operator does work on values; the values it works on are operands. In `price * 2`, `*` is the operator; `price` and `2` are the operands.

**Q22.** What are punctuators? Name four. *(E · 6.6)*

**Answer.** Symbols that group or separate parts of a statement: `( )`, `[ ]`, `,`, `:` (also `.`, `{ }`, `;`).

**Q23.** What is an escape sequence? Give two. What is the length of `"a\tb"`? *(M · 6.6)*

**Answer.** A backslash and a character that together stand for one character you cannot type directly: `\n` (new line), `\t` (tab). `len("a\tb")` is 3.

**Q24.** What is a variable in Python? *(E · 6.7)*

**Answer.** A name tied to an object in memory; the object carries the value and its type. The name can later be tied to another object.

**Q25.** What happens in the three steps of `marks = 92`? *(M · 6.7)*

**Answer.** (1) Python makes the object 92 (an int) in memory; (2) it makes the name `marks`, if new; (3) it ties the name to the object.

**Q26.** Show with an example that two names can refer to one object. *(M · 6.7)*

**Answer.** `a = [1]` then `b = a`: `id(a) == id(b)` prints True; one object, two tags.

**Q27.** Give two differences between static and dynamic typing. *(M · 6.7)*

**Answer.** (1) *Who has the type:* static (C++, Java): the variable (box); dynamic (Python): only the object. (2) *When types are checked:* static: before the program runs; dynamic: while it runs.

**Q28.** Why is it wrong to call Python "weakly typed"? *(H · 6.7)*

**Answer.** Python never mixes types quietly: `"5" + 3` stops with TypeError. It is dynamically typed (names have no type) but strongly typed (values are not mixed).

**Q29.** What is swapping? Why does it usually need a third variable? *(M · 6.7)*

**Answer.** Exchanging the values of two variables. Writing `x = y` first would wipe out the old value of x, so it is first saved in a third variable: `t = x`, `x = y`, `y = t`.

**Q30.** Why is `x = x + 1` correct in Python but impossible in mathematics? *(M · 6.7)*

**Answer.** In Python `=` is an assignment: work out x + 1, then tie x to the result. In mathematics `=` says both sides are equal, and no number equals itself plus 1.

**Q31.** What are an expression and a statement? Give one example of each. *(E · 6.3)*

**Answer.** An expression gives a value: `price * 2`. A statement is an instruction that does something: `total = price * 2`.

**Q32.** Differentiate between a `#` comment and a triple-quoted note. *(M · 6.8)*

**Answer.** A `#` comment runs to the end of the line and is skipped by Python. A triple-quoted note is a string that may run over many lines; on its own line it is made and thrown away.

**Q33.** What is a docstring? *(E · 6.8)*

**Answer.** A triple-quoted note as the first statement of a program (or function), telling a user what it does and how to use it.

**Q34.** What are physical and logical lines? *(M · 6.3)*

**Answer.** A physical line is a line as you see it; a logical line is one whole statement as Python reads it. One logical line may run over several physical lines inside brackets or after `\`.

**Q35.** What is PEP 8? Give two of its rules. *(E · 6.5)*

**Answer.** Python's style guide (PEP = Python Enhancement Proposal). Rules: snake_case names; 4 spaces per indent; lines of at most 79 characters; one statement per line (any two).

