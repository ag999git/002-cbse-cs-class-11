# Good practice: Notes for people

*Chapter 6 · Good practice. The printed chapter shows two ways to write a note over several lines. Here are comments that help, docstrings, and triple quotes used for a string you keep and print.*

## Comments that help

| Program part | A comment that helps |
|---|---|
| The top of every program | what it does, for whom, and the date: `# Total and grade for one student; Asha, Class XI-A` |
| A line whose reason is not obvious | `# 22/7 because the question asks for it, not math.pi` |
| A value with a meaning | `PASS_MARK = 33  # CBSE pass mark, out of 100` |
| A part of a long program | `# --- read the marks ---`, `# --- print the result ---` |

| Avoid | Because |
|---|---|
| `x = x + 1  # add 1 to x` | it repeats the code |
| a comment on every line | the useful ones get lost |
| a comment that is no longer true | worse than none: change it with the code |

## Docstrings

A triple-quoted note as the **first statement** of a program is its **docstring**: a description for **users**.
Python keeps it, and other tools can show it:

```python
"""Report card: reads marks, prints the total.
Class XI-A, Term 1."""
print(__doc__.splitlines()[0])
```

*Output:*

```text
Report card: reads marks, prints the total.
```

In Class XII you will write a docstring as the first line of every function.

## Triple quotes for a string you keep

The same triple quotes can make a **string over several lines** that you store in a name and print. This is not a
note: the string is kept and used.

```python
s = """Line 1
Line 2
Line 3"""
print(s)
print(len(s))
```

*Output:*

```text
Line 1
Line 2
Line 3
20
```

The length is 20: 18 letters, digits and spaces, plus 2 new-line characters (one for each Enter inside the quotes).
Chapter 11 (Strings) uses these strings.

| Basis of difference | A triple-quoted **note** | A triple-quoted **string** |
|---|---|---|
| Written | on its own line | after `=`, or inside `print(...)` |
| Python | makes the string, then throws it away | keeps it under a name |
| Used for | notes and docstrings | text over several lines: addresses, poems, menus |
