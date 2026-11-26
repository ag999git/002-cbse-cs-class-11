# Helps you understand: the full ASCII table, explained

*Chapter 4 · Helps you understand. The printed book has the ASCII chart and the codes to remember (section 4.5); this page has every code with its binary and hex, and the patterns in the bits.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. The patterns in the bits

| Characters | Codes | 7-bit pattern | What the pattern says |
|---|:-:|---|---|
| control codes | 0–31 | 0000000 to 0011111 | the two leftmost bits are 00 |
| space and signs | 32–47 | 0100000 to 0101111 | starts 010 |
| digits '0'–'9' | 48–57 | 0110000 to 0111001 | starts 011 0: the last 4 bits are the digit itself ('7' = 011 0111) |
| capitals A–Z | 65–90 | 1000001 to 1011010 | starts 10: the last 5 bits count the letter (A = 1, B = 2 …) |
| small letters a–z | 97–122 | 1100001 to 1111010 | starts 11: the same last 5 bits as the capital; only the bit worth 32 differs |

**Two tricks that follow:** to change a capital to a small letter, add 32 (switch on the bit worth 32); to get the value of
a digit character, subtract 48 (or keep only its last 4 bits).

## 2. All 128 codes

| Code | Binary (7 bits) | Hex | Character |
|:-:|:-:|:-:|---|
| 0 | 0000000 | 00 | NUL (null) |
| 1 | 0000001 | 01 | control code |
| 2 | 0000010 | 02 | control code |
| 3 | 0000011 | 03 | control code |
| 4 | 0000100 | 04 | control code |
| 5 | 0000101 | 05 | control code |
| 6 | 0000110 | 06 | control code |
| 7 | 0000111 | 07 | BEL (bell) |
| 8 | 0001000 | 08 | BS (backspace) |
| 9 | 0001001 | 09 | TAB (horizontal tab) |
| 10 | 0001010 | 0A | LF (line feed: new line) |
| 11 | 0001011 | 0B | control code |
| 12 | 0001100 | 0C | control code |
| 13 | 0001101 | 0D | CR (carriage return: back to the start of the line) |
| 14 | 0001110 | 0E | control code |
| 15 | 0001111 | 0F | control code |
| 16 | 0010000 | 10 | control code |
| 17 | 0010001 | 11 | control code |
| 18 | 0010010 | 12 | control code |
| 19 | 0010011 | 13 | control code |
| 20 | 0010100 | 14 | control code |
| 21 | 0010101 | 15 | control code |
| 22 | 0010110 | 16 | control code |
| 23 | 0010111 | 17 | control code |
| 24 | 0011000 | 18 | control code |
| 25 | 0011001 | 19 | control code |
| 26 | 0011010 | 1A | control code |
| 27 | 0011011 | 1B | ESC (escape) |
| 28 | 0011100 | 1C | control code |
| 29 | 0011101 | 1D | control code |
| 30 | 0011110 | 1E | control code |
| 31 | 0011111 | 1F | control code |
| 32 | 0100000 | 20 | space |
| 33 | 0100001 | 21 | `!` |
| 34 | 0100010 | 22 | `"` |
| 35 | 0100011 | 23 | `#` |
| 36 | 0100100 | 24 | `$` |
| 37 | 0100101 | 25 | `%` |
| 38 | 0100110 | 26 | `&` |
| 39 | 0100111 | 27 | `'` |
| 40 | 0101000 | 28 | `(` |
| 41 | 0101001 | 29 | `)` |
| 42 | 0101010 | 2A | `*` |
| 43 | 0101011 | 2B | `+` |
| 44 | 0101100 | 2C | `,` |
| 45 | 0101101 | 2D | `-` |
| 46 | 0101110 | 2E | `.` |
| 47 | 0101111 | 2F | `/` |
| 48 | 0110000 | 30 | `0` |
| 49 | 0110001 | 31 | `1` |
| 50 | 0110010 | 32 | `2` |
| 51 | 0110011 | 33 | `3` |
| 52 | 0110100 | 34 | `4` |
| 53 | 0110101 | 35 | `5` |
| 54 | 0110110 | 36 | `6` |
| 55 | 0110111 | 37 | `7` |
| 56 | 0111000 | 38 | `8` |
| 57 | 0111001 | 39 | `9` |
| 58 | 0111010 | 3A | `:` |
| 59 | 0111011 | 3B | `;` |
| 60 | 0111100 | 3C | `<` |
| 61 | 0111101 | 3D | `=` |
| 62 | 0111110 | 3E | `>` |
| 63 | 0111111 | 3F | `?` |
| 64 | 1000000 | 40 | `@` |
| 65 | 1000001 | 41 | `A` |
| 66 | 1000010 | 42 | `B` |
| 67 | 1000011 | 43 | `C` |
| 68 | 1000100 | 44 | `D` |
| 69 | 1000101 | 45 | `E` |
| 70 | 1000110 | 46 | `F` |
| 71 | 1000111 | 47 | `G` |
| 72 | 1001000 | 48 | `H` |
| 73 | 1001001 | 49 | `I` |
| 74 | 1001010 | 4A | `J` |
| 75 | 1001011 | 4B | `K` |
| 76 | 1001100 | 4C | `L` |
| 77 | 1001101 | 4D | `M` |
| 78 | 1001110 | 4E | `N` |
| 79 | 1001111 | 4F | `O` |
| 80 | 1010000 | 50 | `P` |
| 81 | 1010001 | 51 | `Q` |
| 82 | 1010010 | 52 | `R` |
| 83 | 1010011 | 53 | `S` |
| 84 | 1010100 | 54 | `T` |
| 85 | 1010101 | 55 | `U` |
| 86 | 1010110 | 56 | `V` |
| 87 | 1010111 | 57 | `W` |
| 88 | 1011000 | 58 | `X` |
| 89 | 1011001 | 59 | `Y` |
| 90 | 1011010 | 5A | `Z` |
| 91 | 1011011 | 5B | `[` |
| 92 | 1011100 | 5C | `\` |
| 93 | 1011101 | 5D | `]` |
| 94 | 1011110 | 5E | `^` |
| 95 | 1011111 | 5F | `_` |
| 96 | 1100000 | 60 | `` ` `` |
| 97 | 1100001 | 61 | `a` |
| 98 | 1100010 | 62 | `b` |
| 99 | 1100011 | 63 | `c` |
| 100 | 1100100 | 64 | `d` |
| 101 | 1100101 | 65 | `e` |
| 102 | 1100110 | 66 | `f` |
| 103 | 1100111 | 67 | `g` |
| 104 | 1101000 | 68 | `h` |
| 105 | 1101001 | 69 | `i` |
| 106 | 1101010 | 6A | `j` |
| 107 | 1101011 | 6B | `k` |
| 108 | 1101100 | 6C | `l` |
| 109 | 1101101 | 6D | `m` |
| 110 | 1101110 | 6E | `n` |
| 111 | 1101111 | 6F | `o` |
| 112 | 1110000 | 70 | `p` |
| 113 | 1110001 | 71 | `q` |
| 114 | 1110010 | 72 | `r` |
| 115 | 1110011 | 73 | `s` |
| 116 | 1110100 | 74 | `t` |
| 117 | 1110101 | 75 | `u` |
| 118 | 1110110 | 76 | `v` |
| 119 | 1110111 | 77 | `w` |
| 120 | 1111000 | 78 | `x` |
| 121 | 1111001 | 79 | `y` |
| 122 | 1111010 | 7A | `z` |
| 123 | 1111011 | 7B | `{` |
| 124 | 1111100 | 7C | \| |
| 125 | 1111101 | 7D | `}` |
| 126 | 1111110 | 7E | `~` |
| 127 | 1111111 | 7F | DEL (delete) |

The control codes 1–31 not named above were used for old teleprinters and are rarely seen today.
