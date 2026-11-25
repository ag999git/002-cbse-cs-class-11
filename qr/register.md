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
