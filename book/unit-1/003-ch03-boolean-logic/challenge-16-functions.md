# Challenge: all 16 gates of two inputs

*Chapter 3 · Challenge (beyond the syllabus). Not needed for the exam; for those who enjoy a puzzle.*

## The question

A gate with two inputs, A and B, has a truth table of **four rows** (00, 01, 10, 11). How many **different** gates of two inputs can there be? The book has shown you six (AND, OR, NAND, NOR, XOR, and XNOR online). Are there more?

## Think before you read on

The output column has four cells. Each cell can be 0 or 1, on its own. So the output column is itself a 4-digit pattern of 0s and 1s, and every different pattern is a different gate.

- 1 cell: 2 patterns. 2 cells: 4. 3 cells: 8. **4 cells: 2⁴ = 16 patterns.**
- This is the same doubling as the rows of a truth table (section 3.1), used one level up: the rows double with the inputs, and the gates double with the rows.

## All sixteen

Read each line across: the four outputs are for AB = 00, 01, 10, 11.

| No. | 00 | 01 | 10 | 11 | Name | Expression |
|:-:|:-:|:-:|:-:|:-:|---|:-:|
| 0 | 0 | 0 | 0 | 0 | Always 0 (FALSE) | 0 |
| 1 | 0 | 0 | 0 | 1 | AND | A·B |
| 2 | 0 | 0 | 1 | 0 | A but not B | A·B' |
| 3 | 0 | 0 | 1 | 1 | A (copy A, ignore B) | A |
| 4 | 0 | 1 | 0 | 0 | B but not A | A'·B |
| 5 | 0 | 1 | 0 | 1 | B (copy B, ignore A) | B |
| 6 | 0 | 1 | 1 | 0 | XOR | A ⊕ B |
| 7 | 0 | 1 | 1 | 1 | OR | A + B |
| 8 | 1 | 0 | 0 | 0 | NOR | (A + B)' |
| 9 | 1 | 0 | 0 | 1 | XNOR (same answer) | (A ⊕ B)' |
| 10 | 1 | 0 | 1 | 0 | NOT B | B' |
| 11 | 1 | 0 | 1 | 1 | A or not B | A + B' |
| 12 | 1 | 1 | 0 | 0 | NOT A | A' |
| 13 | 1 | 1 | 0 | 1 | not A, or B ("if A then B") | A' + B |
| 14 | 1 | 1 | 1 | 0 | NAND | (A·B)' |
| 15 | 1 | 1 | 1 | 1 | Always 1 (TRUE) | 1 |

## What to notice

- **The six gates of the book are all here**: AND (1), XOR (6), OR (7), NOR (8), NAND (14), and NOT, twice (10 and 12, each ignoring one input).
- **Each gate has a partner turned round**: number *n* and number 15 − *n* are opposites in every cell. AND (1) and NAND (14); OR (7) and NOR (8); XOR (6) and XNOR (9). That is why NAND and NOR exist: they are AND and OR "then *ulta*".
- **Two are not really gates**: 0 and 15 ignore both inputs.
- **NAND alone can build all sixteen** (and so can NOR alone): that is what "universal" means.

## Try it yourself

1. Which numbers in the table ignore input B completely? *Answer:* 0, 3, 12 and 15 (the output for 00 equals 01, and for 10 equals 11).
2. With **three** inputs the truth table has 8 rows. How many different 3-input gates are there? *Answer:* 2⁸ = **256**.
