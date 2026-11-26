# QR code register

**One row for every QR code in the book.** The QR pictures, the short forwarding pages of the website and the places
of the codes in the chapters are all made from this table by `tools/qr_build.py`, so they can never disagree.

- **ID**: chapter (2 digits) + number (2 digits). It is the short address inside the code: `https://ag999git.github.io/002-cbse-cs-class-11/q/ID/`.
- **Kind** and **Name**: the two-line label printed under the code.
- **Section** and **Beside the paragraph that starts with**: where the code floats in the printed chapter (at the right of that paragraph).
- **Opens**: the page of the website the short address forwards to (a path inside `book/`). To move a page, change only this column: the printed code keeps working.

| ID | Kind | Name | Section | Beside the paragraph that starts with | Opens |
|---|---|---|---|---|---|
| 0101 | Index | All online pages | Start | **The online pages of this chapter.** | unit-1/001-ch01-computer-system-organisation/index.md |
| 0102 | Beyond syllabus | Types of computers | 1.1 | **What happens between pressing 2, +, 3 | unit-1/001-ch01-computer-system-organisation/beyond-types-and-history.md |
| 0103 | See it | Device gallery | 1.3 | **How does a computer know what you want | unit-1/001-ch01-computer-system-organisation/see-it-device-gallery.md |
| 0104 | Sometimes asked | Word size and buses | 1.4 | **Who decides what happens next inside a computer?** | unit-1/001-ch01-computer-system-organisation/sometimes-asked-word-size-and-buses.md |
| 0105 | Sometimes asked | EPROM and flash | 1.6 | **What happens to your unsaved homework when the power goes?** | unit-1/001-ch01-computer-system-organisation/sometimes-asked-types-of-rom-ram.md |
| 0106 | See it | Inside the computer | 1.6 | **Where do your photos stay when the phone is switched off?** | unit-1/001-ch01-computer-system-organisation/see-it-inside-the-computer.md |
| 0107 | Beyond syllabus | Memory hierarchy | 1.6 | **Why does a computer need so many kinds of memory?** | unit-1/001-ch01-computer-system-organisation/beyond-memory-hierarchy.md |
| 0108 | Challenge | Units of memory | 1.7 | **How many paise are there in ₹5?** | unit-1/001-ch01-computer-system-organisation/challenge-units-of-memory.md |
| 0109 | Practice | 350 more questions | Questions with answers | These questions are for **learning** | unit-1/001-ch01-computer-system-organisation/questions/index.md |
| 0110 | Revise | Flashcards, glossary | End | **Revise online.** | unit-1/001-ch01-computer-system-organisation/flashcards.md |
| 0301 | Index | All online pages | Start | **The online pages of this chapter.** | unit-1/003-ch03-boolean-logic/index.md |
| 0302 | Challenge | All 16 gates | 3.4 | *Reading the table:* the columns 00, 01, 10, 11 | unit-1/003-ch03-boolean-logic/challenge-16-functions.md |
| 0303 | Beyond syllabus | XNOR in depth | 3.4 | **Common mistake.** Drawing XOR without the extra curved line. | unit-1/003-ch03-boolean-logic/beyond-xnor.md |
| 0304 | Beyond syllabus | SOP, POS, K-maps | 3.5 | **How do you check a long expression?** | unit-1/003-ch03-boolean-logic/beyond-sop-pos-kmap.md |
| 0305 | Challenge | Two bits, three results | 3.5 | **Can a gate have more than two inputs?** | unit-1/003-ch03-boolean-logic/challenge-two-bits-three-results.md |
| 0306 | Sometimes asked | Duality, tautology | 3.7 | **Common mistake.** A + A' = 0. | unit-1/003-ch03-boolean-logic/sometimes-asked-duality-tautology.md |
| 0401 | Index | All online pages | Start | **Helps you understand.** | unit-1/004-ch04-number-systems-and-encoding/index.md |
| 0402 | See it | Trays and meter | 4.2 | Learn the **binary row** by heart | unit-1/004-ch04-number-systems-and-encoding/see-it-trays-and-meter.md |
| 0403 | See it | Converter | 4.3 | *Reading the flowchart:* | unit-1/004-ch04-number-systems-and-encoding/see-it-converter.md |
| 0404 | Sometimes asked | Double dabble | 4.3 | **Online.** A second method for binary to decimal | unit-1/004-ch04-number-systems-and-encoding/sometimes-asked-double-dabble.md |
| 0405 | Beyond syllabus | Why 0.1 + 0.2 ≠ 0.3 | 4.4 | **Worked example 6.** | unit-1/004-ch04-number-systems-and-encoding/beyond-floating-point.md |
| 0406 | Sometimes asked | Binary arithmetic | 4.4 | **Common mistake.** Multiplying the whole number | unit-1/004-ch04-number-systems-and-encoding/sometimes-asked-binary-arithmetic.md |
| 0407 | See it | Letters to bytes | 4.5 | **How does the computer know which number stands for which letter?** | unit-1/004-ch04-number-systems-and-encoding/see-it-letters-to-bytes.md |
| 0408 | Beyond syllabus | UTF-8 bits | 4.5 | **One register for the whole world.** | unit-1/004-ch04-number-systems-and-encoding/beyond-utf8-bits.md |
| 0409 | Sometimes asked | Typing Indian text | 4.5 | **Online.** How to type Hindi | unit-1/004-ch04-number-systems-and-encoding/sometimes-asked-typing-indian-languages.md |
| 0410 | Practice | 327 more questions | Questions with answers | These questions are for **learning** | unit-1/004-ch04-number-systems-and-encoding/questions/index.md |
| 0411 | Revise | Flashcards, glossary | Questions (answer to Q26) | **Answer.** 011 111 | unit-1/004-ch04-number-systems-and-encoding/flashcards.md |

**Retired IDs** (never printed; never reuse them): 0307 (memory palace of Chapter 3; removed 26 Nov 2026, when memory palaces were put on hold for the whole book).
