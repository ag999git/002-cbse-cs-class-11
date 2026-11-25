# Chapter 3: Boolean Logic and Logic Circuits: Multiple-choice questions (40)

*Chapter 3 · Questions (online). The questions of the printed chapter and many more, each followed by its answer and the reason. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every Boolean answer on this page was checked by a program (`tools/ch03_typed_questions.py`).*

## 3.2–3.3 The gates

**Q1.** Which gate gives output 1 only when all its inputs are 1? *(E · 3.2)*  
(a) OR (b) AND (c) NOR (d) XOR

**Answer.** (b) AND. *How to answer:* write the letter **and** the name.

**Q2.** The gate that gives 1 when its two inputs are the same: *(E · 3.4)*  
(a) XOR (b) XNOR (c) NAND (d) OR

**Answer.** (b) XNOR. *Why:* it is XOR turned round.

**Q3.** Which gate gives 1 when all inputs are 0? *(E · 3.3)*  
(a) AND (b) OR (c) NOR (d) XOR

**Answer.** (c) NOR. *Why:* OR gives 0 then, and NOR turns it round.

**Q4.** Which gate gives 0 only when all its inputs are 1? *(E · 3.3)*  
(a) AND (b) OR (c) NAND (d) NOR

**Answer.** (c) NAND. *Why:* AND gives 1 only then, and NAND turns it round.

**Q5.** The output of a NOR gate when A = 0 and B = 1 is *(E · 3.3)*  
(a) 0 (b) 1 (c) 01 (d) cannot be found

**Answer.** (a) 0. *Why:* one input is 1, so OR gives 1 and NOR turns it to 0.

**Q6.** NAND is *(E · 3.3)*  
(a) NOT then AND (b) AND then NOT (c) OR then NOT (d) AND then OR

**Answer.** (b). *Why:* the bubble is at the output.

**Q7.** An OR symbol with a bubble at its output is the *(E · 3.3)*  
(a) NAND gate (b) XNOR gate (c) NOR gate (d) NOT gate

**Answer.** (c) NOR gate: Y = (A + B)'.

**Q8.** Which is the expression of the XOR gate? *(M · 3.4)*  
(a) A·B + A'·B' (b) A'·B + A·B' (c) A + B (d) (A·B)'

**Answer.** (b). *Why:* each term is 1 in one of the two rows where A and B differ. (a) is XNOR.

**Q9.** 1 ⊕ 1 ⊕ 1 = ? *(M · 3.5)*  
(a) 0 (b) 1 (c) 3 (d) 2

**Answer.** (b) 1. *Why:* an odd number of 1s.

**Q10.** Which is NOT a universal gate? *(E · 3.3)*  
(a) NAND (b) NOR (c) XOR (d) none

**Answer.** (c) XOR. *Why:* only NAND and NOR can build every gate.

**Q11.** Joining both inputs of a NOR gate gives *(M · 3.3)*  
(a) AND (b) OR (c) NOT (d) XOR

**Answer.** (c) NOT. *Why:* (A + A)' = A' (idempotent law).

**Q12.** How many NAND gates are needed to make an AND gate? *(M · 3.3)*  
(a) 1 (b) 2 (c) 3 (d) 4

**Answer.** (b) 2. *Why:* one NAND gives (A·B)'; a second NAND with its inputs joined turns it round: ((A·B)')' = A·B.

**Q13.** How many NOR gates are needed to make an OR gate? *(M · 3.3)*  
(a) 1 (b) 2 (c) 3 (d) 4

**Answer.** (b) 2. *Why:* one NOR gives (A + B)'; a second NOR with joined inputs turns it round.

**Q14.** Switches in parallel make *(E · 3.4)*  
(a) AND (b) OR (c) NOT (d) XOR

**Answer.** (b) OR. *Why:* one closed switch is enough.

**Q15.** A staircase light that can be switched from either end works like the *(M · 3.4)*  
(a) AND gate (b) OR gate (c) XOR gate (d) NAND gate

**Answer.** (c) XOR gate. *Why:* flipping either switch changes the light (section 3.4).

**Q16.** In a Venn diagram, shading only the overlap of circles A and B shows *(E · 3.2)*  
(a) A + B (b) A·B (c) A' (d) A ⊕ B

**Answer.** (b) A·B (AND): only the part that is in both.

## 3.1 and 3.5 Truth tables

**Q17.** How many rows has the truth table of a 4-input AND gate? *(E · 3.1)*  
(a) 4 (b) 8 (c) 16 (d) 32

**Answer.** (c) 16. *Why:* 2⁴.

**Q18.** How many rows has the truth table of an expression in A, B and C? *(E · 3.1)*  
(a) 3 (b) 6 (c) 8 (d) 9

**Answer.** (c) 8. *Why:* 2³; each input doubles the rows. *Trap:* not 2 × 3 = 6.

**Q19.** In a truth table of A, B, C written in counting order, the 6th row is *(M · 3.1)*  
(a) 1 0 1 (b) 1 1 0 (c) 1 0 0 (d) 0 1 1

**Answer.** (a) 1 0 1. *Why:* the rows count 0 to 7, so the 6th row is 5 = 101 in binary.

