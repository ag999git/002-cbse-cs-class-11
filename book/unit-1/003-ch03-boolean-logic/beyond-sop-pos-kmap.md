# Beyond syllabus: from a truth table back to an expression: SOP, POS and K-maps

*Chapter 3 · Beyond syllabus (Class XII and engineering). The printed book goes from an expression to its truth table; this page goes the other way.*

*Every table and answer on this page was computed by a program (`tools/boolean_pages.py`) and checked row by row.*

## 1. Minterms and maxterms

- A **minterm** is an AND of all the inputs, each primed or not, that is 1 in exactly **one** row: row 101 has the minterm A·B'·C.
- A **maxterm** is an OR of all the inputs that is 0 in exactly one row: row 101 has the maxterm (A' + B + C').
- **SOP** (sum of products): OR together the minterms of the rows where F = 1. **POS** (product of sums): AND together the maxterms of the rows where F = 0.
- Rows are numbered by counting in binary: 000 is row 0, 101 is row 5. F = Σ(1, 3) means F = 1 in rows 1 and 3.

## 2. The Karnaugh map (K-map)

A K-map is the truth table drawn as a grid, with the columns in the order 00, 01, **11**, 10 so that neighbours differ in one input only. Circle groups of 1s (sizes 1, 2, 4, 8; they may wrap round the edges); each group becomes one short product term, because the input that changes inside the group drops out.

### Example 1: F = 1 in rows 1, 3, 5, 7

**Canonical SOP** (one minterm for each 1): F = A'·B'·C + A'·B·C + A·B'·C + A·B·C

**Canonical POS** (one maxterm for each 0): F = (A + B + C)·(A + B' + C)·(A' + B + C)·(A' + B' + C)

**K-map:**

| A \ BC | 00 | 01 | 11 | 10 |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | **1** | **1** | 0 |
| 1 | 0 | **1** | **1** | 0 |

**Minimal SOP** (largest groups of 1s): **F = C**

### Example 2: F = 1 in rows 0, 1, 2, 6

**Canonical SOP** (one minterm for each 1): F = A'·B'·C' + A'·B'·C + A'·B·C' + A·B·C'

**Canonical POS** (one maxterm for each 0): F = (A + B' + C')·(A' + B + C)·(A' + B + C')·(A' + B' + C')

**K-map:**

| A \ BC | 00 | 01 | 11 | 10 |
|:-:|:-:|:-:|:-:|:-:|
| 0 | **1** | **1** | 0 | **1** |
| 1 | 0 | 0 | 0 | **1** |

**Minimal SOP** (largest groups of 1s): **F = A'·B' + B·C'**

## 3. Practice (answers computed)

**Q1.** F(A, B, C) = Σ(3, 5). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B·C + A·B'·C. Minimal: **A'·B·C + A·B'·C**.

**Q2.** F(A, B, C) = Σ(1, 4, 6). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C + A·B'·C' + A·B·C'. Minimal: **A'·B'·C + A·C'**.

**Q3.** F(A, B, C) = Σ(1, 3, 5, 6). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C + A'·B·C + A·B'·C + A·B·C'. Minimal: **A'·C + A·B·C' + B'·C**.

**Q4.** F(A, B, C) = Σ(4, 7). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A·B'·C' + A·B·C. Minimal: **A·B'·C' + A·B·C**.

**Q5.** F(A, B, C) = Σ(1, 5). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C + A·B'·C. Minimal: **B'·C**.

**Q6.** F(A, B, C) = Σ(0, 2, 3, 6, 7). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C' + A'·B·C' + A'·B·C + A·B·C' + A·B·C. Minimal: **A'·C' + B**.

**Q7.** F(A, B, C) = Σ(0, 1, 2, 6). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C' + A'·B'·C + A'·B·C' + A·B·C'. Minimal: **A'·B' + B·C'**.

**Q8.** F(A, B, C) = Σ(1, 2, 4). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C + A'·B·C' + A·B'·C'. Minimal: **A'·B'·C + A'·B·C' + A·B'·C'**.

**Q9.** F(A, B, C) = Σ(1, 4, 5, 7). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C + A·B'·C' + A·B'·C + A·B·C. Minimal: **A·B' + A·C + B'·C**.

**Q10.** F(A, B, C) = Σ(0, 3, 5, 6). Write the canonical SOP and the minimal SOP.

**Answer.** Canonical: A'·B'·C' + A'·B·C + A·B'·C + A·B·C'. Minimal: **A'·B'·C' + A'·B·C + A·B'·C + A·B·C'**.
