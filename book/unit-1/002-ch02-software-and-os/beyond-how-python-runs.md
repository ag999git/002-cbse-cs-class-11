# Beyond syllabus: How Python really runs

*Chapter 2 · Beyond syllabus. For the exam, Python is an interpreted language. Inside, it works in two stages. This page shows them, with the real output of a real Python.*

## Two stages

1. **Compile to bytecode.** Python reads the **whole** file, checks its grammar, and turns it into **bytecode**: short,
   simple instructions for an imaginary machine.
2. **Run the bytecode.** The **Python virtual machine** (a program inside Python) carries out the bytecode one
   instruction at a time, the way an interpreter does.

## The real bytecode of a two-line program

The program:

```python
a = 10
print(a + 5)
```

prints `15`. Its bytecode, as Python 3.12 shows it with the `dis` module:

```text
  0           0 RESUME                   0
  1           2 LOAD_CONST               0 (10)
              4 STORE_NAME               0 (a)
  2           6 PUSH_NULL
              8 LOAD_NAME                1 (print)
             10 LOAD_NAME                0 (a)
             12 LOAD_CONST               1 (5)
             14 BINARY_OP                0 (+)
             18 CALL                     1
             26 POP_TOP
             28 RETURN_CONST             2 (None)
```

`LOAD_CONST` puts a value on a stack, `STORE_NAME` saves it in a variable, `BINARY_OP` adds, `CALL` calls `print`.
(The exact names change a little between Python versions.)

## Why it matters

- A **grammar error anywhere** stops Python before **line 1** runs, because stage 1 reads the whole file first. Try
  `b = a +` in line 3: Python reports a SyntaxError in line 3, and nothing is printed.
- A **mistake found only while running** (dividing by 0, an unknown name) stops it **at that line**, after the lines
  before it have run.
- Python saves the bytecode of imported modules in a `__pycache__` folder (`.pyc` files), so they start faster next time.

## So, compiler or interpreter?

For the syllabus and the exam: **interpreter**. The full truth: Python compiles to bytecode, then interprets the bytecode.
Java does something similar; C and C++ are compiled all the way to machine code.
