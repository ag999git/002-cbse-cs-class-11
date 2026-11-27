# Chapter 6: Getting Started with Python: Multiple-choice questions (50)

*Chapter 6 · Questions (online). One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Meet Python (6.1)

**Q1.** Python is named after: (a) a snake (b) a British comedy show (c) a Greek god (d) its first computer *(E · 6.1)*

**Answer.** (b) a British comedy show. *Why:* Guido van Rossum liked *Monty Python's Flying Circus*.

**Q2.** Python 2 was retired on: (a) 1 Jan 2008 (b) 1 Jan 2015 (c) 1 Jan 2020 (d) 1 Jan 2024 *(E · 6.1)*

**Answer.** (c) 1 Jan 2020. *Why:* no fixes at all since then, even for security.

**Q3.** Which is NOT a feature of Python? (a) interpreted (b) case-sensitive (c) every variable's type must be declared (d) cross-platform *(E · 6.1)*

**Answer.** (c) every variable's type must be declared. *Why:* Python is dynamically typed: no declarations.

**Q4.** A language whose statements are translated and run one at a time is: (a) compiled (b) interpreted (c) assembled (d) machine language *(E · 6.1)*

**Answer.** (b) interpreted. *Why:* this is what Python's interpreter does (Chapter 2).

**Q5.** "Free and open source" means the software is: (a) free for 30 days (b) free to use, and its source code is open to all (c) free but secret (d) paid but shared *(M · 6.1)*

**Answer.** (b) free to use, and its source code is open to all. *Why:* freeware is free without its source code; shareware is a trial.

**Q6.** Python 3.0, the big clean-up, came in: (a) 1991 (b) 2000 (c) 2008 (d) 2020 *(E · 6.1)*

**Answer.** (c) 2008. *Why:* December 2008.

**Q7.** "Cross-platform" means a Python program: (a) runs on Windows, Linux and macOS without change (b) needs the internet (c) runs only on phones (d) can be shared *(E · 6.1)*

**Answer.** (a) runs on Windows, Linux and macOS without change. *Why:* the same .py file runs everywhere Python is installed.

**Q8.** In Python 3, `print "Hi"` gives: (a) Hi (b) "Hi" (c) a SyntaxError (d) nothing *(M · 6.1)*

**Answer.** (c) a SyntaxError. *Why:* Python 3 says: `SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?`

## Your Python workshop (6.2)

**Q9.** IDE stands for: (a) Internet Development Engine (b) Integrated Development Environment (c) Interpreted Data Editor (d) Internal Design Environment *(E · 6.2)*

**Answer.** (b) Integrated Development Environment. *Why:* one program to write, run and correct programs.

**Q10.** Which tool runs your code on Google's computers? (a) IDLE (b) Thonny (c) Google Colab (d) VS Code *(E · 6.2)*

**Answer.** (c) Google Colab. *Why:* Colab is a cloud tool: it needs the internet.

**Q11.** Which tool comes with Python itself? (a) IDLE (b) VS Code (c) Jupyter (d) Colab *(E · 6.2)*

**Answer.** (a) IDLE. *Why:* IDLE is installed with Python.

**Q12.** Jupyter Notebook runs your code: (a) on Google's computers (b) on a server on your own computer (c) in the browser only, without Python (d) only on phones *(M · 6.2)*

**Answer.** (b) on a server on your own computer. *Why:* the browser only shows the cells; a local Jupyter server runs Python.

**Q13.** Which of these needs no installation? (a) IDLE (b) Thonny (c) VS Code (d) Google Colab *(E · 6.2)*

**Answer.** (d) Google Colab. *Why:* only a browser and a Google sign-in.

**Q14.** The tool used in most school labs and the practical exam is: (a) IDLE (b) Colab (c) Jupyter (d) PyCharm *(E · 6.2)*

**Answer.** (a) IDLE. *Why:* it comes with Python and needs no internet.

**Q15.** A notebook (Colab, Jupyter) is made of: (a) pages (b) cells (c) shells (d) scripts *(E · 6.2)*

**Answer.** (b) cells. *Why:* each cell holds code or text and is run on its own.

## First program and the two modes (6.3)

**Q16.** In IDLE's shell window you work in: (a) script mode (b) interactive mode (c) compile mode (d) debug mode *(E · 6.3)*

