# Sometimes asked: duality, tautology and fallacy

*Chapter 3 · Sometimes asked. The printed book (section 3.7) gives the definitions; this page gives more practice.*

*Every table and answer on this page was computed by a program (`tools/boolean_pages.py`) and checked row by row.*

- **Dual:** swap + with ·, and 0 with 1. Letters and primes stay as they are. If a law is true, its dual is also true.
- **Tautology:** 1 in every row (A + A'). **Fallacy:** 0 in every row (A·A').
- **Dual is not complement:** the complement also primes every letter.

## Duals

**Q1.** Write the dual of C' + C·Y.

**Answer.** C'·(C + Y)

**Q2.** Write the dual of B' + B·C.

**Answer.** B'·(B + C)

**Q3.** Write the dual of X·1 + B·0.

**Answer.** (X + 0)·(B + 1)

**Q4.** Write the dual of B' + B·A.

**Answer.** B'·(B + A)

**Q5.** Write the dual of (B + 0)·X.

**Answer.** B·1 + X

**Q6.** Write the dual of X·1 + A·0.

**Answer.** (X + 0)·(A + 1)

**Q7.** Write the dual of B' + B·Y.

**Answer.** B'·(B + Y)

**Q8.** Write the dual of A + X·Y.

**Answer.** A·(X + Y)

**Q9.** Write the dual of C·B' + 1.

**Answer.** (C + B')·0

**Q10.** Write the dual of B·1 + A·0.

**Answer.** (B + 0)·(A + 1)

## Tautology, fallacy or neither?

**Q11.** Is A + A' a tautology, a fallacy, or neither?

**Answer.** It is a tautology (1 in every row).

**Q12.** Is A·A' a tautology, a fallacy, or neither?

**Answer.** It is a fallacy (0 in every row).

**Q13.** Is A + 1 a tautology, a fallacy, or neither?

**Answer.** It is a tautology (1 in every row).

**Q14.** Is A·0 a tautology, a fallacy, or neither?

**Answer.** It is a fallacy (0 in every row).

**Q15.** Is A + A'·B a tautology, a fallacy, or neither?

**Answer.** It is neither (it is 0 in some rows and 1 in others).

**Q16.** Is (A + B)·(A' + B)' a tautology, a fallacy, or neither?

**Answer.** It is neither (it is 0 in some rows and 1 in others).

**Q17.** Is A·B + A·B' + A' a tautology, a fallacy, or neither?

**Answer.** It is a tautology (1 in every row).

**Q18.** Is A·(A' + B)·B' a tautology, a fallacy, or neither?

**Answer.** It is a fallacy (0 in every row).

**Q19.** Is A + B a tautology, a fallacy, or neither?

**Answer.** It is neither (it is 0 in some rows and 1 in others).

**Q20.** Is (A·A')' a tautology, a fallacy, or neither?

**Answer.** It is a tautology (1 in every row).
