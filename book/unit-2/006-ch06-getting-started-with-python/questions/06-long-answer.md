# Chapter 6: Getting Started with Python: Long-answer questions (12)

*Chapter 6 · Questions (online). Four or five marks each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Long answers

**Q1.** Explain five features of Python, and what each means for a student. *(M · 6.1)*

**Answer.** (1) **Easy to read:** short, English-like statements: fewer lines, fewer mistakes. (2) **Interpreted:** one statement at a time: try a line and see the answer at once. (3) **Free and open source:** nothing to buy; the source code is open. (4) **Cross-platform:** the same program runs at school (Windows) and at home (Linux, macOS). (5) **Dynamically typed:** no declarations: `marks = 92` is enough. (Also: large standard library, case-sensitive, used everywhere.)

**Q2.** Compare interactive mode and script mode in five points, with an example of each. *(M · 6.3)*

**Answer.** | Basis | Interactive mode | Script mode |
|---|---|---|
| Where | the shell, after `>>>` | the editor, a `.py` file |
| Runs | one statement at a time, at once | the whole file, line 1 to the end |
| Saved? | no | yes |
| Bare expression `7 + 5` | value shown | nothing shown |
| Best for | trying a statement, quick sums | programs of more than a few lines |

Example: `>>> 2 ** 10` shows 1024 in the shell; a script needs `print(2 ** 10)`.

**Q3.** Describe five places to write Python: where the code runs, whether it needs installing, and what each is best for. *(M · 6.2)*

**Answer.** IDLE: your computer; comes with Python; learning and the exam. Thonny: your computer; install; beginners (shows values). VS Code: your computer; install + Python extension; bigger projects. Jupyter: a server on your own computer, shown in the browser; install; notebooks without the internet. Google Colab: Google's computers (cloud); no install, needs a sign-in and the internet; practice anywhere.

**Q4.** Cut `area = 3.14 * r * r  # circle` into tokens. Name the kind of each, and say what happens to the comment. *(M · 6.4)*

**Answer.** 7 tokens: `area` identifier, `=` operator, `3.14` literal, `*` operator, `r` identifier, `*` operator, `r` identifier. `# circle` is a comment: Python skips it before making tokens, so it is not a token.

**Q5.** State the rules for identifiers and two conventions. Then classify: `studentName`, `student_name`, `2ndTerm`, `term_2`, `MAX`, `for`, `For`, `total$`. *(M · 6.5)*

**Answer.** Rules: begin with a letter or `_`; then only letters, digits, `_`; not a keyword; case-sensitive; any length. Conventions: snake_case; CAPITALS for constants. Valid: `student_name`, `term_2`, `For`, `studentName` (legal, but camelCase), `MAX` (a constant). Invalid: `2ndTerm` (digit first), `total$` (`$`), `for` (keyword).

**Q6.** Explain the kinds of literal with examples, and show their types with a program. *(M · 6.6)*

```python
for v in [33, 3.5, "33", True, None, 2+3j]:
    print(repr(v), type(v))
```


**Answer.** String (`"33"`), integer (`33`), floating point (`3.5`), Boolean (`True`), complex (`2+3j`) and the special literal `None`. Output:

```text
33 <class 'int'>
3.5 <class 'float'>
'33' <class 'str'>
True <class 'bool'>
None <class 'NoneType'>
(2+3j) <class 'complex'>
```
Each value carries its own type; `type()` reports it.

**Q7.** Explain, with the price-tag picture and a program, how variables work in Python. *(H · 6.7)*

```python
marks = 92
total = marks
print(id(marks) == id(total))
marks = 95
print(marks, total, id(marks) == id(total))
```


**Answer.** A variable is a tag tied to an object. `total = marks` ties a second tag to the same object (`id` equal: True). `marks = 95` makes a new object and moves only the tag `marks`; `total` stays on 92. Output:

```text
True
95 92 False
```


**Q8.** Compare static and dynamic typing in a table of four points, using the box and the tag. *(H · 6.7)*

**Answer.** | Basis | Static (C++, Java) | Dynamic (Python) |
|---|---|---|
| A variable is | a box with a type | a tag on an object |
| Declaration | needed: `int marks;` | none |
| Checked | before running | while running |
| Another type later? | no | yes: `marks = "A+"` |

Python is still strongly typed: `"5" + 3` is a TypeError.

**Q9.** Explain L-value and R-value. Why are `5 = x` and `x + 1 = 5` errors, but `x = x + 1` is correct? *(M · 6.7)*

**Answer.** The L-value (left of `=`) says WHERE the result goes: a name. The R-value (right) says WHAT the value is: anything that gives a value. `5 = x` and `x + 1 = 5` have a literal and an expression on the left: nothing can be tied to them. `x = x + 1` works out x + 1 (R-value), then ties the name x (L-value) to it.

**Q10.** Write a documented program for a bill: 3 notebooks at ₹45 each and 2 pens at ₹10 each. Use constants for the prices. *(M · 6.7, 6.8)*

**Answer.** 

```python
# Shopping bill: 3 notebooks and 2 pens
NOTEBOOK_PRICE = 45   # rupees each
PEN_PRICE = 10
notebooks = 3
pens = 2
total = notebooks * NOTEBOOK_PRICE + pens * PEN_PRICE
print("Total bill:", total, "rupees")
```
Output:

```text
Total bill: 155 rupees
```
Constants in capitals, snake_case names, a comment at the top and one saying what the numbers mean.

**Q11.** Rotate three values so that a gets b's value, b gets c's and c gets a's: (i) with a third variable, (ii) in one line. Then rotate them back. *(H · 6.7)*

**Answer.** 

```python
a, b, c = 1, 2, 3
t = a      # with a third variable
a = b
b = c
c = t
print(a, b, c)
a, b, c = c, a, b   # back again, in one line
print(a, b, c)
```
Output:

```text
2 3 1
1 2 3
```
In (ii) the whole right side is worked out first, so no value is lost.

**Q12.** Explain the two kinds of note in Python with an example of each, and write a short documented program. *(M · 6.8)*

**Answer.** `#` comments (to the end of the line, for readers of the code) and a triple-quoted docstring at the top (for users).

```python
"""Average of three test marks.
Asha, Class XI-A."""
MAX_MARKS = 25          # each test is out of 25
t1, t2, t3 = 20, 18, 22
average = (t1 + t2 + t3) / 3   # a plain average, no weights
print("Average:", round(average, 2), "out of", MAX_MARKS)
```
Output:

```text
Average: 20.0 out of 25
```


