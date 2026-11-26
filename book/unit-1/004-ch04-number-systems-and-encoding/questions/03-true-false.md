# Chapter 4: Number Systems and Encoding Schemes: True or false (30)

*Chapter 4 · Questions (online). One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Concepts

**Q1.** Hexadecimal has 16 digits. *(E · 4.1)*

**Answer.** True: 0 to 9 and A to F.

**Q2.** A computer stores pictures as numbers. *(E · 4.1)*

**Answer.** True: everything is stored as numbers in binary.

**Q3.** (100)₂ is greater than (100)₈. *(E · 4.2)*

**Answer.** False: (100)₂ = 4 and (100)₈ = 64.

**Q4.** The digit 8 can appear in an octal number. *(E · 4.2)*

**Answer.** False: octal digits are 0 to 7.

**Q5.** Adding a 0 on the right of a binary number doubles it. *(M · 4.2)*

**Answer.** True: every bit moves one place left.

**Q6.** The MSB of a binary number is the rightmost bit. *(E · 4.2)*

**Answer.** False: the MSB is the leftmost bit.

**Q7.** In the division method, the first remainder is the most significant digit. *(M · 4.3)*

**Answer.** False: it is the least significant (units) digit.

**Q8.** Octal to hexadecimal is best done through binary. *(E · 4.3)*

**Answer.** True.

**Q9.** Every decimal fraction can be written exactly in binary. *(M · 4.4)*

**Answer.** False: 0.1, 0.2, 0.3 repeat for ever.

**Q10.** 0.5 is (0.1)₂. *(E · 4.4)*

**Answer.** True: the first place after the binary point is worth ½.

**Q11.** ASCII can represent Hindi letters. *(E · 4.5)*

**Answer.** False: ASCII has only 128 codes, for English.

**Q12.** The ASCII code of '0' is 0. *(M · 4.5)*

**Answer.** False: it is 48; code 0 is NUL, which prints nothing.

**Q13.** ISCII uses 8 bits. *(E · 4.5)*

**Answer.** True: 256 codes.

**Q14.** Unicode includes all the ASCII characters with the same numbers. *(E · 4.5)*

**Answer.** True: U+0000 to U+007F.

**Q15.** In UTF-8 every character takes the same number of bytes. *(E · 4.5)*

**Answer.** False: 1 to 4 bytes; that is UTF-32 (always 4).

**Q16.** The emoji 😀 takes 4 bytes in UTF-8. *(M · 4.5)*

**Answer.** True: it is U+1F600, above U+FFFF (most emojis are).

## Working it out

**Q17.** (679)₁₀ = (2A7)₁₆ *(E · 4.3)*

**Answer.** True. *Check:* both are 679 in decimal.

**Q18.** (11101001)₂ = (EB)₁₆ *(E · 4.3)*

**Answer.** False: (11101001)₂ = (E9)₁₆, which is 233; (EB)₁₆ is 235.

**Q19.** (889)₁₀ = (1101111001)₂ *(E · 4.3)*

**Answer.** True. *Check:* both are 889 in decimal.

**Q20.** (755)₁₀ = (1011110100)₂ *(E · 4.3)*

**Answer.** False: (755)₁₀ = (1011110011)₂, which is 755; (1011110100)₂ is 756.

**Q21.** (813)₁₀ = (32D)₁₆ *(E · 4.3)*

**Answer.** True. *Check:* both are 813 in decimal.

**Q22.** (1010010100)₂ = (295)₁₆ *(E · 4.3)*

**Answer.** False: (1010010100)₂ = (294)₁₆, which is 660; (295)₁₆ is 661.

**Q23.** (369)₁₀ = (101110001)₂ *(E · 4.3)*

**Answer.** True. *Check:* both are 369 in decimal.

**Q24.** (327)₁₀ = (511)₈ *(E · 4.3)*

**Answer.** False: (327)₁₀ = (507)₈, which is 327; (511)₈ is 329.

**Q25.** (73)₁₀ = (1001001)₂ *(E · 4.3)*

**Answer.** True. *Check:* both are 73 in decimal.

**Q26.** (744)₁₀ = (2E9)₁₆ *(E · 4.3)*

**Answer.** False: (744)₁₀ = (2E8)₁₆, which is 744; (2E9)₁₆ is 745.

**Q27.** (782)₁₀ = (30E)₁₆ *(E · 4.3)*

**Answer.** True. *Check:* both are 782 in decimal.

**Q28.** (554)₈ = (16D)₁₆ *(E · 4.3)*

**Answer.** False: (554)₈ = (16C)₁₆, which is 364; (16D)₁₆ is 365.

**Q29.** (325)₁₀ = (145)₁₆ *(E · 4.3)*

**Answer.** True. *Check:* both are 325 in decimal.

**Q30.** (186)₁₀ = (CA)₁₆ *(E · 4.3)*

**Answer.** False: (186)₁₀ = (BA)₁₆, which is 186; (CA)₁₆ is 202.
