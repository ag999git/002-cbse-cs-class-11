# Helps you understand: All 35 keywords

*Chapter 6 · Helps you understand. The printed chapter groups the 35 keywords by purpose. Here is each one with a one-line meaning, a tiny example and the chapter where you meet it. You do not need to learn them all now.*

| Keyword | What it does | Tiny example | Chapter |
|---|---|---|:-:|
| `False` | the Boolean value "no" | `passed = False` | 7 |
| `None` | "no value yet" | `result = None` | 7 |
| `True` | the Boolean value "yes" | `ready = True` | 7 |
| `and` | both must be true | `age >= 18 and has_id` | 7 |
| `as` | a second name, in imports | `import math as m` | 15 |
| `assert` | stop if a condition is false (a check) | `assert marks <= 100` | Class XII |
| `async` | starts a task that can wait (advanced) | (not in school Python) | beyond |
| `await` | waits for such a task (advanced) | (not in school Python) | beyond |
| `break` | leave a loop at once | `break` | 10 |
| `class` | defines a new kind of object (not in the syllabus) | (not in your syllabus) | beyond |
| `continue` | skip to the next turn of a loop | `continue` | 10 |
| `def` | defines a function | `def area(r):` | Class XII |
| `del` | deletes a name or an item | `del marks[0]` | 12 |
| `elif` | "else if": another test | `elif marks >= 60:` | 9 |
| `else` | what to do otherwise | `else:` | 9 |
| `except` | what to do when an error happens | `except ValueError:` | Class XII |
| `finally` | runs at the end, error or not | `finally:` | Class XII |
| `for` | repeat for each item | `for i in range(5):` | 10 |
| `from` | take something from a module | `from math import pi` | 15 |
| `global` | use a name from outside a function | `global count` | Class XII |
| `if` | test a condition | `if marks >= 33:` | 9 |
| `import` | bring in a module | `import math` | 15 |
| `in` | is it a member? / each item of | `'a' in 'cat'` | 7, 10 |
| `is` | the same object? | `x is None` | 7 |
| `lambda` | a one-line function without a name | `lambda x: x * 2` | Class XII |
| `nonlocal` | use a name from the enclosing function | `nonlocal total` | beyond |
| `not` | the opposite | `not passed` | 7 |
| `or` | at least one must be true | `rain or homework` | 7 |
| `pass` | do nothing (a placeholder) | `pass` | 9 |
| `raise` | cause an error on purpose | `raise ValueError` | Class XII |
| `return` | give a value back from a function | `return area` | Class XII |
| `try` | try something that may fail | `try:` | Class XII |
| `while` | repeat while a condition is true | `while n > 0:` | 10 |
| `with` | open something and close it safely | `with open("a.txt") as f:` | Class XII |
| `yield` | give values one at a time (advanced) | (advanced) | beyond |

*The list is Python's own (`keyword.kwlist`, Python 3.12.7), sorted as Python sorts it: capital letters come before small
ones.*

## Why do `True`, `False` and `None` begin with a capital?

They are **values**, not instructions, and Python's makers gave the three built-in values capital first letters, as
names of special things often have in English. So `true` and `none` are ordinary names you may use (but should not),
while `True` and `None` are keywords.

## Soft keywords: not in your syllabus

Newer Pythons also have a few **soft keywords** (`_`, `case`, `match`, `type`): words that act as keywords only in one special
statement and are ordinary names everywhere else. They are not in your syllabus, and older books do not list them; if
you see them, you can ignore them.
