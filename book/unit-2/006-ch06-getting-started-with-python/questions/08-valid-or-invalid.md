# Chapter 6: Getting Started with Python: Valid or invalid? (40)

*Chapter 6 · Questions (online). Generated drills: every answer was decided by Python itself (`str.isidentifier()`, `keyword` and Python's own parser). None repeats a name or literal printed in the book or on the "Literals up close" page. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Is it valid? (identifiers)

**Q1.** Is `first_name` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** letters, digits and `_` only, not beginning with a digit.

**Q2.** Is `firstName` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** legal; Python's convention would be snake_case.

**Q3.** Is `1st_name` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** begins with a digit.

**Q4.** Is `name1` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** letters, digits and `_` only, not beginning with a digit.

**Q5.** Is `first-name` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** `-` is not allowed.

**Q6.** Is `first name` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** a space is not allowed.

**Q7.** Is `_` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** begins with `_`, which counts as a letter.

**Q8.** Is `__name` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** begins with `_`, which counts as a letter.

**Q9.** Is `Name` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** legal (capital and small letters are allowed).

**Q10.** Is `NAME` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** letters, digits and `_` only, not beginning with a digit.

**Q11.** Is `elif` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** a keyword.

**Q12.** Is `Elif` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** it is not the keyword `elif`: capital and small letters differ.

**Q13.** Is `import` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** a keyword.

**Q14.** Is `imports` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** letters, digits and `_` only, not beginning with a digit.

**Q15.** Is `try_2` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** letters, digits and `_` only, not beginning with a digit.

**Q16.** Is `try` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** a keyword.

**Q17.** Is `class2` a valid identifier? *(E · 6.5)*

**Answer.** **Valid:** letters, digits and `_` only, not beginning with a digit.

**Q18.** Is `my.name` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** `.` is not allowed.

**Q19.** Is `rate%` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** `%` is not allowed.

**Q20.** Is `pin@code` a valid identifier? *(E · 6.5)*

**Answer.** **Invalid:** `@` is not allowed.

## Is it valid? (literals)

**Q21.** Is `100` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **int**: value 100.

**Q22.** Is `-3.5` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **float**: value -3.5; strictly, `-` is an operator in front of the literal 3.5.

**Q23.** Is `0b11` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **int**: value 3.

**Q24.** Is `0b12` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **invalid**: 2 is not a binary digit.

**Q25.** Is `0o7` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **int**: value 7.

**Q26.** Is `0o8` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **invalid**: 8 is not an octal digit.

**Q27.** Is `0xff` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **int**: value 255.

**Q28.** Is `0xfg` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **invalid**: g is not a hexadecimal digit.

**Q29.** Is `1.5e2` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **float**: value 150.0.

**Q30.** Is `1.5e` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **invalid**: no digits after e.

**Q31.** Is `3e-2` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **float**: value 0.03.

**Q32.** Is `4_000` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **int**: value 4000.

**Q33.** Is `4__000` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **invalid**: only single underscores between digits.

**Q34.** Is `"Delhi"` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **str**: value 'Delhi'.

**Q35.** Is `'Mumbai"` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **invalid**: the quotes do not match.

**Q36.** Is `"""Chennai"""` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **str**: value 'Chennai'.

**Q37.** Is `False` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **bool**: value False.

**Q38.** Is `false` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **a name, not a literal**: Python looks for a variable of this name.

**Q39.** Is `7j` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **complex**: value 7j.

**Q40.** Is `0` a valid literal? If so, of what type? *(M · 6.6)*

**Answer.** **int**: value 0.

