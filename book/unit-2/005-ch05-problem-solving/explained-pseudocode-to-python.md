# Explained: Pseudocode to Python, line for line

*Chapter 5 · Explained. The printed book (section 5.6) writes every algorithm in pseudocode. Here each pseudocode of the chapter stands beside its Python program, so you can see which line becomes which. You will learn the Python from Chapter 6 on; for now, just notice how close the two are.*

*Every number on this page was computed by a program (`tools/ch05_pages2.py`) and checked.*

## 1. The keywords and their Python

| Pseudocode | Python | Example |
|---|---|---|
| INPUT a | `a = int(input())` | a whole number typed by the user |
| PRINT sum | `print(sum)` | |
| COMPUTE, SET x = … | `x = …` | `area = length * breadth` |
| IF … THEN … ELSE … END IF | `if …:` … `else:` … | indentation instead of END IF |
| ELSE IF | `elif …:` | |
| WHILE … END WHILE | `while …:` | |
| FOR i = 1 TO n | `for i in range(1, n + 1):` | range stops just before its end |
| INCREMENT i | `i = i + 1` or `i += 1` | |
| × ÷ ≤ ≥ ≠ = (in a test) | `* / <= >= != ==` | `==` asks, `=` gives a value |
| remainder of a ÷ b | `a % b` | |

## 2. Every algorithm of the chapter

Each Python program was run on the test inputs of the book and gave the same answers as the flowchart.

### W1. Sum of two numbers

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT a, b
 3  COMPUTE sum = a + b
 4  PRINT sum
```

</div>
<div markdown>

**Python**

```python
a = int(input())
b = int(input())
print(a + b)
```

</div>
</div>

### W2. Area and perimeter of a rectangle

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT length, breadth
 3  COMPUTE area = length × breadth
 4  COMPUTE perimeter = 2 × (length + breadth)
 5  PRINT area, perimeter
```

</div>
<div markdown>

**Python**

```python
length = int(input())
breadth = int(input())
print(length * breadth, 2 * (length + breadth))
```

</div>
</div>

### W3. The larger of two numbers

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT a, b
 3  IF a > b THEN
 4      PRINT a
    ELSE
 5      PRINT b
    END IF
```

</div>
<div markdown>

**Python**

```python
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)
```

</div>
</div>

### W4. Even or odd

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT n
 3  IF remainder of n ÷ 2 = 0 THEN
 4      PRINT "Even"
    ELSE
 5      PRINT "Odd"
    END IF
```

</div>
<div markdown>

**Python**

```python
n = int(input())
if n % 2 == 0:
    print('Even')
else:
    print('Odd')
```

</div>
</div>

### W5. The greatest of three numbers

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT a, b, c
 3  IF a > b THEN
 4      IF a > c THEN
 5          PRINT a
        ELSE
 6          PRINT c
        END IF
    ELSE
 7      IF b > c THEN
 8          PRINT b
        ELSE
 9          PRINT c
        END IF
    END IF
```

</div>
<div markdown>

**Python**

```python
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
```

</div>
</div>

### W6. Report card: result and grade

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT the 5 marks
 3  COMPUTE total, % = total ÷ 5, low = lowest mark
 4  IF low ≥ 33 THEN
 6      IF % ≥ 90 THEN
 7          PRINT "Grade A"
 8      ELSE IF % ≥ 75 THEN
 9          PRINT "Grade B"
10      ELSE IF % ≥ 60 THEN
11          PRINT "Grade C"
        ELSE
12          PRINT "Grade D"
        END IF
    ELSE
 5      PRINT "Fail"
    END IF
```

</div>
<div markdown>

**Python**

```python
m = [int(input()) for _ in range(5)]
per = sum(m) / 5
if min(m) >= 33:
    if per >= 90:
        print('Grade A')
    elif per >= 75:
        print('Grade B')
    elif per >= 60:
        print('Grade C')
    else:
        print('Grade D')
else:
    print('Fail')
```

</div>
</div>

