# Chapter 4: Number Systems and Encoding Schemes: Spot the mistake (15)

*Chapter 4 · Questions (online). Each question shows a worked answer with one mistake: find it, say why it is wrong, and correct it. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Spot the mistake

**Q1.** A student converts (228)₁₀ to binary: remainders 0, 0, 1, 0, 0, 1, 1, 1, answer (00100111)₂. Find the mistake. *(M · 4.3)*

**Answer.** The remainders were read **downward**. The first remainder is the units digit, so read upward: (11100100)₂.

**Q2.** A student converts (122)₁₀ to binary: remainders 0, 1, 0, 1, 1, 1, 1, answer (0101111)₂. Find the mistake. *(M · 4.3)*

**Answer.** The remainders were read **downward**. The first remainder is the units digit, so read upward: (1111010)₂.

**Q3.** A student converts (163)₁₀ to binary: remainders 1, 1, 0, 0, 0, 1, 0, 1, answer (11000101)₂. Find the mistake. *(M · 4.3)*

**Answer.** The remainders were read **downward**. The first remainder is the units digit, so read upward: (10100011)₂.

**Q4.** A student converts (32)₁₀ to binary: remainders 0, 0, 0, 0, 0, 1, answer (000001)₂. Find the mistake. *(M · 4.3)*

**Answer.** The remainders were read **downward**. The first remainder is the units digit, so read upward: (100000)₂.

**Q5.** A student converts (1011000100)₂ to octal by grouping from the left and filling the last group with 0s: answer (5420)₈. Find the mistake. *(M · 4.3)*

**Answer.** Groups must start at the point (the right end) and be padded on the **left**: groups of 3 from the point: 001 011 000 100 → (1304)₈.

**Q6.** A student converts (11100010111)₂ to octal by grouping from the left and filling the last group with 0s: answer (7056)₈. Find the mistake. *(M · 4.3)*

**Answer.** Groups must start at the point (the right end) and be padded on the **left**: groups of 3 from the point: 011 100 010 111 → (3427)₈.

**Q7.** A student converts (1100101010)₂ to octal by grouping from the left and filling the last group with 0s: answer (6250)₈. Find the mistake. *(M · 4.3)*

**Answer.** Groups must start at the point (the right end) and be padded on the **left**: groups of 3 from the point: 001 100 101 010 → (1452)₈.

**Q8.** A student writes (3549)₁₀ in hexadecimal as (131313)₁₆. Find the mistake. *(E · 4.3)*

**Answer.** Remainders 10 to 15 must be written as single letters A to F. 3549 ÷ 16 again and again: remainders D (13), D (13), D (13); read upward → (DDD)₁₆.

**Q9.** A student writes (466)₁₀ in hexadecimal as (1132)₁₆. Find the mistake. *(E · 4.3)*

**Answer.** Remainders 10 to 15 must be written as single letters A to F. 466 ÷ 16 again and again: remainders 2, D (13), 1; read upward → (1D2)₁₆.

**Q10.** A student writes (508)₁₀ in hexadecimal as (11512)₁₆. Find the mistake. *(E · 4.3)*

**Answer.** Remainders 10 to 15 must be written as single letters A to F. 508 ÷ 16 again and again: remainders C (12), F (15), 1; read upward → (1FC)₁₆.

**Q11.** A student finds (1101)₂ = 26, numbering the positions from 1. Find the mistake. *(M · 4.2)*

**Answer.** Positions start at **0** for the units place, so every place value was doubled. 8 + 4 + 1 = 13.

**Q12.** A student finds (10110)₂ = 44, numbering the positions from 1. Find the mistake. *(M · 4.2)*

**Answer.** Positions start at **0** for the units place, so every place value was doubled. 16 + 4 + 2 = 22.

**Q13.** A student finds (111001)₂ = 114, numbering the positions from 1. Find the mistake. *(M · 4.2)*

**Answer.** Positions start at **0** for the units place, so every place value was doubled. 32 + 16 + 8 + 1 = 57.

**Q14.** A student converts (0.375)₁₀ to binary and writes (0.110)₂. Find the mistake. *(M · 4.4)*

**Answer.** The whole parts were read upward. In the multiplication method they are read **downward**: 0.375 × 2 = 0.75 → 0; 0.75 × 2 = 1.5 → 1; 0.5 × 2 = 1 → 1 → (0.011)₂.

**Q15.** A student writes: the ASCII code of '4' is 4. Find the mistake. *(E · 4.5)*

**Answer.** '4' is a character, not the number four; its code is 48 + 4 = 52.
