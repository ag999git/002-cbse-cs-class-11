# Helps you understand: Python's limits

*Chapter 6 · Helps you understand. The printed chapter lists the features of Python. Every language also has limits. Here are Python's, why each one exists, and why it rarely matters at school.*

| Limit | Why it exists | Does it matter at school? |
|---|---|---|
| **Slower than C or C++** for heavy calculation | Python's interpreter reads and runs your statements one at a time while the program runs; a C++ compiler turns the whole program into machine code first | Hardly ever: your programs finish in a blink. Big Python libraries (NumPy, used in science) run their heavy parts in C to get the speed back |
| **Fewer ready-made libraries for some jobs** (for example, fast mobile games or device drivers) | Each language grew where its users were: C for operating systems, Java for Android apps, Python for data, AI and teaching | No |
| **Not easy to convert** to another language | Python's short, flexible statements (no declared types, indentation for blocks) have no one-to-one match in C or Java | No |
| **Types are not fixed on names** (some books: "not strong on type-binding") | This is **dynamic typing** (section 6.7): a name can be tied to an `int` now and a `str` later | Yes, a little: a mix-up of types shows only when that line runs |

## "Not strong on type-binding" is not "weakly typed"

Some books list "not strong on type-binding" as a minus. It means only that a **name** has no fixed type: the box-or-tag
idea of section 6.7. It does **not** mean Python mixes types carelessly. Python refuses to add text to a number:

```python
print("5" + 3)
```

```text
TypeError: can only concatenate str (not "int") to str
```

So Python is **dynamically** typed (names have no type) but **strongly** typed (values are never mixed quietly). In
the exam: "Python is dynamically typed"; never "Python is weakly typed".
