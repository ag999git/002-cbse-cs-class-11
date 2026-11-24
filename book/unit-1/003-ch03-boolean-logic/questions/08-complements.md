# Chapter 3: finding the complement (40 questions)

*Chapter 3 · Questions (online). Every expression here was generated and every answer computed by a program (`tools/boolean_bank.py`), then checked against the truth table, so the answers cannot contain slips. Try each question on paper before you read the answer below it.*


**Method** (section 3.6 of the book): prime the whole expression; open each bracket with De Morgan (+ becomes ·, · becomes +, every term gets a prime); remove double primes; stop when primes sit only on letters.

**Q1.** Find the complement of F = A·B + A·B'.

**Answer.** F' = (A·B + A·B')'<br>= (A·B)'·(A·B')'<br>= (A' + B')·(A' + B)

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q2.** Find the complement of F = A'·B·C' + A·C' + A'·D.

**Answer.** F' = (A'·B·C' + A·C' + A'·D)'<br>= (A'·B·C')'·(A·C')'·(A'·D)'<br>= (A + B' + C)·(A' + C)·(A + D')

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q3.** Find the complement of F = B·D' + C·D'.

**Answer.** F' = (B·D' + C·D')'<br>= (B·D')'·(C·D')'<br>= (B' + D)·(C' + D)

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q4.** Find the complement of F = A·C + A·B'.

**Answer.** F' = (A·C + A·B')'<br>= (A·C)'·(A·B')'<br>= (A' + C')·(A' + B)

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q5.** Find the complement of F = C·D + B'·C·D' + C·D'.

**Answer.** F' = (C·D + B'·C·D' + C·D')'<br>= (C·D)'·(B'·C·D')'·(C·D')'<br>= (C' + D')·(B + C' + D)·(C' + D)

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q6.** Find the complement of F = A·B·C + B·C'.

**Answer.** F' = (A·B·C + B·C')'<br>= (A·B·C)'·(B·C')'<br>= (A' + B' + C')·(B' + C)

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q7.** Find the complement of F = B·C + A'·B.

**Answer.** F' = (B·C + A'·B)'<br>= (B·C)'·(A'·B)'<br>= (B' + C')·(A + B')

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q8.** Find the complement of F = A·C + A'·C.

**Answer.** F' = (A·C + A'·C)'<br>= (A·C)'·(A'·C)'<br>= (A' + C')·(A + C')

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q9.** Find the complement of F = A'·B·C + A·C + B'·C.

**Answer.** F' = (A'·B·C + A·C + B'·C)'<br>= (A'·B·C)'·(A·C)'·(B'·C)'<br>= (A + B' + C')·(A' + C')·(B + C')

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q10.** Find the complement of F = B'·C' + A·B' + A·B.

**Answer.** F' = (B'·C' + A·B' + A·B)'<br>= (B'·C')'·(A·B')'·(A·B)'<br>= (B + C)·(A' + B)·(A' + B')

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q11.** Find the complement of F = A'·B·C' + A·B·C.

**Answer.** F' = (A'·B·C' + A·B·C)'<br>= (A'·B·C')'·(A·B·C)'<br>= (A + B' + C)·(A' + B' + C')

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q12.** Find the complement of F = A'·B + A·B.

**Answer.** F' = (A'·B + A·B)'<br>= (A'·B)'·(A·B)'<br>= (A + B')·(A' + B')

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q13.** Find the complement of F = A'·B' + A'·B.

**Answer.** F' = (A'·B' + A'·B)'<br>= (A'·B')'·(A'·B)'<br>= (A + B)·(A + B')

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q14.** Find the complement of F = A·C + A·B'·C'.

**Answer.** F' = (A·C + A·B'·C')'<br>= (A·C)'·(A·B'·C')'<br>= (A' + C')·(A' + B + C)

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q15.** Find the complement of F = (B + C)·(A + B).

**Answer.** F' = ((B + C)·(A + B))'<br>= (B + C)' + (A + B)'<br>= B'·C' + A'·B'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q16.** Find the complement of F = (A + B')·(A + C).

**Answer.** F' = ((A + B')·(A + C))'<br>= (A + B')' + (A + C)'<br>= A'·B + A'·C'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q17.** Find the complement of F = (A + C')·(A + B')·(A' + B).