**Answer.** (b) interactive mode. *Why:* one statement at a time, answered at once.

**Q17.** Which line of a SCRIPT shows something on the screen? (a) `7 + 5` (b) `print(7 + 5)` (c) `x = 7 + 5` (d) `# 7 + 5` *(E · 6.3)*

**Answer.** (b) `print(7 + 5)`. *Why:* a script shows a value only through print().

**Q18.** The `= RESTART: …` line in the shell means: (a) an error (b) IDLE cleared the shell's memory before running the file (c) the computer restarted (d) the program ended *(M · 6.3)*

**Answer.** (b) IDLE cleared the shell's memory before running the file. *Why:* it is IDLE's own line, not your output.

**Q19.** The last line of an error message tells you: (a) the time (b) the kind of error and its cause (c) the file size (d) the Python version *(E · 6.3)*

**Answer.** (b) the kind of error and its cause. *Why:* read it first, then go to the line number.

**Q20.** A line that begins with spaces for no reason gives: (a) NameError (b) IndentationError (c) TypeError (d) no error *(E · 6.3)*

**Answer.** (b) IndentationError. *Why:* Python uses the spaces at the start of a line to mark blocks.

**Q21.** The prompt `>>>` means: (a) an error (b) Python is waiting for a statement (c) the program has ended (d) a comment *(E · 6.3)*

**Answer.** (b) Python is waiting for a statement. *Why:* type a statement and press Enter.

**Q22.** The better way to write one long statement over two lines is: (a) inside brackets (b) with a `;` (c) with `#` (d) it is not possible *(M · 6.3)*

**Answer.** (a) inside brackets. *Why:* Python does not end a statement while a bracket is open; `\` also works but breaks easily.

**Q23.** Work typed in the shell is lost when: (a) you press Enter (b) the shell is closed (c) you use print (d) you type a comment *(E · 6.3)*

**Answer.** (b) the shell is closed. *Why:* save programs as scripts to keep them.

## Character set and tokens (6.4)

**Q24.** Which is a white-space character? (a) `_` (b) tab (c) `#` (d) `@` *(E · 6.4)*

**Answer.** (b) tab. *Why:* space, tab and new line are white space.

**Q25.** How many tokens are in `print("Hi", 5)`? (a) 4 (b) 5 (c) 6 (d) 7 *(M · 6.4)*

**Answer.** (c) 6. *Why:* `print`, `(`, `"Hi"`, `,`, `5`, `)`: counted by Python's tokenizer.

**Q26.** In `x = 5  # five`, the part `# five` is: (a) a literal (b) a comment, which is not a token (c) an operator (d) a keyword *(E · 6.4)*

**Answer.** (b) a comment, which is not a token. *Why:* Python skips it before cutting the line into tokens.

**Q27.** In `if a >= b:`, the token `>=` is: (a) a punctuator (b) an operator (c) a keyword (d) a literal *(E · 6.4)*

**Answer.** (b) an operator. *Why:* it does work on two values: a comparison.

**Q28.** In `if a >= b:`, the token `:` is: (a) an operator (b) a punctuator (c) a literal (d) an identifier *(E · 6.4)*

**Answer.** (b) a punctuator. *Why:* it ends a line that starts a block.

**Q29.** `"33"` is: (a) an integer literal (b) a string literal (c) an identifier (d) a keyword *(E · 6.4)*

**Answer.** (b) a string literal. *Why:* quotes make it text.

**Q30.** Hindi or Tamil letters may appear in a Python program in: (a) nowhere (b) strings and comments (and even names) (c) only in keywords (d) only in numbers *(M · 6.4)*

**Answer.** (b) strings and comments (and even names). *Why:* Python uses Unicode (Chapter 4).

## Keywords and identifiers (6.5)

**Q31.** Which is a keyword? (a) `print` (b) `input` (c) `None` (d) `main` *(M · 6.5)*

**Answer.** (c) `None`. *Why:* `print` and `input` are names of functions, not keywords.

**Q32.** Which is NOT a keyword? (a) `elif` (b) `lambda` (c) `print` (d) `pass` *(M · 6.5)*

**Answer.** (c) `print`. *Why:* `print` is a built-in function.

**Q33.** Which is a valid identifier? (a) `my-name` (b) `_count` (c) `3rd` (d) `for` *(E · 6.5)*

