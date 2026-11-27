# Practice: Tricky assignments and `None`

*Chapter 6 · Practice. Section 6.7 swaps two values with `x, y = y, x`. Here are harder ones: several names on the left, the same name twice, and the special value `None`. Every output was made by running Python 3.12.7.*

**The one rule:** Python works out the **whole right side first**, from left to right, using the values the names have **before** the line; then it ties the names on the left, from left to right. If a name appears twice on the left, the last value wins.

**`None` in the shell:** typing a name tied to `None` shows nothing; `print()` shows the word `None`.

## Predict the output

**Q1.** Predict the output. *(H · 6.7)*

```python
x, x = 20, 30
print(x)
```


**Answer.** 

```text
30
```
*Why:* the right side gives (20, 30); x is tied to 20, then to 30.

**Q2.** Predict the output. *(H · 6.7)*

```python
a, b, c = 5, 10, 7
b, c, a = a + 1, b + 2, c - 1
print(a, b, c)
```


**Answer.** 

```text
6 6 12
```
*Why:* the right side (6, 12, 6) is worked out first, then b, c, a are tied in order.

**Q3.** Predict the output. *(H · 6.7)*

```python
x, y = 1, 2
x, y = y + 1, x + 2
print(x, y)
```


**Answer.** 

```text
3 3
```
*Why:* the right side uses the OLD x and y: (2 + 1, 1 + 2).

**Q4.** Predict the output. *(H · 6.7)*

```python
p, q = 3, 5
q, p = p - 2, p + 2
print(p, q)
```


**Answer.** 

```text
5 1
```
*Why:* the right side is (1, 5): q = 1, p = 5.

**Q5.** Predict the output. *(H · 6.7)*

```python
x = 10
y, y = x + 2, x + 5
print(y)
```


**Answer.** 

```text
15
```
*Why:* y is tied to 12, then to 15.

**Q6.** Predict the output. *(H · 6.7)*

```python
x, x = 20, 30
y, y = x + 10, x + 20
print(x, y)
```


**Answer.** 

```text
30 50
```
*Why:* x ends as 30; then y is tied to 40, then to 50.

**Q7.** Predict the output. *(H · 6.7)*

```python
a = b = c = 5
b = 6
print(a, b, c)
```


**Answer.** 

```text
5 6 5
```
*Why:* b = 6 moves only b.

**Q8.** Predict the output. *(H · 6.7)*

```python
a, b = 2, 3
a = a + b
b = a - b
a = a - b
print(a, b)
```


**Answer.** 

```text
3 2
```
*Why:* a swap without a third variable, using + and −.

**Q9.** Predict the output. *(H · 6.7)*

```python
a, b = 4, 9
a, b = b, a + b
print(a, b)
```


**Answer.** 

```text
9 13
```
*Why:* right side first: (9, 4 + 9).

**Q10.** Predict the output. *(H · 6.7)*

```python
m, n = 1, 1
m, n = n, m + n
m, n = n, m + n
print(m, n)
```


**Answer.** 

```text
2 3
```
*Why:* each line uses the old m and n (like the Fibonacci numbers).

**Q11.** Predict the output. *(H · 6.7)*

```python
x = 5
x, y = x * 2, x * 3
print(x, y)
```


**Answer.** 

```text
10 15
```
*Why:* x * 2 and x * 3 both use the old x = 5.

**Q12.** Predict the output. *(H · 6.7)*

```python
i, j = 0, 1
i, j = j, i
j, i = i, j
print(i, j)
```


**Answer.** 

```text
0 1
```
*Why:* swapped, then swapped back.

**Q13.** Predict the output. *(H · 6.7)*

```python
a, b, c = "x", "y", "z"
a, b, c = c, a, b
print(a + b + c)
```


**Answer.** 

```text
zxy
```


**Q14.** Predict the output. *(H · 6.7)*

```python
x = y = 0
x = x + 1
y = y + 2
print(x, y)
```


**Answer.** 

```text
1 2
```


**Q15.** Predict the output. *(H · 6.7)*

```python
n = 5
n, m = n + 1, n + 2
print(n, m)
```


**Answer.** 

```text
6 7
```


**Q16.** Predict the output. *(M · 6.6)*

```python
result = None
print(result)
```


**Answer.** 

```text
None
```
*Why:* print shows the word None.

**Q17.** Predict the output. *(M · 6.6)*

```python
print(None)
```


**Answer.** 

```text
None
```
*Why:* print shows the word None.

**Q18.** Predict the output. *(M · 6.6)*

```python
x = None
print(type(x))
```


**Answer.** 

```text
<class 'NoneType'>
```
*Why:* None is the only value of its type.

**Q19.** Predict the output. *(M · 6.6)*

```python
x = None
x = 5
print(x)
```


**Answer.** 

```text
5
```


**Q20.** Predict the output. *(M · 6.6)*

```python
x = None
print(x is None)
```


**Answer.** 

```text
True
```
*Why:* `is None` is the right way to test for None.

**Q21.** Predict the output. *(M · 6.6)*

```python
print(print("Hi"))
```


**Answer.** 

```text
Hi
None
```
*Why:* print() shows Hi, and gives back None, which the outer print shows.

**Q22.** Predict the output. *(M · 6.6)*

```python
a = print("A")
print(a)
```


**Answer.** 

```text
A
None
```
*Why:* print gives back None.

**Q23.** Predict the output. *(M · 6.6)*

```python
x = None
y = x
print(y)
```


**Answer.** 

```text
None
```


**Q24.** Predict the output. *(M · 6.6)*

```python
x = 0
print(x is None)
```


**Answer.** 

```text
False
```
*Why:* 0 is a value: it is not None.

**Q25.** Predict the output. *(M · 6.6)*

```python
x = ""
print(x is None, len(x))
```


**Answer.** 

```text
False 0
```
*Why:* an empty string is a value, not None.