### W7. Average of numbers until 0 is typed

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  SET sum = 0, count = 0
 3  INPUT x
 4  WHILE x ≠ 0
 5      COMPUTE sum = sum + x
 6      INCREMENT count
 3      INPUT x
    END WHILE
 7  COMPUTE avg = sum ÷ count
 8  PRINT avg
```

</div>
<div markdown>

**Python**

```python
total = count = 0
x = int(input())
while x != 0:
    total = total + x
    count = count + 1
    x = int(input())
print(total / count)
```

</div>
</div>

### W8. GCD and LCM by Euclid's method

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT a, b
 3  SET x = a, y = b
 4  WHILE b ≠ 0
 5      COMPUTE r = remainder of a ÷ b
 6      SET a = b
 7      SET b = r
    END WHILE
 8  COMPUTE LCM = x × y ÷ a
 9  PRINT a, LCM
```

</div>
<div markdown>

**Python**

```python
a = int(input())
b = int(input())
x, y = a, b
while b != 0:
    r = a % b
    a = b
    b = r
lcm = x * y // a
print(a, lcm)
```

</div>
</div>

### W9. The series 1 + x + x² + … + xⁿ

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT x, n
 3  SET sum = 1, term = 1, i = 1
 4  WHILE i ≤ n
 5      COMPUTE term = term × x
 6      COMPUTE sum = sum + term
 7      INCREMENT i
    END WHILE
 8  PRINT sum
```

</div>
<div markdown>

**Python**

```python
x = int(input())
n = int(input())
total, term, i = 1, 1, 1
while i <= n:
    term = term * x
    total = total + term
    i = i + 1
print(total)
```

</div>
</div>

### W10. The factorial of n

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT n
 3  SET fact = 1, i = 1
 4  WHILE i ≤ n
 5      COMPUTE fact = fact × i
 6      INCREMENT i
    END WHILE
 7  PRINT fact
```

</div>
<div markdown>

**Python**

```python
n = int(input())
fact, i = 1, 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)
```

</div>
</div>

### ATM. Cash from an ATM

<div class="grid2" markdown>
<div markdown>

**Pseudocode**

```text
 2  INPUT card                (the bank finds the balance)
 3  SET tries = 0
 4  INPUT pin
 5  WHILE pin is wrong
 6      INCREMENT tries
 7      IF tries = 3 THEN
 8          PRINT "Card blocked" and STOP
        END IF
 4      INPUT pin
    END WHILE
 9  INPUT amount
10  IF amount is a multiple of 100 AND amount <= balance THEN
11      PRINT the cash
    ELSE
12      PRINT "Cannot pay this amount"
    END IF
```

</div>
<div markdown>

**Python**

```python
balance = int(input())
tries = 0
while True:
    pin = int(input())
    if pin == 4321:
        amount = int(input())
        if amount % 100 == 0 and amount <= balance:
            print('Cash', amount)
        else:
            print('Cannot pay this amount')
        break
    tries = tries + 1
    if tries == 3:
        print('Card blocked')
        break
```

</div>
</div>

*Notice:* in W6 the five marks are kept together as one list, `m`; in the ATM, Python leaves the loop with `break`. These are ways of writing the same steps that you will meet in Chapters 9 and 10.

## 3. The same algorithm in three styles

There is no single standard for pseudocode. Books and teachers write it in different styles; all are accepted if the
steps are exact and in order. Here is W3, the larger of two numbers, three ways:

<div class="grid2" markdown>
<div markdown>

**Style 1: this book (as NCERT)**

```text
INPUT a, b
IF a > b THEN
    PRINT a
ELSE
    PRINT b
END IF
```

</div>
<div markdown>

**Style 2: numbered steps**

```text
Step 1: Start
Step 2: Read a, b
Step 3: If a > b then
            Display a
        Else
            Display b
        Endif
Step 4: Stop
```

</div>
</div>

**Style 3: BEGIN … END, with ←**

```text
BEGIN
    READ a, b
    IF a > b
        big ← a
    ELSE
        big ← b
    ENDIF
    WRITE big
END
```

*What stays the same in every style:* one step on a line, the IF with both of its paths, the closing END IF, and the indentation. ← and = both mean "put the value into".
