# Revise: Chapter 6 cheat sheet

*Chapter 6 · Revise. The whole chapter on one A4 page, to print and keep. Every example on it was run in Python.*

[Download the printable A4 sheet (PDF)](../../assets/cheatsheets/ch06-cheat-sheet.pdf){ .md-button .md-button--primary }

## Running Python

**Shell** (interactive): `>>>` one statement, answered at once; not saved.

**Script**: File → New File, save as `name.py`, **F5** (Run Module); output in the shell.

```python
print("Hello", 11)
```

*Output:* `Hello 11`

In a script a bare `7 + 5` shows nothing; the shell and the last line of a Colab cell show it.

Read an error message: the **last line** first, then the line number.

## Interactive or script?

| Kind | Examples |
|---|---|
| Where | the shell, after `>>>` · the editor, a `.py` file |
| Runs | one statement at once · the whole file |
| Saved? | no · yes |
| <code>7 + 5</code> | value shown · nothing (use `print`) |
| Best for | trying a line · programs |

## Expression or statement?

An **expression** gives a value: `7 + 5`, `price * 2`, `marks >= 33`.

A **statement** does something: `total = price * 2`, `import math`, `pass`.

Long statement: continue it inside brackets `( )`; avoid `;` between statements.

## Tokens: the five kinds

| Kind | Examples |
|---|---|
| keyword | `if` `for` `True` `and` |
| identifier | `marks` `print` |
| literal | `33` `"Pass"` `2.5e3` |
| operator | `+ >= = //` |
| punctuator | `( ) [ ] , : .` |

A comment is **not** a token: Python skips it. `if marks >= 33: print("Pass")` has 9 tokens.

## The 35 keywords

`and` `as` `assert` `async` `await` `break` `class` `continue` `def` `del` `elif` `else` `except` `False` `finally` `for` `from` `global` `if` `import` `in` `is` `lambda` `None` `nonlocal` `not` `or` `pass` `raise` `return` `True` `try` `while` `with` `yield`

Only `True`, `False`, `None` begin with a capital. `print` is **not** a keyword.

## Names (identifiers)

**Rules** (else an error): begin with a letter or `_`; then letters, digits, `_` only (no space, `$ - . @`); not a keyword; case counts; any length.

**Conventions** (PEP 8): `total_marks` (snake_case); `PASS_MARK` for constants; never `l O I` alone; 4 spaces per indent.

## Literals

```python
print(type(33), type("33"))
```

*Output:* `<class 'int'> <class 'str'>`

```python
print(type(3.5), type(None))
```

*Output:* `<class 'float'> <class 'NoneType'>`

```python
print(0b101, 0o17, 0x1F, 2.5e3)
```

*Output:* `5 15 31 2500.0`

```python
print(len("a\tb\n"))
```

*Output:* `4`

`\n` new line, `\t` tab: one character each.

## Variables: a name tied to an object

```python
x = 3
y = x
x = x + 2
print(x, y)
```

*Output:* `5 3`

```python
a = b = 0
x, y = 5, 7
x, y = y, x
print(a, b, x, y)
```

*Output:* `0 0 7 5`

```python
n = 5
n = "five"
print(type(n))
```

*Output:* `<class 'str'>`

**L-value** (left of `=`): a name. **R-value**: anything that gives a value. `=` means "becomes", not "equals". Dynamic typing: the **object** has the type.

## Comments and notes

```python
# a note for people
print("ok")  # an inline comment
```

*Output:* `ok`

Several lines: `#` on each, or `"""` … `"""` (a docstring at the top).

## First errors

| Program | Python says |
|---|---|
| `Print("Hi")` | `NameError: name 'Print' is not defined. Did you mean: 'print'?` |
| `print("Hi"` | `SyntaxError: '(' was never closed` |
| `x = 5`<br>`y = 6` | `IndentationError: unexpected indent` |
| `class = 5` | `SyntaxError: invalid syntax` |
| `print("A" + 1)` | `TypeError: can only concatenate str (not "int") to str` |

