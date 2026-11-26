# Chapter 4: Number Systems and Encoding Schemes: Fill in the blanks (30)

*Chapter 4 · Questions (online). One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Concepts

**Q1.** The number of digits in a number system is called its ______ or radix. *(E · 4.1)*

**Answer.** base.

**Q2.** The largest digit of base 7 would be ______. *(M · 4.1)*

**Answer.** 6. *Why:* base b has digits 0 to b − 1.

**Q3.** In hexadecimal, the digit E stands for the decimal value ______. *(E · 4.1)*

**Answer.** 14.

**Q4.** One hexadecimal digit stands for ______ bits. *(E · 4.1)*

**Answer.** 4.

**Q5.** The bit with the largest place value is called the ______. *(E · 4.2)*

**Answer.** MSB (most significant bit).

**Q6.** (10)₈ is equal to ______ in decimal. *(E · 4.2)*

**Answer.** 8. *Why:* "10" in any base is the base itself.

**Q7.** The place value of the position −2 in binary is ______. *(M · 4.2)*

**Answer.** ¼ = 0.25 (2⁻²).

**Q8.** With 6 bits, the largest number is ______. *(M · 4.2)*

**Answer.** 63 = 2⁶ − 1.

**Q9.** In the division method the remainders are read from ______ to ______. *(E · 4.3)*

**Answer.** bottom, top.

**Q10.** To convert octal to hexadecimal, we first convert to ______. *(E · 4.3)*

**Answer.** binary.

**Q11.** When grouping the fraction part, extra 0s are added on the ______. *(M · 4.3)*

**Answer.** right (at the far end of the fraction).

**Q12.** In the multiplication method for fractions, the whole-number parts are read from ______ to ______. *(E · 4.4)*

**Answer.** top, bottom.

**Q13.** ISCII stands for Indian Script Code for ______ Interchange. *(E · 4.5)*

**Answer.** Information.

**Q14.** The ASCII code of 'a' is ______. *(E · 4.5)*

**Answer.** 97.

**Q15.** Unicode gives each character a unique number called its ______. *(E · 4.5)*

**Answer.** code point.

**Q16.** UTF-32 is a ______-length encoding. *(E · 4.5)*

**Answer.** fixed (always 4 bytes).

**Q17.** The ₹ sign takes ______ bytes in UTF-8. *(M · 4.5)*

**Answer.** 3. *Why:* U+20B9 is between U+0800 and U+FFFF.

**Q18.** A capital letter and its small letter differ by ______ in ASCII. *(E · 4.5)*

**Answer.** 32.

## Working it out

**Q19.** (37)₁₀ = (______)₂ *(E · 4.3)*

**Answer.** 100101. *Why:* 37 ÷ 2 again and again: remainders 1, 0, 1, 0, 0, 1; read upward → (100101)₂.

**Q20.** (125)₁₀ = (______)₂ *(E · 4.3)*

**Answer.** 1111101. *Why:* 125 ÷ 2 again and again: remainders 1, 0, 1, 1, 1, 1, 1; read upward → (1111101)₂.

**Q21.** (182)₁₀ = (______)₂ *(E · 4.3)*

**Answer.** 10110110. *Why:* 182 ÷ 2 again and again: remainders 0, 1, 1, 0, 1, 1, 0, 1; read upward → (10110110)₂.

**Q22.** (132)₁₀ = (______)₂ *(E · 4.3)*

**Answer.** 10000100. *Why:* 132 ÷ 2 again and again: remainders 0, 0, 1, 0, 0, 0, 0, 1; read upward → (10000100)₂.

**Q23.** (315)₈ = (______)₁₀ *(E · 4.3)*

**Answer.** 205. *Why:* 3 × 64 + 8 + 5 × 1 = 205.

**Q24.** (236)₈ = (______)₁₀ *(E · 4.3)*

**Answer.** 158. *Why:* 2 × 64 + 3 × 8 + 6 × 1 = 158.

**Q25.** (366)₈ = (______)₁₀ *(E · 4.3)*

**Answer.** 246. *Why:* 3 × 64 + 6 × 8 + 6 × 1 = 246.

**Q26.** (11111111001)₂ = (______)₁₆ *(E · 4.3)*

**Answer.** 7F9. *Why:* groups of 4 from the point: 0111 1111 1001 → (7F9)₁₆.

**Q27.** (110011110011)₂ = (______)₁₆ *(E · 4.3)*

**Answer.** CF3. *Why:* groups of 4 from the point: 1100 1111 0011 → (CF3)₁₆.

**Q28.** (101001101011)₂ = (______)₁₆ *(E · 4.3)*

**Answer.** A6B. *Why:* groups of 4 from the point: 1010 0110 1011 → (A6B)₁₆.

**Q29.** The ASCII codes of "GOA" are ______. *(E · 4.5)*

**Answer.** 71 79 65.

**Q30.** The ASCII codes of "Pune" are ______. *(E · 4.5)*

**Answer.** 80 117 110 101.