**Q20.** The value of Y = (A + B)'·C when A = 0, B = 0, C = 1 is *(M · 3.5)*  
(a) 0 (b) 1 (c) 2 (d) C'

**Answer.** (b) 1. *Why:* A + B = 0, so (A + B)' = 1, and 1·1 = 1.

## 3.6–3.7 Laws, De Morgan, duality

**Q21.** A + 1 = ? *(E · 3.7)*  
(a) A (b) 1 (c) 0 (d) A'

**Answer.** (b) 1. *Why:* null law: one 1 is enough for OR.

**Q22.** A · 0 = ? *(E · 3.7)*  
(a) A (b) 1 (c) 0 (d) A'

**Answer.** (c) 0. *Why:* null law: one 0 keeps AND at 0.

**Q23.** A · 1 = ? *(E · 3.7)*  
(a) 0 (b) 1 (c) A (d) A'

**Answer.** (c) A. *Why:* identity law: a 1 does not change an AND.

**Q24.** A + A = ? *(E · 3.7)*  
(a) 2A (b) A (c) 1 (d) 0

**Answer.** (b) A. *Why:* idempotent law; there is no "2" in Boolean algebra.

**Q25.** A · A' = ? *(E · 3.7)*  
(a) 1 (b) A (c) 0 (d) A'

**Answer.** (c) 0. *Why:* complement law: A and A' are never both 1.

**Q26.** (A')' = ? *(E · 3.7)*  
(a) A' (b) A (c) 1 (d) 0

**Answer.** (b) A. *Why:* involution: *ulta* of *ulta* is *seedha*.

**Q27.** The law A·B = B·A is the *(E · 3.7)*  
(a) associative law (b) commutative law (c) distributive law (d) absorption law

**Answer.** (b) commutative law: only the order changes.

**Q28.** The law A·(B + C) = A·B + A·C is the *(E · 3.7)*  
(a) distributive law (b) associative law (c) idempotent law (d) involution law

**Answer.** (a) distributive law.

**Q29.** A + A·B = ? *(E · 3.7)*  
(a) A·B (b) B (c) A (d) 1

**Answer.** (c) A. *Why:* absorption: if A = 1 the answer is 1; if A = 0 both terms are 0.

**Q30.** A + A'·B = ? *(M · 3.7)*  
(a) A (b) B (c) A + B (d) A·B

**Answer.** (c) A + B. *Why:* the redundant-literal law.

**Q31.** (P · Q)' is equal to *(E · 3.6)*  
(a) P' · Q' (b) P' + Q' (c) P + Q (d) (P + Q)'

**Answer.** (b) P' + Q'. *Why:* De Morgan's second law: open the bracket, flip the sign, prime each letter. *Trap:* (a) forgets to flip the sign.

**Q32.** The complement of A·B is *(E · 3.6)*  
(a) A'·B' (b) A' + B' (c) A + B (d) (A + B)'

**Answer.** (b) A' + B'. *Why:* De Morgan's second law.

**Q33.** The complement of A + B' is *(M · 3.6)*  
(a) A'·B (b) A' + B (c) A·B' (d) A'·B'

**Answer.** (a) A'·B. *Why:* first law: (A + B')' = A'·(B')' = A'·B.

**Q34.** Bubble pushing shows that a NOR gate is the same as *(H · 3.6)*  
(a) an AND gate with bubbles on its inputs (b) an OR gate with bubbles on its inputs (c) a NAND gate (d) an AND gate

**Answer.** (a). *Why:* (A + B)' = A'·B' (De Morgan's first law): the NOTs move to the inputs and OR becomes AND.

**Q35.** The dual of A + 0 = A is *(E · 3.7)*  
(a) A·1 = A (b) A·0 = 0 (c) A + 1 = 1 (d) A' + 1 = A'

**Answer.** (a). *Why:* swap + with · and 0 with 1.

**Q36.** The dual of A·(B + C) is *(M · 3.7)*  
(a) A + B·C (b) A'·(B' + C') (c) A·B + C (d) (A + B)·C

**Answer.** (a) A + B·C. *Why:* swap · and +; letters keep their primes. (b) is a complement, not a dual.

**Q37.** A + A' is a *(E · 3.7)*  
(a) fallacy (b) tautology (c) dual (d) complement

**Answer.** (b) tautology. *Why:* it is 1 in every row.

**Q38.** Which expression is a fallacy? *(E · 3.7)*  
(a) A + A' (b) A·A' (c) A + 1 (d) A·1

**Answer.** (b) A·A'. *Why:* it is 0 in every row.

## 3.8 Circuits and history

**Q39.** The order in which an expression is worked out is *(E · 3.8)*  
(a) AND, OR, NOT, brackets (b) brackets, NOT, AND, OR (c) OR, AND, NOT, brackets (d) left to right only

**Answer.** (b): B-N-A-O.

**Q40.** Boolean algebra was developed by *(E · 3.1)*  
(a) Claude Shannon (b) George Boole (c) Charles Babbage (d) Alan Turing

**Answer.** (b) George Boole, an English mathematician, in 1854. Claude Shannon later (1938) used it for switch circuits.
