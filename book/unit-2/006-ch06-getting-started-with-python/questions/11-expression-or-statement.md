# Chapter 6: Getting Started with Python: Expression or statement? Size of a string? (20)

*Chapter 6 · Questions (online). The kinds of question some school papers ask (written in our own words); every answer was decided by Python (`ast`, `len`). Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Expression or statement?

**Q1.** Is `7 + 5` an expression or a statement? *(M · 6.3)*

**Answer.** **An expression:** it gives a value.

**Q2.** Is `x = 7 + 5` an expression or a statement? *(M · 6.3)*

**Answer.** **A statement:** it does something (assigns, imports, deletes or does nothing on purpose) and gives no value.

**Q3.** Is `marks >= 33` an expression or a statement? *(M · 6.3)*

**Answer.** **An expression:** it gives a value.

**Q4.** Is `import math` an expression or a statement? *(M · 6.3)*

**Answer.** **A statement:** it does something (assigns, imports, deletes or does nothing on purpose) and gives no value.

**Q5.** Is `a * b - c` an expression or a statement? *(M · 6.3)*

**Answer.** **An expression:** it gives a value.

**Q6.** Is `del x` an expression or a statement? *(M · 6.3)*

**Answer.** **A statement:** it does something (assigns, imports, deletes or does nothing on purpose) and gives no value.

**Q7.** Is `pass` an expression or a statement? *(M · 6.3)*

**Answer.** **A statement:** it does something (assigns, imports, deletes or does nothing on purpose) and gives no value.

**Q8.** Is `"Hi" * 2` an expression or a statement? *(M · 6.3)*

**Answer.** **An expression:** it gives a value.

**Q9.** Is `total += 1` an expression or a statement? *(M · 6.3)*

**Answer.** **A statement:** it does something (assigns, imports, deletes or does nothing on purpose) and gives no value.

**Q10.** Is `x, y = 1, 2` an expression or a statement? *(M · 6.3)*

**Answer.** **A statement:** it does something (assigns, imports, deletes or does nothing on purpose) and gives no value.

## Size of a string

**Q11.** What does `len("Python")` give? *(M · 6.6)*

**Answer.** **6**.

**Q12.** What does `len("Class XI")` give? *(M · 6.6)*

**Answer.** **8**.

**Q13.** What does `len("a\nb")` give? *(M · 6.6)*

**Answer.** **3**. An escape sequence counts as one character.

**Q14.** What does `len("\t\t")` give? *(M · 6.6)*

**Answer.** **2**. An escape sequence counts as one character.

**Q15.** What does `len("It's")` give? *(M · 6.6)*

**Answer.** **4**.

**Q16.** What does `len("C:\\data")` give? *(M · 6.6)*

**Answer.** **7**. An escape sequence counts as one character.

**Q17.** What does `len("")` give? *(M · 6.6)*

**Answer.** **0**. The empty string has no characters.

**Q18.** What does `len("""ab↵cd""")` give? *(M · 6.6)*

**Answer.** **5**. The Enter inside triple quotes is a new-line character.

**Q19.** What does `len(" ")` give? *(M · 6.6)*

**Answer.** **1**.

**Q20.** What does `len("\"Hi\"")` give? *(M · 6.6)*

**Answer.** **4**. An escape sequence counts as one character.

