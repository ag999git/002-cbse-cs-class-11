# Sometimes asked: double dabble: a second way from binary to decimal

*Chapter 4 · Sometimes asked. The printed book uses place values (Road 2) and points here for the second method that some teachers and books use.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. The method

Start with 0. Take the bits **from the left**. For each bit: **double what you have, then add the bit.**
When the bits are used up, you have the number in decimal.

**Example:** (110101)₂

| Have | Next bit | Double, then add | New value |
|:-:|:-:|---|:-:|
| 0 | 1 | 2 × 0 + 1 | **1** |
| 1 | 1 | 2 × 1 + 1 | **3** |
| 3 | 0 | 2 × 3 + 0 | **6** |
| 6 | 1 | 2 × 6 + 1 | **13** |
| 13 | 0 | 2 × 13 + 0 | **26** |
| 26 | 1 | 2 × 26 + 1 | **53** |

So (110101)₂ = (53)₁₀. Check by place values: 32 + 16 + 4 + 1 = 53. ✓

## 2. Why it works

Doubling moves everything one place to the **left** (every place is worth twice the place to its right), and adding the
new bit fills the units place. After the last bit, every bit has been doubled the right number of times: the leftmost bit
of a 6-bit number is doubled 5 times, so it is worth 2⁵ = 32, exactly its place value.

## 3. It works in any base

For octal, multiply by 8 instead of 2; for hex, by 16:

**(357)₈:** 0 × 8 + 3 = 3; 3 × 8 + 5 = 29; 29 × 8 + 7 = 239 → **239**.

**(2F9)₁₆:** 0 × 16 + 2 = 2; 2 × 16 + 15 = 47; 47 × 16 + 9 = 761 → **761**.

## 4. Which method should I use in the exam?

Either is correct. The **place-value** method (Road 2) shows the working most clearly and is what most marking schemes
expect; double dabble is quicker in your head for long binary numbers. Use one to work, the other to check.

## 5. Practice (answers below each)

**Q1.** Convert (1011)₂ to decimal by double dabble.

**Answer.** 1 → 2 → 5 → 11; so (1011)₂ = **11**.

**Q2.** Convert (11100)₂ to decimal by double dabble.

**Answer.** 1 → 3 → 7 → 14 → 28; so (11100)₂ = **28**.

**Q3.** Convert (100101)₂ to decimal by double dabble.

**Answer.** 1 → 2 → 4 → 9 → 18 → 37; so (100101)₂ = **37**.

**Q4.** Convert (1111111)₂ to decimal by double dabble.

**Answer.** 1 → 3 → 7 → 15 → 31 → 63 → 127; so (1111111)₂ = **127**.

**Q5.** Convert (10110110)₂ to decimal by double dabble.

**Answer.** 1 → 2 → 5 → 11 → 22 → 45 → 91 → 182; so (10110110)₂ = **182**.

**Q6.** Convert (110011001)₂ to decimal by double dabble.

**Answer.** 1 → 3 → 6 → 12 → 25 → 51 → 102 → 204 → 409; so (110011001)₂ = **409**.

**Q7.** Convert (76)₈ to decimal by "multiply and add".

**Answer.** 7 → 62; so **62**.

**Q8.** Convert (1234)₈ to decimal by "multiply and add".

**Answer.** 1 → 10 → 83 → 668; so **668**.

**Q9.** Convert (BAD)₁₆ to decimal by "multiply and add".

**Answer.** 11 → 186 → 2989; so **2989**.

**Q10.** Convert (7E5)₁₆ to decimal by "multiply and add".

**Answer.** 7 → 126 → 2021; so **2021**.

