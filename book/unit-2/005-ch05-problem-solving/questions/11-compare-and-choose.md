# Chapter 5: Problem Solving: Compare and choose (20)

*Chapter 5 · Questions (online). Counting steps (section 5.8). Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch05_typed_questions.py`).*

## Compare and choose

**Q1.** At most how many looks does halving need to find a name among 50 sorted names? One by one? *(M · 5.8)*

**Answer.** Halving **6**, one by one **50**. *Why:* 5 looks handle only 31 names; 6 looks handle 63.

**Q2.** At most how many looks does halving need to find a name among 200 sorted names? One by one? *(M · 5.8)*

**Answer.** Halving **8**, one by one **200**. *Why:* 7 looks handle only 127 names; 8 looks handle 255.

**Q3.** At most how many looks does halving need to find a name among 4,000 sorted names? One by one? *(M · 5.8)*

**Answer.** Halving **12**, one by one **4,000**. *Why:* 11 looks handle only 2,047 names; 12 looks handle 4,095.

**Q4.** At most how many looks does halving need to find a name among 10,00,000 sorted names? One by one? *(M · 5.8)*

**Answer.** Halving **20**, one by one **10,00,000**. *Why:* 19 looks handle only 5,24,287 names; 20 looks handle 10,48,575.

**Q5.** At most how many looks does halving need to find a name among 64 sorted names? One by one? *(M · 5.8)*

**Answer.** Halving **7**, one by one **64**. *Why:* 6 looks handle only 63 names; 7 looks handle 127.

**Q6.** Among the 16 names A to P in order, which names does halving open to find C? *(M · 5.8)*

**Answer.** H, D, B, C: **4** looks (one by one: 3).

**Q7.** Among the 16 names A to P in order, which names does halving open to find J? *(M · 5.8)*

**Answer.** H, L, J: **3** looks (one by one: 10).

**Q8.** Among the 16 names A to P in order, which names does halving open to find O? *(M · 5.8)*

**Answer.** H, L, N, O: **4** looks (one by one: 15).

**Q9.** How many divisions does Euclid need for the GCD of 48 and 36, and how many does listing all divisors need? *(M · 5.8)*

**Answer.** Euclid **2** (GCD 12); listing **84** (48 + 36 trial divisions).

**Q10.** How many divisions does Euclid need for the GCD of 100 and 75, and how many does listing all divisors need? *(M · 5.8)*

**Answer.** Euclid **2** (GCD 25); listing **175** (100 + 75 trial divisions).

**Q11.** How many divisions does Euclid need for the GCD of 610 and 377, and how many does listing all divisors need? *(M · 5.8)*

**Answer.** Euclid **13** (GCD 1); listing **987** (610 + 377 trial divisions).

**Q12.** How many divisions do methods (i) n − 1, (ii) n ÷ 2 and (iii) √n make to test 101? Is it prime? *(H · 5.8)*

**Answer.** (i) 99, (ii) 49, (iii) 9: **prime**.

**Q13.** How many divisions do methods (i) n − 1, (ii) n ÷ 2 and (iii) √n make to test 143? Is it prime? *(H · 5.8)*

**Answer.** (i) 10, (ii) 10, (iii) 10: **not prime**. 143 = 11 × 13.

**Q14.** How many divisions do methods (i) n − 1, (ii) n ÷ 2 and (iii) √n make to test 1,009? Is it prime? *(H · 5.8)*

**Answer.** (i) 1,007, (ii) 503, (iii) 30: **prime**.

**Q15.** To add 1 + 2 + … + 100, how many additions does a loop make, and how many operations does the formula n(n + 1) ÷ 2 make? *(E · 5.8)*

**Answer.** Loop: **100** additions; formula: **3** operations. Both give 5,050.

**Q16.** To add 1 + 2 + … + 1,000, how many additions does a loop make, and how many operations does the formula n(n + 1) ÷ 2 make? *(E · 5.8)*

**Answer.** Loop: **1,000** additions; formula: **3** operations. Both give 5,00,500.

**Q17.** Which uses more memory: testing primes by dividing up to √n, or by a stored list of the 25 primes up to 100? *(E · 5.8)*

**Answer.** The stored list: it must be kept in memory. Dividing up to √n stores nothing extra.

**Q18.** For 10,201, which prime method gives a wrong answer, and why? *(H · 5.8)*

**Answer.** Method (iv): none of the 25 primes up to 100 divides 10,201, so it says prime, but 10,201 = 101 × 101.

**Q19.** A phone has 2,000 contacts in order. A student says halving needs 1,000 looks at most. Is that right? *(M · 5.8)*

**Answer.** No: at most **11** (2¹¹ − 1 = 2,047). Halving throws away half of what is LEFT at every look.

**Q20.** An algorithm takes 4 steps for 10 items and 400 for 1,000. Another takes 20 steps for 10 items and 60 for 1,000. Which is better for large lists? *(H · 5.8)*

**Answer.** The second: its steps grow slowly (like halving); the first grows with the number of items, and much faster.

