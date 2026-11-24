# Challenge: two bits for three results

*Chapter 3 · Challenge (beyond the syllabus). Not needed for the exam; it joins Chapter 3 (gates) to Chapter 4 (bits).*

## The question

In the Class XI result, each subject has **three** possible results: **pass**, **compartment** (a second chance in a supplementary exam) or **fail**. A Boolean value has only **two**: 1 or 0. How can a computer store a result with three values, and then decide, with gates alone, whether a student is promoted?

## One bit is not enough

One bit gives 2 patterns (0, 1): enough for pass/fail, but there is no pattern left for compartment. **Two bits** give 2² = 4 patterns: enough for three results, with one pattern to spare.

Call the two bits of a subject **P** ("passed") and **C** ("compartment"):

| P | C | Result | Failed: (P + C)' |
|:-:|:-:|---|:-:|
| 0 | 0 | Fail | 1 |
| 0 | 1 | Compartment | 0 |
| 1 | 0 | Pass | 0 |
| 1 | 1 | Cannot happen | 0 |

- Pass = 10, compartment = 01, fail = 00. The pattern 11 ("passed and compartment") **cannot happen**; a program must never produce it.
- **Failed** is 1 only when P = 0 **and** C = 0, that is, when **neither** is 1: a **NOR** gate, (P + C)'.
- *The rule behind it:* n bits give 2ⁿ patterns, so a thing with k different values needs the smallest n with 2ⁿ ≥ k. Three values need 2 bits; five values would need 3 bits (Chapter 4).

## Two subjects: Maths and English

Now each student has four bits: Pm, Cm for Maths and Pe, Ce for English. The school's rule (a simplified one, for this puzzle):

- **Promoted** if the student passed **both**: **Pm · Pe** (AND).
- **Failed** if the student failed **either**: (Pm + Cm)' + (Pe + Ce)' (an OR of two NORs).
- **Compartment exam** if the student failed **neither** but has a compartment in **at least one**: (Pm + Cm) · (Pe + Ce) · (Cm + Ce).

Four bits give 2⁴ = 16 rows, but 7 of them contain the impossible pattern 11, so only **9** can happen:

| Pm | Cm | Pe | Ce | Maths | English | Promoted: Pm·Pe | Compartment exam: (Pm + Cm)·(Pe + Ce)·(Cm + Ce) | Failed: (Pm + Cm)' + (Pe + Ce)' |
|:-:|:-:|:-:|:-:|---|---|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | Fail | Fail | 0 | 0 | 1 |
| 0 | 0 | 0 | 1 | Fail | Compartment | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | Fail | Pass | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | Compartment | Fail | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | Compartment | Compartment | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | Compartment | Pass | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | Pass | Fail | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | Pass | Compartment | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | Pass | Pass | 1 | 0 | 0 |

## What to notice

- In every row **exactly one** of the three outputs is 1: no student is both promoted and failed. (The program that made this table checks it for every row.)
- The compartment rule needs **three** factors. Leave out (Cm + Ce) and a student who passed both would also be sent to the compartment exam. Try it on row Pm = 1, Pe = 1.

## Try it yourself

1. Use De Morgan's first law to write "Failed" without any bracket that has a prime outside it. *Answer:* (Pm + Cm)' + (Pe + Ce)' = Pm'·Cm' + Pe'·Ce'.
2. A fourth result, "absent", is added. How many bits does each subject need now? *Answer:* still 2: four values, and 2² = 4.
3. A fifth result, "result withheld", is added. *Answer:* 3 bits, since 2² = 4 is too few and 2³ = 8 is enough.
