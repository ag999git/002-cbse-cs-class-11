# Challenge: puzzles with bases

*Chapter 4 · Challenge. For students who like a puzzle. Each answer is below its question; try first.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

**Q1.** In which base b does "121" mean 49?

**Answer.** b = 6. *Why:* 121 in base 6 = 1 × 6^2 + 2 × 6^1 + 1 × 6^0 = 49.

**Q2.** In which base b does "144" mean 81?

**Answer.** b = 7. *Why:* 144 in base 7 = 1 × 7^2 + 4 × 7^1 + 4 × 7^0 = 81.

**Q3.** In which base b does "1000" mean 343?

**Answer.** b = 7. *Why:* 1000 in base 7 = 1 × 7^3 + 0 × 7^2 + 0 × 7^1 + 0 × 7^0 = 343.

**Q4.** Which is the largest: (777)₈, (1FF)₁₆, (111111111)₂?

**Answer.** All are 511! (777)₈ = 511, (1FF)₁₆ = 511, (111111111)₂ = 511. *Why:* each is "all top digits", and 8³ = 2⁹ = 512, and 1FF = 1 0000 0000 − 1 in binary terms.

**Q5.** With four weights of 1, 3, 9 and 27 kg on a balance (a weight may go on either pan), every whole number of kilograms from 1 to 40 can be weighed. Why 40, and why these weights?

**Answer.** 1 + 3 + 9 + 27 = 40. Each weight can be on the left pan, the right pan, or off: three choices, like the digits −1, 0, 1 of a base-3 system ("balanced ternary"). For example 5 = 9 − 3 − 1: 9 with the load on one side, 3 and 1 with the load on the other.

**Q6.** A number is 2-digit in decimal and 7-digit in binary. Which numbers can it be?

**Answer.** Seven bits cover 64 to 127; two decimal digits cover 10 to 99. So **64 to 99**.

**Q7.** Why does every odd number end in 1 in binary, and why does a multiple of 8 end in 000?

**Answer.** The last bit is the units place; odd means one unit is left over. A multiple of 8 = 2³ has nothing in the 1, 2 and 4 places, so its last three bits are 0 (just as a multiple of 1000 ends in 000 in decimal).

**Q8.** Without converting to decimal, is (3A7)₁₆ even or odd?

**Answer.** Odd. *Why:* 16 is even, so only the last digit decides; 7 is odd.

**Q9.** How many digits does 2¹⁰⁰ have in binary, octal and hexadecimal?

**Answer.** 2¹⁰⁰ is 1 followed by 100 zeros in binary: **101 bits**. 100 = 3 × 33 + 1, so in octal it is 2 followed by 33 zeros: **34 digits**. 100 = 4 × 25, so in hex it is 1 followed by 25 zeros: **26 digits**.
