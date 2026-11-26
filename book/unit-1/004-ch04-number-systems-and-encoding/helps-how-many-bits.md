# Helps you understand: how many bits does a number need?

*Chapter 4 · Helps you understand. The printed book says n inputs give 2ⁿ patterns (Chapter 3) and seven bits reach 127 (section 4.2); this page turns that into a rule you can use.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. The rule

With **n bits** there are **2ⁿ patterns**, so they can stand for the numbers **0 to 2ⁿ − 1**.

| Bits n | Patterns 2ⁿ | Numbers | Where you meet it |
|:-:|:-:|:-:|---|
| 1 | 2 | 0 to 1 | one switch: on or off |
| 2 | 4 | 0 to 3 |  |
| 3 | 8 | 0 to 7 | one octal digit |
| 4 | 16 | 0 to 15 | one hex digit (a nibble) |
| 5 | 32 | 0 to 31 |  |
| 6 | 64 | 0 to 63 |  |
| 7 | 128 | 0 to 127 | ASCII |
| 8 | 256 | 0 to 255 | one byte; ISCII |
| 10 | 1,024 | 0 to 1,023 | about a thousand (1024 = 1 KB) |
| 16 | 65,536 | 0 to 65,535 | two bytes; UTF-16 unit |
| 32 | 4,294,967,296 | 0 to 4,294,967,295 | UTF-32; four bytes |

## 2. How many bits for a given number?

Find the smallest n with 2ⁿ greater than the number. Or convert the number to binary and count the bits.

| Number | Smallest power of 2 above it | Bits needed | Check in binary |
|:-:|:-:|:-:|---|
| 5 | 2^3 = 8 | **3** | 101 |
| 31 | 2^5 = 32 | **5** | 11111 |
| 32 | 2^6 = 64 | **6** | 100000 |
| 100 | 2^7 = 128 | **7** | 1100100 |
| 255 | 2^8 = 256 | **8** | 11111111 |
| 256 | 2^9 = 512 | **9** | 100000000 |
| 1,000 | 2^10 = 1,024 | **10** | 1111101000 |
| 100,000 | 2^17 = 131,072 | **17** | 11000011010100000 |
| 10,000,000 | 2^24 = 16,777,216 | **24** | 100110001001011010000000 |

**One crore (1,00,00,000) needs 24 bits**, because 2²⁴ = 1,67,77,216 is the first power of 2 above it.

## 3. The same in octal and hex

n octal digits reach 8ⁿ − 1; n hex digits reach 16ⁿ − 1. Each octal digit is 3 bits and each hex digit 4 bits, so the
number of hex digits is about a quarter of the number of bits (rounded up).

| Digits | Largest octal | = decimal | Largest hex | = decimal |
|:-:|:-:|:-:|:-:|:-:|
| 1 | (7)₈ | 7 | (F)₁₆ | 15 |
| 2 | (77)₈ | 63 | (FF)₁₆ | 255 |
| 3 | (777)₈ | 511 | (FFF)₁₆ | 4,095 |
| 4 | (7777)₈ | 4,095 | (FFFF)₁₆ | 65,535 |
