# Chapter 4: Number Systems and Encoding Schemes: Numbers with a fractional part (30)

*Chapter 4 · Questions (online). Section 4.4. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## To decimal (place values after the point)

**Q1.** Convert (110.011)₂ to decimal. *(M · 4.4)*

**Answer.** 6.375. *Working:* 4 + 2 + 1/4 + 1/8 = 6.375.

**Q2.** Convert (1011.101)₂ to decimal. *(M · 4.4)*

**Answer.** 11.625. *Working:* 8 + 2 + 1 + 1/2 + 1/8 = 11.625.

**Q3.** Convert (0.1101)₂ to decimal. *(M · 4.4)*

**Answer.** 0.8125. *Working:* 1/2 + 1/4 + 1/16 = 0.8125.

**Q4.** Convert (11.0011)₂ to decimal. *(M · 4.4)*

**Answer.** 3.1875. *Working:* 2 + 1 + 1/8 + 1/16 = 3.1875.

**Q5.** Convert (37.4)₈ to decimal. *(M · 4.4)*

**Answer.** 31.5. *Working:* 3 × 8 + 7 × 1 + 4 × 1/8 = 31.5.

**Q6.** Convert (125.24)₈ to decimal. *(M · 4.4)*

**Answer.** 85.3125. *Working:* 64 + 2 × 8 + 5 × 1 + 2 × 1/8 + 4 × 1/64 = 85.3125.

**Q7.** Convert (0.71)₈ to decimal. *(M · 4.4)*

**Answer.** 0.890625. *Working:* 7 × 1/8 + 1/64 = 0.890625.

**Q8.** Convert (A.8)₁₆ to decimal. *(M · 4.4)*

**Answer.** 10.5. *Working:* 10 × 1 + 8 × 1/16 = 10.5.

**Q9.** Convert (1F.4)₁₆ to decimal. *(M · 4.4)*

**Answer.** 31.25. *Working:* 16 + 15 × 1 + 4 × 1/16 = 31.25.

**Q10.** Convert (3C.28)₁₆ to decimal. *(M · 4.4)*

**Answer.** 60.1562. *Working:* 3 × 16 + 12 × 1 + 2 × 1/16 + 8 × 1/256 = 60.1562.

## From decimal (multiply)

**Q11.** Convert (0.4375)₁₀ to binary. *(M · 4.4)*

**Answer.** (0.0111)₂. *Working:* 0.4375 × 2 = 0.875 → 0; 0.875 × 2 = 1.75 → 1; 0.75 × 2 = 1.5 → 1; 0.5 × 2 = 1 → 1; fraction 0: stop.

**Q12.** Convert (0.84375)₁₀ to binary. *(M · 4.4)*

**Answer.** (0.11011)₂. *Working:* 0.84375 × 2 = 1.6875 → 1; 0.6875 × 2 = 1.375 → 1; 0.375 × 2 = 0.75 → 0; 0.75 × 2 = 1.5 → 1; 0.5 × 2 = 1 → 1; fraction 0: stop.

**Q13.** Convert (0.09375)₁₀ to binary. *(M · 4.4)*

**Answer.** (0.00011)₂. *Working:* 0.09375 × 2 = 0.1875 → 0; 0.1875 × 2 = 0.375 → 0; 0.375 × 2 = 0.75 → 0; 0.75 × 2 = 1.5 → 1; 0.5 × 2 = 1 → 1; fraction 0: stop.

**Q14.** Convert (0.71875)₁₀ to binary. *(M · 4.4)*

**Answer.** (0.10111)₂. *Working:* 0.71875 × 2 = 1.4375 → 1; 0.4375 × 2 = 0.875 → 0; 0.875 × 2 = 1.75 → 1; 0.75 × 2 = 1.5 → 1; 0.5 × 2 = 1 → 1; fraction 0: stop.

**Q15.** Convert (0.5625)₁₀ to binary. *(M · 4.4)*

**Answer.** (0.1001)₂. *Working:* 0.5625 × 2 = 1.125 → 1; 0.125 × 2 = 0.25 → 0; 0.25 × 2 = 0.5 → 0; 0.5 × 2 = 1 → 1; fraction 0: stop.

