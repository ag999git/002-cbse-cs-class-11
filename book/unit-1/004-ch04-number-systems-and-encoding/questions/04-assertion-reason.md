# Chapter 4: Number Systems and Encoding Schemes: Assertion and reason (15)

*Chapter 4 · Questions (online). For each: (a) both true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true. One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Assertion and reason

**Q1.** A: Octal is a short form of binary. R: 8 = 2³. *(E · 4.1)*

**Answer.** (a). One octal digit is exactly 3 bits.

**Q2.** A: Hexadecimal uses letters A to F. R: Hexadecimal is used for memory addresses. *(M · 4.1)*

**Answer.** (b). Both true, but letters are used because 16 digits need 6 more symbols.

**Q3.** A: (10)₁₆ = 16. R: "10" in any base is the base itself. *(E · 4.2)*

**Answer.** (a).

**Q4.** A: (1001)₂ is odd. R: The LSB of every odd number is 1. *(E · 4.2)*

**Answer.** (a).

**Q5.** A: (19)₈ is a valid octal number. R: Octal digits go from 0 to 7. *(E · 4.2)*

**Answer.** (d). 9 is not an octal digit, so A is false.

**Q6.** A: In the division method the remainders are read upward. R: The first remainder is the units digit. *(E · 4.3)*

**Answer.** (a).

**Q7.** A: Octal can be converted to hexadecimal through binary. R: Both 8 and 16 are powers of 2. *(M · 4.3)*

**Answer.** (a).

**Q8.** A: A whole binary number is padded with 0s on the left. R: A 0 on the left of a whole number adds nothing. *(M · 4.3)*

**Answer.** (a).

**Q9.** A: 0.1 cannot be written exactly in binary. R: The denominator of 1/10 has the factor 5. *(H · 4.4)*

**Answer.** (a). Only fractions whose denominator is a power of 2 end in binary.

**Q10.** A: ASCII uses 7 bits. R: ASCII was made for Indian languages. *(E · 4.5)*

**Answer.** (c). ASCII was made for English.

**Q11.** A: The ASCII code of 'b' is 98. R: A small letter's code is 32 more than its capital's, and 'B' is 66. *(M · 4.5)*

**Answer.** (a). 66 + 32 = 98.

**Q12.** A: ISCII codes 0 to 127 are the same as ASCII. R: ISCII was designed to keep English text unchanged. *(E · 4.5)*

**Answer.** (a).

**Q13.** A: UTF-32 wastes space for English text. R: UTF-32 uses 4 bytes for every character. *(E · 4.5)*

**Answer.** (a).

**Q14.** A: UTF-8 is used by most web pages. R: UTF-8 is a fixed-length encoding. *(E · 4.5)*

**Answer.** (c). UTF-8 is variable-length.

**Q15.** A: In UTF-32 the 100th character can be found directly. R: All characters have the same size in UTF-32. *(M · 4.5)*

**Answer.** (a). It starts at byte 99 × 4 = 396.
