# Sometimes asked: typing Hindi and other Indian languages

*Chapter 4 · Sometimes asked. NCERT has an activity on it and some books describe it. The printed book points here from section 4.5.*

*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*

## 1. Three ways to type in an Indian script

| Way | How it works | Good for |
|---|---|---|
| **InScript keyboard** | each key of an ordinary keyboard gives one letter or sign of the script; the same layout serves all Indian scripts | fast typing after practice; the Government of India standard |
| **Phonetic (transliteration) typing** | you type in English letters as it sounds ("namaste") and the program shows नमस्ते | beginners; phones |
| **Handwriting or voice** | write on the screen with a finger, or speak | phones |

Whatever way you type, what is stored is the same: **Unicode code points**, usually in **UTF-8**.

## 2. InScript, the standard keyboard

- The first InScript layout was part of the ISCII standard **IS 13194:1991** (section 4.5 of the book).
- Today's **Enhanced InScript** is the Bureau of Indian Standards standard **IS 16350:2016**. It is built to work with
  Unicode and covers the scripts of all 22 official languages of India.
- Because ISCII gave the same sound the same place in every script, InScript puts the same sound on the same key in
  every script: learn it once for Hindi and you can type Bengali or Tamil on the same keys.

## 3. Activity (about 20 minutes)

1. On a computer, add the Hindi language and its keyboard in the language settings; on a phone, add Hindi to the
   keyboard languages.
2. Type your name in Devanagari (or in your own state's script).
3. Count its characters, then use the chapter's notebook to see its code points and its size in UTF-8 and UTF-32.
4. Compare with your name in English: which takes more bytes in UTF-8, and why? (Each English letter takes 1 byte;
   each Devanagari code point takes 3.)

## 4. Unicode in Indian e-governance

Indian government websites and documents use Unicode for Indian languages, so that text typed in one office can be read
in any other, on any device. This is the "one register for the whole school" of the printed book, at the scale of a
country.
