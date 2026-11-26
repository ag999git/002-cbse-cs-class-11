# Beyond syllabus: other codes: BCD, Excess-3, Gray code, EBCDIC and parity

*Chapter 4 · Beyond syllabus. Not in the Class XI syllabus; taught in engineering courses on digital circuits, and asked now and then in olympiads.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

| Decimal | Binary | BCD (8421) | Excess-3 | Gray code |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0000 | 0000 | 0011 | 0000 |
| 1 | 0001 | 0001 | 0100 | 0001 |
| 2 | 0010 | 0010 | 0101 | 0011 |
| 3 | 0011 | 0011 | 0110 | 0010 |
| 4 | 0100 | 0100 | 0111 | 0110 |
| 5 | 0101 | 0101 | 1000 | 0111 |
| 6 | 0110 | 0110 | 1001 | 0101 |
| 7 | 0111 | 0111 | 1010 | 0100 |
| 8 | 1000 | 1000 | 1011 | 1100 |
| 9 | 1001 | 1001 | 1100 | 1101 |

## 1. BCD (binary-coded decimal)

Each **decimal digit** is written in 4 bits, separately: 259 in BCD is 0010 0101 1001, not the binary of 259
(100000011). Used where numbers are shown digit by digit: calculators, digital clocks, meters. The 4-bit
patterns 1010 to 1111 are not used.

## 2. Excess-3

BCD plus 3 for each digit. Its trick: the 9's complement of a digit is found by turning every bit round (4 → 0111, and
9 − 4 = 5 → 1000). Used in old calculating machines.

## 3. Gray code

Counting in Gray code, **only one bit changes** from one number to the next (see the table: 3 → 4 is 0010 → 0110).
In ordinary binary, 7 → 8 changes all four bits (0111 → 1000), and a sensor reading the bits at slightly different
moments could see a wrong number in between. Gray code is used in **rotary encoders** (the knob of a volume control,
the position sensor of a motor) for this reason. To get it: copy the leftmost bit, then each next Gray bit is the XOR
(Chapter 3) of two neighbouring binary bits.

## 4. EBCDIC

**Extended Binary Coded Decimal Interchange Code**: IBM's 8-bit code for its mainframe computers (1960s), different
from ASCII. 'A' is C1 in hex (193) in EBCDIC but 41 (65) in ASCII. Still used on some bank and government mainframes.

## 5. Parity bit: a simple check for errors

An extra bit is added so that the number of 1s is **even** (even parity) or **odd** (odd parity). If one bit is
flipped on the way, the count is wrong and the error is noticed (though not corrected).

| Data (7 bits) | Number of 1s | Even-parity bit | Sent (8 bits) |
|:-:|:-:|:-:|:-:|
| 1000001 ('A') | 2 | 0 | 01000001 |
| 1000011 ('C') | 3 | 1 | 11000011 |
| 0110111 ('7') | 5 | 1 | 10110111 |
