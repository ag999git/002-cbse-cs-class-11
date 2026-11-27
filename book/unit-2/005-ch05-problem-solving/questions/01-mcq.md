# Chapter 5: Problem Solving: Multiple-choice questions (45)

*Chapter 5 · Questions (online). One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch05_typed_questions.py`).*

## Problems and steps (5.1, 5.2)

**Q1.** The first step of problem solving is to: (a) write the code (b) analyse the problem (c) test the program (d) draw the flowchart *(E · 5.2)*

**Answer.** (b) analyse the problem. *Why:* you must know the inputs and outputs before any steps can be written.

**Q2.** Finding WHERE and WHY a program gives a wrong answer is called: (a) testing (b) coding (c) debugging (d) analysis *(E · 5.2)*

**Answer.** (c) debugging. *Why:* testing shows that a fault exists; debugging finds its cause and removes it.

**Q3.** Changing a program after it is delivered (for a new grade table) is: (a) debugging (b) maintenance (c) analysis (d) acceptance testing *(E · 5.2)*

**Answer.** (b) maintenance. *Why:* the program worked; the need changed.

**Q4.** A teacher types 39 instead of 93 and the report card is wrong. This shows that: (a) the algorithm is wrong (b) wrong input gives wrong output (c) the computer made a mistake (d) the program needs debugging *(E · 5.1)*

**Answer.** (b) wrong input gives wrong output. *Why:* the computer follows the steps exactly with whatever it is given.

**Q5.** Testing each part of a program alone is: (a) unit testing (b) integration testing (c) system testing (d) acceptance testing *(E · 5.2)*

**Answer.** (a) unit testing. *Why:* a unit is one part; integration testing joins the parts.

**Q6.** Testing done by the user before the program is delivered is: (a) unit testing (b) integration testing (c) acceptance testing (d) debugging *(E · 5.2)*

**Answer.** (c) acceptance testing. *Why:* the user accepts (or refuses) the program.

**Q7.** For marks from 0 to 100, which is boundary test data? (a) 67 (b) 33 (c) "sixty" (d) −5 *(M · 5.2)*

**Answer.** (b) 33. *Why:* 33 is the pass mark: a limit. 67 is normal; "sixty" and −5 are abnormal.

**Q8.** Which test data must the program REFUSE? (a) 0 (b) 100 (c) −5 (d) 33 *(E · 5.2)*

**Answer.** (c) −5. *Why:* a mark cannot be negative; 0 and 100 are extreme but allowed.

**Q9.** The grammar of a programming language is its: (a) syntax (b) algorithm (c) pseudocode (d) output *(E · 5.2)*

**Answer.** (a) syntax. *Why:* a syntax error breaks the grammar (Chapter 8).

## Algorithms (5.3)

**Q10.** An algorithm is: (a) a program in Python (b) a finite list of exact steps that solves a problem (c) a flowchart only (d) a kind of computer *(E · 5.3)*

**Answer.** (b) a finite list of exact steps that solves a problem. *Why:* it can be written in words, pseudocode or a flowchart, and in any language.

**Q11.** "Keep asking for the PIN" (for ever) breaks: (a) precision (b) finiteness (c) input (d) output *(E · 5.3)*

**Answer.** (b) finiteness. *Why:* an algorithm must always stop.

**Q12.** "Give some money" breaks: (a) finiteness (b) precision (c) uniqueness (d) input *(E · 5.3)*

**Answer.** (b) precision. *Why:* "some" is not exact.

**Q13.** An algorithm may have no input, but it must have: (a) a loop (b) at least one output (c) a decision (d) a variable *(M · 5.3)*

**Answer.** (b) at least one output. *Why:* Knuth: input zero or more, output one or more ("print 1 to 10" has no input).

**Q14.** "Print tomorrow's Sensex" is exact but cannot be done. It breaks: (a) finiteness (b) effectiveness (c) output (d) input *(H · 5.3)*

**Answer.** (b) effectiveness. *Why:* effectiveness means every step can really be carried out.

**Q15.** The word "algorithm" comes from the name of: (a) Euclid (b) al-Khwarizmi (c) Knuth (d) Aryabhata *(E · 5.3)*

**Answer.** (b) al-Khwarizmi. *Why:* his book on Indian numerals survives as "Algoritmi de numero Indorum".

**Q16.** Euclid's method finds the GCD of 30 and 21 in: (a) 1 division (b) 2 divisions (c) 3 divisions (d) 51 divisions *(M · 5.3)*

**Answer.** (c) 3 divisions. *Why:* 30 ÷ 21 r 9; 21 ÷ 9 r 3; 9 ÷ 3 r 0.

**Q17.** Which is true of an algorithm and a program? (a) both are tied to one language (b) an algorithm can be run directly by a computer (c) a program is an algorithm written in a programming language (d) an algorithm is always longer *(M · 5.3)*

**Answer.** (c) a program is an algorithm written in a programming language. *Why:* the algorithm is the plan; the program is the plan in Python (or another language).

**Q18.** In the ATM, the step "the same card, PIN and amount always give the same result" shows: (a) finiteness (b) uniqueness (c) precision (d) input *(M · 5.3)*

**Answer.** (b) uniqueness. *Why:* each step's result depends only on the input and the steps before.

## Flowcharts (5.4, 5.5)

**Q19.** Which symbol holds a Yes/No question? (a) rectangle (b) parallelogram (c) diamond (d) rounded rectangle *(E · 5.4)*

**Answer.** (c) diamond. *Why:* a decision has one way in and two ways out.

**Q20.** "Input a, b" is drawn in a: (a) rectangle (b) parallelogram (c) diamond (d) circle *(E · 5.4)*

**Answer.** (b) parallelogram. *Why:* the parallelogram is for input and output.

**Q21.** "sum = a + b" is drawn in a: (a) rectangle (b) parallelogram (c) diamond (d) oval *(E · 5.4)*

**Answer.** (a) rectangle. *Why:* a calculation is a process.

**Q22.** The small circle with a letter in a flowchart is a: (a) terminal (b) connector (c) decision (d) process *(E · 5.4)*

**Answer.** (b) connector. *Why:* it joins two parts of a long chart.

**Q23.** How many Start symbols may a flowchart have? (a) none (b) exactly one (c) one for each loop (d) any number *(E · 5.4)*

**Answer.** (b) exactly one. *Why:* an algorithm has one beginning.

**Q24.** Repeating "enter the PIN" up to three times is: (a) sequence (b) selection (c) repetition (d) decomposition *(E · 5.4)*

**Answer.** (c) repetition. *Why:* the same steps are done again.

**Q25.** Which signal word points to a LOOP? (a) calculate (b) whether (c) until (d) display *(E · 5.5)*

**Answer.** (c) until. *Why:* "until" means repeat until a condition holds.

**Q26.** "Only students with 75% attendance may sit" contains a hidden: (a) loop (b) decision (c) output (d) connector *(M · 5.5)*

**Answer.** (b) decision. *Why:* there is no "if", but a choice is made.

**Q27.** A loop needs a start value, a test and: (a) a connector (b) a change inside the loop (c) two Stops (d) an output *(M · 5.5)*

**Answer.** (b) a change inside the loop. *Why:* without the change the test never becomes No: the loop never ends.

**Q28.** "Find the sum of n numbers" is mainly a: (a) process (b) decision (c) loop (d) terminal *(M · 5.5)*

**Answer.** (c) loop. *Why:* "find" can be three shapes; here n numbers means repeat.

**Q29.** In W5, the greatest of three, the shortcut "a > b AND a > c, then b > a AND b > c, else c" gives the wrong answer for: (a) 1, 2, 3 (b) 5, 5, 2 (c) 3, 2, 1 (d) 2, 9, 4 *(H · 5.5)*

**Answer.** (b) 5, 5, 2. *Why:* with a = b = 5 both tests are No, so it prints c = 2.

**Q30.** In the five-step method, the step after Read is: (a) List (b) Draw (c) Mark (d) Check *(E · 5.5)*

**Answer.** (c) Mark. *Why:* Read, Mark, List, Draw, Check.

## Pseudocode, dry runs and comparing (5.6 to 5.9)

**Q31.** Pseudocode is: (a) a programming language (b) a picture of the steps (c) steps in structured English that a computer cannot run (d) machine code *(E · 5.6)*

**Answer.** (c) steps in structured English that a computer cannot run. *Why:* pseudo = false: it looks like code but is for people.

**Q32.** Which keyword repeats while a condition is true? (a) IF (b) WHILE (c) PRINT (d) INPUT *(E · 5.6)*

**Answer.** (b) WHILE. *Why:* WHILE … END WHILE.

**Q33.** In pseudocode, indentation shows: (a) the output (b) which lines are inside an IF or a loop (c) comments (d) the input *(E · 5.6)*

**Answer.** (b) which lines are inside an IF or a loop. *Why:* indented lines belong to the block above them.

**Q34.** A trace table has one column for each: (a) step (b) variable (c) symbol (d) input only *(E · 5.7)*

**Answer.** (b) variable. *Why:* it records how every variable changes.

**Q35.** Following an algorithm by hand with sample inputs is a: (a) dry run (b) compilation (c) decomposition (d) flowchart *(E · 5.7)*

**Answer.** (a) dry run. *Why:* it is done on paper, without a computer.

**Q36.** At most how many looks does halving need for 1,000 sorted contacts? (a) 10 (b) 100 (c) 500 (d) 1,000 *(M · 5.8)*

**Answer.** (a) 10. *Why:* 2¹⁰ − 1 = 1,023 names can be handled in 10 looks.

**Q37.** Halving search works only when the list is: (a) short (b) in order (c) of numbers (d) printed *(E · 5.8)*

**Answer.** (b) in order. *Why:* it throws away the half that cannot hold the name, which needs the order.

**Q38.** Which prime test uses the most memory? (a) divide up to n − 1 (b) divide up to n ÷ 2 (c) divide up to √n (d) divide by a stored list of primes *(M · 5.8)*

**Answer.** (d) divide by a stored list of primes. *Why:* it must keep the list.

**Q39.** How many divisions does "up to √n" need to show that 997 is prime? (a) 30 (b) 497 (c) 995 (d) 25 *(H · 5.8)*

**Answer.** (a) 30. *Why:* d = 2 to 31, because 31 × 31 = 961 ≤ 997 < 32 × 32.

**Q40.** Breaking a big problem into smaller parts is: (a) debugging (b) decomposition (c) abstraction (d) iteration *(E · 5.9)*

**Answer.** (b) decomposition. *Why:* each part can then be solved and tested separately.

**Q41.** A metro map shows stations and lines but not streets. This is: (a) decomposition (b) abstraction (c) pattern recognition (d) an algorithm *(M · 5.9)*

**Answer.** (b) abstraction. *Why:* abstraction keeps only what matters.

**Q42.** Building a program from small ready-made parts is: (a) top-down design (b) bottom-up design (c) stepwise refinement (d) unit testing *(M · 5.9)*

**Answer.** (b) bottom-up design. *Why:* top-down starts from the whole and breaks it down.

**Q43.** Two programs of 500 lines are easier than one of 1,000 lines because: (a) they are shorter in total (b) effort grows faster than size (c) they need no testing (d) they use less memory *(H · 5.9)*

**Answer.** (b) effort grows faster than size. *Why:* with effort as size squared: 25 + 25 = 50 units against 100.

**Q44.** Which pair of words means the same? (a) loop and decision (b) repetition and iteration (c) sequence and selection (d) input and output *(E · 5.4)*

**Answer.** (b) repetition and iteration. *Why:* a loop = repetition = iteration.

**Q45.** The formula n(n + 1) ÷ 2 for 1 + 2 + … + n needs, whatever n is: (a) n additions (b) three operations (c) n multiplications (d) no operations *(M · 5.8)*

**Answer.** (b) three operations. *Why:* one addition, one multiplication, one division.

