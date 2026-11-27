# Good practice: PEP 8 for Class XI, and what a PEP is

*Chapter 6 · Good practice. The printed chapter names six conventions from PEP 8. Here are fifteen, each with a poor and a good example, and what a PEP is. Every example on this page is legal Python: style is about reading, not about running.*

## What is a PEP?

**PEP = Python Enhancement Proposal**: a numbered document that proposes a change to Python, or records a rule or a
decision. Anyone may write one; Python's core team accepts or rejects it. Two are famous:

- **PEP 8**: *Style Guide for Python Code*, the rules for writing Python that is easy to read.
- **PEP 20**: *The Zen of Python*, nineteen short sayings about good programs.

## Fifteen PEP 8 rules

| # | Rule | Poor | Good |
|:-:|---|---|---|
| 1 | Meaningful names | `tm = 450` | `total_marks = 450` |
| 2 | snake_case for variables | `TotalMarks = 450` | `total_marks = 450` |
| 3 | CAPITALS for constants | `pass_mark = 33` | `PASS_MARK = 33` |
| 4 | Never `l`, `O`, `I` as one-letter names | `l = 1` | `count = 1` |
| 5 | 4 spaces per indent level | `if True:`<br>&nbsp;&nbsp;`x = 1` | `if True:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`x = 1` |
| 6 | One statement per line | `a = 1; b = 2` | `a = 1`<br>`b = 2` |
| 7 | Spaces around `=` and operators | `total=a+b*2` | `total = a + b * 2` |
| 8 | No space inside brackets | `print( total )` | `print(total)` |
| 9 | A space after a comma | `print(a,b)` | `print(a, b)` |
| 10 | Lines of at most 79 characters | a line of more than 79 characters | `x = 1  # a short comment` |
| 11 | Comments: `# ` and a space, saying why | `x = x + 1 #add 1` | `x = x + 1  # one more student` |
| 12 | Blank lines to separate parts | `a = 1`<br>`print(a)`<br>`b = 2`<br>`print(b)` | `a = 1`<br>`print(a)`<br>&nbsp;<br>`b = 2`<br>`print(b)` |
| 13 | Names do not hide built-ins | `print = 5` | `points = 5` |
| 14 | Comparisons with `None` use `is` | `x = None`<br>`print(x == None)` | `x = None`<br>`print(x is None)` |
| 15 | No `\` where brackets will do | `total = 1 + \`<br>&nbsp;&nbsp;&nbsp;&nbsp;`2` | `total = (1 +`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`2)` |

## The Zen of Python (PEP 20)

Type `import this` in the shell. Python prints nineteen sayings; the first four are:

```text
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
```

## What the examiner looks for (practical exam)

The lab test is marked **60% logic, 20% documentation, 20% code quality**.

| Under | The examiner looks for |
|---|---|
| Documentation | a comment at the top (what the program does); comments that say **why**; clear prompts and output messages |
| Code quality | meaningful snake_case names; 4-space indents; one statement per line; no needless repetition |
