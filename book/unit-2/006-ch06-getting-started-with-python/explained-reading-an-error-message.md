# Explained: Reading an error message

*Chapter 6 · Explained. The printed chapter says: look at the line number and the last line. Here is a whole error message, part by part, and the eight errors beginners meet first, each made by running Python.*

## A whole error message

```python
marks = 92
total = marks + bonus
print(total)
```

*Python prints:*

```text
Traceback (most recent call last):
  File "<string>", line 2, in <module>
NameError: name 'bonus' is not defined
```

| Part | What it tells you |
|---|---|
| `Traceback (most recent call last):` | "Here is where things went wrong", printed before every error |
| `File "<string>", line 2` | **the line number** (in IDLE you see your file name); go to that line first |
| the line itself, sometimes with `^` marks | the statement Python was running, and where |
| **the last line** | **the kind of error and its cause**: read this first |

## The first eight errors

| # | Program | The last line Python prints | Why | Correct it |
|:-:|---|---|---|---|
| 1 | `print("Hello"` | `SyntaxError: '(' was never closed` | a bracket opened but never closed | close the bracket: `print("Hello")` |
| 2 | `print "Hello"` | `SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?` | Python 2 style, without brackets | `print("Hello")` |
| 3 | `Print("Hello")` | `NameError: name 'Print' is not defined. Did you mean: 'print'?` | capital P: `Print` is not a known name | `print`, small letters |
| 4 | `print(totl)` | `NameError: name 'totl' is not defined` | a name used before it is given a value (often a spelling mistake) | spell it as created: `total` |
| 5 | `x = 5`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(x)` | `IndentationError: unexpected indent` | a line starts with spaces for no reason | start the line at the left edge |
| 6 | `print("Marks: " + 92)` | `TypeError: can only concatenate str (not "int") to str` | text and a number joined with `+` | `print("Marks:", 92)` |
| 7 | `print(10 / 0)` | `ZeroDivisionError: division by zero` | division by zero | check the divisor before dividing (Chapter 9) |
| 8 | `class = "XI-A"` | `SyntaxError: invalid syntax` | a keyword used as a name | another name: `section = "XI-A"` |

*Messages made by Python 3.12.7; other versions may word them a little differently.*

## Three habits

1. Read the **last line** first, then go to the **line number**.
2. Correct **one** error, save, run again: the next error may be a different one.
3. A `SyntaxError` stops the program **before** any line runs; most other errors stop it **at** the line, after the
   lines above have run. Chapter 8 explains why, and the three kinds of error (syntax, run-time, logical).
