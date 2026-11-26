# Sometimes asked: Unicode code points of Indian scripts

*Chapter 4 · Sometimes asked. The printed book gives the Devanagari block and a few code points (section 4.5); this page has every Indian script block and how to look up any character.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

| Script | Block | First letter "a" of the script | Its code point |
|---|:-:|:-:|:-:|
| Devanagari (Hindi, Marathi, Sanskrit, Nepali …) | U+0900 to U+097F | अ | U+0905 |
| Bengali and Assamese | U+0980 to U+09FF | অ | U+0985 |
| Gurmukhi (Punjabi) | U+0A00 to U+0A7F | ਅ | U+0A05 |
| Gujarati | U+0A80 to U+0AFF | અ | U+0A85 |
| Oriya (Odia) | U+0B00 to U+0B7F | ଅ | U+0B05 |
| Tamil | U+0B80 to U+0BFF | அ | U+0B85 |
| Telugu | U+0C00 to U+0C7F | అ | U+0C05 |
| Kannada | U+0C80 to U+0CFF | ಅ | U+0C85 |
| Malayalam | U+0D00 to U+0D7F | അ | U+0D05 |

Each Indian script has a block of 128 places, and the letters sit in **the same order** in every block (the order of
ISCII). So "a" is always the 6th place (…05), and ka is always …15:

| Script | ka | Code point |
|---|:-:|:-:|
| Devanagari | क | U+0915 |
| Bengali and Assamese | ক | U+0995 |
| Gurmukhi | ਕ | U+0A15 |
| Gujarati | ક | U+0A95 |
| Oriya | କ | U+0B15 |
| Tamil | க | U+0B95 |

## How to look up any character

- **On the web:** the Unicode Consortium publishes a code chart for every block (search "Unicode code charts").
- **In Python** (Chapter 6 onward): `ord('क')` gives 2325 and `hex(ord('क'))` gives '0x915'; `chr(0x20B9)` gives '₹'.
- **In a word processor:** type the hex code point and press Alt+X (in Microsoft Word): 20b9 then Alt+X gives ₹.

## A few facts

- The **₹** sign (U+20B9) was added in Unicode 6.0, in **2010**, the year India adopted it.
- Unicode 17.0 (September 2025) has 159,801 characters from 172 scripts.
- The Hindi digits ० to ९ are U+0966 to U+096F; they are different characters from 0 to 9 (U+0030 to U+0039).
