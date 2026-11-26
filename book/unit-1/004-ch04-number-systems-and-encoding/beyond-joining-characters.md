# Beyond syllabus: characters that join: why नमस्ते is 6 code points

*Chapter 4 · Beyond syllabus. The printed book counts नमस्ते as 6 code points (question 24); this page explains why. Useful again in Chapter 11 (strings).*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. What you see and what is stored

On the screen नमस्ते looks like three letters: न, म, स्ते. In the computer it is **six code points**:

| # | Character | Code point | Name | Bytes in UTF-8 |
|:-:|:-:|:-:|---|:-:|
| 1 | न | U+0928 | devanagari letter na | 3 |
| 2 | म | U+092E | devanagari letter ma | 3 |
| 3 | स | U+0938 | devanagari letter sa | 3 |
| 4 | ◌् | U+094D | devanagari sign virama | 3 |
| 5 | त | U+0924 | devanagari letter ta | 3 |
| 6 | ◌े | U+0947 | devanagari vowel sign e | 3 |

- **्** (the halant, or virama) is a character of its own: it removes the vowel of the letter before it and joins it to
  the next letter, so स + ् + त is drawn as स्त.
- **े** (the vowel sign e) is also a character of its own; the font draws it on top of त.
- The **font** decides how the joined shapes look. The text stores only the code points, in the order they are spoken.

So in Python `len('नमस्ते')` gives **6**, and the word takes **18 bytes** in UTF-8 (6 × 3).

## 2. More joined letters

| What you see | Code points | How many | UTF-8 bytes |
|:-:|---|:-:|:-:|
| क्ष | क (U+0915) + ◌् (U+094D) + ष (U+0937) | 3 | 9 |
| त्र | त (U+0924) + ◌् (U+094D) + र (U+0930) | 3 | 9 |
| ज्ञ | ज (U+091C) + ◌् (U+094D) + ञ (U+091E) | 3 | 9 |
| श्री | श (U+0936) + ◌् (U+094D) + र (U+0930) + ◌ी (U+0940) | 4 | 12 |
| कि | क (U+0915) + ◌ि (U+093F) | 2 | 6 |

In **कि** the vowel sign ि is drawn **before** क, but it is stored **after** it: the stored order is the spoken order.

## 3. Emojis join too

| What you see | Stored as | Code points | UTF-8 bytes |
|:-:|---|:-:|:-:|
| 👨‍👩‍👧 (a family) | man + zero-width joiner + woman + zero-width joiner + girl | 5 | 18 |
| 🇮🇳 (the flag of India) | regional indicator I + regional indicator N | 2 | 8 |

The **zero-width joiner** (U+200D) is an invisible character that asks the phone to draw its two neighbours as one
picture. A phone that does not know the joined picture shows the separate emojis instead.

## 4. Why it matters

- **Counting:** "how many letters?" has two answers: the code points (what `len()` counts) and what a reader sees as
  one letter (called a *grapheme*).
- **Storage:** a short Hindi word can take many bytes (नमस्ते: 18 bytes in UTF-8, 24 in UTF-32).
- **Cutting text:** cutting a string after 3 code points gives नमस, which reads differently: never cut in the middle
  of a joined letter.

## 5. Questions

**Q1.** How many code points and how many UTF-8 bytes does "क्षमा" have?

**Answer.** 5 code points (क, ्, ष, म, ा) and 15 bytes (5 × 3).

**Q2.** Why does the vowel sign of कि come after क in memory, though it is drawn before it?

**Answer.** Unicode stores characters in the order they are spoken (k, then i); the font draws ि on the left.
