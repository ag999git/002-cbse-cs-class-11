# Chapter 3: Boolean Logic and Logic Circuits: True or false (25)

*Chapter 3 · Questions (online). The questions of the printed chapter and many more, each followed by its answer and the reason. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every Boolean answer on this page was checked by a program (`tools/ch03_typed_questions.py`).*

**Q1.** A NOT gate can have two inputs. *(E · 3.2)*

**Answer.** False. *Why:* it has exactly one.

**Q2.** An OR gate gives 1 when both its inputs are 1. *(E · 3.2)*

**Answer.** True. *Why:* at least one input is 1.

**Q3.** An OR gate gives 0 in only one row of its truth table. *(E · 3.2)*

**Answer.** True. *Why:* only when all inputs are 0.

**Q4.** An XOR gate gives 1 when both its inputs are 1. *(E · 3.4)*

**Answer.** False. *Why:* XOR gives 0 when the inputs are the same; "exclusive" excludes the both-1 row.

**Q5.** XNOR is XOR followed by NOT. *(E · 3.4)*

**Answer.** True.

**Q6.** A 2-input NOR gate gives 1 in only one row of its truth table. *(E · 3.3)*

**Answer.** True. *Why:* only when both inputs are 0.

**Q7.** Every other gate can be built from NAND gates alone. *(E · 3.3)*

**Answer.** True. *Why:* NAND is a universal gate.

**Q8.** Two push-to-break switches in series make a NOR gate. *(M · 3.4)*

**Answer.** True. *Why:* the bulb lights only when neither is pressed.

**Q9.** Two switches in parallel make an AND gate. *(E · 3.4)*

**Answer.** False. *Why:* in parallel one closed switch is enough: that is OR.

**Q10.** The truth table of a NOT gate has two rows. *(E · 3.1)*

**Answer.** True. *Why:* one input: 2¹ = 2 rows.

**Q11.** "Shut the door" is a logical statement. *(E · 3.1)*

**Answer.** False. *Why:* an order is neither true nor false.

**Q12.** In Boolean algebra 1 + 1 = 10. *(E · 3.1)*

**Answer.** False. *Why:* + is OR, so 1 + 1 = 1. 1 + 1 = 10 is binary addition (Chapter 4).

**Q13.** A · A = A². *(E · 3.7)*

**Answer.** False. *Why:* A · A = A (idempotent law); Boolean algebra has no powers.

**Q14.** A · A' = 1. *(E · 3.7)*

**Answer.** False. *Why:* A and A' are never both 1: A·A' = 0.

**Q15.** A · (A + B) = A. *(M · 3.7)*

**Answer.** True. *Why:* absorption law (the dual of A + A·B = A).

**Q16.** A·B + A·B' = A. *(M · 3.7)*

**Answer.** True. *Why:* A·(B + B') = A·1 = A.

**Q17.** A + B·C = (A + B)·C. *(M · 3.7)*

**Answer.** False. *Why:* AND comes first, so A + B·C = A + (B·C). With A = 1, B = 0, C = 0 the left side is 1 and the right side is 0.

**Q18.** (A + B)' = A'·B'. *(E · 3.6)*

**Answer.** True. *Why:* De Morgan's first law.

**Q19.** (A · B)' = A' · B'. *(E · 3.6)*

**Answer.** False. *Why:* the sign must flip: (A · B)' = A' + B'. With A = 1, B = 0 the left side is 1 and A'·B' is 0.

**Q20.** The dual of an expression is the same as its complement. *(M · 3.7)*

**Answer.** False. *Why:* the dual does not prime the letters.

**Q21.** The dual is found by swapping + with · and 0 with 1, without priming the letters. *(E · 3.7)*

**Answer.** True.

**Q22.** If a Boolean law is true, its dual is also true. *(E · 3.7)*

**Answer.** True. *Why:* the principle of duality.

**Q23.** A tautology is 0 in every row. *(E · 3.7)*

**Answer.** False. *Why:* a tautology is 1 in every row; 0 in every row is a fallacy.

**Q24.** XNOR is the complement of XOR. *(E · 3.4)*

**Answer.** True. *Why:* XNOR = (A ⊕ B)'.

**Q25.** NOT has the highest priority among NOT, AND and OR. *(E · 3.8)*

**Answer.** True. *Why:* the order is brackets, NOT, AND, OR.
