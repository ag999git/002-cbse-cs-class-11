# Beyond syllabus: why 0.1 + 0.2 is not 0.3 in Python

*Chapter 4 · Beyond syllabus. The printed book shows that 0.1 repeats for ever in binary (section 4.4); this page shows what that does to a computer's arithmetic. Useful again in Chapter 7 (data types).*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. The surprise

Type this in Python (Chapter 6 onward):

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
```

Python is not broken. The reason is in section 4.4 of the book.

## 2. The reason: 0.1 never ends in binary

Multiply by 2 again and again (the book's method): 0.1 → 0.000110011001… The block **0011** repeats for ever, because the
denominator of 1/10 has the factor 5 (see "Why the methods work"). A computer has only a fixed number of bits, so it must
**cut 0.1 off**, and the number it stores is very slightly different from 0.1:

> 0.1 is stored as **0.1000000000000000055511151231257827021181583404541015625**

The same happens to 0.2 and to 0.3. When the slightly-wrong 0.1 and 0.2 are added, the tiny errors add up to a number
that is not the stored 0.3; Python shows it as 0.30000000000000004.

## 3. How a computer stores numbers with a point

Like scientific notation (6.02 × 10²³), but in binary: a **sign**, a **fraction** (the significant bits) and an
**exponent** (where the point goes). This is the international standard **IEEE 754**. Python's `float` uses 64 bits:

| Part | Bits | 0.1 in Python |
|---|:-:|---|
| sign | 1 | 0 (positive) |
| exponent | 11 | 01111111011 |
| fraction | 52 | 1001100110011001100110011001100110011001100110011010 |

Look at the fraction: **1001 1001 1001 …**, the repeating pattern of 0.1, cut off after 52 bits (the last bits are
rounded). A shorter 32-bit version (single precision) has 1 + 8 + 23 bits: 0 01111011 10011001100110011001101.

## 4. What to do about it in Python

| Need | Use | Example |
|---|---|---|
| show a few decimal places | `round(x, n)` | `round(0.1 + 0.2, 2)` gives 0.3 |
| compare two floats | `math.isclose(a, b)` | `math.isclose(0.1 + 0.2, 0.3)` gives True |
| exact money (rupees and paise) | whole paise, or the `decimal` module | store ₹10.50 as 1050 paise |
| exact fractions | the `fractions` module | `Fraction(1, 10)` |

**Rule of thumb:** never test two floats with `==`; never store money as a float.

## 5. Questions

**Q1.** Why can 0.5 + 0.25 be stored exactly, but not 0.1 + 0.2?

**Answer.** 0.5 = ½ and 0.25 = ¼ have denominators that are powers of 2, so they end in binary ((0.1)₂ and (0.01)₂);
0.1 and 0.2 have the factor 5 in their denominators and repeat for ever, so they are cut off.

**Q2.** Will `0.75 + 0.125 == 0.875` be True in Python?

**Answer.** True: all three end in binary (3/4, 1/8, 7/8), so they are stored exactly.
