# Compare: Strong and weak typing

*Chapter 6 · Compare. The printed chapter says that Python is strongly typed and JavaScript, the language of web pages, is weakly typed. Here are the same lines in both, run in Python and in Node.js (a program that runs JavaScript).*

## Two different questions

- **Static or dynamic?** *When* are types checked: before the program runs (static: Java, C, C++) or while it runs (dynamic: Python, JavaScript)? See [Python and Java, step by step](compare-python-and-java.md).
- **Strong or weak?** *What happens when two types meet*, as in `"5" + 3`? A strongly typed language refuses to mix them quietly; a weakly typed language converts one of them for you and goes on.

The two questions are independent. Python is **dynamic and strong**. JavaScript is **dynamic and weak**.

## The same lines in Python and JavaScript

| Line | Python | JavaScript | What JavaScript did |
|---|---|---|---|
| `"5" + 3` | `TypeError: can only concatenate str (not "int") to str` | `"53"` | turned 3 into the text "3" and joined |
| `"5" - 3` | `TypeError: unsupported operand type(s) for -: 'str' and 'int'` | `2` | turned "5" into the number 5 and subtracted |
| `"5" == 5` | `False` | `true` | compared after turning "5" into a number |

JavaScript guessed differently each time: `+` turned the number into text, `-` turned the text into a number. Such guesses are behind many bugs on web pages: a form field holds the text "5", and adding 3 gives "53".

**Python makes you say what you mean:**

```python
print(int("5") + 3)     # the number 8
print("5" + str(3))     # the text "53"
```

Output:

```text
8
53
```

## Where Java stands

Java is **static and strong**, with one well-known exception: its `+` joins text with anything, so `"5" + 3` gives `53` in Java too (compiled and run). But `"5" - 3` is refused by the Java compiler (`error: bad operand types for binary operator '-'`), as in Python.

| Language | Types checked | Mixes types quietly? | In short |
|---|---|---|---|
| Python | while running | no | dynamic and strong |
| JavaScript | while running | yes | dynamic and weak |
| Java | before running (compiler) | no (except `+` with text) | static and strong |

**Exam point.** "Python is weakly typed" is wrong. Python is **dynamically** typed (a name has no type) and **strongly** typed (values are never mixed quietly).

[Back to Chapter 6](index.md)
