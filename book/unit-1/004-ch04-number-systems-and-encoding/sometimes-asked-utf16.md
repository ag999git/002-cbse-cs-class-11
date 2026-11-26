# Sometimes asked: UTF-16, the third way

*Chapter 4 · Sometimes asked. The syllabus names UTF-8 and UTF-32; some books also describe UTF-16, which sits between them.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. How UTF-16 works

UTF-16 stores a code point in **2 bytes** (one 16-bit unit) if it fits, and in **4 bytes** (two units, called a
**surrogate pair**) if it does not. Every character of the common scripts, including all Indian scripts, fits in 2 bytes;
emojis and rare scripts take 4.

| Character | Code point | UTF-8 bytes | UTF-16 bytes | UTF-32 bytes |
|:-:|:-:|:-:|:-:|:-:|
| A | U+0041 | 1 | 2 | 4 |
| é | U+00E9 | 2 | 2 | 4 |
| ₹ | U+20B9 | 3 | 2 | 4 |
| अ | U+0905 | 3 | 2 | 4 |
| ஆ | U+0B86 | 3 | 2 | 4 |
| 😀 | U+1F600 | 4 | 4 | 4 |

**हम सब एक** (the printed worked example): UTF-8 20 bytes, UTF-16 **16 bytes**, UTF-32 32 bytes.

## 2. The three compared

| Basis of difference | UTF-8 | UTF-16 | UTF-32 |
|---|---|---|---|
| Bytes per character | 1 to 4 | 2 or 4 | always 4 |
| English text | smallest (1 byte) | 2 bytes | 4 bytes |
| Hindi text | 3 bytes | **2 bytes** (smallest) | 4 bytes |
| Old ASCII files | read unchanged | must be converted | must be converted |
| Where used | the web, e-mail, Python files | inside Windows, Java and JavaScript | inside some programs |

So for a text that is mostly Hindi, UTF-16 is smaller than UTF-8; for English or mixed web pages, UTF-8 is smaller. The
web chose UTF-8 because most of its markup (HTML tags) is plain ASCII.
