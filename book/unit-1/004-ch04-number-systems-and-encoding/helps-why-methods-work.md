# Helps you understand: why the methods work

*Chapter 4 · Helps you understand. The printed book shows each method and gives the reason in a "Why?" box; this page shows the reason step by step, with algebra you already know.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. Why does dividing give the digits?

Any whole number n, divided by the base b, gives a quotient q and a remainder r:

**n = q × b + r**, and r is always smaller than b, so r is one digit of base b.

- The part **q × b** is a whole number of "b's": it fills the places from the b's place leftwards.
- The part **r** is what is left over for the **units** place.

So the first remainder is the **units digit**. Now do the same with q: its remainder is the next digit, in the b's place,
and so on. That is why the remainders are read **upward**: the first one found is the last digit written.

Example: 45 = 22 × 2 + 1, so the units digit of 45 in binary is **1**. The whole ladder:

| Divide | Quotient | Remainder |
|:-:|:-:|:-:|
| 45 ÷ 2 | 22 | **1** |
| 22 ÷ 2 | 11 | **0** |
| 11 ÷ 2 | 5 | **1** |
| 5 ÷ 2 | 2 | **1** |
| 2 ÷ 2 | 1 | **0** |
| 1 ÷ 2 | 0 | **1** |

Read the remainders upward: (45)₁₀ = (101101)₂.

## 2. Why does multiplying give the fraction digits?

A fraction f in base b looks like 0.d₁d₂d₃…, which means f = d₁/b + d₂/b² + d₃/b³ + …

Multiply both sides by b: **f × b = d₁ + d₂/b + d₃/b² + …**

The whole-number part of f × b is exactly **d₁**, the first digit after the point. What is left over (the fraction part) is
0.d₂d₃…, so multiplying again gives d₂. The digits come out **in order**, nearest the point first: read **downward**.

| Fraction × 2 | Whole part (digit) | Fraction left |
|:-:|:-:|:-:|
| 0.8125 × 2 = 1.625 | **1** | 0.625 |
| 0.625 × 2 = 1.25 | **1** | 0.25 |
| 0.25 × 2 = 0.5 | **0** | 0.5 |
| 0.5 × 2 = 1 | **1** | 0 |

So (0.8125)₁₀ = (0.1101)₂. Check: ½ + ¼ + 1/16 = 0.8125. ✓

## 3. Which fractions end in binary, and which go on for ever?

A fraction ends in base b only if, written in its lowest terms, its denominator has **no prime factor other than those of b**.
For binary (b = 2) the denominator must be a power of 2: 2, 4, 8, 16 …

| Decimal | As a fraction | Denominator | In binary |
|:-:|:-:|:-:|---|
| 0.5 | 1/2 | 2 (a power of 2) | (0.1)₂, ends |
| 0.25 | 1/4 | 4 (a power of 2) | (0.01)₂, ends |
| 0.375 | 3/8 | 8 (a power of 2) | (0.011)₂, ends |
| 0.625 | 5/8 | 8 (a power of 2) | (0.101)₂, ends |
| 0.1 | 1/10 | 10 (has a factor 5) | (0.00011…)₂, repeats for ever |
| 0.2 | 1/5 | 5 (has a factor 5) | (0.0011…)₂, repeats for ever |
| 0.3 | 3/10 | 10 (has a factor 5) | (0.01001…)₂, repeats for ever |
| 0.75 | 3/4 | 4 (a power of 2) | (0.11)₂, ends |

This is why 0.1, a very ordinary decimal, cannot be stored exactly in a computer: its denominator 10 = 2 × 5 has a 5.

## 4. Why can we group bits for octal and hex, but not for decimal?

- 8 = 2³: one octal place is worth exactly three binary places. A group of 3 bits has 2³ = 8 patterns, one for each octal digit.
- 16 = 2⁴: one hex place is worth exactly four binary places; 4 bits have 16 patterns.
- 10 is **not** a power of 2: no whole number of bits matches one decimal digit (3 bits make 8 patterns, too few; 4 bits make
  16, too many). That is why decimal must go by division or place values.

| Base | A power of 2? | Method |
|:-:|:-:|---|
| 8 = 2³ | yes | group the bits in 3s |
| 16 = 2⁴ | yes | group the bits in 4s |
| 10 | no | divide, or use place values |
