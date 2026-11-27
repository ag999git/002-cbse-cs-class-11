# Chapter 6: Getting Started with Python: Case studies (8)

*Chapter 6 · Questions (online). Each case has three parts. Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets. Every output and error message on this page was made by running Python 3.12.7 (`tools/ch06_typed_questions.py`).*

## Case studies

**Q1.** **Riya's script.** Riya tested these lines in the shell and saw 168 and 3600. She saved them as a script, ran it, and saw only "Done".

```python
7 * 24
60 * 60
print("Done")
```
(a) Why do the numbers not appear? (b) Correct the script. (c) Where else would the numbers appear without print?

**Answer.** (a) In a script a bare expression shows nothing; only print() shows output. (b) `print(7 * 24)` and `print(60 * 60)`. (c) In the shell and in the last line of a Colab or Jupyter cell.

**Q2.** **Arjun copies code from a PDF.** He pasted this from a book page:

```python
1 marks = 90
2 print(marks)
```
(a) What goes wrong? (b) Why? (c) What habit prevents it?

**Answer.** (a) `SyntaxError: invalid syntax`. (b) The line numbers of the book were copied into the program. (c) Copy code from the website or the notebooks, not from a PDF; delete line numbers and `>>>` signs.

**Q3.** **A lab without the internet.** The school's internet fails on the day of a practical. (a) Which tools still work: IDLE, Colab, Jupyter? (b) Why? (c) Which one is used in the exam?

**Answer.** (a) IDLE and Jupyter. (b) They run Python on the computer itself (Jupyter through a local server); Colab runs on Google's computers through the internet. (c) IDLE.

**Q4.** **Names in a marks program.** A student used the names `a`, `b`, `l`, `Total-Marks`, `print` and `PASS`. (a) Which name stops the program? (b) Which names are legal but poor, and why? (c) Suggest better names.

**Answer.** (a) `Total-Marks` (`-` is not allowed). (b) `a`, `b` (meaningless), `l` (looks like 1), `print` (hides the function), `PASS` is fine only if it is a constant. (c) `maths_marks`, `science_marks`, `count`, `total_marks`, `PASS_MARK`.

**Q5.** **Kunal's token homework.** He must cut `if total >= 33 and attendance >= 75:` into tokens. (a) How many tokens? (b) Name the kinds. (c) Is `and` an operator or a keyword?

**Answer.** (a) **9** tokens. (b) keywords `if`, `and`; identifiers `total`, `attendance`; operators `>=` (twice); literals `33`, `75`; punctuator `:`. (c) Both: a keyword that works as a (logical) operator.

**Q6.** **The shopkeeper's price tags.** Neha models her shop:

```python
price = 120
quantity = 3
print(price * quantity)
price = 100
print(price * quantity)
```
(a) What is printed? (b) Draw what happens to the tag `price`. (c) Why does the first answer not change?

**Answer.** (a)

```text
360
300
```
(b) `price` is first tied to 120, then moved to a new object 100; 120 has no tag now. (c) The first product was worked out and printed before the tag moved; nothing remembers the expression.

**Q7.** **Sneha's swap.** She wants to swap a and b:

```python
a, b = 3, 8
a = b
b = a
print(a, b)
```
(a) What is printed? (b) What went wrong? (c) Correct it in two ways.

**Answer.** (a) `8 8`. (b) `a = b` wiped out the old value of a before it was saved. (c) `t = a`, `a = b`, `b = t`; or `a, b = b, a`.

**Q8.** **Rohit's error message.**

```python
total = 450
print(Total)
```
(a) Which error is shown? (b) What is its cause? (c) Which feature of Python explains it?

**Answer.** (a) `NameError: name 'Total' is not defined. Did you mean: 'total'?`. (b) The name was created as `total` but used as `Total`. (c) Python is case-sensitive.

