# Beyond syllabus: how UTF-8 packs the bits

*Chapter 4 · Beyond syllabus. The printed book says UTF-8 uses 1 to 4 bytes (section 4.5); this page shows exactly how the bits are placed.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. The patterns

| Code points | Bytes | Byte patterns (x = a bit of the code point) | Free bits |
|---|:-:|---|:-:|
| U+0000 to U+007F | 1 | 0xxxxxxx | 7 |
| U+0080 to U+07FF | 2 | 110xxxxx 10xxxxxx | 11 |
| U+0800 to U+FFFF | 3 | 1110xxxx 10xxxxxx 10xxxxxx | 16 |
| U+10000 to U+10FFFF | 4 | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx | 21 |

- The **first byte** says how many bytes the character has: it starts with as many 1s as there are bytes (110 = 2,
  1110 = 3, 11110 = 4). A byte starting with 0 is a whole ASCII character on its own.
- Every **following byte** starts with 10. So a program can always find where a character starts, even in the middle of
  a text: this is the "board on every vehicle" of the printed parking-lot picture.

## 2. Worked examples

**é** (U+00E9): 2 bytes. Code point in binary, filled to 11 bits: 00011101001. Into the pattern 110xxxxx 10xxxxxx → 11000011 10101001 → **C3 A9** in hex.

**₹** (U+20B9): 3 bytes. Code point in binary, filled to 16 bits: 0010000010111001. Into the pattern 1110xxxx 10xxxxxx 10xxxxxx → 11100010 10000010 10111001 → **E2 82 B9** in hex.

**अ** (U+0905): 3 bytes. Code point in binary, filled to 16 bits: 0000100100000101. Into the pattern 1110xxxx 10xxxxxx 10xxxxxx → 11100000 10100100 10000101 → **E0 A4 85** in hex.

**😀** (U+1F600): 4 bytes. Code point in binary, filled to 21 bits: 000011111011000000000. Into the pattern 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx → 11110000 10011111 10011000 10000000 → **F0 9F 98 80** in hex.

## 3. Decoding: from bytes back to the character

Take E0 A4 85. In binary: 1110 0000 · 10 100100 · 10 000101. The first byte starts with 1110, so 3 bytes. Remove the
markers (1110, 10, 10) and join what is left: 0000 100100 000101 = 0000 1001 0000 0101 = 0905 in hex → **U+0905 = अ**.

## 4. Why is it designed like this?

- ASCII text is unchanged (one byte, starting with 0).
- No byte of a long character can be mistaken for an ASCII character (they all start with 1).
- A damaged byte spoils only one character; the reader finds the next start and carries on.
