# Chapter 5: Problem Solving: Case studies (8)

*Chapter 5 · Questions (online). Each case has three parts. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch05_typed_questions.py`).*

## Case studies

**Q1.** **Case: the canteen token machine.** A machine takes the amount paid, the price of a thali (₹60) and gives tokens and change. (i) What are the inputs and outputs? (ii) Write the algorithm in steps for one customer paying ₹200 for 3 thalis. (iii) Which test data would you choose? *(M · 5.3)*

**Answer.** (i) Inputs: number of thalis, amount paid; outputs: tokens, change, or "pay more". (ii) bill = 3 × 60 = 180; is 200 ≥ 180? Yes: give 3 tokens and ₹20 change. (iii) Exact amount (180), less (150: "pay more"), much more (500), 0 thalis.

**Q2.** **Case: the class monitor election.** Votes for two candidates, A and B, are typed one by one; "X" ends. (i) Which block repeats? (ii) Write the pseudocode to count the votes and print the winner. (iii) What should happen on a tie? *(M · 5.6)*

**Answer.** (i) Reading a vote and adding it to a count. (ii) SET a = 0, b = 0; INPUT v; WHILE v ≠ "X": IF v = "A" THEN INCREMENT a ELSE INCREMENT b END IF; INPUT v; END WHILE; IF a > b THEN PRINT "A" ELSE IF b > a THEN PRINT "B" ELSE PRINT "Tie" END IF. (iii) A third result, "Tie", must be printed; a two-way IF would wrongly name B.

**Q3.** **Case: the bus pass.** Students under 18 travel free; 18 to 25 pay half (₹250); others pay ₹500. (i) Mark the decisions. (ii) Draw the ladder. (iii) Choose boundary test data. *(E · 5.5)*

**Answer.** (i) "under 18", "18 to 25": two decisions. (ii) age < 18? Yes: 0; No: age ≤ 25? Yes: 250; No: 500. (iii) 17, 18, 25, 26.

**Q4.** **Case: the library fine.** A book is due in 14 days; ₹2 a day for the next 10 late days, then ₹5 a day. (i) Write the conditions. (ii) Find the fine for 20 days and for 30 days. (iii) Which values are boundaries? *(H · 5.4)*

**Answer.** (i) days ≤ 14: 0; days ≤ 24: (days − 14) × 2; else 20 + (days − 24) × 5. (ii) 20 days: 6 × 2 = ₹12; 30 days: 20 + 6 × 5 = ₹50. (iii) 14, 15, 24, 25.

**Q5.** **Case: the cricket scorer.** The scorer writes the runs after every ball. (i) What is this like in a dry run? (ii) An over has 1, 4, 0, 6, 2, 1. Make the trace of the total. (iii) Why is one line per ball useful? *(E · 5.7)*

**Answer.** (i) A trace table, one row each time something changes. (ii) 1, 5, 5, 11, 13, 14. (iii) Any mistake can be found at the ball where it crept in.

**Q6.** **Case: finding a roll number.** The marks list of 1,000 students is sorted by roll number. (i) Which search would you use? (ii) At most how many looks? (iii) What if the list were sorted by name instead? *(M · 5.8)*

**Answer.** (i) Halving. (ii) 10. (iii) A search by roll number would have to go one by one (up to 1,000 looks), or the list must be sorted again by roll number.

**Q7.** **Case: the school app.** The school wants one app for attendance, fees, homework and results. (i) Decompose it. (ii) Which part would you build and test first, and why? (iii) What must all the parts agree on? *(M · 5.9)*

**Answer.** (i) Attendance, fees, homework, results, messages to parents. (ii) The student list (roll numbers and classes), because every other part uses it. (iii) The roll number of each student.

**Q8.** **Case: the electricity bill bug.** A program charges ₹5 a unit up to 100 units and ₹7 after; for 150 units it prints ₹1,050. (i) Is that right? (ii) What did the program do? (iii) Fix it. *(M · 5.7)*

**Answer.** (i) No: 100 × 5 + 50 × 7 = ₹850. (ii) It charged all 150 units at ₹7. (iii) bill = 500 + (units − 100) × 7 when units > 100.

