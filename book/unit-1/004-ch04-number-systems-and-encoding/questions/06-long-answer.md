# Chapter 4: Number Systems and Encoding Schemes: Long-answer questions (3, 4 and 5 marks) (14)

*Chapter 4 · Questions (online). Answers with full working, as they should be written in the exam. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Long answers

**Q1.** (i) Convert (692)₁₀ to binary. (ii) From your answer, write it in octal and hexadecimal without dividing again. (iii) Check the hexadecimal answer by converting it back to decimal. [4] *(M · 4.3)*

**Answer.** (i) 692 ÷ 2 again and again: remainders 0, 0, 1, 0, 1, 1, 0, 1, 0, 1; read upward → (1010110100)₂. (ii) groups of 3 from the point: 001 010 110 100 → (1264)₈; groups of 4 from the point: 0010 1011 0100 → (2B4)₁₆. (iii) 2 × 256 + 11 × 16 + 4 × 1 = 692. ✓

**Q2.** (i) Convert (1209)₁₀ to binary. (ii) From your answer, write it in octal and hexadecimal without dividing again. (iii) Check the hexadecimal answer by converting it back to decimal. [4] *(M · 4.3)*

**Answer.** (i) 1209 ÷ 2 again and again: remainders 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1; read upward → (10010111001)₂. (ii) groups of 3 from the point: 010 010 111 001 → (2271)₈; groups of 4 from the point: 0100 1011 1001 → (4B9)₁₆. (iii) 4 × 256 + 11 × 16 + 9 × 1 = 1209. ✓

**Q3.** (i) Convert (898)₁₀ to binary. (ii) From your answer, write it in octal and hexadecimal without dividing again. (iii) Check the hexadecimal answer by converting it back to decimal. [4] *(M · 4.3)*

**Answer.** (i) 898 ÷ 2 again and again: remainders 0, 1, 0, 0, 0, 0, 0, 1, 1, 1; read upward → (1110000010)₂. (ii) groups of 3 from the point: 001 110 000 010 → (1602)₈; groups of 4 from the point: 0011 1000 0010 → (382)₁₆. (iii) 3 × 256 + 8 × 16 + 2 × 1 = 898. ✓

**Q4.** (i) Convert (579)₁₀ to binary. (ii) From your answer, write it in octal and hexadecimal without dividing again. (iii) Check the hexadecimal answer by converting it back to decimal. [4] *(M · 4.3)*

**Answer.** (i) 579 ÷ 2 again and again: remainders 1, 1, 0, 0, 0, 0, 1, 0, 0, 1; read upward → (1001000011)₂. (ii) groups of 3 from the point: 001 001 000 011 → (1103)₈; groups of 4 from the point: 0010 0100 0011 → (243)₁₆. (iii) 2 × 256 + 4 × 16 + 3 × 1 = 579. ✓

**Q5.** Convert (23.375)₁₀ to binary, then to octal and hexadecimal. [4] *(H · 4.4)*

**Answer.** Whole part: 23 ÷ 2 again and again: remainders 1, 1, 1, 0, 1; read upward → (10111)₂. Fraction: 0.375 × 2 = 0.75 → 0; 0.75 × 2 = 1.5 → 1; 0.5 × 2 = 1 → 1, exact. So (10111.011)₂. Octal: groups of 3 from the point: 010 111 . 011 → (27.3)₈. Hex: groups of 4 from the point: 0001 0111 . 0110 → (17.6)₁₆.

**Q6.** Convert (41.8125)₁₀ to binary, then to octal and hexadecimal. [4] *(H · 4.4)*

**Answer.** Whole part: 41 ÷ 2 again and again: remainders 1, 0, 0, 1, 0, 1; read upward → (101001)₂. Fraction: 0.8125 × 2 = 1.625 → 1; 0.625 × 2 = 1.25 → 1; 0.25 × 2 = 0.5 → 0; 0.5 × 2 = 1 → 1, exact. So (101001.1101)₂. Octal: groups of 3 from the point: 101 001 . 110 100 → (51.64)₈. Hex: groups of 4 from the point: 0010 1001 . 1101 → (29.D)₁₆.

