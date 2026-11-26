# Chapter 4: Number Systems and Encoding Schemes: Multiple-choice questions (40)

*Chapter 4 · Questions (online). One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Concepts

**Q1.** The base of the octal system is: (a) 2 (b) 8 (c) 10 (d) 16 *(E · 4.1)*

**Answer.** (b) 8. *Why:* octo = eight; digits 0 to 7.

**Q2.** Which symbol is NOT a hexadecimal digit? (a) A (b) F (c) G (d) 9 *(E · 4.1)*

**Answer.** (c) G. *Why:* hex stops at F (fifteen).

**Q3.** How many digits does the decimal system have? (a) 9 (b) 10 (c) 11 (d) 8 *(E · 4.1)*

**Answer.** (b) 10: 0 to 9.

**Q4.** A computer works in binary because: (a) binary is the oldest system (b) a switch has two states (c) binary numbers are short (d) people find binary easy *(E · 4.1)*

**Answer.** (b). *Why:* telling two states apart is easy and safe; binary numbers are in fact long, not short.

**Q5.** Hexadecimal is used by people mainly because it: (a) is a short form of binary (b) has letters (c) is faster for the CPU (d) is the base of ASCII *(E · 4.1)*

**Answer.** (a). *Why:* one hex digit stands for 4 bits; the CPU itself works in binary.

**Q6.** In 7345, the place value of 3 is: (a) 3 (b) 30 (c) 300 (d) 3000 *(E · 4.2)*

**Answer.** (c) 300. *Why:* 3 is in the hundreds place.

**Q7.** The weight of the leftmost bit of a 6-bit binary number is: (a) 6 (b) 32 (c) 64 (d) 16 *(M · 4.2)*

**Answer.** (b) 32. *Why:* positions run 5, 4, … 0, and 2⁵ = 32.

**Q8.** The LSB of a binary number is the bit: (a) on the left (b) on the right (c) in the middle (d) with the largest value *(E · 4.2)*

**Answer.** (b) on the right: it has the smallest place value.

**Q9.** What comes after (77)₈? (a) (78)₈ (b) (80)₈ (c) (100)₈ (d) (88)₈ *(M · 4.2)*

**Answer.** (c) (100)₈. *Why:* both digits are at the top (7), so both roll over and carry.

**Q10.** What comes after (1F)₁₆? (a) (20)₁₆ (b) (1G)₁₆ (c) (110)₁₆ (d) (2F)₁₆ *(M · 4.2)*

**Answer.** (a) (20)₁₆. *Why:* F rolls over to 0 and carries 1 into the 16s place.

**Q11.** To convert decimal to binary we: (a) multiply by 2 (b) divide by 2 and read the remainders upward (c) divide by 2 and read the remainders downward (d) group in 3s *(E · 4.3)*

**Answer.** (b). *Why:* the first remainder is the units digit, so it comes last.

**Q12.** Binary is converted to hexadecimal by grouping bits in: (a) 2s (b) 3s (c) 4s (d) 8s *(E · 4.3)*

**Answer.** (c) 4s. *Why:* 16 = 2⁴.

**Q13.** The best way to convert octal to hexadecimal is: (a) directly (b) through binary (c) through ASCII (d) it cannot be done *(E · 4.3)*

**Answer.** (b) through binary: each octal digit to 3 bits, then regroup in 4s.

**Q14.** When a whole binary number is grouped, extra 0s are added: (a) on the right (b) on the left (c) in the middle (d) anywhere *(M · 4.3)*

**Answer.** (b) on the left: a 0 on the left adds nothing; on the right it would double the number.

**Q15.** When converting a decimal fraction to binary, we: (a) divide by 2 (b) multiply by 2 and read the whole parts downward (c) multiply by 2 and read upward (d) group in 4s *(E · 4.4)*

**Answer.** (b). *Why:* the first digit found is the one nearest the point.

**Q16.** Which decimal fraction has an exact binary form? (a) 0.1 (b) 0.2 (c) 0.75 (d) 0.3 *(M · 4.4)*

**Answer.** (c) 0.75 = 3/4. *Why:* its denominator is a power of 2.

**Q17.** ASCII stands for: (a) American Standard Code for Information Interchange (b) American Scientific Code for Information Interchange (c) Advanced Standard Code for Internet Interchange (d) American Standard Computer Information Index *(E · 4.5)*

**Answer.** (a).

**Q18.** How many characters can 8-bit ISCII represent? (a) 128 (b) 255 (c) 256 (d) 512 *(E · 4.5)*

**Answer.** (c) 256 = 2⁸, numbered 0 to 255.

**Q19.** The ASCII code of the space character is: (a) 0 (b) 20 (c) 32 (d) 48 *(M · 4.5)*

**Answer.** (c) 32. *Why:* the first printable code; 0 is NUL.

**Q20.** Unicode code points are usually written in: (a) binary (b) octal (c) decimal (d) hexadecimal, after U+ *(E · 4.5)*

**Answer.** (d), for example U+0905 for अ.

**Q21.** In UTF-8, an English letter takes: (a) 1 byte (b) 2 bytes (c) 3 bytes (d) 4 bytes *(E · 4.5)*

**Answer.** (a) 1 byte, the same as in ASCII.

**Q22.** Which encoding is used by almost all web pages? (a) ASCII (b) ISCII (c) UTF-8 (d) UTF-32 *(E · 4.5)*

**Answer.** (c) UTF-8.

## Working it out

