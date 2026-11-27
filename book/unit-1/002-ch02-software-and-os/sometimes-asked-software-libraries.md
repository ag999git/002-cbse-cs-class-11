# Sometimes asked: Software libraries

*Chapter 2 · Sometimes asked. Both reference books ask "What is a software library? Name some Python libraries." Here is the answer, with real examples. Python modules are taught fully in Chapter 15.*

## What a library is

A **software library** is a collection of ready-made, tested code (functions) that any programmer can use instead of
writing it again. In Python, each library is a **module** that you bring in with `import`.

*Like:* a reference book on the shelf. You do not work out √144 by hand every time; you look it up.

## Real examples (run on a computer, real output)

```python
import math
print(math.sqrt(144))        # 12.0
print(math.pi)               # 3.141592653589793
print(math.ceil(4.2), math.floor(4.8))   # 5 4

import statistics
print(statistics.mean([82, 75, 91]))     # 82.66666666666667

import random
print(random.randint(1, 6))  # a dice throw: any number from 1 to 6
```

## Libraries you will meet

| Library | What it gives | Where |
|---|---|---|
| `math` | sqrt, pi, ceil, floor, pow, sin, cos | Class XI syllabus (Chapter 15) |
| `random` | random, randint, randrange | Class XI syllabus (Chapter 15) |
| `statistics` | mean, median, mode | Class XI syllabus (Chapter 15) |
| NumPy | fast arrays and maths on lakhs of numbers | beyond the syllabus |
| Pandas | tables of data (like a spreadsheet in code) | beyond the syllabus (Informatics Practices) |
| Matplotlib | charts and graphs | beyond the syllabus |

## Why libraries help

1. **Saves time:** the code is already written.
2. **Fewer bugs:** it has been tested by thousands of users.
3. **Programs stay short:** one line `math.sqrt(x)` instead of a loop.
