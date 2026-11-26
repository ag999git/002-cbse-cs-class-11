# Sometimes asked: 1's and 2's complement

*Chapter 4 · Sometimes asked. Not in the syllabus wording, but asked in some school papers and needed for "how does a computer subtract?".*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. What they are

- **1's complement:** turn every bit round: 0 becomes 1, 1 becomes 0. (Like NOT in Chapter 3, on every bit.)
- **2's complement:** the 1's complement, **plus 1**.
- **Shortcut for the 2's complement:** from the right, copy the bits up to and including the first 1; turn round all the
  bits after it.

Always work with a **fixed number of bits** (here 8): the complement of a number depends on how many bits it has.

| Number (8 bits) | 1's complement | 2's complement | Check: number + 2's complement |
|:-:|:-:|:-:|---|
| 00000101 (5) | 11111010 | 11111011 | 5 + 251 = 256 = 2⁸: the carry leaves 8 zeros |
| 00001100 (12) | 11110011 | 11110100 | 12 + 244 = 256 = 2⁸: the carry leaves 8 zeros |
| 00101000 (40) | 11010111 | 11011000 | 40 + 216 = 256 = 2⁸: the carry leaves 8 zeros |
| 01100100 (100) | 10011011 | 10011100 | 100 + 156 = 256 = 2⁸: the carry leaves 8 zeros |
| 00000001 (1) | 11111110 | 11111111 | 1 + 255 = 256 = 2⁸: the carry leaves 8 zeros |
| 01111111 (127) | 10000000 | 10000001 | 127 + 129 = 256 = 2⁸: the carry leaves 8 zeros |

## 2. Why computers use the 2's complement

In 8 bits, the 2's complement of a number behaves exactly like its **negative**: adding it gives 0 (the carry out of the
eighth bit is dropped). So a computer can **subtract by adding**: A − B = A + (2's complement of B). One adding circuit does
both jobs.

## 3. Subtraction by adding

**13 − 6:** 00001101 + 11111010 (the 2's complement of 00000110) = 1 00000111; drop the carry: **00000111** = 7. ✓

**45 − 20:** 00101101 + 11101100 (the 2's complement of 00010100) = 1 00011001; drop the carry: **00011001** = 25. ✓

**100 − 37:** 01100100 + 11011011 (the 2's complement of 00100101) = 1 00111111; drop the carry: **00111111** = 63. ✓

## 4. Signed numbers in 8 bits

With the 2's complement, 8 bits hold **−128 to +127**. The leftmost bit tells the sign: 0 for positive, 1 for negative.
More on the "Beyond syllabus: signed numbers" page.

## 5. Practice (answers below each)

**Q1.** Find the 1's and 2's complement of 00001001 (8 bits).

**Answer.** 1's: 11110110; 2's: 11110111.

**Q2.** Find the 1's and 2's complement of 00011001 (8 bits).

**Answer.** 1's: 11100110; 2's: 11100111.

**Q3.** Find the 1's and 2's complement of 01000000 (8 bits).

**Answer.** 1's: 10111111; 2's: 11000000.

**Q4.** Find the 1's and 2's complement of 01001101 (8 bits).

**Answer.** 1's: 10110010; 2's: 10110011.

**Q5.** Find the 1's and 2's complement of 01111000 (8 bits).

**Answer.** 1's: 10000111; 2's: 10001000.

**Q6.** Using the 2's complement in 8 bits, find 20 − 7.

**Answer.** 00010100 + 11111001 → drop the carry → 00001101 = 13.

**Q7.** Using the 2's complement in 8 bits, find 50 − 18.

**Answer.** 00110010 + 11101110 → drop the carry → 00100000 = 32.

**Q8.** Using the 2's complement in 8 bits, find 91 − 45.

**Answer.** 01011011 + 11010011 → drop the carry → 00101110 = 46.

**Q9.** Using the 2's complement in 8 bits, find 64 − 1.

**Answer.** 01000000 + 11111111 → drop the carry → 00111111 = 63.

**Q10.** Using the 2's complement in 8 bits, find 99 − 99.

**Answer.** 01100011 + 10011101 → drop the carry → 00000000 = 0.

