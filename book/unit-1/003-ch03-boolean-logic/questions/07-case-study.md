# Chapter 3: Boolean Logic and Logic Circuits: Case studies (6 cases, 26 questions)

*Chapter 3 · Questions (online). The questions of the printed chapter and many more, each followed by its answer and the reason. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every Boolean answer on this page was checked by a program (`tools/ch03_typed_questions.py`).*

## Case 1: A circuit in three stages

A circuit has three stages: stage 1 = A AND B; stage 2 = NOT C; stage 3 = stage 1 NOR stage 2.

**1.1** Output of stage 1 when A = 1, B = 1? *[1 mark]*

**Answer.** 1.

**1.2** Output of stage 2 when C = 0? *[1 mark]*

**Answer.** 1.

**1.3** Write the final expression. *[1 mark]*

**Answer.** Y = (A·B + C')'.

**1.4** Final output when A = 1, B = 1, C = 0? *[1 mark]*

**Answer.** (1 + 1)' = 1' = **0**.

**1.5** How many rows has its truth table? *[1 mark]*

**Answer.** 2³ = 8.

## Case 2: AND, NOT and NOR

In a circuit, A and B go into an AND gate; C goes into a NOT gate; the two outputs go into a NOR gate whose output is Y.

**2.1** Write the expression for Y. *[1 mark]*

**Answer.** Y = (A·B + C')'.

**2.2** Simplify it using De Morgan's laws. *[1 mark]*

**Answer.** First law: Y = (A·B)' · (C')' = (A·B)' · C. Second law on (A·B)': **Y = (A' + B') · C**.

**2.3** Find Y when A = 0, B = 1, C = 1. *[1 mark]*

**Answer.** A·B = 0 and C' = 0, so Y = (0 + 0)' = **1**. Check with the simplified form: (1 + 0) · 1 = 1.

**2.4** How many rows does its truth table have? *[1 mark]*

**Answer.** 2³ = 8.

**2.5** Find Y when A = 1, B = 1, C = 1 from both expressions. *[1 mark]*

**Answer.** Original: (1 + 0)' = 0. Simplified: (0 + 0) · 1 = 0. Both give **Y = 0**, which shows the simplification is right.

## Case 3: The school fire alarm

A school's science lab has a fire alarm that must ring when the smoke sensor (S) gives 1 **or** both the heat sensor (H) **and** the gas sensor (G) give 1.

**3.1** Write the Boolean expression. *[1 mark]*

**Answer.** Y = S + H·G.

**3.2** Describe the circuit. *[1 mark]*

**Answer.** H and G into an AND gate; its output and S into an OR gate.

**3.3** How many rows has its truth table? *[1 mark]*

**Answer.** 2³ = 8.

**3.4** Find the output when S = 0, H = 1, G = 0. *[1 mark]*

**Answer.** Y = 0 + 1·0 = **0**: the alarm stays silent.

## Case 4: The bank locker

A bank locker opens (Y = 1) only when the manager's key (M) **and** the customer's key (K) are both turned, **and** the alarm switch (S) is **not** on.

**4.1** Write the Boolean expression. *[1 mark]*

**Answer.** Y = M·K·S'.

**4.2** Which gates are needed? *[1 mark]*

**Answer.** One NOT gate (for S') and one 3-input AND gate (or two 2-input AND gates).

**4.3** Find Y when M = 1, K = 1, S = 1. *[1 mark]*

**Answer.** Y = 1·1·0 = **0**: with the alarm on, the locker stays shut.

**4.4** In how many of the 8 rows of its truth table does the locker open? *[1 mark]*

**Answer.** **One**: M = 1, K = 1, S = 0. *Why:* an AND gives 1 in only one row.

## Case 5: Can Riya go out to play?

Riya may go out to play (Y = 1) only when her homework is **not** pending (H = 0) and it is **not** raining (R = 0).

**5.1** Which single gate gives Y from H and R? *[1 mark]*

**Answer.** The **NOR** gate: Y = (H + R)'.

**5.2** Write Y another way using De Morgan's law. *[1 mark]*

**Answer.** Y = H' · R' (first law): "no homework **and** no rain".

**5.3** Find Y when H = 0 and R = 1. *[1 mark]*

**Answer.** Y = (0 + 1)' = **0**: it is raining, so she stays in.

**5.4** Write the truth table. *[1 mark]*

**Answer.**

| H | R | Y = (H + R)' |
|:-:|:-:|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

## Case 6: Three judges

In a quiz, three judges A, B and C each press 1 (yes) or 0 (no). A team goes through (Y = 1) when **at least two** judges say yes.

**6.1** Write the Boolean expression. *[1 mark]*

**Answer.** Y = A·B + B·C + A·C: any pair saying yes is enough.

**6.2** How many rows has its truth table? *[1 mark]*

**Answer.** 2³ = 8.

**6.3** Find Y when A = 1, B = 0, C = 1. *[1 mark]*

**Answer.** Y = 0 + 0 + 1 = **1**: two judges said yes.

**6.4** In how many rows is Y = 1? *[1 mark]*

**Answer.** **4**: 011, 101, 110 and 111.

| A | B | C | Y |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |
