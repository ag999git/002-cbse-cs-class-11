# Chapter 4: Number Systems and Encoding Schemes: Case studies (8)

*Chapter 4 · Questions (online). Each case has three parts. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Case studies

**Q1.** **Case: the school scoreboard.** A digital scoreboard shows runs in binary lights. The score is 147. (i) Which lights are on? (ii) How many lights are needed for scores up to 300? (iii) Write 147 in hexadecimal for the scorer's app. *(M · 4.3)*

**Answer.** (i) 10010011 (128 + 16 + 2 + 1). (ii) 9, because 2⁸ = 256 is too few and 2⁹ = 512 is enough. (iii) (93)₁₆.

**Q2.** **Case: file permissions.** On a Linux computer, a teacher gives a file the permission 750 (octal). (i) Write 750 in binary. (ii) Each group of 3 bits is read (r), write (w), run (x) for the owner, the group and others: what may each do? (iii) Why is octal convenient here? *(M · 4.3)*

**Answer.** (i) 111 101 000. (ii) owner rwx (read, write, run); group r-x (read, run); others --- (nothing). (iii) Each octal digit is exactly 3 bits, one bit for each permission.

**Q3.** **Case: the school website colour.** The designer chooses the colour #2E8B57. (i) What are the red, green and blue values in decimal? (ii) How many bits does one colour need? (iii) How many colours can be made? *(M · 4.3)*

**Answer.** (i) red 2E = 46, green 8B = 139, blue 57 = 87. (ii) 24 bits (3 bytes). (iii) 2²⁴ = 16,777,216.

**Q4.** **Case: a secret note.** Riya sends Arjun the numbers 83 87 65 67 72 72. (i) Decode them in ASCII. (ii) Write the first code in binary. (iii) How would the note change if every number were 32 more? *(E · 4.5)*

**Answer.** (i) SWACHH. (ii) 83 = 1010011. (iii) every letter would become small: "swachh".

**Q5.** **Case: a Hindi message.** A phone sends "नमस्ते भारत". It has 11 code points: all Devanagari except one space. (i) How many bytes in UTF-8? (ii) In UTF-32? (iii) Which should the app use, and why? *(M · 4.5)*

**Answer.** (i) 10 × 3 + 1 = **31 bytes**. (ii) 11 × 4 = **44 bytes**. (iii) UTF-8: smaller here, used by the web, and the same app can send English cheaply.

**Q6.** **Case: garbled text.** A shop's bill shows "â‚¹ 250" where "₹ 250" should be. (i) What has gone wrong? (ii) How many bytes does ₹ take in UTF-8? (iii) How can it be fixed? *(M · 4.5)*

**Answer.** (i) The ₹ was stored in UTF-8 but read with an old one-byte table, so its 3 bytes became 3 characters. (ii) 3 (E2 82 B9). (iii) Read the text as UTF-8 (both sides must use the same encoding).

**Q7.** **Case: storing roll numbers.** A school has 1,800 students. (i) How many bits are needed for each roll number? (ii) How many hexadecimal digits? (iii) Write roll number 1,500 in hex. *(M · 4.2)*

**Answer.** (i) 11, because 2¹⁰ = 1024 is too few and 2¹¹ = 2048 is enough. (ii) 3 (11 bits fit in 3 × 4 = 12). (iii) (5DC)₁₆.

**Q8.** **Case: an old Hindi file.** A government office has documents typed in ISCII in the 1990s. (i) How many codes does ISCII have? (ii) Why can such a file not hold Hindi and Tamil together? (iii) Why should the office convert them to Unicode? *(M · 4.5)*

**Answer.** (i) 256 (8 bits). (ii) All Indian scripts share the same upper 96 places, so a file holds one Indian script at a time. (iii) Unicode gives every script its own block, works on every device and is the standard used for e-governance.
