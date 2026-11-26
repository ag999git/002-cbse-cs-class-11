# Sometimes asked: binary arithmetic

*Chapter 4 · Sometimes asked. Not in the syllabus wording, but school papers set it now and then. The printed book points here at the end of section 4.4.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. The four rules of binary addition

| Sum | Result | Write | Carry | Like in decimal |
|:-:|:-:|:-:|:-:|---|
| 0 + 0 | 0 | 0 | 0 | 0 + 0 |
| 0 + 1 | 1 | 1 | 0 | 0 + 1 |
| 1 + 0 | 1 | 1 | 0 | 1 + 0 |
| 1 + 1 | (10)₂ = 2 | 0 | 1 | 9 + 1 = 10: write 0, carry 1 |
| 1 + 1 + 1 | (11)₂ = 3 | 1 | 1 | (with a carry coming in) |

*Why a carry at 1 + 1?* Binary has no digit 2. Two in binary is "10": one in the twos place, nothing in the units. It is
the meter rolling over (section 4.2).

## 2. Worked examples

**Add (1011)₂ and (110)₂.**

```
carry    111  
          1011
     +     110
       -------
         10001
```
Check in decimal: 11 + 6 = 17. ✓

**Add (11011)₂ and (1101)₂.**

```
carry    11111 
          11011
     +     1101
       --------
         101000
```
Check in decimal: 27 + 13 = 40. ✓

**Add (111111)₂ and (1)₂.**

```
carry    111111 
          111111
     +         1
       ---------
         1000000
```
Check in decimal: 63 + 1 = 64. ✓

## 3. Subtraction with borrowing

| Difference | Result | Note |
|:-:|:-:|---|
| 0 − 0 | 0 | |
| 1 − 0 | 1 | |
| 1 − 1 | 0 | |
| 0 − 1 | 1, borrow 1 | borrow from the next place: (10)₂ − 1 = 1 |

- (1101)₂ − (110)₂ = **(111)₂**. Check: 13 − 6 = 7. ✓
- (10000)₂ − (1)₂ = **(1111)₂**. Check: 16 − 1 = 15. ✓

Computers do not subtract this way: they add the **2's complement** instead (next page).

## 4. Common mistakes

| Mistake | Why it is wrong | Correct |
|---|---|---|
| 1 + 1 = 2 | there is no digit 2 in binary | 1 + 1 = (10)₂: write 0, carry 1 |
| forgetting the carry in the last column | the carry is a new leftmost digit | 1 + 1 at the left end gives a new 1 in front |
| 1 + 1 + 1 = 10 | three is (11)₂ | write 1, carry 1 |

## 5. Practice (answers below each)

**Q1.** (101)₂ + (11)₂

**Answer.** (1000)₂. *Check:* 5 + 3 = 8.

**Q2.** (1110)₂ + (1011)₂

**Answer.** (11001)₂. *Check:* 14 + 11 = 25.

**Q3.** (10101)₂ + (1111)₂

**Answer.** (100100)₂. *Check:* 21 + 15 = 36.

**Q4.** (110110)₂ + (101101)₂

**Answer.** (1100011)₂. *Check:* 54 + 45 = 99.

**Q5.** (1111)₂ + (1111)₂

**Answer.** (11110)₂. *Check:* 15 + 15 = 30.

**Q6.** (1100)₂ − (101)₂

**Answer.** (111)₂. *Check:* 12 − 5 = 7.

**Q7.** (10010)₂ − (111)₂

**Answer.** (1011)₂. *Check:* 18 − 7 = 11.

**Q8.** (11111)₂ − (10101)₂

**Answer.** (1010)₂. *Check:* 31 − 21 = 10.

**Q9.** (100000)₂ − (1)₂

**Answer.** (11111)₂. *Check:* 32 − 1 = 31.

**Q10.** (1011)₂ − (1011)₂

**Answer.** (0)₂. *Check:* 11 − 11 = 0.

