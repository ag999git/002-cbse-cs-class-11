# Helps you understand: Statements over several lines

*Chapter 6 · Helps you understand. The printed chapter shows one statement written over two lines. Here are the two names for lines, both ways to continue a statement, and why `;` is poor style.*

## Physical and logical lines

- A **physical line** is a line you see on the screen, ending where you pressed Enter.
- A **logical line** is one whole statement, as Python reads it.

Usually they are the same. When a statement is long, one **logical** line may run over several **physical** lines.

## Way 1 (better): inside brackets

Python does not end a statement while a bracket `(`, `[` or `{` is still open.

```python
total = (90 + 85 + 78
         + 92 + 88)
print("Total:", total)
```

*Output:*

```text
Total: 433
```

## Way 2: a backslash at the very end of a line

```python
total = 90 + 85 + 78 \
        + 92 + 88
print("Total:", total)
```

Same output. The `\` must be the **last** character of the line (not even a space after it).

## What goes wrong without either

```python
total = 90 + 85
        + 78
```

```text
IndentationError: unexpected indent
```

The first line is a complete statement, so Python ends it there; the second line then starts with spaces for no reason.

## The opposite: several statements on one line

```python
a = 1; b = 2; print(a + b)
```

*Output:*

```text
3
```

Legal, but poor style (PEP 8): one statement per line is easier to read and to correct, because an error message gives
one line number.

| Basis of difference | Brackets | Backslash `\` | Semicolon `;` |
|---|---|---|---|
| What it does | one statement over several lines | one statement over several lines | several statements on one line |
| Style | preferred | allowed, easy to break | avoid |
