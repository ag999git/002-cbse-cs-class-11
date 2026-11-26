# Beyond syllabus: signed numbers: how a computer stores −5

*Chapter 4 · Beyond syllabus. Not in the Class XI syllabus; it follows on from the "1's and 2's complement" page and prepares for data types (Chapter 7).*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

| Number | Sign and magnitude | 1's complement | 2's complement |
|:-:|:-:|:-:|:-:|
| +5 | 00000101 | 00000101 | 00000101 |
| -5 | 10000101 | 11111010 | 11111011 |
| +1 | 00000001 | 00000001 | 00000001 |
| -1 | 10000001 | 11111110 | 11111111 |
| +127 | 01111111 | 01111111 | 01111111 |
| -127 | 11111111 | 10000000 | 10000001 |
| +0 | 00000000 | 00000000 | 00000000 |

- **Sign and magnitude:** the leftmost bit is the sign (0 +, 1 −), the rest is the size. Simple, but it has two zeros
  (+0 and −0) and adding needs special rules.
- **1's complement:** a negative number is its positive turned round. Still two zeros.
- **2's complement:** a negative number is the 2's complement of its positive. **One zero**, and adding works with the
  ordinary adding circuit. Almost every computer uses it.

| Bits | Range in 2's complement |
|:-:|---|
| 8 | −128 to +127 |
| 16 | −32,768 to +32,767 |
| 32 | −2,147,483,648 to +2,147,483,647 |
| 64 | −9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 |

**Overflow:** in 8 bits, 127 + 1 gives 1000 0000, which reads as −128: the result did not fit. Programs in languages with
fixed-size numbers must watch for this. **Python's whole numbers have no fixed size**: Python simply uses more bytes when a
number grows, so `2 ** 100` is exact.