**Q7.** Convert (13.6)₁₀ to binary (to 6 places if it does not end), then to octal and hexadecimal. [4] *(H · 4.4)*

**Answer.** Whole part: 13 ÷ 2 again and again: remainders 1, 0, 1, 1; read upward → (1101)₂. Fraction: 0.6 × 2 = 1.2 → 1; 0.2 × 2 = 0.4 → 0; 0.4 × 2 = 0.8 → 0; 0.8 × 2 = 1.6 → 1; 0.6 came back, so the digits 1001 repeat (to 6 places). So (1101.100110)₂. Octal: groups of 3 from the point: 001 101 . 100 110 → (15.46)₈. Hex: groups of 4 from the point: 1101 . 1001 1000 → (D.98)₁₆.

**Q8.** Convert (6357.42)₈ to hexadecimal. Show every step. [3] *(H · 4.3)*

**Answer.** To bits: 6 → 110, 3 → 011, 5 → 101, 7 → 111 . 4 → 100, 2 → 010 → (110011101111.10001)₂. Regroup: groups of 4 from the point: 1100 1110 1111 . 1000 1000 → (CEF.88)₁₆.

**Q9.** Convert (A9F.C8)₁₆ to octal. Show every step. [3] *(H · 4.3)*

**Answer.** To bits: A → 1010, 9 → 1001, F → 1111 . C → 1100, 8 → 1000 → (101010011111.11001)₂. Regroup: groups of 3 from the point: 101 010 011 111 . 110 010 → (5237.62)₈.

**Q10.** Explain the place-value method of converting a number in base b to decimal. Convert (2B.4)₁₆ to decimal. [3] *(M · 4.2)*

**Answer.** Multiply each digit by b to the power of its position (0, 1, 2 … left of the point; −1, −2 … right of it) and add. 2 × 16 + 11 × 1 + 4 × 1/16 = 43.25.

**Q11.** What is an encoding scheme? Compare ASCII, ISCII and Unicode in a table (four points). [4] *(M · 4.5)*

**Answer.** A table giving each character a fixed number that everyone uses.

| Basis of difference | ASCII | ISCII | Unicode |
|---|---|---|---|
| Bits | 7 | 8 | 8 to 32 per unit (UTF-8, UTF-32) |
| Characters | 128 | 256 | 159,801 (17.0) |
| Scripts | English | English + ten Indian | every script |
| First 128 codes | — | same as ASCII | same as ASCII |

**Q12.** Explain UTF-8 and UTF-32 with the parking-lot example. Which would you choose for a website, and why? [4] *(M · 4.5)*

**Answer.** UTF-8: slots cut to size, 1 to 4 bytes per character; small, but the 100th character is found by counting from the start. UTF-32: every slot bus-size, always 4 bytes; large, but the 100th character starts at byte 396. A website should use UTF-8: English and HTML stay 1 byte per character, old ASCII files work, and every script can still be stored.

**Q13.** How many bytes does "भारत 2047" take in UTF-8 and in UTF-32? Show the count. [3] *(H · 4.5)*

**Answer.** Code points: 4 Devanagari (भ, ा, र, त: the vowel sign ा is a code point of its own) and 5 ASCII (the space and 2, 0, 4, 7). UTF-8: 4 × 3 + 5 × 1 = **17 bytes**. UTF-32: 9 × 4 = **36 bytes**.

**Q14.** Encode the word "Kerala" in ASCII (decimal and 7-bit binary) and find its size in bytes in ASCII, UTF-8 and UTF-32. [4] *(M · 4.5)*

**Answer.** K 75 1001011 | e 101 1100101 | r 114 1110010 | a 97 1100001 | l 108 1101100 | a 97 1100001. Capital K is 75; the small letters are 32 more than their capitals (e 101, r 114, a 97, l 108). Size: ASCII 6 bytes, UTF-8 6 bytes, UTF-32 24 bytes.
