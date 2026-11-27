# Explained: The four prime tests, worked

*Chapter 5 · Explained. The printed book (section 5.8) compares four ways to test whether a number is prime. Here each method is worked for 97, 91, 997 and 10,201, with the divisions counted by a program, and the reason why the shorter methods are still right.*

*Every number on this page was computed by a program (`tools/ch05_pages2.py`) and checked.*

## 1. The four methods

| Method | Divide n by | Stop |
|:-:|---|---|
| (i) | 2, 3, 4 … up to n − 1 | at the first divisor: n is **not prime** |
| (ii) | 2, 3, 4 … up to n ÷ 2 | the same |
| (iii) | 2, 3, 4 … while d × d ≤ n (up to √n) | the same |
| (iv) | the 25 primes up to 100, kept in a list (but never n itself) | the same; works only for n below 10,201 |

If no division leaves remainder 0, n is **prime**.

## 2. Divisions needed

| n | Really prime? | (i) | (ii) | (iii) | (iv) |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 97 | yes | 95, says prime | 47, says prime | 8, says prime | 24, says prime |
| 91 | no | 6, says not prime | 6, says not prime | 6, says not prime | 4, says not prime |
| 997 | yes | 995, says prime | 497, says prime | 30, says prime | 25, says prime |
| 10,201 | no | 100, says not prime | 100, says not prime | 100, says not prime | 25, says prime **(wrong!)** |
| 10,00,003 | yes | 10,00,001, says prime | 5,00,000, says prime | 999, says prime | not allowed |

- For a **prime** the method tries every divisor it allows, so the counts differ hugely: 995, 497, 30, 25 for 997.
- For a number that is **not** prime, every method stops at the first divisor: 91 = 7 × 13 stops at 7 in all four.
- For **10,201** method (iv) is **wrong**: none of the 25 primes up to 100 divides it, so it says "prime", but
  10,201 = 101 × 101. That is the limit of method (iv).

## 3. Method (iii) for 97, every division

| d | d × d | 97 ÷ d | Remainder |
|:-:|:-:|:-:|:-:|
| 2 | 4 | 48 | 1 |
| 3 | 9 | 32 | 1 |
| 4 | 16 | 24 | 1 |
| 5 | 25 | 19 | 2 |
| 6 | 36 | 16 | 1 |
| 7 | 49 | 13 | 6 |
| 8 | 64 | 12 | 1 |
| 9 | 81 | 10 | 7 |

The next d would be 10, but 10 × 10 = 100 is more than 97, so we stop: no remainder was 0, so **97 is prime**, after only **8** divisions (method (i) needs 95).

## 4. 91, by all four methods

| Method | Divisions made | Remainders |
|:-:|:-:|---|
| (i) | 6 | 91 ÷ 2 r 1, 91 ÷ 3 r 1, 91 ÷ 4 r 3, 91 ÷ 5 r 1, 91 ÷ 6 r 1, 91 ÷ 7 r 0 |
| (ii) | 6 | 91 ÷ 2 r 1, 91 ÷ 3 r 1, 91 ÷ 4 r 3, 91 ÷ 5 r 1, 91 ÷ 6 r 1, 91 ÷ 7 r 0 |
| (iii) | 6 | 91 ÷ 2 r 1, 91 ÷ 3 r 1, 91 ÷ 4 r 3, 91 ÷ 5 r 1, 91 ÷ 6 r 1, 91 ÷ 7 r 0 |
| (iv) | 4 | 91 ÷ 2 r 1, 91 ÷ 3 r 1, 91 ÷ 5 r 1, 91 ÷ 7 r 0 |

All four stop at 7: 91 ÷ 7 = 13 remainder **0**, so 91 is **not prime**. *Trap:* 91 looks prime; always test it.

## 5. Why n ÷ 2 is enough (method ii)

Any divisor of n other than n itself is **at most n ÷ 2**, because the smallest other factor is 2, and n = 2 × (n ÷ 2). For 100 the divisors are 1, 2, 4, 5, 10, 20, 25, 50, 100: after 50 the next is 100 itself.

## 6. Why √n is enough (method iii)

Factors come in **pairs** whose product is n:

- 100 = 1 × 100 = 2 × 50 = 4 × 25 = 5 × 20 = 10 × 10; √100 = 10.
- 36 = 1 × 36 = 2 × 18 = 3 × 12 = 4 × 9 = 6 × 6; √36 = 6.

In every pair the smaller factor is at most √n. So if no number up to √n divides n, no number above √n can either: its partner would have been found already.

## 7. Why method (iv) works below 10,201, and its two limits

- A number that is not prime has a factor ≤ its square root (section 6), and so a **prime** factor ≤ its square root.
  Below 10,201 = 101 × 101 the square root is below 101, so that prime factor is one of the 25 primes up to 100.
- **Limit 1:** do not divide n by itself. 7 is in the list and 7 ÷ 7 leaves 0, yet 7 is prime.
- **Limit 2:** from 10,201 on, a number can have all its prime factors above 100: 10,201 = 101 × 101 slips through.
- Its price is **memory**: the list of 25 primes must be stored. That is time against space (section 5.8).

## 8. Try it yourself

**Test 221 by method (iii). How many divisions?**

??? success "Answer"
    12 divisions (d = 2 to 13). 221 ÷ 13 leaves 0 (221 = 13 × 17), so 221 is not prime.

**Test 113 by method (iii). How many divisions?**

??? success "Answer"
    9 divisions (d = 2 to 10). 11 × 11 = 121 is more than 113, and no remainder was 0, so 113 is prime.

