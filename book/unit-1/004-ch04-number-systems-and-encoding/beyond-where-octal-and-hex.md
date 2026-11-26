# Beyond syllabus: where you meet octal and hex

*Chapter 4 · Beyond syllabus. "Why learn hex?" The printed book says hex and octal are short forms of binary; here is where people actually use them.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. Colours on screens and web pages

A colour is written **#RRGGBB**: two hex digits each for red, green and blue, each from 00 (none) to FF (255, full).
This book's orange is **#C55A11**: red C5 = 197, green 5A = 90, blue 11 = 17.

| Colour | Hex | Red, green, blue |
|---|:-:|:-:|
| black | #000000 | 0, 0, 0 |
| white | #FFFFFF | 255, 255, 255 |
| pure red | #FF0000 | 255, 0, 0 |
| this book's orange | #C55A11 | 197, 90, 17 |
| saffron of the national flag (often given as) | #FF9933 | 255, 153, 51 |

Each colour uses 3 bytes = 24 bits, so a screen can show 2²⁴ = 16,777,216 colours.

## 2. File permissions in octal

On Linux and Android, who may read (r = 4), write (w = 2) and run (x = 1) a file is written as three octal digits, for the
owner, the group and everyone else. **755** means rwx r-x r-x: 7 = 4 + 2 + 1 for the owner, 5 = 4 + 1 for the others.
Each octal digit is exactly 3 bits: one bit for each permission. That is why octal is used here.

| Octal | Bits | Permission |
|:-:|:-:|:-:|
| 0 | 000 | --- |
| 1 | 001 | --x |
| 2 | 010 | -w- |
| 3 | 011 | -wx |
| 4 | 100 | r-- |
| 5 | 101 | r-x |
| 6 | 110 | rw- |
| 7 | 111 | rwx |

## 3. Memory addresses and network addresses

- Memory addresses are shown in hex (0x7FFE…): 64 bits become 16 hex digits instead of 64 bits.
- A network card's **MAC address** is 48 bits written as 6 pairs of hex digits, such as 3C:52:82:1A:7F:09.
- **IPv6** internet addresses are 128 bits, written as 8 groups of 4 hex digits.

## 4. Unicode charts

Every code point is written in hex (U+20B9), because the blocks start at round hex numbers (U+0900) and the charts are
laid out in rows of 16.
