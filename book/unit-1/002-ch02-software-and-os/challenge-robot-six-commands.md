# Challenge: The robot that knows six commands

*Chapter 2 · Challenge. An activity for two students and a classroom. It shows why programs must use exact commands, what a translator does, and what a syntax error is.*

## The rules

One student is the **robot**. It understands only these six commands, exactly as written:

1. `MOVE n (steps forward)`
2. `TURN LEFT`
3. `TURN RIGHT`
4. `PICK UP`
5. `PUT DOWN`
6. `SAY "words"`

The other student is the **programmer**, who wants the robot to "put the book from the table on the chair".

## Round 1: high-level vs low-level

"Put the book on the chair" is a **high-level** instruction: the robot does not understand it. The programmer must break
it into the robot's own commands, for example:

```text
MOVE 3
TURN LEFT
MOVE 2
PICK UP
TURN RIGHT
TURN RIGHT
MOVE 2
PUT DOWN
SAY "Done"
```

This is what a **translator** does: it turns one high-level instruction into many small machine instructions.

## Round 2: compiler or interpreter?

- **Compiler style:** a third student reads the whole list first, checks every line, and only then hands it to the robot.
- **Interpreter style:** the third student reads one line, the robot does it at once, then the next line.

## Round 3: a syntax error

Add the line `FLY TO THE TABLE`. The robot refuses: it is not one of its six commands. In compiler style the robot does
nothing at all until the list is fixed; in interpreter style it carries out the lines before it, then stops.

## Think about it

1. Why must the robot's commands be exact? *(A computer cannot guess what "go near the table" means.)*
2. Write the commands to bring the book back. *(Many answers are right; check by acting it out.)*