**Q16.** Convert (0.2)₁₀ to binary, to 6 places. *(H · 4.4)*

**Answer.** ≈ (0.001100…)₂. *Working:* 0.2 × 2 = 0.4 → 0; 0.4 × 2 = 0.8 → 0; 0.8 × 2 = 1.6 → 1; 0.6 × 2 = 1.2 → 1; 0.2 came back, so the digits 0011 repeat; it does not end (a fraction came back).

**Q17.** Convert (0.7)₁₀ to binary, to 6 places. *(H · 4.4)*

**Answer.** ≈ (0.101100…)₂. *Working:* 0.7 × 2 = 1.4 → 1; 0.4 × 2 = 0.8 → 0; 0.8 × 2 = 1.6 → 1; 0.6 × 2 = 1.2 → 1; 0.2 × 2 = 0.4 → 0; 0.4 came back, so the digits 0110 repeat; it does not end (a fraction came back).

**Q18.** Convert (0.45)₁₀ to binary, to 6 places. *(H · 4.4)*

**Answer.** ≈ (0.011100…)₂. *Working:* 0.45 × 2 = 0.9 → 0; 0.9 × 2 = 1.8 → 1; 0.8 × 2 = 1.6 → 1; 0.6 × 2 = 1.2 → 1; 0.2 × 2 = 0.4 → 0; 0.4 × 2 = 0.8 → 0; it does not end (6 places reached).

**Q19.** Convert (0.828125)₁₀ to octal. *(H · 4.4)*

**Answer.** (0.65)₈. *Working:* 0.828125 × 8 = 6.625 → 6; 0.625 × 8 = 5 → 5.

**Q20.** Convert (0.9375)₁₀ to hexadecimal. *(H · 4.4)*

**Answer.** (0.F)₁₆. *Working:* 0.9375 × 16 = 15 → F.

**Q21.** Convert (0.3125)₁₀ to octal. *(H · 4.4)*

**Answer.** (0.24)₈. *Working:* 0.3125 × 8 = 2.5 → 2; 0.5 × 8 = 4 → 4.

**Q22.** Convert (0.6484375)₁₀ to hexadecimal. *(H · 4.4)*

**Answer.** (0.A6)₁₆. *Working:* 0.648438 × 16 = 10.375 → A; 0.375 × 16 = 6 → 6.

## Between binary, octal and hexadecimal (group away from the point)

**Q23.** Convert (101.011)₂ to octal. *(M · 4.4)*

**Answer.** (5.3)₈. *Working:* groups of 3 from the point: 101 . 011 → (5.3)₈.

**Q24.** Convert (1101.1011)₂ to hexadecimal. *(M · 4.4)*

**Answer.** (D.B)₁₆. *Working:* groups of 4 from the point: 1101 . 1011 → (D.B)₁₆.

**Q25.** Convert (10.01101)₂ to octal. *(M · 4.4)*

**Answer.** (2.32)₈. *Working:* groups of 3 from the point: 010 . 011 010 → (2.32)₈.

**Q26.** Convert (111001.101)₂ to hexadecimal. *(M · 4.4)*

**Answer.** (39.A)₁₆. *Working:* groups of 4 from the point: 0011 1001 . 1010 → (39.A)₁₆.

**Q27.** Convert (0.10111)₂ to octal. *(M · 4.4)*

**Answer.** (0.56)₈. *Working:* groups of 3 from the point: 000 . 101 110 → (0.56)₈.

**Q28.** Convert (11101.01)₂ to hexadecimal. *(M · 4.4)*

**Answer.** (1D.4)₁₆. *Working:* groups of 4 from the point: 0001 1101 . 0100 → (1D.4)₁₆.

**Q29.** Convert (5.36)₈ to binary. *(M · 4.4)*

**Answer.** (101.01111)₂. *Working:* 5 → 101 . 3 → 011, 6 → 110 → (101.01111)₂.

**Q30.** Convert (B.A)₁₆ to binary. *(M · 4.4)*

**Answer.** (1011.101)₂. *Working:* B → 1011 . A → 1010 → (1011.101)₂.