**Answer.** (b) `_count`. *Why:* `-` is not allowed; a digit cannot come first; `for` is a keyword.

**Q34.** Which is NOT a valid identifier? (a) `Total_1` (b) `total1` (c) `total 1` (d) `TOTAL` *(E · 6.5)*

**Answer.** (c) `total 1`. *Why:* a space makes two names.

**Q35.** Python's convention for variable names is: (a) camelCase (b) snake_case (c) ALL CAPITALS (d) any style *(E · 6.5)*

**Answer.** (b) snake_case. *Why:* small letters joined by `_` (PEP 8).

**Q36.** A name in capitals, like `PASS_MARK`, is meant for: (a) a keyword (b) a constant (c) a function (d) a comment *(E · 6.5)*

**Answer.** (b) a constant. *Why:* a value that never changes.

**Q37.** Which pair are BOTH keywords? (a) `True` and `False` (b) `true` and `false` (c) `print` and `input` (d) `If` and `Else` *(M · 6.5)*

**Answer.** (a) `True` and `False`. *Why:* keywords are written exactly: `true` and `If` are ordinary names.

**Q38.** How long may an identifier be? (a) 8 characters (b) 32 characters (c) 79 characters (d) any length *(M · 6.5)*

**Answer.** (d) any length. *Why:* PEP 8 limits a LINE to 79 characters, not a name.

**Q39.** Which name hides one of Python's own functions? (a) `length` (b) `len` (c) `size` (d) `count1` *(M · 6.5)*

**Answer.** (b) `len`. *Why:* after `len = 5`, `len("abc")` stops working.

## Literals, operators, punctuators (6.6)

**Q40.** The value of `0o17` is: (a) 17 (b) 15 (c) 0 (d) 1.7 *(M · 6.6)*

**Answer.** (b) 15. *Why:* `0o` means octal: 1 × 8 + 7 = 15.

**Q41.** Which is a floating-point literal? (a) `25` (b) `2.5e3` (c) `"2.5"` (d) `0x25` *(E · 6.6)*

**Answer.** (b) `2.5e3`. *Why:* 2.5e3 = 2500.0.

**Q42.** `None` stands for: (a) zero (b) an empty string (c) no value (d) False *(E · 6.6)*

**Answer.** (c) no value. *Why:* it is the special literal.

**Q43.** In `print(a, b)`, the comma is: (a) an operator (b) a punctuator (c) a literal (d) a keyword *(E · 6.6)*

**Answer.** (b) a punctuator. *Why:* it separates items.

**Q44.** `=` in `x = 5` is called the: (a) equality operator (b) assignment operator (c) comparison (d) punctuator only *(E · 6.6)*

**Answer.** (b) assignment operator. *Why:* equality is tested with `==` (Chapter 7).

## Variables (6.7)

**Q45.** In Python, a variable is best described as: (a) a box of fixed type (b) a name tied to an object (c) a memory address you type (d) a keyword *(E · 6.7)*

**Answer.** (b) a name tied to an object. *Why:* the price-tag picture of section 6.7.

**Q46.** After `a = 5`, `b = a`, `a = 7`, the value of `b` is: (a) 5 (b) 7 (c) 12 (d) an error *(M · 6.7)*

**Answer.** (a) 5. *Why:* `a = 7` moves only the tag `a`.

**Q47.** `type(x)` gives the type of: (a) the name x (b) the object x is tied to (c) the line (d) the keyword *(M · 6.7)*

**Answer.** (b) the object x is tied to. *Why:* a name has no type of its own.

**Q48.** Which statement is an error? (a) `x = 10` (b) `x + 1 = 5` (c) `x = x + 1` (d) `x = y = 0` *(M · 6.7)*

**Answer.** (b) `x + 1 = 5`. *Why:* the left side of `=` must be a name, not an expression.

**Q49.** Python is: (a) statically typed (b) dynamically typed (c) untyped (d) weakly typed *(M · 6.7)*

**Answer.** (b) dynamically typed. *Why:* names have no fixed type; values are never mixed quietly (strongly typed).

## Comments (6.8)

**Q50.** A docstring is: (a) a comment starting with // (b) a triple-quoted note as the first statement of a program or function (c) any string (d) an error message *(M · 6.8)*

**Answer.** (b) a triple-quoted note as the first statement of a program or function. *Why:* it tells the user what the program does.

