# Sometimes asked: extended ASCII and garbled text

*Chapter 4 · Sometimes asked. The printed book gives one line on extended ASCII (section 4.5); this page has the full story and the garbled-text puzzle.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. Extended ASCII

ASCII uses 7 bits (codes 0 to 127). A byte has 8 bits, so 128 more codes (128 to 255) were free. Computer makers filled
them with accented letters (é, ü, ñ), lines for drawing boxes, and symbols. But **each maker filled them differently**:
these sets are called **code pages**. Code 233 was é in one code page and a different letter in another. Text that used
codes above 127 came out wrong on a computer with another code page: the "two registers" problem of the printed book.

| Fact | |
|---|---|
| Codes 0 to 127 | the same everywhere (plain ASCII) |
| Codes 128 to 255 | different in each code page (Windows-1252, ISO 8859-1, Indian code pages …) |
| Why it could not become a world standard | 128 extra places cannot hold the world's scripts, and nobody agreed which 128 |
| What replaced it | Unicode |

## 2. The garbled-text puzzle: "â‚¹" instead of ₹

You may have seen "â‚¹" in a message where ₹ should be. Here is what happened:

1. The sender's phone stored ₹ in **UTF-8**: three bytes, E2 82 B9.
2. The receiving program wrongly read the text with an old one-byte table (Windows-1252), where **each byte is one
   character**.
3. In that table E2 is "â", 82 is "‚" and B9 is "¹". So one ₹ became three wrong characters.

The bytes were right; the **table** used to read them was wrong. The same happens to é, which becomes "Ã©".
This kind of garbled text even has a name, **mojibake** (Japanese for "changed characters").

**The cure:** both sides must use the same encoding, and today that is almost always UTF-8. In a browser or editor,
choosing "UTF-8" as the encoding usually brings the text back.
