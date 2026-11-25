# Chapter 3: Boolean Logic and Logic Circuits: Assertion and reason (15)

*Chapter 3 · Questions (online). The questions of the printed chapter and many more, each followed by its answer and the reason. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every Boolean answer on this page was checked by a program (`tools/ch03_typed_questions.py`).*

For each question choose: (a) both A and R are true, and R explains A; (b) both are true, but R does not explain A; (c) A is true, R is false; (d) A is false, R is true.

**Q1.** A: An OR gate gives 1 when A = 1 and B = 1. R: An OR gate gives 1 when at least one input is 1. *(E · 3.2)*

**Answer.** (a). *Why:* R is the rule of OR, and it covers the case in A.

**Q2.** A: NAND is a universal gate. R: NAND gives 0 only when all inputs are 1. *(M · 3.3)*

**Answer.** (b). *Why:* both are true, but R only describes NAND; it does not say why every gate can be built from it.

**Q3.** A: NOR is a universal gate. R: The output of a NOR gate is 1 only when all inputs are 0. *(M · 3.3)*

**Answer.** (b). *Why:* both true, but R is only NOR's truth table, not the reason it can build every gate. *Exam tip:* ask "does R tell **why** A is true?"

**Q4.** A: A NAND gate gives 1 when A = 0 and B = 0. R: NAND is an AND gate followed by NOT. *(E · 3.3)*

**Answer.** (a). *Why:* AND gives 0, and the NOT turns it into 1: R explains A.

**Q5.** A: XOR is a universal gate. R: XOR gives 1 when its inputs differ. *(M · 3.4)*

**Answer.** (d). *Why:* A is false (only NAND and NOR are universal); R is true.

**Q6.** A: A NOT gate has one input. R: NOT is the only universal gate. *(E · 3.3)*

**Answer.** (c). *Why:* A is true; R is false (NAND and NOR are the universal gates).

**Q7.** A: A truth table with 3 inputs has 8 rows. R: Each input doubles the number of rows. *(E · 3.1)*

**Answer.** (a). *Why:* 2 × 2 × 2 = 8: R is the reason.

**Q8.** A: A · A' = 0. R: A and A' can never both be 1. *(E · 3.7)*

**Answer.** (a). *Why:* AND needs both to be 1.

**Q9.** A: A + A' is a tautology. R: A and A' are opposites, so one of them is always 1. *(E · 3.7)*

**Answer.** (a). *Why:* R is exactly why the OR is always 1.

**Q10.** A: An expression that is always 1 is a fallacy. R: A + A' is always 1. *(E · 3.7)*

**Answer.** (d). *Why:* A is false (that is a tautology); R is true.

**Q11.** A: The dual of A + A' = 1 is A · A' = 0. R: Duality swaps + with · and 1 with 0. *(E · 3.7)*

**Answer.** (a). *Why:* R is the rule that gives A.

**Q12.** A: The complement of A + B is A' + B'. R: De Morgan's law changes + into ·. *(M · 3.6)*

**Answer.** (d). *Why:* A is false (it is A'·B'); R is true.

**Q13.** A: (A + B)' = A' · B'. R: A prime over a bracket primes each letter but keeps the sign. *(M · 3.6)*

**Answer.** (c). *Why:* A is true (first law); R is false: the sign flips too.

**Q14.** A: Bubble pushing turns a NAND gate into an OR gate with NOT on its inputs. R: (A·B)' = A' + B'. *(H · 3.6)*

**Answer.** (a). *Why:* the picture is De Morgan's second law.

**Q15.** A: A + B·C and (A + B)·C are different expressions. R: AND is worked out before OR. *(M · 3.8)*

**Answer.** (a). *Why:* because AND comes first, A + B·C means A + (B·C), which differs from (A + B)·C.
