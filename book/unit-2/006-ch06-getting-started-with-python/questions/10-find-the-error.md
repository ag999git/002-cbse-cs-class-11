# Chapter 6: Getting Started with Python: Find the error (25)

*Chapter 6 · Questions (online). Every error message is the real one from Python; every corrected program was run without error. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Find the error

**Q1.** Find the error and correct it. *(M · 6.3–6.7)*

```python
Print("Welcome")
```


**Answer.** Python says: `NameError: name 'Print' is not defined. Did you mean: 'print'?`. *Why:* `print` is written in small letters; Python is case-sensitive. Corrected:

```python
print("Welcome")
```


**Q2.** Find the error and correct it. *(M · 6.3–6.7)*

```python
print("Welcome)
```


**Answer.** Python says: `SyntaxError: unterminated string literal (detected at line 1)`. *Why:* the string is not closed. Corrected:

```python
print("Welcome")
```


**Q3.** Find the error and correct it. *(M · 6.3–6.7)*

```python
print "Welcome"
```


**Answer.** Python says: `SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?`. *Why:* Python 3 needs brackets. Corrected:

```python
print("Welcome")
```


**Q4.** Find the error and correct it. *(M · 6.3–6.7)*

```python
print("Total:", total)
```


**Answer.** Python says: `NameError: name 'total' is not defined`. *Why:* the name is used before it is given a value. Corrected:

```python
total = 0
print("Total:", total)
```


**Q5.** Find the error and correct it. *(M · 6.3–6.7)*

```python
marks = 90
print(Marks)
```


**Answer.** Python says: `NameError: name 'Marks' is not defined. Did you mean: 'marks'?`. *Why:* the name was created with a small m. Corrected:

```python
marks = 90
print(marks)
```


**Q6.** Find the error and correct it. *(M · 6.3–6.7)*

```python
roll-no = 12
print(roll-no)
```


**Answer.** Python says: `SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?`. *Why:* `-` is not allowed in a name. Corrected:

```python
roll_no = 12
print(roll_no)
```


**Q7.** Find the error and correct it. *(M · 6.3–6.7)*

```python
2nd_term = 80
```


**Answer.** Python says: `SyntaxError: invalid decimal literal`. *Why:* a name may not begin with a digit. Corrected:

```python
term_2 = 80
```


**Q8.** Find the error and correct it. *(M · 6.3–6.7)*

```python
total marks = 450
```


**Answer.** Python says: `SyntaxError: invalid syntax`. *Why:* a name may not contain a space. Corrected:

```python
total_marks = 450
```


**Q9.** Find the error and correct it. *(M · 6.3–6.7)*

```python
for = 5
```


**Answer.** Python says: `SyntaxError: invalid syntax`. *Why:* `for` is a keyword. Corrected:

```python
count = 5
```


**Q10.** Find the error and correct it. *(M · 6.3–6.7)*

```python
10 = x
```


**Answer.** Python says: `SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?`. *Why:* the value goes on the right. Corrected:

```python
x = 10
```


**Q11.** Find the error and correct it. *(M · 6.3–6.7)*

```python
x + y = 15
```


**Answer.** Python says: `SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?`. *Why:* the left side of `=` must be a name. Corrected:

```python
x, y = 7, 8
total = x + y
```


**Q12.** Find the error and correct it. *(M · 6.3–6.7)*

```python
x = 5
  print(x)
```


**Answer.** Python says: `IndentationError: unexpected indent`. *Why:* the second line starts with spaces for no reason. Corrected:

```python
x = 5
print(x)
```


**Q13.** Find the error and correct it. *(M · 6.3–6.7)*

```python
print("Marks: " + 92)
```


**Answer.** Python says: `TypeError: can only concatenate str (not "int") to str`. *Why:* text and a number cannot be joined with `+`. Corrected:

```python
print("Marks:", 92)
```


**Q14.** Find the error and correct it. *(M · 6.3–6.7)*

```python
print(10 / 0)
```


**Answer.** Python says: `ZeroDivisionError: division by zero`. *Why:* division by zero. Corrected:

```python
print(10 / 2)
```


**Q15.** Find the error and correct it. *(M · 6.3–6.7)*

```python
x = 012
```


**Answer.** Python says: `SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers`. *Why:* a whole number may not begin with 0. Corrected:

```python
x = 12
```


**Q16.** Find the error and correct it. *(M · 6.3–6.7)*

```python
x = 0b102
```


**Answer.** Python says: `SyntaxError: invalid digit '2' in binary literal`. *Why:* 2 is not a binary digit. Corrected:

```python
x = 0b101
```


**Q17.** Find the error and correct it. *(M · 6.3–6.7)*

```python
pin = 0o189
```


**Answer.** Python says: `SyntaxError: invalid digit '8' in octal literal`. *Why:* 8 and 9 are not octal digits. Corrected:

```python
pin = 0o17
```


**Q18.** Find the error and correct it. *(M · 6.3–6.7)*

```python
name = 'Asha"
```


**Answer.** Python says: `SyntaxError: unterminated string literal (detected at line 1)`. *Why:* the opening and closing quotes differ. Corrected:

```python
name = "Asha"
```


**Q19.** Find the error and correct it. *(M · 6.3–6.7)*

```python
// my program
print(1)
```


**Answer.** Python says: `SyntaxError: invalid syntax`. *Why:* a comment starts with `#`, not `//`. Corrected:

```python
# my program
print(1)
```


**Q20.** Find the error and correct it. *(M · 6.3–6.7)*

```python
print("A")
print("B"
```


**Answer.** Python says: `SyntaxError: '(' was never closed`. *Why:* a bracket is not closed; even line 1 does not run. Corrected:

```python
print("A")
print("B")
```


**Q21.** Find the error and correct it. *(M · 6.3–6.7)*

```python
a, b = 1, 2, 3
```


**Answer.** Python says: `ValueError: too many values to unpack (expected 2)`. *Why:* three values cannot go into two names. Corrected:

```python
a, b, c = 1, 2, 3
```


**Q22.** Find the error and correct it. *(M · 6.3–6.7)*

```python
a, b, c = 1, 2
```


**Answer.** Python says: `ValueError: not enough values to unpack (expected 3, got 2)`. *Why:* two values cannot go into three names. Corrected:

```python
a, b = 1, 2
```


**Q23.** Find the error and correct it. *(M · 6.3–6.7)*

```python
price = 50$
```


**Answer.** Python says: `SyntaxError: invalid syntax`. *Why:* `$` is not part of Python. Corrected:

```python
price = 50
```


**Q24.** Find the error and correct it. *(M · 6.3–6.7)*

```python
print(len(5))
```


**Answer.** Python says: `TypeError: object of type 'int' has no len()`. *Why:* a number has no length; text does. Corrected:

```python
print(len("5"))
```


**Q25.** Find the error and correct it. *(M · 6.3–6.7)*

```python
class = "XI"
print(class)
```


**Answer.** Python says: `SyntaxError: invalid syntax`. *Why:* `class` is a keyword. Corrected:

```python
section = "XI"
print(section)
```


