# Helps you understand: Python's story and versions

*Chapter 6 · Helps you understand. The printed chapter has a timeline of Python's life. Here is the story behind it, why old Python 2 programs fail today, and how to find your own version.*

## The story in short

| When | What happened |
|---|---|
| Dec 1989 | Guido van Rossum, a Dutch programmer, starts Python during the Christmas holidays as a hobby project |
| Feb 1991 | The first public release, version 0.9.0 |
| 1994 | Version 1.0 |
| 2000 | Python 2.0 |
| Dec 2008 | **Python 3.0**: a big clean-up; some old programs no longer run |
| 1 Jan 2020 | **Python 2 retired**: no more fixes, even for security |
| Oct 2024 | Python 3.13, with a new, coloured shell |
| Oct 2026 | **Python 3.15**, the latest at the time of this book |

**Where the ideas came from.** Python grew out of **ABC**, a teaching language Guido worked on in the 1980s: easy to
read, with indentation instead of brackets. It also borrowed ideas from **Modula-3**. The name comes from the British
comedy show *Monty Python's Flying Circus*, not from the snake.

## Python 2 vs Python 3: why an old program fails

Many old books and websites still show Python 2. The most visible difference is `print`. In Python 2 it was a
statement; in Python 3 it is a **function**, so it needs brackets.

```python
print "Hi"        # Python 2: no brackets
```

Python 3 refuses it at once:

```text
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

| Basis of difference | Python 2 (retired 2020) | Python 3 (today) |
|---|---|---|
| `print` | a statement: `print "Hi"` | a function: `print("Hi")` |
| `7 / 2` | `3` (whole-number division) | `3.5` (true division); `7 // 2` gives `3` |
| Text | ASCII by default | **Unicode** by default: `"नमस्ते"` works everywhere |
| Support | none since 1 Jan 2020 | new version every October |

*If a program from a book or website will not run, look first for `print` without brackets.*

## Which version do I have?

In a terminal (Command Prompt or PowerShell on Windows):

```text
python --version
```

Inside Python (the shell, a script or a Colab cell):

```python
import sys
print(sys.version)
```

On the computer that checked this page, it printed `3.12.7`. **This book needs Python 3.12 or later.** Every program in it
was run on 3.12; newer versions may word a few error messages slightly differently.

## Why the version numbers matter in the exam

They do not, except two facts: **Python 3** is the Python of the syllabus, and **Guido van Rossum** created it.
