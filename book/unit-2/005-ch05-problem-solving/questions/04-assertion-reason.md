# Chapter 5: Problem Solving: Assertion and reason (15)

*Chapter 5 · Questions (online). One mark each. *Choose:* (a) both A and R are true and R explains A; (b) both are true but R does not explain A; (c) A is true, R is false; (d) A is false, R is true. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch05_typed_questions.py`).*

## Assertion and reason

**Q1.** A: Debugging comes after testing. R: Testing shows that a fault exists. *(E · 5.2)*

**Answer.** (a). you can only look for the cause of a fault that has been found.

**Q2.** A: Boundary values must be tested. R: Faults often hide at the limits, such as > instead of ≥. *(E · 5.2)*

**Answer.** (a). the pass-mark bug shows only for exactly 33.

**Q3.** A: An algorithm must be finite. R: Every algorithm has at least one input. *(M · 5.3)*

**Answer.** (c). R is false: an algorithm may have no input.

**Q4.** A: Euclid's method always stops. R: Each remainder is smaller than the divisor before it. *(H · 5.3)*

**Answer.** (a). the numbers shrink, so the remainder must reach 0.

**Q5.** A: The same algorithm can be coded in Python and in Java. R: An algorithm is not tied to any language. *(E · 5.3)*

**Answer.** (a). the plan is the same in every language.

**Q6.** A: A decision box has two ways out. R: A condition is either true or false. *(E · 5.4)*

**Answer.** (a). Yes and No are the only two answers.

**Q7.** A: Input is drawn in a parallelogram. R: The parallelogram is also used for output. *(M · 5.4)*

**Answer.** (b). both true; R does not say why input uses it.

**Q8.** A: The ATM allows only three wrong PINs. R: A 4-digit PIN has 10,000 possible values. *(M · 5.4)*

**Answer.** (a). with unlimited tries a thief could try them all.

**Q9.** A: The shortcut "a > b AND a > c, then b > a AND b > c, else c" is wrong. R: With two equal largest numbers both tests are No. *(H · 5.5)*

**Answer.** (a). 5, 5, 2 gives 2.

**Q10.** A: In W6, the grade questions are asked from 90 down. R: In a ladder the first Yes decides the answer. *(M · 5.5)*

**Answer.** (a). asking ≥ 60 first would give C to everyone above 60.

**Q11.** A: Pseudocode can be run by a computer. R: Pseudocode uses keywords like IF and WHILE. *(E · 5.6)*

**Answer.** (d). A is false: it must first be coded.

**Q12.** A: A trace table helps to find logical errors. R: It shows the value of every variable after each step. *(M · 5.7)*

**Answer.** (a). you see the step where a value goes wrong.

**Q13.** A: Halving is faster than one-by-one search for a sorted list. R: Each look throws away half of what is left. *(E · 5.8)*

**Answer.** (a). 100 → 50 → 25 …: 7 looks for 100 names.

**Q14.** A: Method (iv) of prime testing needs more memory. R: It divides by the 25 primes up to 100, kept in a list. *(M · 5.8)*

**Answer.** (a). the list must be stored.

**Q15.** A: Decomposition makes testing easier. R: Each part can be tested alone before the parts are joined. *(E · 5.9)*

**Answer.** (a). unit testing, then integration testing.

