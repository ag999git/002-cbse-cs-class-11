# Sometimes asked: Literals up close

*Chapter 6 · Sometimes asked. The printed chapter lists the kinds of literal in one table; Chapter 7 studies each kind. Here are the details some papers ask: escape sequences, the size of a string, other ways to write numbers, and 30 "valid or invalid?" drills, every answer decided by Python.*

## Escape sequences: characters you cannot type directly inside quotes

| Sequence | Means |
|:-:|---|
| `\n` | new line |
| `\t` | tab (a jump to the next column) |
| `\\` | one backslash |
| `\'` | a single quote inside '...' |
| `\"` | a double quote inside "..." |

```python
print("Name:\tAsha\nClass:\tXI")
```

*Output:*

```text
Name:	Asha
Class:	XI
```

**An escape sequence is one character**, though you type two. So:

| String | `len()` | Why |
|---|:-:|---|
| `"ab\nc"` | 4 | a, b, new line, c |
| `"Asha\'s"` | 6 | the escape counts as one character |
| `"C:\\temp"` | 7 | C, :, one backslash, t, e, m, p |
| `"\t5"` | 2 | tab, 5 |
| `"""Hi↵All"""` | 6 | H, i, new line, A, l, l: the Enter inside triple quotes is a new-line character |

## Numbers written other ways

| Kind | Written as | Value |
|---|---|---|
| int | `0b101` | `5` |
| int | `0o17` | `15` |
| int | `0x1F` | `31` |
| float | `2.5e3` | `2500.0` |
| float | `1e-3` | `0.001` |
| int | `1_000_000` | `1000000` |
| complex | `2+3j` | `(2+3j)` |

`0b` = binary, `0o` = octal, `0x` = hexadecimal (Chapter 4); `e` = "times ten to the power"; `_` only for reading
(one million); `j` marks the imaginary part of a complex number.

## 30 drills: valid or invalid? what type?

*Cover the answer column, decide, then check. Every answer was made by Python.*

| # | Literal | Answer | Why |
|:-:|---|---|---|
| 1 | `25` | **int** | value 25 |
| 2 | `-7` | **int** | value -7; strictly, `-` is an operator in front of the literal 7 |
| 3 | `0b101` | **int** | value 5 |
| 4 | `0o17` | **int** | value 15 |
| 5 | `0o28` | **invalid** | 8 is not an octal digit (only 0–7) |
| 6 | `0x1F` | **int** | value 31 |
| 7 | `0xG1` | **invalid** | G is not a hexadecimal digit (only 0–9, A–F) |
| 8 | `3.14` | **float** | value 3.14 |
| 9 | `.5` | **float** | value 0.5 |
| 10 | `7.` | **float** | value 7.0 |
| 11 | `2.5e3` | **float** | value 2500.0 |
| 12 | `1.7E` | **invalid** | no digits after E |
| 13 | `0.17E2.3` | **invalid** | the power after E must be a whole number |
| 14 | `1,234` | **a tuple, not a number** | the comma makes two values: (1, 234) |
| 15 | `17,225E02` | **a tuple, not a number** | the comma makes two values: (17, 22500.0) |
| 16 | `"Pass"` | **str** | value 'Pass' |
| 17 | `'A'` | **str** | value 'A' |
| 18 | `"Asha's"` | **str** | value "Asha's" |
| 19 | `'Hi"` | **invalid** | the opening and closing quotes are different |
| 20 | `"""Hi"""` | **str** | value 'Hi' |
| 21 | `True` | **bool** | value True |
| 22 | `true` | **a name, not a literal** | Python looks for a variable of this name |
| 23 | `None` | **NoneType (the special literal)** | value None |
| 24 | `2+3j` | **complex** | value (2+3j) |
| 25 | `1_000_000` | **int** | value 1000000 |
| 26 | `012` | **invalid** | a whole number may not begin with 0 |
| 27 | `00` | **int** | value 0 |
| 28 | `1e-3` | **float** | value 0.001 |
| 29 | `"5"` | **str** | value '5' |
| 30 | `5.0` | **float** | value 5.0 |

**Two traps from the drills.** `012` is invalid in Python 3 (a leading zero is not allowed, except for zero itself:
old Python 2 read it as octal). And `1,234` is legal but is **two** numbers in a tuple, not one thousand two hundred and
thirty-four.
