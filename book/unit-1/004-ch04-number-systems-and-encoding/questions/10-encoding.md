# Chapter 4: Number Systems and Encoding Schemes: Encoding: ASCII and Unicode (30)

*Chapter 4 · Questions (online). Section 4.5. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Encode in ASCII

**Q1.** Encode "INDIA" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 73 78 68 73 65; in binary 1001001 1001110 1000100 1001001 1000001.

**Q2.** Encode "Delhi" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 68 101 108 104 105; in binary 1000100 1100101 1101100 1101000 1101001.

**Q3.** Encode "CODE" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 67 79 68 69; in binary 1000011 1001111 1000100 1000101.

**Q4.** Encode "Byte" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 66 121 116 101; in binary 1000010 1111001 1110100 1100101.

**Q5.** Encode "KV2" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 75 86 50; in binary 1001011 1010110 0110010.

**Q6.** Encode "ok!" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 111 107 33; in binary 1101111 1101011 0100001.

**Q7.** Encode "Hi 5" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 72 105 32 53; in binary 1001000 1101001 0100000 0110101.

**Q8.** Encode "RAM" in ASCII (decimal and 7-bit binary). *(E · 4.5)*

**Answer.** 82 65 77; in binary 1010010 1000001 1001101.

## Decode ASCII

**Q9.** Decode the ASCII codes 77 85 77 66 65 73. *(E · 4.5)*

**Answer.** "MUMBAI". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

**Q10.** Decode the ASCII codes 67 104 97 105. *(E · 4.5)*

**Answer.** "Chai". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

**Q11.** Decode the ASCII codes 66 72 65 82 65 84. *(E · 4.5)*

**Answer.** "BHARAT". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

**Q12.** Decode the ASCII codes 68 97 116 97. *(E · 4.5)*

**Answer.** "Data". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

**Q13.** Decode the ASCII codes 71 79 32 49 49. *(E · 4.5)*

**Answer.** "GO 11". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

**Q14.** Decode the ASCII codes 84 97 106. *(E · 4.5)*

**Answer.** "Taj". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

**Q15.** Decode the ASCII codes 67 80 85. *(E · 4.5)*

**Answer.** "CPU". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

**Q16.** Decode the ASCII codes 89 101 115. *(E · 4.5)*

**Answer.** "Yes". *Hint:* A = 65, a = 97, space = 32, '0' = 48.

## Bytes in UTF-8 and UTF-32

**Q17.** How many bytes does "Hello" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **5**, UTF-32 **20** (5 code points × 4). *Working (UTF-8 bytes per code point):* H 1, e 1, l 1, l 1, o 1.

**Q18.** How many bytes does "नमस्ते" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **18**, UTF-32 **24** (6 code points × 4). *Working (UTF-8 bytes per code point):* न 3, म 3, स 3, ् 3, त 3, े 3.

**Q19.** How many bytes does "₹500" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **6**, UTF-32 **16** (4 code points × 4). *Working (UTF-8 bytes per code point):* ₹ 3, 5 1, 0 1, 0 1.

**Q20.** How many bytes does "India भारत" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **18**, UTF-32 **40** (10 code points × 4). *Working (UTF-8 bytes per code point):* I 1, n 1, d 1, i 1, a 1, space 1, भ 3, ा 3, र 3, त 3.

**Q21.** How many bytes does "தமிழ்" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **15**, UTF-32 **20** (5 code points × 4). *Working (UTF-8 bytes per code point):* த 3, ம 3, ி 3, ழ 3, ் 3.

**Q22.** How many bytes does "😀 OK" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **7**, UTF-32 **16** (4 code points × 4). *Working (UTF-8 bytes per code point):* 😀 4, space 1, O 1, K 1.

**Q23.** How many bytes does "é" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **2**, UTF-32 **4** (1 code points × 4). *Working (UTF-8 bytes per code point):* é 2.

**Q24.** How many bytes does "क ख ग" take in UTF-8 and in UTF-32? *(M · 4.5)*

**Answer.** UTF-8 **11**, UTF-32 **20** (5 code points × 4). *Working (UTF-8 bytes per code point):* क 3, space 1, ख 3, space 1, ग 3.

## Code points

**Q25.** Write the Unicode code point of "B" (latin capital letter b) and its value in decimal. *(M · 4.5)*

**Answer.** U+0042 = 66. *Why:* (hex to decimal) 4 × 16 + 2 × 1 = 66.

**Q26.** Write the Unicode code point of "z" (latin small letter z) and its value in decimal. *(M · 4.5)*

**Answer.** U+007A = 122. *Why:* (hex to decimal) 7 × 16 + 10 × 1 = 122.

**Q27.** Write the Unicode code point of "ई" (devanagari letter ii) and its value in decimal. *(M · 4.5)*

**Answer.** U+0908 = 2312. *Why:* (hex to decimal) 9 × 256 + 8 × 1 = 2312.

**Q28.** Write the Unicode code point of "ङ" (devanagari letter nga) and its value in decimal. *(M · 4.5)*

**Answer.** U+0919 = 2329. *Why:* (hex to decimal) 9 × 256 + 16 + 9 × 1 = 2329.

**Q29.** Write the Unicode code point of "₹" (indian rupee sign) and its value in decimal. *(M · 4.5)*

**Answer.** U+20B9 = 8377. *Why:* (hex to decimal) 2 × 4096 + 11 × 16 + 9 × 1 = 8377.

**Q30.** Write the Unicode code point of "©" (copyright sign) and its value in decimal. *(M · 4.5)*

**Answer.** U+00A9 = 169. *Why:* (hex to decimal) 10 × 16 + 9 × 1 = 169.
