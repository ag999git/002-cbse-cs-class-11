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
| 0201 | Index | All online pages | Start | **Your phone is the real example in every section | unit-1/002-ch02-software-and-os/index.md |
| 0202 | Sometimes asked | Grouping software | 2.1 | *Reading the figure:* each layer works | unit-1/002-ch02-software-and-os/sometimes-asked-grouping-software.md |
| 0203 | Explained | The airport in full | 2.5 | **Music is playing, Maps is guiding you | unit-1/002-ch02-software-and-os/explained-airport-part-by-part.md |
| 0204 | Explained | Utilities on a phone | 2.2 | *Cyber link (Chapter 18):* an antivirus | unit-1/002-ch02-software-and-os/explained-utilities-on-your-phone.md |
| 0205 | Step by step | Installing a printer | 2.2 | *Where the analogy stops:* a remote's code set | unit-1/002-ch02-software-and-os/step-by-step-installing-a-printer.md |
| 0206 | Helps you understand | Kinds of applications | 2.3 | **A replica jersey or one with your name on it?** | unit-1/002-ch02-software-and-os/helps-kinds-of-application-software.md |
| 0207 | See it | Translators at work | 2.4 | **Translators.** An **assembler** | unit-1/002-ch02-software-and-os/see-it-compiler-interpreter.md |
| 0208 | Challenge | Six-command robot | 2.4 | **Common mistake.** "An interpreter also makes | unit-1/002-ch02-software-and-os/challenge-robot-six-commands.md |
| 0209 | Sometimes asked | Linker and loader | 2.4 | **Answer.** A compiler. *Why:* it translates the whole program | unit-1/002-ch02-software-and-os/sometimes-asked-source-to-running-program.md |
| 0210 | Sometimes asked | Software libraries | 2.4 | **Answer.** Lines 1 to 3. | unit-1/002-ch02-software-and-os/sometimes-asked-software-libraries.md |
| 0211 | Beyond syllabus | How Python runs | 2.4 | *On your phone:* Google Translate does both. | unit-1/002-ch02-software-and-os/beyond-how-python-runs.md |
| 0212 | Explained | The OS at work | 2.5 | **Common mistake.** "The OS is just the home screen." | unit-1/002-ch02-software-and-os/explained-os-at-work.md |
| 0213 | Step by step | Tapping an app | 2.5 | *When you tap an app icon,* | unit-1/002-ch02-software-and-os/step-by-step-tap-an-app.md |
| 0214 | Beyond syllabus | Types of OS | 2.5 | **Answer.** It shares out the CPU, memory, files and devices | unit-1/002-ch02-software-and-os/beyond-types-of-os.md |
| 0215 | Explained | Report a cyber crime | 2.5 | *Cyber link:* the screen lock | unit-1/002-ch02-software-and-os/explained-report-a-cyber-crime.md |
| 0216 | Beyond syllabus | Interface history | 2.6 | **Play your favourite song, five ways.** | unit-1/002-ch02-software-and-os/beyond-ui-timeline.md |
| 0217 | Challenge | Ten safe commands | 2.6 | *CUI vs GUI:* a CUI needs | unit-1/002-ch02-software-and-os/challenge-safe-commands.md |
| 0218 | Practice | About 250 questions | Questions | These questions are for **learning** | unit-1/002-ch02-software-and-os/questions/index.md |
| 0219 | Revise | Flashcards, glossary | Summary | **Revise online.** | unit-1/002-ch02-software-and-os/flashcards.md |
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
| 0501 | Index | All online pages | Start | **You find the larger of two numbers | unit-2/005-ch05-problem-solving/index.md |
| 0502 | Explained | Testing and debugging | 5.2 | **Testing and debugging, in plain words.** | unit-2/005-ch05-problem-solving/explained-testing-and-debugging.md |
| 0503 | Explained | ATM algorithm | 5.3 | **How the algorithm works.** | unit-2/005-ch05-problem-solving/explained-atm-algorithm.md |
| 0504 | Step by step | Euclid step by step | 5.3 | **A purely computing algorithm: Euclid | unit-2/005-ch05-problem-solving/step-by-step-euclid-gcd.md |
| 0505 | Sometimes asked | More symbols | 5.4 | *Standards:* | unit-2/005-ch05-problem-solving/sometimes-asked-more-symbols.md |
| 0506 | Practice | Five-step practice | 5.5 | **A student who is not confident | unit-2/005-ch05-problem-solving/practice-five-step-method.md |
| 0507 | See it | Dry-run player | 5.5 | **The worked examples are numbered | unit-2/005-ch05-problem-solving/see-it-dry-run-player.md |
| 0508 | Practical | 22 practical charts | 5.5 | *The string, list and dictionary programs | unit-2/005-ch05-problem-solving/practical-flowcharts.md |
| 0509 | Explained | Pseudocode to Python | 5.6 | **Pseudocode is like Hinglish:** | unit-2/005-ch05-problem-solving/explained-pseudocode-to-python.md |
| 0510 | Practice | Trace tables | 5.7 | **The cricket scorer writes | unit-2/005-ch05-problem-solving/practice-trace-tables.md |
| 0511 | Step by step | Halving search | 5.8 | **How halving finds M | unit-2/005-ch05-problem-solving/step-by-step-halving-search.md |
| 0512 | Explained | Four prime tests | 5.8 | **Why the shorter methods are still right.** | unit-2/005-ch05-problem-solving/explained-prime-tests.md |
| 0513 | Explained | More decompositions | 5.9 | More systems decomposed | unit-2/005-ch05-problem-solving/explained-more-decompositions.md |
| 0514 | Practice | About 300 questions | Questions with answers | These questions are for **learning** | unit-2/005-ch05-problem-solving/questions/index.md |
| 0515 | Revise | Flashcards, glossary | Summary | **Revise online.** | unit-2/005-ch05-problem-solving/flashcards.md |
| 0601 | Index | All online pages | Start | **You have written algorithms in plain words | unit-2/006-ch06-getting-started-with-python/index.md |
| 0602 | Helps you understand | Story and versions | 6.1 | **Why does almost every school | unit-2/006-ch06-getting-started-with-python/helps-story-and-versions.md |
| 0603 | Helps you understand | Python's limits | 6.1 | Think of a dish at a dhaba | unit-2/006-ch06-getting-started-with-python/helps-python-limits.md |
| 0604 | Step by step | Install Python | 6.2 | Download Python only from **python.org** | get-started/install-python.md |
| 0605 | Get started | Which tool? Start here | 6.2 | **Where do I type Python?** | get-started/index.md |
| 0606 | Explained | Where code runs | 6.2 | **Online, in the website | get-started/where-does-my-code-run.md |
| 0607 | Good practice | When things go wrong | 6.3 | **Spaces at the start of a line matter.** | get-started/when-things-go-wrong.md |
| 0608 | Good practice | AI: learn first | 6.2 | Learn on **IDLE** | unit-2/006-ch06-getting-started-with-python/good-practice-ai-assistants.md |
| 0609 | See it | Interactive or script | 6.3 | In the shell you may type a sum | unit-2/006-ch06-getting-started-with-python/see-it-interactive-or-script.md |
| 0610 | Explained | Error messages | 6.3 | **Reading an error message.** | unit-2/006-ch06-getting-started-with-python/explained-reading-an-error-message.md |
| 0611 | Helps you understand | Long statements | 6.3 | A statement normally ends where the line ends | unit-2/006-ch06-getting-started-with-python/helps-statements-over-several-lines.md |
| 0612 | See it | Token explorer | 6.4 | **How does Python read a line?** | unit-2/006-ch06-getting-started-with-python/see-it-token-explorer.md |
| 0613 | Helps you understand | All 35 keywords | 6.5 | **Can I call my variable | unit-2/006-ch06-getting-started-with-python/helps-all-35-keywords.md |
| 0614 | See it | Identifier checker | 6.5 | A name must obey two kinds of rule | unit-2/006-ch06-getting-started-with-python/see-it-identifier-checker.md |
| 0615 | Good practice | PEP 8 for Class XI | 6.5 | **Why follow these conventions?** | unit-2/006-ch06-getting-started-with-python/good-practice-pep8-and-peps.md |
| 0616 | Sometimes asked | Literals up close | 6.6 | **Which parts of a statement are fixed values?** | unit-2/006-ch06-getting-started-with-python/sometimes-asked-literals-up-close.md |
| 0617 | See it | Names and objects | 6.7 | **What does `marks = 92` really do?** | unit-2/006-ch06-getting-started-with-python/see-it-names-and-objects.md |
| 0618 | Practice | Tricky assignments | 6.7 | **Python's shortcut: | unit-2/006-ch06-getting-started-with-python/practice-tricky-assignments-and-none.md |
| 0619 | Good practice | Notes for people | 6.8 | **Way 1** gives true comments | unit-2/006-ch06-getting-started-with-python/good-practice-notes-for-people.md |
| 0620 | Practice | Four Colab notebooks | Start | Each line of code has its own stripe | unit-2/006-ch06-getting-started-with-python/practice-colab-notebooks.md |
| 0621 | Revise | Cheat sheet (A4) | Summary | **Revise online.** | unit-2/006-ch06-getting-started-with-python/revise-cheat-sheet.md |
| 0622 | Practice | About 320 questions | Questions with answers | These questions are for **learning** | unit-2/006-ch06-getting-started-with-python/questions/index.md |
| 0623 | Revise | Flashcards, glossary | Summary | **Flashcards and glossary.** | unit-2/006-ch06-getting-started-with-python/flashcards.md |
| 0624 | Compare | Python and Java | 6.7 | **Not every language works like this.** | unit-2/006-ch06-getting-started-with-python/compare-python-and-java.md |
| 0625 | Compare | Strong and weak | 6.7 | Static and dynamic answer one question | unit-2/006-ch06-getting-started-with-python/compare-strong-and-weak-typing.md |

**Retired IDs** (never printed; never reuse them): 0307 (memory palace of Chapter 3; removed 26 Nov 2026, when memory palaces were put on hold for the whole book).
