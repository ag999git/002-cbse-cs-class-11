# Chapter 4: Number Systems and Encoding Schemes: Short-answer questions (1, 2 and 3 marks) (30)

*Chapter 4 · Questions (online). Answers as they should be written in the exam. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch04_typed_questions.py`).*

## Concepts

**Q1.** Why does a computer use binary and not decimal? *(E · 4.1)*

**Answer.** A switch or a wire has two states (on/off, high/low voltage). Two states are easy and safe to tell apart; ten voltage levels would be confused whenever the voltage wobbles.

**Q2.** Why do people use octal and hexadecimal if the computer uses binary? *(E · 4.1)*

**Answer.** Long strings of bits are hard to read and copy; one octal digit stands for 3 bits and one hex digit for 4, so the same value is written in a third or a quarter of the length.

**Q3.** What is meant by the base of a number system? Give the base of each of the four systems. *(E · 4.1)*

**Answer.** The number of digits it uses (also called radix): binary 2, octal 8, decimal 10, hexadecimal 16.

**Q4.** Why does hexadecimal need letters? *(E · 4.1)*

**Answer.** It has 16 digits but we have only ten digit symbols (0–9); six single symbols were needed for ten to fifteen, so A–F are used. "15" would be read as two digits.

**Q5.** What is place value? Explain with the number (725)₈. *(M · 4.2)*

**Answer.** What a digit is worth because of its place: digit × base^position. 7 × 64 + 2 × 8 + 5 × 1 = 448 + 16 + 5 = 469.

**Q6.** What are the MSB and the LSB? Name them in (101100)₂. *(E · 4.2)*

**Answer.** The MSB is the leftmost bit (largest place value, here the 1 worth 32); the LSB is the rightmost bit (here the 0 worth 1).

**Q7.** Write the next three numbers after (7)₈ in octal. *(E · 4.2)*

**Answer.** (10)₈, (11)₈, (12)₈. *Why:* after 7 the units place rolls over and carries.

**Q8.** Why are the remainders read upward in the division method? *(M · 4.3)*

**Answer.** The first remainder is the units digit, the last digit of the answer; each later remainder belongs one place further left.

**Q9.** Why is grouping by 3 bits allowed for octal? *(M · 4.3)*

**Answer.** Because 8 = 2³: 3 bits have exactly 8 patterns, one for each octal digit, so each group is exactly one octal digit.

**Q10.** Why is octal to hexadecimal done through binary and not directly? *(M · 4.3)*

**Answer.** 8 and 16 are not powers of each other, so their digits do not match group to group; both are powers of 2, so binary is the bridge.

**Q11.** Why are the digits read downward in the multiplication method for fractions? *(M · 4.4)*

**Answer.** Multiplying by the base moves the digit nearest the point across it first, so the first digit found is the first after the point.

**Q12.** When do you stop multiplying when converting a decimal fraction? *(M · 4.4)*

**Answer.** When the fraction part becomes 0 (exact), when a fraction part repeats (it goes on for ever), or when the question gives the number of places.

**Q13.** What is an encoding scheme? Why is it needed? *(E · 4.5)*

**Answer.** A table that gives every character a fixed number (code) that everyone agrees on. A computer can store only numbers, and everyone must use the same table so that text moves correctly between computers.

**Q14.** Differentiate between ASCII and ISCII (two points). *(E · 4.5)*

**Answer.** | Basis of difference | ASCII | ISCII |
|---|---|---|
| Bits, codes | 7 bits, 128 | 8 bits, 256 |
| Scripts | English only | English + ten Indian scripts |

**Q15.** What is a code point? Give the code point of A and of ₹. *(E · 4.5)*

**Answer.** The unique number Unicode gives a character, written U+ and hex: A = U+0041, ₹ = U+20B9.

**Q16.** Give two advantages of UTF-8 over UTF-32. *(E · 4.5)*

**Answer.** English (ASCII) text takes 1 byte per letter instead of 4; old ASCII files are already valid UTF-8.

**Q17.** Give one advantage of UTF-32 over UTF-8. *(M · 4.5)*

**Answer.** Every character has the same size, so the nth character is found directly (it starts at byte 4 × (n − 1)) and characters are counted as bytes ÷ 4.

**Q18.** Why could ASCII not become a world standard? *(M · 4.5)*

**Answer.** It has only 128 codes, enough for English; the 8-bit extensions filled codes 128–255 differently from maker to maker.

## Conversions

**Q19.** Convert (520)₁₀ to octal and hexadecimal. [2] *(E · 4.3)*

**Answer.** 520 ÷ 8 again and again: remainders 0, 1, 0, 1; read upward → (1010)₈. 520 ÷ 16 again and again: remainders 8, 0, 2; read upward → (208)₁₆. So (520)₁₀ = (1010)₈ = (208)₁₆.

**Q20.** Convert (982)₁₀ to octal and hexadecimal. [2] *(E · 4.3)*

**Answer.** 982 ÷ 8 again and again: remainders 6, 2, 7, 1; read upward → (1726)₈. 982 ÷ 16 again and again: remainders 6, D (13), 3; read upward → (3D6)₁₆. So (982)₁₀ = (1726)₈ = (3D6)₁₆.

**Q21.** Convert (990)₁₀ to octal and hexadecimal. [2] *(E · 4.3)*

**Answer.** 990 ÷ 8 again and again: remainders 6, 3, 7, 1; read upward → (1736)₈. 990 ÷ 16 again and again: remainders E (14), D (13), 3; read upward → (3DE)₁₆. So (990)₁₀ = (1736)₈ = (3DE)₁₆.

**Q22.** Convert (10110111110)₂ to octal and hexadecimal. [2] *(E · 4.3)*

**Answer.** groups of 3 from the point: 010 110 111 110 → (2676)₈; groups of 4 from the point: 0101 1011 1110 → (5BE)₁₆.

**Q23.** Convert (11000111000)₂ to octal and hexadecimal. [2] *(E · 4.3)*

**Answer.** groups of 3 from the point: 011 000 111 000 → (3070)₈; groups of 4 from the point: 0110 0011 1000 → (638)₁₆.

**Q24.** Convert (11101010011)₂ to octal and hexadecimal. [2] *(E · 4.3)*

**Answer.** groups of 3 from the point: 011 101 010 011 → (3523)₈; groups of 4 from the point: 0111 0101 0011 → (753)₁₆.

**Q25.** Convert (1A2)₁₆ to octal. [2] *(M · 4.3)*

**Answer.** To bits: 1 → 0001, A → 1010, 2 → 0010 → (110100010)₂; regroup in 3s: groups of 3 from the point: 110 100 010 → (642)₈.

**Q26.** Convert (515)₁₆ to octal. [2] *(M · 4.3)*

**Answer.** To bits: 5 → 0101, 1 → 0001, 5 → 0101 → (10100010101)₂; regroup in 3s: groups of 3 from the point: 010 100 010 101 → (2425)₈.

**Q27.** Convert (A46)₁₆ to octal. [2] *(M · 4.3)*

**Answer.** To bits: A → 1010, 4 → 0100, 6 → 0110 → (101001000110)₂; regroup in 3s: groups of 3 from the point: 101 001 000 110 → (5106)₈.

**Q28.** Convert (0.6875)₁₀ to binary. [2] *(M · 4.4)*

**Answer.** 0.6875 × 2 = 1.375 → 1; 0.375 × 2 = 0.75 → 0; 0.75 × 2 = 1.5 → 1; 0.5 × 2 = 1 → 1; fraction now 0, so (0.6875)₁₀ = (0.1011)₂.

**Q29.** Convert (0.40625)₁₀ to binary. [2] *(M · 4.4)*

**Answer.** 0.40625 × 2 = 0.8125 → 0; 0.8125 × 2 = 1.625 → 1; 0.625 × 2 = 1.25 → 1; 0.25 × 2 = 0.5 → 0; 0.5 × 2 = 1 → 1; fraction now 0, so (0.40625)₁₀ = (0.01101)₂.

**Q30.** Convert (0.15625)₁₀ to binary. [2] *(M · 4.4)*

**Answer.** 0.15625 × 2 = 0.3125 → 0; 0.3125 × 2 = 0.625 → 0; 0.625 × 2 = 1.25 → 1; 0.25 × 2 = 0.5 → 0; 0.5 × 2 = 1 → 1; fraction now 0, so (0.15625)₁₀ = (0.00101)₂.