**Answer.** F' = ((A + C')·(A + B')·(A' + B))'<br>= (A + C')' + (A + B')' + (A' + B)'<br>= A'·C + A'·B + A·B'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q18.** Find the complement of F = (A' + C')·(A + C).

**Answer.** F' = ((A' + C')·(A + C))'<br>= (A' + C')' + (A + C)'<br>= A·C + A'·C'

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q19.** Find the complement of F = (A + B')·(A + B).

**Answer.** F' = ((A + B')·(A + B))'<br>= (A + B')' + (A + B)'<br>= A'·B + A'·B'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q20.** Find the complement of F = (A' + B)·(A + B)·(A + B').

**Answer.** F' = ((A' + B)·(A + B)·(A + B'))'<br>= (A' + B)' + (A + B)' + (A + B')'<br>= A·B' + A'·B' + A'·B

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q21.** Find the complement of F = (A' + B)·(A + B').

**Answer.** F' = ((A' + B)·(A + B'))'<br>= (A' + B)' + (A + B')'<br>= A·B' + A'·B

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q22.** Find the complement of F = (A + D)·(A + B).

**Answer.** F' = ((A + D)·(A + B))'<br>= (A + D)' + (A + B)'<br>= A'·D' + A'·B'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q23.** Find the complement of F = (A' + B')·(B' + D').

**Answer.** F' = ((A' + B')·(B' + D'))'<br>= (A' + B')' + (B' + D')'<br>= A·B + B·D

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q24.** Find the complement of F = (A + C)·(B + C').

**Answer.** F' = ((A + C)·(B + C'))'<br>= (A + C)' + (B + C')'<br>= A'·C' + B'·C

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q25.** Find the complement of F = (B + C')·(B + C)·(B' + C).

**Answer.** F' = ((B + C')·(B + C)·(B' + C))'<br>= (B + C')' + (B + C)' + (B' + C)'<br>= B'·C + B'·C' + B·C'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q26.** Find the complement of F = (A' + B)·(A + B).

**Answer.** F' = ((A' + B)·(A + B))'<br>= (A' + B)' + (A + B)'<br>= A·B' + A'·B'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q27.** Find the complement of F = (A' + B)·(A + C')·(A' + B').

**Answer.** F' = ((A' + B)·(A + C')·(A' + B'))'<br>= (A' + B)' + (A + C')' + (A' + B')'<br>= A·B' + A'·C + A·B

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q28.** Find the complement of F = A·(B' + A).

**Answer.** F' = (A·(B' + A))'<br>= A' + (B' + A)'<br>= A' + B·A'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q29.** Find the complement of F = (A + B')'·C'.

**Answer.** F' = ((A + B')'·C')'<br>= A + B' + C

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q30.** Find the complement of F = (A + B)'·C.

**Answer.** F' = ((A + B)'·C)'<br>= A + B + C'

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q31.** Find the complement of F = A' + (B·C)'.

**Answer.** F' = (A' + (B·C)')'<br>= A·B·C

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q32.** Find the complement of F = (A·B)' + C.

**Answer.** F' = ((A·B)' + C)'<br>= A·B·C'

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q33.** Find the complement of F = (A + B·A)'.

**Answer.** F' = (A + B·A)''<br>= A + B·A

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q34.** Find the complement of F = A + (B'·C)'.

**Answer.** F' = (A + (B'·C)')'<br>= A'·B'·C

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q35.** Find the complement of F = A·(B' + A').

**Answer.** F' = (A·(B' + A'))'<br>= A' + (B' + A')'<br>= A' + B·A

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q36.** Find the complement of F = (A' + B'·C)'.

**Answer.** F' = (A' + B'·C)''<br>= A' + B'·C

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q37.** Find the complement of F = (A + B·C')'.

**Answer.** F' = (A + B·C')''<br>= A + B·C'

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q38.** Find the complement of F = (A + B)'·C'.

**Answer.** F' = ((A + B)'·C')'<br>= A + B + C

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.

**Q39.** Find the complement of F = (A'·B)' + C'.

**Answer.** F' = ((A'·B)' + C')'<br>= A'·B·C

*Check:* with every input 1, F = 1 and F' = 0: opposites, as they must be.

**Q40.** Find the complement of F = A·(B' + C').

**Answer.** F' = (A·(B' + C'))'<br>= A' + (B' + C')'<br>= A' + B·C

*Check:* with every input 1, F = 0 and F' = 1: opposites, as they must be.
