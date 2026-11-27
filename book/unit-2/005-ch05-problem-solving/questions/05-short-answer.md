# Chapter 5: Problem Solving: Short-answer questions (30)

*Chapter 5 · Questions (online). Two or three marks each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch05_typed_questions.py`).*

## Short answers

**Q1.** [2] Name the steps of problem solving in order. *(E · 5.2)*

**Answer.** Analyse the problem; develop an algorithm; code it; test it; debug it; and after delivery, maintain it.

**Q2.** [2] Give one difference between testing and debugging, with an example. *(E · 5.2)*

**Answer.** Testing shows THAT a fault exists (a student with 33 is told Fail); debugging finds WHY (the program asked "> 33") and fixes it (≥ 33).

**Q3.** [2] What are normal, extreme and abnormal test data for an age from 1 to 120? Give one of each. *(M · 5.2)*

**Answer.** Normal 35; extreme 1 or 120; abnormal −4 or 150 or "ten".

**Q4.** [2] Name the four kinds of testing named by NCERT. *(E · 5.2)*

**Answer.** Unit, integration, system, acceptance.

**Q5.** [2] Define an algorithm. Name its five characteristics. *(E · 5.3)*

**Answer.** A finite list of exact steps that turns the input into the output. Precision, uniqueness, finiteness, input, output.

**Q6.** [2] Why must an algorithm be finite? Give an example of a step that breaks it. *(E · 5.3)*

**Answer.** A step list that never ends gives no answer. "Keep asking for the PIN" (with no limit).

**Q7.** [2] Find the GCD and LCM of 36 and 24 by Euclid's method. *(M · 5.3)*

**Answer.** 36 ÷ 24 r 12; 24 ÷ 12 r 0: GCD 12. LCM = 36 × 24 ÷ 12 = 72.

**Q8.** [2] Write two differences between an algorithm and a program. *(E · 5.3)*

**Answer.** An algorithm is in plain words or a flowchart and cannot be run; a program is in a programming language and can be run. An algorithm is not tied to a language; a program is.

**Q9.** [2] Draw the symbols for a terminal, a process and a decision, and say what each is for. *(E · 5.4)*

**Answer.** Rounded rectangle: Start/Stop. Rectangle: a calculation or setting a value. Diamond: a Yes/No question.

**Q10.** [2] Name the three building blocks of an algorithm and give an ATM example of each. *(E · 5.4)*

**Answer.** Sequence: card, then PIN, then amount. Selection: PIN right? Repetition: up to 3 PIN tries.

**Q11.** [2] Write the condition: "marks are between 40 and 60, both included". *(M · 5.4)*

**Answer.** marks ≥ 40 AND marks ≤ 60.

**Q12.** [2] Write the condition: "a customer gets a discount on a bill over ₹5,000 or with a gold card". *(M · 5.4)*

**Answer.** bill > 5000 OR card = gold.

**Q13.** [2] What are the three things every loop needs? Show them in the ATM. *(M · 5.5)*

**Answer.** A start value (tries = 0), a test (tries = 3?) and a change inside the loop (tries = tries + 1).

**Q14.** [2] Mark the shapes for: "Accept marks of 40 students and display the average." *(M · 5.5)*

**Answer.** "Accept" input; "40 students" loop; "average" process (a formula); "display" output.

**Q15.** [2] Why does W6 test the lowest mark, and why ≥ rather than >? *(M · 5.5)*

**Answer.** If the lowest mark is 33 or more, every mark is. Exactly 33 passes, so ≥.

**Q16.** [2] Write pseudocode to print the even numbers from 2 to 20. *(E · 5.6)*

**Answer.** SET n = 2; WHILE n ≤ 20: PRINT n; COMPUTE n = n + 2; END WHILE.

**Q17.** [2] Write pseudocode to input a number and print whether it is positive, negative or zero. *(M · 5.6)*

**Answer.** INPUT n; IF n > 0 THEN PRINT "Positive" ELSE IF n < 0 THEN PRINT "Negative" ELSE PRINT "Zero" END IF.

**Q18.** [2] Give two differences between a flowchart and pseudocode. *(E · 5.6)*

**Answer.** A flowchart is a picture, pseudocode is text. A flowchart shows the flow at a glance; pseudocode is easier to change.

**Q19.** [2] What is a dry run? Why is it useful? *(E · 5.7)*

**Answer.** Following an algorithm by hand with sample inputs. It shows whether it gives the right answer, and where a wrong value appears.

**Q20.** [2] Find the bug: "IF age > 18 THEN PRINT 'Can vote'". Fix it. *(E · 5.7)*

**Answer.** An 18-year-old is refused. Use age ≥ 18.

**Q21.** [2] Find the bug: "SET i = 10; WHILE i > 0: PRINT i; INCREMENT i; END WHILE". *(M · 5.7)*

**Answer.** i grows 10, 11, 12 … and stays > 0: it never stops. DECREMENT i instead.

**Q22.** [2] Why is the "nice" test (5 h 20 min + 7 h 30 min) not enough for the time adder? *(M · 5.7)*

**Answer.** Its minutes add up to less than 60, so the missing carry never shows.

**Q23.** [2] What is time complexity? Give an example from the chapter. *(M · 5.8)*

**Answer.** How the number of steps grows with the input. One-by-one search needs up to n looks; halving needs about log₂ n.

**Q24.** [2] At most how many guesses find a number from 1 to 500 by halving? Why? *(M · 5.8)*

**Answer.** 9: 8 guesses handle only 255 numbers, 9 handle 511.

**Q25.** [2] Why does halving need a sorted list? *(E · 5.8)*

**Answer.** It throws away the half that cannot hold the name; that is known only if the list is in order.

**Q26.** [2] Why is dividing up to n ÷ 2 enough to test whether n is prime? *(M · 5.8)*

**Answer.** The smallest factor other than 1 is 2, so the largest other than n is n ÷ 2.

**Q27.** [2] Define decomposition and give two of its advantages. *(E · 5.9)*

**Answer.** Breaking a big problem into smaller parts. Each part is simpler; parts are built at the same time and tested alone.

**Q28.** [2] What is stepwise refinement? Show one step of it for "make tea". *(E · 5.9)*

**Answer.** Breaking a step into smaller steps. "Make tea" → boil water; add tea leaves; add milk and sugar; strain.

**Q29.** [2] Name the four parts of computational thinking. *(E · 5.9)*

**Answer.** Decomposition, pattern recognition, abstraction, algorithms.

**Q30.** [3] Decompose an online shopping app into five parts. *(M · 5.9)*

**Answer.** Catalogue (search, product pages); cart; payment; delivery (address, tracking); returns and reviews.

