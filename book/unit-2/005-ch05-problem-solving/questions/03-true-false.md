# Chapter 5: Problem Solving: True or false (35)

*Chapter 5 · Questions (online). One mark each. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every number on this page was computed and checked by a program (`tools/ch05_typed_questions.py`).*

## True or false

**Q1.** Testing and debugging mean the same. *(E · 5.2)*

**Answer.** False. *Why:* testing finds that something is wrong; debugging finds the cause and removes it.

**Q2.** Analysis comes before writing the algorithm. *(E · 5.2)*

**Answer.** True. *Why:* the inputs and outputs must be known first.

**Q3.** A program that passes one test is correct. *(M · 5.7)*

**Answer.** False. *Why:* one test can miss boundary values; the time adder passed one test and failed another.

**Q4.** The word "bug" was first used when a moth was found in a computer. *(M · 5.2)*

**Answer.** False. *Why:* the word was already used for faults; the 1947 moth made it famous.

**Q5.** An algorithm can be written without a computer language. *(E · 5.3)*

**Answer.** True. *Why:* in plain words, pseudocode or a flowchart.

**Q6.** An algorithm must have at least one input. *(M · 5.3)*

**Answer.** False. *Why:* zero or more inputs; "print 1 to 10" has none.

**Q7.** An algorithm must have at least one output. *(M · 5.3)*

**Answer.** True. *Why:* otherwise it achieves nothing that can be seen.

**Q8.** Euclid's method needs the larger number first. *(H · 5.3)*

**Answer.** False. *Why:* if the smaller is first, round 1 gives quotient 0 and swaps the numbers.

**Q9.** The GCD of 17 and 5 is 1. *(M · 5.3)*

**Answer.** True. *Why:* 17 ÷ 5 r 2; 5 ÷ 2 r 1; 2 ÷ 1 r 0.

**Q10.** A flowchart may have two Stop symbols. *(M · 5.4)*

**Answer.** False. *Why:* this book's rule (and the exam's): one Start and one Stop; paths join before Stop.

**Q11.** A rectangle is used for input. *(E · 5.4)*

**Answer.** False. *Why:* input and output use the parallelogram.

**Q12.** A decision box can have three ways out. *(M · 5.4)*

**Answer.** False. *Why:* a Yes/No question has two answers; a third choice needs a second diamond.

**Q13.** An oval is accepted for the terminal symbol. *(E · 5.4)*

**Answer.** True. *Why:* this book draws a rounded rectangle, as NCERT does.

**Q14.** A loop must always have a counter. *(M · 5.4)*

**Answer.** False. *Why:* it may stop on a condition, such as "until 0 is typed".

**Q15.** "Accept numbers till 0 is entered" signals a loop. *(E · 5.5)*

**Answer.** True. *Why:* "till" means repeat until.

**Q16.** "Find the area" always means a loop. *(M · 5.5)*

**Answer.** False. *Why:* it is a process (a formula); "find" can be three shapes.

**Q17.** In W6, "≥ 33" and "> 33" give the same result for every mark. *(M · 5.5)*

**Answer.** False. *Why:* for exactly 33, > says Fail.

**Q18.** The flowchart of W10 (factorial) prints 1 for n = 0. *(H · 5.5)*

**Answer.** True. *Why:* the loop never runs and fact stays 1; 0! = 1.

**Q19.** A computer can run pseudocode directly. *(E · 5.6)*

**Answer.** False. *Why:* it must first be written in a programming language.

**Q20.** There is one fixed standard for pseudocode. *(E · 5.6)*

**Answer.** False. *Why:* styles differ; the steps must be exact and in order.

**Q21.** IF … THEN … ELSE shows selection. *(E · 5.6)*

**Answer.** True. *Why:* it chooses one of two paths.

**Q22.** A dry run needs a computer. *(E · 5.7)*

**Answer.** False. *Why:* it is done by hand, on paper.

**Q23.** A trace table shows only the final answer. *(E · 5.7)*

**Answer.** False. *Why:* it shows every value after each step or round.

**Q24.** "i = 1; WHILE i ≤ 10: PRINT i; END WHILE" stops after 10 lines. *(M · 5.7)*

**Answer.** False. *Why:* i never changes, so it prints 1 for ever.

**Q25.** Halving search works on any list. *(E · 5.8)*

**Answer.** False. *Why:* only on a list in order.

**Q26.** Halving finds any of 16 sorted names in at most 4 looks. *(H · 5.8)*

**Answer.** False. *Why:* at most 5: P, for example, needs H, L, N, O, P.

**Q27.** Dividing up to √n is enough to test whether n is prime. *(M · 5.8)*

**Answer.** True. *Why:* factors come in pairs, one of each pair is at most √n.

**Q28.** Dividing by the 25 primes up to 100 correctly tests 10,201. *(H · 5.8)*

**Answer.** False. *Why:* 10,201 = 101 × 101 has no prime factor up to 100.

**Q29.** A faster algorithm is always better. *(M · 5.8)*

**Answer.** False. *Why:* it may need more memory, or a sorted list.

**Q30.** Remembering tables instead of counting is time against space. *(M · 5.8)*

**Answer.** True. *Why:* it saves time but uses memory.

**Q31.** Decomposition lets parts be built by different teams at the same time. *(E · 5.9)*

**Answer.** True. *Why:* each part is simpler and can be tested alone.

**Q32.** Stepwise refinement is also called top-down design. *(E · 5.9)*

**Answer.** True. *Why:* a big step is broken into smaller steps.

**Q33.** Unit testing checks that the parts work together. *(E · 5.9)*

**Answer.** False. *Why:* that is integration testing; unit testing checks one part alone.

**Q34.** Pattern recognition means noticing what repeats. *(M · 5.9)*

**Answer.** True. *Why:* every grade in W6 is one more "% ≥ …?".

**Q35.** Computational thinking is only for programmers. *(M · 5.9)*

**Answer.** False. *Why:* Jeannette Wing: a way of solving problems that everyone should learn.