**Q23.** (117)₁₀ in binary is: (a) (1110011)₂ (b) (1010111)₂ (c) (1110110)₂ (d) (1110101)₂ *(E · 4.3)*

**Answer.** (d) (1110101)₂. *Why:* 117 ÷ 2 again and again: remainders 1, 0, 1, 0, 1, 1, 1; read upward → (1110101)₂.

**Q24.** (162)₁₀ in binary is: (a) (10100000)₂ (b) (10100011)₂ (c) (10100010)₂ (d) (01000101)₂ *(E · 4.3)*

**Answer.** (c) (10100010)₂. *Why:* 162 ÷ 2 again and again: remainders 0, 1, 0, 0, 0, 1, 0, 1; read upward → (10100010)₂.

**Q25.** (142)₁₀ in binary is: (a) (01110001)₂ (b) (10001100)₂ (c) (10001110)₂ (d) (10001111)₂ *(E · 4.3)*

**Answer.** (c) (10001110)₂. *Why:* 142 ÷ 2 again and again: remainders 0, 1, 1, 1, 0, 0, 0, 1; read upward → (10001110)₂.

**Q26.** (173)₁₀ in binary is: (a) (10101011)₂ (b) (10101101)₂ (c) (10110101)₂ (d) (10101110)₂ *(E · 4.3)*

**Answer.** (b) (10101101)₂. *Why:* 173 ÷ 2 again and again: remainders 1, 0, 1, 1, 0, 1, 0, 1; read upward → (10101101)₂.

**Q27.** (67)₁₀ in binary is: (a) (1100001)₂ (b) (1000001)₂ (c) (1000011)₂ (d) (1000100)₂ *(E · 4.3)*

**Answer.** (c) (1000011)₂. *Why:* 67 ÷ 2 again and again: remainders 1, 1, 0, 0, 0, 0, 1; read upward → (1000011)₂.

**Q28.** (B6C)₁₆ in decimal is: (a) 2923 (b) 2924 (c) 2940 (d) 3179 *(M · 4.3)*

**Answer.** (b) 2924. *Why:* 11 × 256 + 6 × 16 + 12 × 1 = 2924.

**Q29.** (3CF)₁₆ in decimal is: (a) 975 (b) 974 (c) 991 (d) 4035 *(M · 4.3)*

**Answer.** (a) 975. *Why:* 3 × 256 + 12 × 16 + 15 × 1 = 975.

**Q30.** (28F)₁₆ in decimal is: (a) 655 (b) 671 (c) 654 (d) 3970 *(M · 4.3)*

**Answer.** (a) 655. *Why:* 2 × 256 + 8 × 16 + 15 × 1 = 655.

**Q31.** (944)₁₆ in decimal is: (a) 2371 (b) 1097 (c) 2372 (d) 2388 *(M · 4.3)*

**Answer.** (c) 2372. *Why:* 9 × 256 + 4 × 16 + 4 × 1 = 2372.

**Q32.** (1000100100)₂ in octal is: (a) (4401)₈ (b) (4220)₈ (c) (1044)₈ (d) (1045)₈ *(M · 4.3)*

**Answer.** (c) (1044)₈. *Why:* groups of 3 from the point: 001 000 100 100 → (1044)₈. *Trap:* grouping from the left gives (4220)₈.

**Q33.** (1000111)₂ in octal is: (a) (107)₈ (b) (434)₈ (c) (701)₈ (d) (110)₈ *(M · 4.3)*

**Answer.** (a) (107)₈. *Why:* groups of 3 from the point: 001 000 111 → (107)₈. *Trap:* grouping from the left gives (434)₈.

**Q34.** (1110100100)₂ in octal is: (a) (1644)₈ (b) (1645)₈ (c) (4461)₈ (d) (7220)₈ *(M · 4.3)*

**Answer.** (a) (1644)₈. *Why:* groups of 3 from the point: 001 110 100 100 → (1644)₈. *Trap:* grouping from the left gives (7220)₈.

**Q35.** (1010100101)₂ in octal is: (a) (1245)₈ (b) (5421)₈ (c) (5224)₈ (d) (1246)₈ *(M · 4.3)*

**Answer.** (a) (1245)₈. *Why:* groups of 3 from the point: 001 010 100 101 → (1245)₈. *Trap:* grouping from the left gives (5224)₈.

**Q36.** (11100101)₂ in octal is: (a) (345)₈ (b) (346)₈ (c) (543)₈ (d) (712)₈ *(M · 4.3)*

**Answer.** (a) (345)₈. *Why:* groups of 3 from the point: 011 100 101 → (345)₈. *Trap:* grouping from the left gives (712)₈.

**Q37.** The ASCII code of 'G' is: (a) 103 (b) 72 (c) 70 (d) 71 *(E · 4.5)*

**Answer.** (d) 71. *Why:* A is 65, G is the 7th letter: 65 + 6.

**Q38.** The ASCII code of 'k' is: (a) 107 (b) 75 (c) 108 (d) 106 *(E · 4.5)*

**Answer.** (a) 107. *Why:* a is 97, k is the 11th letter: 97 + 10.

**Q39.** The ASCII code of '9' is: (a) 57 (b) 89 (c) 9 (d) 56 *(E · 4.5)*

**Answer.** (a) 57. *Why:* '0' is 48: 48 + 9.

**Q40.** The ASCII code of 'Z' is: (a) 89 (b) 90 (c) 91 (d) 122 *(E · 4.5)*

**Answer.** (b) 90. *Why:* A is 65, Z the 26th letter: 65 + 25.
