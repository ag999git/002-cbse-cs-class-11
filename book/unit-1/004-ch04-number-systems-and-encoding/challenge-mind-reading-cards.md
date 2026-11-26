# Challenge: the binary mind-reading cards

*Chapter 4 · Challenge. A classroom trick that is binary in disguise. Print the six cards, try it on a friend, then explain how it works.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

**Card 1** (first number 1)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
| 17 | 19 | 21 | 23 | 25 | 27 | 29 | 31 |
| 33 | 35 | 37 | 39 | 41 | 43 | 45 | 47 |
| 49 | 51 | 53 | 55 | 57 | 59 | 61 | 63 |

**Card 2** (first number 2)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 2 | 3 | 6 | 7 | 10 | 11 | 14 | 15 |
| 18 | 19 | 22 | 23 | 26 | 27 | 30 | 31 |
| 34 | 35 | 38 | 39 | 42 | 43 | 46 | 47 |
| 50 | 51 | 54 | 55 | 58 | 59 | 62 | 63 |

**Card 3** (first number 4)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 4 | 5 | 6 | 7 | 12 | 13 | 14 | 15 |
| 20 | 21 | 22 | 23 | 28 | 29 | 30 | 31 |
| 36 | 37 | 38 | 39 | 44 | 45 | 46 | 47 |
| 52 | 53 | 54 | 55 | 60 | 61 | 62 | 63 |

**Card 4** (first number 8)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
| 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
| 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |

**Card 5** (first number 16)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
| 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
| 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |

**Card 6** (first number 32)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |
| 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
| 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
| 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |

## How to do the trick

1. Ask a friend to think of a number from 1 to 63.
2. Show the six cards; the friend says only "yes" or "no": is the number on this card?
3. Add the **first numbers** of the "yes" cards. That is the number.

## Why it works

Card 1 has every number whose **1s bit** is 1; card 2 every number whose **2s bit** is 1; card 3 the **4s bit**; and so on
up to 32. The friend's yes/no answers are the bits of the number, and adding the first numbers adds the place values of
the 1 bits: the cake trays of the printed book. For 45 = 32 + 8 + 4 + 1: yes, no, yes, yes, no, yes (cards 1 to 6).
