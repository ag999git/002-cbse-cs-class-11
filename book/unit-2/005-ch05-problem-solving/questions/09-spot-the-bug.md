# Chapter 5: Problem Solving: Spot the bug (15)

*Chapter 5 · Questions (online). Each flowchart is a book flowchart with one or two boxes changed. Find what goes wrong by a dry run. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch05_typed_questions.py`).*

## Spot the bug

**Q1.** In the flowchart of W6 (report card: result and grade), box 4 asks "low > 33?". Dry-run it for 33, 40, 50, 60, 70: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **Fail**; it should print **Grade D**. *Fix:* low ≥ 33.

**Q2.** In the flowchart of W6 (report card: result and grade), box 3 divides the total by 4. Dry-run it for 80, 75, 70, 72, 78: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **Grade A**; it should print **Grade B**. *Fix:* divide by 5.

**Q3.** In the flowchart of W6 (report card: result and grade), the ladder asks ≥ 60 first. Dry-run it for 95, 92, 88, 91, 94: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **Grade C**; it should print **Grade A**. *Fix:* ask 90, then 75, then 60.

**Q4.** In the flowchart of W6 (report card: result and grade), box 3 takes the HIGHEST mark as low. Dry-run it for 20, 90, 90, 90, 90: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **Grade B**; it should print **Fail**. *Fix:* the lowest mark: min.

**Q5.** In the flowchart of W7 (average of numbers until 0 is typed), count starts at 1. Dry-run it for 6, 9, 0: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **5.0**; it should print **7.5**. *Fix:* count = 0.

**Q6.** In the flowchart of W7 (average of numbers until 0 is typed), the average divides by count + 1 (the 0 is counted). Dry-run it for 4, 8, 6, 0: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **4.5**; it should print **6.0**. *Fix:* avg = sum ÷ count.

**Q7.** In the flowchart of W8 (gcd and lcm by euclid's method), boxes 6 and 7 move the values the wrong way. Dry-run it for 30, 21: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **nothing: it stops with division by zero**; it should print **3 210**. *Fix:* a = b, then b = r.

**Q8.** In the flowchart of W10 (the factorial of n), fact starts at 0. Dry-run it for 5: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **0**; it should print **120**. *Fix:* fact = 1.

**Q9.** In the flowchart of W10 (the factorial of n), the loop asks "i < n?". Dry-run it for 5: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **24**; it should print **120**. *Fix:* i ≤ n.

**Q10.** In the flowchart of W9 (the series 1 + x + x² + … + xⁿ), sum starts at 0, so the first term 1 is never added. Dry-run it for 2, 3: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **14**; it should print **15**. *Fix:* sum = 1.

**Q11.** In the flowchart of W9 (the series 1 + x + x² + … + xⁿ), box 5 adds x instead of multiplying. Dry-run it for 2, 3: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **16**; it should print **15**. *Fix:* term = term × x.

**Q12.** In the flowchart of W3 (the larger of two numbers), box 3 asks "a < b?" but prints a on Yes. Dry-run it for 7, 12: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **7**; it should print **12**. *Fix:* a > b.

**Q13.** In the flowchart of W4 (even or odd), box 3 asks "remainder = 1?" but its Yes prints Even. Dry-run it for 8: what does it print, what should it print, and what is the fix? *(M · 5.7)*

**Answer.** It prints **Odd**; it should print **Even**. *Fix:* remainder of n ÷ 2 = 0.

**Q14.** In W8, box 8 is written "lcm = x × y ÷ b". What happens for 30, 21, and why? *(H · 5.7)*

**Answer.** It stops with **division by zero**: the loop ends when b = 0, so x × y ÷ b divides by 0. The GCD is in **a** at that point: lcm = x × y ÷ a = 210.

**Q15.** The greatest of three is written as: IF a > b AND a > c THEN PRINT a ELSE IF b > a AND b > c THEN PRINT b ELSE PRINT c. Dry-run it for 5, 5, 2. *(H · 5.5)*

**Answer.** It prints **2**; the greatest is 5. Both tests are No because neither 5 is greater than the other. *Fix:* the nested tests of W5 (or use ≥).

