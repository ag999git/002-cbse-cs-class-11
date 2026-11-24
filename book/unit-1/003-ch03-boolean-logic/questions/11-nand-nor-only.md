# Chapter 3: circuits with NAND gates only, or NOR gates only (20 questions)

*Chapter 3 · Questions (online). Universal gates in practice (section 3.3). Every answer was computed by a program and checked: it gives the same truth table as the original expression.*

**Method.** A sum of products (A·B + C·D) becomes **NAND-NAND**: F = ((A·B)'·(C·D)')'. A product of sums ((A + B)·(C + D)) becomes **NOR-NOR**: F = ((A + B)' + (C + D)')'. Both follow from De Morgan's laws. In each answer, every prime closes one gate.

## NAND only

**Q1.** Write F = A'·B' + A·C' using only NAND gates.

**Answer.** F = (((A·A)'·(B·B)')'·(A·(C·C)')')'. (6 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q2.** Write F = A·C' + B'·C using only NAND gates.

**Answer.** F = ((A·(C·C)')'·((B·B)'·C)')'. (5 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q3.** Write F = B·C' + B·C + A·C using only NAND gates.

**Answer.** F = ((B·(C·C)')'·(B·C)'·(A·C)')'. (5 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q4.** Write F = A'·C + A·B + A·C using only NAND gates.

**Answer.** F = (((A·A)'·C)'·(A·B)'·(A·C)')'. (5 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q5.** Write F = A'·B + A·B' + A·B using only NAND gates.

**Answer.** F = (((A·A)'·B)'·(A·(B·B)')'·(A·B)')'. (6 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q6.** Write F = A·B' + A'·B + B·C using only NAND gates.

**Answer.** F = ((A·(B·B)')'·((A·A)'·B)'·(B·C)')'. (6 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q7.** Write F = B·C' + A'·B' using only NAND gates.

**Answer.** F = ((B·(C·C)')'·((A·A)'·(B·B)')')'. (6 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q8.** Write F = B·C + A·C using only NAND gates.

**Answer.** F = ((B·C)'·(A·C)')'. (3 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q9.** Write F = B'·C + B·C' + A·C using only NAND gates.

**Answer.** F = (((B·B)'·C)'·(B·(C·C)')'·(A·C)')'. (6 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

**Q10.** Write F = A·C' + A·B using only NAND gates.

**Answer.** F = ((A·(C·C)')'·(A·B)')'. (4 NAND gates: each AND becomes a NAND, the OR becomes a NAND (De Morgan), and a primed letter X' is a NAND with both inputs X.)

## NOR only

**Q11.** Write F = (A' + C)·(A + B)·(A + B') using only NOR gates.

**Answer.** F = (((A + A)' + C)' + (A + B)' + (A + (B + B)')')'. (6 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q12.** Write F = (B' + C')·(A' + C)·(A' + B) using only NOR gates.

**Answer.** F = (((B + B)' + (C + C)')' + ((A + A)' + C)' + ((A + A)' + B)')'. (8 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q13.** Write F = (A' + C')·(B + C) using only NOR gates.

**Answer.** F = (((A + A)' + (C + C)')' + (B + C)')'. (5 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q14.** Write F = (A + B)·(A + C) using only NOR gates.

**Answer.** F = ((A + B)' + (A + C)')'. (3 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q15.** Write F = (A + B)·(A + C)·(B + C) using only NOR gates.

**Answer.** F = ((A + B)' + (A + C)' + (B + C)')'. (4 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q16.** Write F = (A + B)·(B + C)·(A' + C) using only NOR gates.

**Answer.** F = ((A + B)' + (B + C)' + ((A + A)' + C)')'. (5 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q17.** Write F = (B' + C')·(A' + C) using only NOR gates.

**Answer.** F = (((B + B)' + (C + C)')' + ((A + A)' + C)')'. (6 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q18.** Write F = (A' + B')·(A + C) using only NOR gates.

**Answer.** F = (((A + A)' + (B + B)')' + (A + C)')'. (5 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q19.** Write F = (A + B)·(A' + B') using only NOR gates.

**Answer.** F = ((A + B)' + ((A + A)' + (B + B)')')'. (5 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)

**Q20.** Write F = (A + B')·(A' + B')·(A + C) using only NOR gates.

**Answer.** F = ((A + (B + B)')' + ((A + A)' + (B + B)')' + (A + C)')'. (7 NOR gates: each OR becomes a NOR, the AND becomes a NOR (De Morgan), and a primed letter X' is a NOR with both inputs X.)
