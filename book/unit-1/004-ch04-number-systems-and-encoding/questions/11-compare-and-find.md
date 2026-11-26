# Chapter 4: Number Systems and Encoding Schemes: Compare, arrange, find the base or the digit (20)

*Chapter 4 · Questions (online). Sections 4.2 and 4.3. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Compare and find

**Q1.** Arrange in increasing order: (2E)₁₆, (117)₈, (11100010)₂, (40)₁₀. *(M · 4.3)*

**Answer.** (40)₁₀, (2E)₁₆, (117)₈, (11100010)₂. *Working:* in decimal they are (2E)₁₆ = 46, (117)₈ = 79, (11100010)₂ = 226, (40)₁₀ = 40.

**Q2.** Arrange in increasing order: (127)₁₀, (150)₈, (10101011)₂, (105)₁₆. *(M · 4.3)*

**Answer.** (150)₈, (127)₁₀, (10101011)₂, (105)₁₆. *Working:* in decimal they are (127)₁₀ = 127, (150)₈ = 104, (10101011)₂ = 171, (105)₁₆ = 261.

**Q3.** Arrange in increasing order: (193)₁₀, (DC)₁₆, (100010010)₂, (72)₈. *(M · 4.3)*

**Answer.** (72)₈, (193)₁₀, (DC)₁₆, (100010010)₂. *Working:* in decimal they are (193)₁₀ = 193, (DC)₁₆ = 220, (100010010)₂ = 274, (72)₈ = 58.

**Q4.** Arrange in increasing order: (DE)₁₆, (85)₁₀, (62)₈, (1101001)₂. *(M · 4.3)*

**Answer.** (62)₈, (85)₁₀, (1101001)₂, (DE)₁₆. *Working:* in decimal they are (DE)₁₆ = 222, (85)₁₀ = 85, (62)₈ = 50, (1101001)₂ = 105.

**Q5.** Arrange in increasing order: (333)₈, (10000011)₂, (15)₁₆, (128)₁₀. *(M · 4.3)*

**Answer.** (15)₁₆, (128)₁₀, (10000011)₂, (333)₈. *Working:* in decimal they are (333)₈ = 219, (10000011)₂ = 131, (15)₁₆ = 21, (128)₁₀ = 128.

**Q6.** Arrange in increasing order: (D7)₁₆, (133)₁₀, (173)₈, (10111101)₂. *(M · 4.3)*

**Answer.** (173)₈, (133)₁₀, (10111101)₂, (D7)₁₆. *Working:* in decimal they are (D7)₁₆ = 215, (133)₁₀ = 133, (173)₈ = 123, (10111101)₂ = 189.

**Q7.** Find the base b if (101)_b = 26. *(H · 4.2)*

**Answer.** b = 5. *Working:* 1 × 5^2 + 0 × 5^1 + 1 × 5^0 = 26.

**Q8.** Find the base b if (23)_b = 19. *(H · 4.2)*

**Answer.** b = 8. *Working:* 2 × 8^1 + 3 × 8^0 = 19.

**Q9.** Find the base b if (110)_b = 42. *(H · 4.2)*

**Answer.** b = 6. *Working:* 1 × 6^2 + 1 × 6^1 + 0 × 6^0 = 42.

**Q10.** Find the base b if (31)_b = 25. *(H · 4.2)*

**Answer.** b = 8. *Working:* 3 × 8^1 + 1 × 8^0 = 25.

**Q11.** Find the base b if (1000)_b = 125. *(H · 4.2)*

**Answer.** b = 5. *Working:* 1 × 5^3 + 0 × 5^2 + 0 × 5^1 + 0 × 5^0 = 125.

**Q12.** Find the base b if (202)_b = 74. *(H · 4.2)*

**Answer.** b = 6. *Working:* 2 × 6^2 + 0 × 6^1 + 2 × 6^0 = 74.

**Q13.** Find the digit x if (xA7)₁₆ = 423. *(H · 4.3)*

**Answer.** x = 1. *Check:* (1A7)₁₆ = 256 + 10 × 16 + 7 × 1 = 423.

**Q14.** Find the digit x if (B8x)₁₆ = 2948. *(H · 4.3)*

**Answer.** x = 4. *Check:* (B84)₁₆ = 11 × 256 + 8 × 16 + 4 × 1 = 2948.

**Q15.** Find the digit x if (2x2)₁₆ = 562. *(H · 4.3)*

**Answer.** x = 3. *Check:* (232)₁₆ = 2 × 256 + 3 × 16 + 2 × 1 = 562.

**Q16.** Find the digit x if (9xD)₁₆ = 2397. *(H · 4.3)*

**Answer.** x = 5. *Check:* (95D)₁₆ = 9 × 256 + 5 × 16 + 13 × 1 = 2397.

**Q17.** What is "1010" worth if it is in base 2? *(E · 4.2)*

**Answer.** 10. *Why:* 8 + 2 = 10. The same digits mean different numbers in different bases: always write the base.

**Q18.** What is "1010" worth if it is in base 8? *(E · 4.2)*

**Answer.** 520. *Why:* 512 + 8 = 520. The same digits mean different numbers in different bases: always write the base.

**Q19.** What is "1010" worth if it is in base 16? *(E · 4.2)*

**Answer.** 4112. *Why:* 4096 + 16 = 4112. The same digits mean different numbers in different bases: always write the base.

**Q20.** What is "1010" worth if it is in base 10? *(E · 4.2)*

**Answer.** 1010. *Why:* 1000 + 10 = 1010. The same digits mean different numbers in different bases: always write the base.
