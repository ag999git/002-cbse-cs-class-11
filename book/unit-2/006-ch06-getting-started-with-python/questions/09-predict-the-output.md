# Chapter 6: Getting Started with Python: Predict the output (40)

*Chapter 6 · Questions (online). Each program was run by Python; the answer box is its real output. Some use things you meet fully in Chapter 7 (`//`, `%`, `**`, `end`, `sep`). Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Predict the output

**Q1.** Predict the output. *(E · 6.3–6.8)*

```python
print("Hello", "Class", 11)
```


**Answer.** 

```text
Hello Class 11
```


**Q2.** Predict the output. *(E · 6.3–6.8)*

```python
print(7 + 5, 7 * 5)
```


**Answer.** 

```text
12 35
```


**Q3.** Predict the output. *(E · 6.3–6.8)*

```python
print("7" + "5")
```


**Answer.** 

```text
75
```
*Why:* two strings joined, not added.

**Q4.** Predict the output. *(E · 6.3–6.8)*

```python
print("ab" * 3)
```


**Answer.** 

```text
ababab
```
*Why:* a string repeated.

**Q5.** Predict the output. *(E · 6.3–6.8)*

```python
x = 10
x = x + 5
print(x)
```


**Answer.** 

```text
15
```


**Q6.** Predict the output. *(E · 6.3–6.8)*

```python
a = 3
b = a
a = 4
print(a, b)
```


**Answer.** 

```text
4 3
```


**Q7.** Predict the output. *(E · 6.3–6.8)*

```python
name = "Asha"
Name = "Ravi"
print(name, Name)
```


**Answer.** 

```text
Asha Ravi
```


**Q8.** Predict the output. *(E · 6.3–6.8)*

```python
x, y = 2, 9
print(y, x)
```


**Answer.** 

```text
9 2
```


**Q9.** Predict the output. *(E · 6.3–6.8)*

```python
a = b = 7
b = b + 1
print(a, b)
```


**Answer.** 

```text
7 8
```


**Q10.** Predict the output. *(E · 6.3–6.8)*

```python
p, q = 4, 6
p, q = q, p
print(p - q)
```


**Answer.** 

```text
2
```


**Q11.** Predict the output. *(E · 6.3–6.8)*

```python
print(type(7), type(7.0))
```


**Answer.** 

```text
<class 'int'> <class 'float'>
```


**Q12.** Predict the output. *(E · 6.3–6.8)*

```python
print(type("7"), type(True))
```


**Answer.** 

```text
<class 'str'> <class 'bool'>
```


**Q13.** Predict the output. *(E · 6.3–6.8)*

```python
x = 5
print(type(x))
x = "five"
print(type(x))
```


**Answer.** 

```text
<class 'int'>
<class 'str'>
```


**Q14.** Predict the output. *(E · 6.3–6.8)*

```python
print(0b11 + 0o11 + 0x11)
```


**Answer.** 

```text
29
```
*Why:* 3 + 9 + 17.

**Q15.** Predict the output. *(E · 6.3–6.8)*

```python
print(1e3)
```


**Answer.** 

```text
1000.0
```
*Why:* a float: 1000.0.

**Q16.** Predict the output. *(E · 6.3–6.8)*

```python
print(len("Python"))
```


**Answer.** 

```text
6
```


**Q17.** Predict the output. *(E · 6.3–6.8)*

```python
print(len("a b c"))
```


**Answer.** 

```text
5
```
*Why:* spaces count as characters.

**Q18.** Predict the output. *(E · 6.3–6.8)*

```python
print("Line1\nLine2")
```


**Answer.** 

```text
Line1
Line2
```


**Q19.** Predict the output. *(E · 6.3–6.8)*

```python
print("Tab\tend")
```


**Answer.** 

```text
Tab	end
```


**Q20.** Predict the output. *(E · 6.3–6.8)*

```python
print(len("\n\t"))
```


**Answer.** 

```text
2
```
*Why:* each escape sequence is one character.

**Q21.** Predict the output. *(M · 6.3–6.8)*

```python
print(5, end=" ")
print(6)
```


**Answer.** 

```text
5 6
```
*Why:* end=" " stops the new line.

**Q22.** Predict the output. *(M · 6.3–6.8)*

```python
print("A", "B", sep="-")
```


**Answer.** 

```text
A-B
```
*Why:* sep sets the separator.

**Q23.** Predict the output. *(M · 6.3–6.8)*

```python
# print("hidden")
print("shown")
```


**Answer.** 

```text
shown
```


**Q24.** Predict the output. *(M · 6.3–6.8)*

```python
x = 3   # x = 4
print(x)
```


**Answer.** 

```text
3
```


**Q25.** Predict the output. *(M · 6.3–6.8)*

```python
"""A docstring
over two lines"""
print("after the note")
```


**Answer.** 

```text
after the note
```


**Q26.** Predict the output. *(M · 6.3–6.8)*

```python
s = """one
two"""
print(s)
```


**Answer.** 

```text
one
two
```


**Q27.** Predict the output. *(M · 6.3–6.8)*

```python
total = (10 +
         20 +
         30)
print(total)
```


**Answer.** 

```text
60
```
*Why:* one statement over three lines, inside brackets.

**Q28.** Predict the output. *(M · 6.3–6.8)*

```python
a = 1; b = 2; print(a + b)
```


**Answer.** 

```text
3
```


**Q29.** Predict the output. *(M · 6.3–6.8)*

```python
x = 5
y = x * 2
x = 100
print(y)
```


**Answer.** 

```text
10
```
*Why:* y was worked out when x was 5.

**Q30.** Predict the output. *(M · 6.3–6.8)*

```python
count = 0
count = count + 1
count = count + 1
print(count)
```


**Answer.** 

```text
2
```


**Q31.** Predict the output. *(M · 6.3–6.8)*

```python
price = 50
price = price * 2
price = price - 10
print(price)
```


**Answer.** 

```text
90
```


**Q32.** Predict the output. *(M · 6.3–6.8)*

```python
x = None
print(x)
```


**Answer.** 

```text
None
```


**Q33.** Predict the output. *(M · 6.3–6.8)*

```python
first, second = "Hi", "there"
print(second, first)
```


**Answer.** 

```text
there Hi
```


**Q34.** Predict the output. *(M · 6.3–6.8)*

```python
a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)
```


**Answer.** 

```text
3 1 2
```


**Q35.** Predict the output. *(M · 6.3–6.8)*

```python
x = 10
y = 3
print(x // y, x % y)
```


**Answer.** 

```text
3 1
```


**Q36.** Predict the output. *(M · 6.3–6.8)*

```python
print(2 ** 3 ** 0)
```


**Answer.** 

```text
2
```
*Why:* `**` is worked out from the right: `3 ** 0` = 1, then `2 ** 1` = 2.

**Q37.** Predict the output. *(M · 6.3–6.8)*

```python
print(10 / 4)
```


**Answer.** 

```text
2.5
```


**Q38.** Predict the output. *(M · 6.3–6.8)*

```python
print(True + True)
```


**Answer.** 

```text
2
```
*Why:* True counts as 1 (Chapter 7).

**Q39.** Predict the output. *(M · 6.3–6.8)*

```python
marks = 92
print("Marks:", marks)
```


**Answer.** 

```text
Marks: 92
```


**Q40.** Predict the output. *(M · 6.3–6.8)*

```python
x = 7
x = "seven"
x = 7.0
print(x, type(x))
```


**Answer.** 

```text
7.0 <class 'float'>
```


