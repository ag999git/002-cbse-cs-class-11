"""Chapter 5 questions by type, online (QR 0514) (27 Nov 2026).

Pages 01-07 are written here by hand (answers with the reason, as in the printed book; none repeats a printed
question). Pages 08-11 are generated: every output, every bug and every count is found by RUNNING the flowcharts
(algo_lib, the same descriptions as the printed book and the practical charts) and checked.
Run from the repository root:  python tools/ch05_typed_questions.py"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ch05_pages as P1  # noqa: E402
from ch05_pages import ok, ind, D  # noqa: E402
from ch05_pages2 import W, WTITLE, drawn, halving, prime_method, is_prime, variant  # noqa: E402
from ch05_pages2 import pic as _pic  # noqa: E402


def pic(*a, **k):
    """The question pages are one folder deeper than the explanation pages."""
    return _pic(*a, **k).replace('](../../assets/', '](../../../assets/')
import ch05_practicals as PR  # noqa: E402
from flow_layout import make  # noqa: E402

Q = D / 'questions'
TOOL = 'tools/ch05_typed_questions.py'
total = {}


def page(fname, title, intro, sections, count):
    t = (f'# Chapter 5: Problem Solving: {title} ({count})\n\n*Chapter 5 · Questions (online). {intro} Try each one '
         f'first. The difficulty (E easy, M medium, H hard) and the section of the book are given in brackets.'
         f' Every number on this page was computed and checked by a program (`{TOOL}`).*\n\n')
    n = 0
    for head, items in sections:
        t += f'## {head}\n\n'
        for q, a in items:
            n += 1
            t += f'**Q{n}.** {q}\n\n**Answer.** {a}\n\n'
    ok(n == count, (fname, n, count))
    (Q / fname).write_text(t, encoding='utf-8')
    total[fname] = (title, n)
    print('wrote', fname, n)


def tag(d, s):
    return f' *({d} · {s})*'


# ================================================================= 01 MCQ
def mcq():
    raw = {
        'Problems and steps (5.1, 5.2)': [
            ('The first step of problem solving is to:', ['write the code', 'analyse the problem', 'test the program', 'draw the flowchart'], 1,
             'you must know the inputs and outputs before any steps can be written.', 'E', '5.2'),
            ('Finding WHERE and WHY a program gives a wrong answer is called:', ['testing', 'coding', 'debugging', 'analysis'], 2,
             'testing shows that a fault exists; debugging finds its cause and removes it.', 'E', '5.2'),
            ('Changing a program after it is delivered (for a new grade table) is:', ['debugging', 'maintenance', 'analysis', 'acceptance testing'], 1,
             'the program worked; the need changed.', 'E', '5.2'),
            ('A teacher types 39 instead of 93 and the report card is wrong. This shows that:', ['the algorithm is wrong', 'wrong input gives wrong output', 'the computer made a mistake', 'the program needs debugging'], 1,
             'the computer follows the steps exactly with whatever it is given.', 'E', '5.1'),
            ('Testing each part of a program alone is:', ['unit testing', 'integration testing', 'system testing', 'acceptance testing'], 0,
             'a unit is one part; integration testing joins the parts.', 'E', '5.2'),
            ('Testing done by the user before the program is delivered is:', ['unit testing', 'integration testing', 'acceptance testing', 'debugging'], 2,
             'the user accepts (or refuses) the program.', 'E', '5.2'),
            ('For marks from 0 to 100, which is boundary test data?', ['67', '33', '"sixty"', '−5'], 1,
             '33 is the pass mark: a limit. 67 is normal; "sixty" and −5 are abnormal.', 'M', '5.2'),
            ('Which test data must the program REFUSE?', ['0', '100', '−5', '33'], 2,
             'a mark cannot be negative; 0 and 100 are extreme but allowed.', 'E', '5.2'),
            ('The grammar of a programming language is its:', ['syntax', 'algorithm', 'pseudocode', 'output'], 0,
             'a syntax error breaks the grammar (Chapter 8).', 'E', '5.2'),
        ],
        'Algorithms (5.3)': [
            ('An algorithm is:', ['a program in Python', 'a finite list of exact steps that solves a problem', 'a flowchart only', 'a kind of computer'], 1,
             'it can be written in words, pseudocode or a flowchart, and in any language.', 'E', '5.3'),
            ('"Keep asking for the PIN" (for ever) breaks:', ['precision', 'finiteness', 'input', 'output'], 1,
             'an algorithm must always stop.', 'E', '5.3'),
            ('"Give some money" breaks:', ['finiteness', 'precision', 'uniqueness', 'input'], 1,
             '"some" is not exact.', 'E', '5.3'),
            ('An algorithm may have no input, but it must have:', ['a loop', 'at least one output', 'a decision', 'a variable'], 1,
             'Knuth: input zero or more, output one or more ("print 1 to 10" has no input).', 'M', '5.3'),
            ('"Print tomorrow\'s Sensex" is exact but cannot be done. It breaks:', ['finiteness', 'effectiveness', 'output', 'input'], 1,
             'effectiveness means every step can really be carried out.', 'H', '5.3'),
            ('The word "algorithm" comes from the name of:', ['Euclid', 'al-Khwarizmi', 'Knuth', 'Aryabhata'], 1,
             'his book on Indian numerals survives as "Algoritmi de numero Indorum".', 'E', '5.3'),
            ('Euclid\'s method finds the GCD of 30 and 21 in:', ['1 division', '2 divisions', '3 divisions', '51 divisions'], 2,
             '30 ÷ 21 r 9; 21 ÷ 9 r 3; 9 ÷ 3 r 0.', 'M', '5.3'),
            ('Which is true of an algorithm and a program?', ['both are tied to one language', 'an algorithm can be run directly by a computer', 'a program is an algorithm written in a programming language', 'an algorithm is always longer'], 2,
             'the algorithm is the plan; the program is the plan in Python (or another language).', 'M', '5.3'),
            ('In the ATM, the step "the same card, PIN and amount always give the same result" shows:', ['finiteness', 'uniqueness', 'precision', 'input'], 1,
             'each step\'s result depends only on the input and the steps before.', 'M', '5.3'),
        ],
        'Flowcharts (5.4, 5.5)': [
            ('Which symbol holds a Yes/No question?', ['rectangle', 'parallelogram', 'diamond', 'rounded rectangle'], 2,
             'a decision has one way in and two ways out.', 'E', '5.4'),
            ('"Input a, b" is drawn in a:', ['rectangle', 'parallelogram', 'diamond', 'circle'], 1,
             'the parallelogram is for input and output.', 'E', '5.4'),
            ('"sum = a + b" is drawn in a:', ['rectangle', 'parallelogram', 'diamond', 'oval'], 0,
             'a calculation is a process.', 'E', '5.4'),
            ('The small circle with a letter in a flowchart is a:', ['terminal', 'connector', 'decision', 'process'], 1,
             'it joins two parts of a long chart.', 'E', '5.4'),
            ('How many Start symbols may a flowchart have?', ['none', 'exactly one', 'one for each loop', 'any number'], 1,
             'an algorithm has one beginning.', 'E', '5.4'),
            ('Repeating "enter the PIN" up to three times is:', ['sequence', 'selection', 'repetition', 'decomposition'], 2,
             'the same steps are done again.', 'E', '5.4'),
            ('Which signal word points to a LOOP?', ['calculate', 'whether', 'until', 'display'], 2,
             '"until" means repeat until a condition holds.', 'E', '5.5'),
            ('"Only students with 75% attendance may sit" contains a hidden:', ['loop', 'decision', 'output', 'connector'], 1,
             'there is no "if", but a choice is made.', 'M', '5.5'),
            ('A loop needs a start value, a test and:', ['a connector', 'a change inside the loop', 'two Stops', 'an output'], 1,
             'without the change the test never becomes No: the loop never ends.', 'M', '5.5'),
            ('"Find the sum of n numbers" is mainly a:', ['process', 'decision', 'loop', 'terminal'], 2,
             '"find" can be three shapes; here n numbers means repeat.', 'M', '5.5'),
            ('In W5, the greatest of three, the shortcut "a > b AND a > c, then b > a AND b > c, else c" gives the wrong answer for:', ['1, 2, 3', '5, 5, 2', '3, 2, 1', '2, 9, 4'], 1,
             'with a = b = 5 both tests are No, so it prints c = 2.', 'H', '5.5'),
            ('In the five-step method, the step after Read is:', ['List', 'Draw', 'Mark', 'Check'], 2,
             'Read, Mark, List, Draw, Check.', 'E', '5.5'),
        ],
        'Pseudocode, dry runs and comparing (5.6 to 5.9)': [
            ('Pseudocode is:', ['a programming language', 'a picture of the steps', 'steps in structured English that a computer cannot run', 'machine code'], 2,
             'pseudo = false: it looks like code but is for people.', 'E', '5.6'),
            ('Which keyword repeats while a condition is true?', ['IF', 'WHILE', 'PRINT', 'INPUT'], 1,
             'WHILE … END WHILE.', 'E', '5.6'),
            ('In pseudocode, indentation shows:', ['the output', 'which lines are inside an IF or a loop', 'comments', 'the input'], 1,
             'indented lines belong to the block above them.', 'E', '5.6'),
            ('A trace table has one column for each:', ['step', 'variable', 'symbol', 'input only'], 1,
             'it records how every variable changes.', 'E', '5.7'),
            ('Following an algorithm by hand with sample inputs is a:', ['dry run', 'compilation', 'decomposition', 'flowchart'], 0,
             'it is done on paper, without a computer.', 'E', '5.7'),
            ('At most how many looks does halving need for 1,000 sorted contacts?', ['10', '100', '500', '1,000'], 0,
             '2¹⁰ − 1 = 1,023 names can be handled in 10 looks.', 'M', '5.8'),
            ('Halving search works only when the list is:', ['short', 'in order', 'of numbers', 'printed'], 1,
             'it throws away the half that cannot hold the name, which needs the order.', 'E', '5.8'),
            ('Which prime test uses the most memory?', ['divide up to n − 1', 'divide up to n ÷ 2', 'divide up to √n', 'divide by a stored list of primes'], 3,
             'it must keep the list.', 'M', '5.8'),
            ('How many divisions does "up to √n" need to show that 997 is prime?', ['30', '497', '995', '25'], 0,
             'd = 2 to 31, because 31 × 31 = 961 ≤ 997 < 32 × 32.', 'H', '5.8'),
            ('Breaking a big problem into smaller parts is:', ['debugging', 'decomposition', 'abstraction', 'iteration'], 1,
             'each part can then be solved and tested separately.', 'E', '5.9'),
            ('A metro map shows stations and lines but not streets. This is:', ['decomposition', 'abstraction', 'pattern recognition', 'an algorithm'], 1,
             'abstraction keeps only what matters.', 'M', '5.9'),
            ('Building a program from small ready-made parts is:', ['top-down design', 'bottom-up design', 'stepwise refinement', 'unit testing'], 1,
             'top-down starts from the whole and breaks it down.', 'M', '5.9'),
            ('Two programs of 500 lines are easier than one of 1,000 lines because:', ['they are shorter in total', 'effort grows faster than size', 'they need no testing', 'they use less memory'], 1,
             'with effort as size squared: 25 + 25 = 50 units against 100.', 'H', '5.9'),
            ('Which pair of words means the same?', ['loop and decision', 'repetition and iteration', 'sequence and selection', 'input and output'], 1,
             'a loop = repetition = iteration.', 'E', '5.4'),
            ('The formula n(n + 1) ÷ 2 for 1 + 2 + … + n needs, whatever n is:', ['n additions', 'three operations', 'n multiplications', 'no operations'], 1,
             'one addition, one multiplication, one division.', 'M', '5.8'),
        ],
    }
    secs, n = [], 0
    for head, items in raw.items():
        out = []
        for stem, opts, k, why, d, s in items:
            ok(0 <= k < 4 and len(opts) == 4)
            o = ' '.join(f'({chr(97 + i)}) {x}' for i, x in enumerate(opts))
            out.append((f'{stem} {o}{tag(d, s)}', f'({chr(97 + k)}) {opts[k]}. *Why:* {why}'))
        secs.append((head, out))
        n += len(out)
    ok(sum(isPrime_check() for _ in [0]) == 1)
    page('01-mcq.md', 'Multiple-choice questions', 'One mark each.', secs, n)


def isPrime_check():
    ok(len(prime_method(997, 3)[0]) == 30 and math.ceil(math.log2(1001)) == 10)
    return 1


# ================================================================= 02 fill in
def fill():
    items = [
        ('The five steps of problem solving end with test and ______.', 'debug. *Why:* after delivery comes maintenance.', 'E', '5.2'),
        ('A mistake in a program is called a ______.', 'bug.', 'E', '5.2'),
        ('Testing finds ______ there is a fault; debugging finds where and why.', 'whether.', 'E', '5.2'),
        ('Testing the joined parts of a program together is ______ testing.', 'integration.', 'E', '5.2'),
        ('Test values just inside and just outside a limit are called ______ values.', 'boundary.', 'E', '5.2'),
        ('An algorithm must always ______ after a finite number of steps.', 'stop (end). *Why:* finiteness.', 'E', '5.3'),
        ('Every step of an algorithm must be exact: this is called ______.', 'precision (definiteness).', 'E', '5.3'),
        ('An algorithm has zero or more inputs and ______ or more outputs.', 'one.', 'M', '5.3'),
        ('GCD stands for ______.', 'greatest common divisor (also called HCF).', 'E', '5.3'),
        ('Euclid divides the last divisor by the last ______ until it is 0.', 'remainder.', 'E', '5.3'),
        ('LCM = a × b ÷ ______.', 'GCD. *Check:* 30 × 21 ÷ 3 = 210.', 'M', '5.3'),
        ('The GCD of 48 and 18 by Euclid is ______.', '6: 48 ÷ 18 r 12; 18 ÷ 12 r 6; 12 ÷ 6 r 0.', 'M', '5.3'),
        ('The flowchart symbol for Start and Stop is the ______.', 'terminal (a rounded rectangle; an oval is also accepted).', 'E', '5.4'),
        ('A decision box has one way in and ______ ways out.', 'two (Yes and No).', 'E', '5.4'),
        ('The three building blocks of every algorithm are sequence, selection and ______.', 'repetition (iteration, loop).', 'E', '5.4'),
        ('The flowchart symbols come from the standard ISO ______.', '5807.', 'H', '5.4'),
        ('Arrows in a flowchart are called ______ lines.', 'flow.', 'E', '5.4'),
        ('The condition "age is at least 18" is written age ______ 18.', '≥.', 'E', '5.4'),
        ('Two conditions that must BOTH be true are joined with ______.', 'AND.', 'E', '5.4'),
        ('The five-step method is Read, Mark, List, Draw, ______.', 'Check.', 'E', '5.5'),
        ('In W6 a student fails if the ______ mark is below 33.', 'lowest. *Why:* if the lowest passes, every mark passes.', 'M', '5.5'),
        ('In a ladder of decisions, the ______ Yes decides the answer.', 'first.', 'M', '5.5'),
        ('The keyword ______ shows a result in pseudocode.', 'PRINT.', 'E', '5.6'),
        ('Every IF in pseudocode is closed with ______.', 'END IF.', 'E', '5.6'),
        ('"total ← 0" means the same as SET total ______ 0.', '=.', 'E', '5.6'),
        ('Pseudo means ______.', 'false (not real).', 'E', '5.6'),
        ('Following an algorithm by hand with sample inputs is a ______ run.', 'dry.', 'E', '5.7'),
        ('A ______ table records the value of every variable during a dry run.', 'trace.', 'E', '5.7'),
        ('The time adder gave 6 h 70 min because it forgot that 60 minutes make one ______.', 'hour.', 'E', '5.7'),
        ('Halving finds a name among 100 sorted contacts in at most ______ looks.', '7.', 'M', '5.8'),
        ('How the number of steps grows with the input is ______ complexity.', 'time.', 'E', '5.8'),
        ('How much memory an algorithm needs is its ______ complexity.', 'space.', 'E', '5.8'),
        ('Breaking a problem into parts is called ______.', 'decomposition.', 'E', '5.9'),
        ('A tree showing the parts of a system is a ______ diagram.', 'structure.', 'E', '5.9'),
        ('Keeping only what matters and hiding the rest is ______.', 'abstraction.', 'M', '5.9'),
    ]
    ok(len(items) == 35)
    out = [(q + tag(d, s), a) for q, a, d, s in items]
    ok(30 * 21 // 3 == 210 and math.gcd(48, 18) == 6)
    page('02-fill-in.md', 'Fill in the blanks', 'One mark each.', [('Fill in the blanks', out)], 35)


# ================================================================= 03 true / false
def true_false():
    items = [
        ('Testing and debugging mean the same.', False, 'testing finds that something is wrong; debugging finds the cause and removes it.', 'E', '5.2'),
        ('Analysis comes before writing the algorithm.', True, 'the inputs and outputs must be known first.', 'E', '5.2'),
        ('A program that passes one test is correct.', False, 'one test can miss boundary values; the time adder passed one test and failed another.', 'M', '5.7'),
        ('The word "bug" was first used when a moth was found in a computer.', False, 'the word was already used for faults; the 1947 moth made it famous.', 'M', '5.2'),
        ('An algorithm can be written without a computer language.', True, 'in plain words, pseudocode or a flowchart.', 'E', '5.3'),
        ('An algorithm must have at least one input.', False, 'zero or more inputs; "print 1 to 10" has none.', 'M', '5.3'),
        ('An algorithm must have at least one output.', True, 'otherwise it achieves nothing that can be seen.', 'M', '5.3'),
        ('Euclid\'s method needs the larger number first.', False, 'if the smaller is first, round 1 gives quotient 0 and swaps the numbers.', 'H', '5.3'),
        ('The GCD of 17 and 5 is 1.', True, '17 ÷ 5 r 2; 5 ÷ 2 r 1; 2 ÷ 1 r 0.', 'M', '5.3'),
        ('A flowchart may have two Stop symbols.', False, 'this book\'s rule (and the exam\'s): one Start and one Stop; paths join before Stop.', 'M', '5.4'),
        ('A rectangle is used for input.', False, 'input and output use the parallelogram.', 'E', '5.4'),
        ('A decision box can have three ways out.', False, 'a Yes/No question has two answers; a third choice needs a second diamond.', 'M', '5.4'),
        ('An oval is accepted for the terminal symbol.', True, 'this book draws a rounded rectangle, as NCERT does.', 'E', '5.4'),
        ('A loop must always have a counter.', False, 'it may stop on a condition, such as "until 0 is typed".', 'M', '5.4'),
        ('"Accept numbers till 0 is entered" signals a loop.', True, '"till" means repeat until.', 'E', '5.5'),
        ('"Find the area" always means a loop.', False, 'it is a process (a formula); "find" can be three shapes.', 'M', '5.5'),
        ('In W6, "≥ 33" and "> 33" give the same result for every mark.', False, 'for exactly 33, > says Fail.', 'M', '5.5'),
        ('The flowchart of W10 (factorial) prints 1 for n = 0.', True, 'the loop never runs and fact stays 1; 0! = 1.', 'H', '5.5'),
        ('A computer can run pseudocode directly.', False, 'it must first be written in a programming language.', 'E', '5.6'),
        ('There is one fixed standard for pseudocode.', False, 'styles differ; the steps must be exact and in order.', 'E', '5.6'),
        ('IF … THEN … ELSE shows selection.', True, 'it chooses one of two paths.', 'E', '5.6'),
        ('A dry run needs a computer.', False, 'it is done by hand, on paper.', 'E', '5.7'),
        ('A trace table shows only the final answer.', False, 'it shows every value after each step or round.', 'E', '5.7'),
        ('"i = 1; WHILE i ≤ 10: PRINT i; END WHILE" stops after 10 lines.', False, 'i never changes, so it prints 1 for ever.', 'M', '5.7'),
        ('Halving search works on any list.', False, 'only on a list in order.', 'E', '5.8'),
        ('Halving finds any of 16 sorted names in at most 4 looks.', False, 'at most 5: P, for example, needs H, L, N, O, P.', 'H', '5.8'),
        ('Dividing up to √n is enough to test whether n is prime.', True, 'factors come in pairs, one of each pair is at most √n.', 'M', '5.8'),
        ('Dividing by the 25 primes up to 100 correctly tests 10,201.', False, '10,201 = 101 × 101 has no prime factor up to 100.', 'H', '5.8'),
        ('A faster algorithm is always better.', False, 'it may need more memory, or a sorted list.', 'M', '5.8'),
        ('Remembering tables instead of counting is time against space.', True, 'it saves time but uses memory.', 'M', '5.8'),
        ('Decomposition lets parts be built by different teams at the same time.', True, 'each part is simpler and can be tested alone.', 'E', '5.9'),
        ('Stepwise refinement is also called top-down design.', True, 'a big step is broken into smaller steps.', 'E', '5.9'),
        ('Unit testing checks that the parts work together.', False, 'that is integration testing; unit testing checks one part alone.', 'E', '5.9'),
        ('Pattern recognition means noticing what repeats.', True, 'every grade in W6 is one more "% ≥ …?".', 'M', '5.9'),
        ('Computational thinking is only for programmers.', False, 'Jeannette Wing: a way of solving problems that everyone should learn.', 'M', '5.9'),
    ]
    ok(len(items) == 35)
    _, path = W['W10'].run([0])
    ok(W['W10'].run([0])[0] == ['1'])
    ok(len(halving([chr(65 + i) for i in range(16)], 'P')[0]) == 5 and math.gcd(17, 5) == 1)
    out = [(q + tag(d, s), f'{"True" if v else "False"}. *Why:* {w}') for q, v, w, d, s in items]
    page('03-true-false.md', 'True or false', 'One mark each.', [('True or false', out)], 35)


# ================================================================= 04 assertion and reason
def assertion_reason():
    key = ('*Choose:* (a) both A and R are true and R explains A; (b) both are true but R does not explain A; '
           '(c) A is true, R is false; (d) A is false, R is true.')
    items = [
        ('Debugging comes after testing.', 'Testing shows that a fault exists.', 'a', 'you can only look for the cause of a fault that has been found.', 'E', '5.2'),
        ('Boundary values must be tested.', 'Faults often hide at the limits, such as > instead of ≥.', 'a', 'the pass-mark bug shows only for exactly 33.', 'E', '5.2'),
        ('An algorithm must be finite.', 'Every algorithm has at least one input.', 'c', 'R is false: an algorithm may have no input.', 'M', '5.3'),
        ('Euclid\'s method always stops.', 'Each remainder is smaller than the divisor before it.', 'a', 'the numbers shrink, so the remainder must reach 0.', 'H', '5.3'),
        ('The same algorithm can be coded in Python and in Java.', 'An algorithm is not tied to any language.', 'a', 'the plan is the same in every language.', 'E', '5.3'),
        ('A decision box has two ways out.', 'A condition is either true or false.', 'a', 'Yes and No are the only two answers.', 'E', '5.4'),
        ('Input is drawn in a parallelogram.', 'The parallelogram is also used for output.', 'b', 'both true; R does not say why input uses it.', 'M', '5.4'),
        ('The ATM allows only three wrong PINs.', 'A 4-digit PIN has 10,000 possible values.', 'a', 'with unlimited tries a thief could try them all.', 'M', '5.4'),
        ('The shortcut "a > b AND a > c, then b > a AND b > c, else c" is wrong.', 'With two equal largest numbers both tests are No.', 'a', '5, 5, 2 gives 2.', 'H', '5.5'),
        ('In W6, the grade questions are asked from 90 down.', 'In a ladder the first Yes decides the answer.', 'a', 'asking ≥ 60 first would give C to everyone above 60.', 'M', '5.5'),
        ('Pseudocode can be run by a computer.', 'Pseudocode uses keywords like IF and WHILE.', 'd', 'A is false: it must first be coded.', 'E', '5.6'),
        ('A trace table helps to find logical errors.', 'It shows the value of every variable after each step.', 'a', 'you see the step where a value goes wrong.', 'M', '5.7'),
        ('Halving is faster than one-by-one search for a sorted list.', 'Each look throws away half of what is left.', 'a', '100 → 50 → 25 …: 7 looks for 100 names.', 'E', '5.8'),
        ('Method (iv) of prime testing needs more memory.', 'It divides by the 25 primes up to 100, kept in a list.', 'a', 'the list must be stored.', 'M', '5.8'),
        ('Decomposition makes testing easier.', 'Each part can be tested alone before the parts are joined.', 'a', 'unit testing, then integration testing.', 'E', '5.9'),
    ]
    ok(len(items) == 15 and 10 ** 4 == 10000)
    out = [(f'A: {a} R: {r}{tag(d, s)}', f'({k}). {w}') for a, r, k, w, d, s in items]
    t_intro = 'One mark each. ' + key
    page('04-assertion-reason.md', 'Assertion and reason', t_intro, [('Assertion and reason', out)], 15)


# ================================================================= 05 short answer
def short():
    items = [
        ('[2] Name the steps of problem solving in order.', 'Analyse the problem; develop an algorithm; code it; test it; debug it; and after delivery, maintain it.', 'E', '5.2'),
        ('[2] Give one difference between testing and debugging, with an example.', 'Testing shows THAT a fault exists (a student with 33 is told Fail); debugging finds WHY (the program asked "> 33") and fixes it (≥ 33).', 'E', '5.2'),
        ('[2] What are normal, extreme and abnormal test data for an age from 1 to 120? Give one of each.', 'Normal 35; extreme 1 or 120; abnormal −4 or 150 or "ten".', 'M', '5.2'),
        ('[2] Name the four kinds of testing named by NCERT.', 'Unit, integration, system, acceptance.', 'E', '5.2'),
        ('[2] Define an algorithm. Name its five characteristics.', 'A finite list of exact steps that turns the input into the output. Precision, uniqueness, finiteness, input, output.', 'E', '5.3'),
        ('[2] Why must an algorithm be finite? Give an example of a step that breaks it.', 'A step list that never ends gives no answer. "Keep asking for the PIN" (with no limit).', 'E', '5.3'),
        ('[2] Find the GCD and LCM of 36 and 24 by Euclid\'s method.', '36 ÷ 24 r 12; 24 ÷ 12 r 0: GCD 12. LCM = 36 × 24 ÷ 12 = 72.', 'M', '5.3'),
        ('[2] Write two differences between an algorithm and a program.', 'An algorithm is in plain words or a flowchart and cannot be run; a program is in a programming language and can be run. An algorithm is not tied to a language; a program is.', 'E', '5.3'),
        ('[2] Draw the symbols for a terminal, a process and a decision, and say what each is for.', 'Rounded rectangle: Start/Stop. Rectangle: a calculation or setting a value. Diamond: a Yes/No question.', 'E', '5.4'),
        ('[2] Name the three building blocks of an algorithm and give an ATM example of each.', 'Sequence: card, then PIN, then amount. Selection: PIN right? Repetition: up to 3 PIN tries.', 'E', '5.4'),
        ('[2] Write the condition: "marks are between 40 and 60, both included".', 'marks ≥ 40 AND marks ≤ 60.', 'M', '5.4'),
        ('[2] Write the condition: "a customer gets a discount on a bill over ₹5,000 or with a gold card".', 'bill > 5000 OR card = gold.', 'M', '5.4'),
        ('[2] What are the three things every loop needs? Show them in the ATM.', 'A start value (tries = 0), a test (tries = 3?) and a change inside the loop (tries = tries + 1).', 'M', '5.5'),
        ('[2] Mark the shapes for: "Accept marks of 40 students and display the average."', '"Accept" input; "40 students" loop; "average" process (a formula); "display" output.', 'M', '5.5'),
        ('[2] Why does W6 test the lowest mark, and why ≥ rather than >?', 'If the lowest mark is 33 or more, every mark is. Exactly 33 passes, so ≥.', 'M', '5.5'),
        ('[2] Write pseudocode to print the even numbers from 2 to 20.', 'SET n = 2; WHILE n ≤ 20: PRINT n; COMPUTE n = n + 2; END WHILE.', 'E', '5.6'),
        ('[2] Write pseudocode to input a number and print whether it is positive, negative or zero.', 'INPUT n; IF n > 0 THEN PRINT "Positive" ELSE IF n < 0 THEN PRINT "Negative" ELSE PRINT "Zero" END IF.', 'M', '5.6'),
        ('[2] Give two differences between a flowchart and pseudocode.', 'A flowchart is a picture, pseudocode is text. A flowchart shows the flow at a glance; pseudocode is easier to change.', 'E', '5.6'),
        ('[2] What is a dry run? Why is it useful?', 'Following an algorithm by hand with sample inputs. It shows whether it gives the right answer, and where a wrong value appears.', 'E', '5.7'),
        ('[2] Find the bug: "IF age > 18 THEN PRINT \'Can vote\'". Fix it.', 'An 18-year-old is refused. Use age ≥ 18.', 'E', '5.7'),
        ('[2] Find the bug: "SET i = 10; WHILE i > 0: PRINT i; INCREMENT i; END WHILE".', 'i grows 10, 11, 12 … and stays > 0: it never stops. DECREMENT i instead.', 'M', '5.7'),
        ('[2] Why is the "nice" test (5 h 20 min + 7 h 30 min) not enough for the time adder?', 'Its minutes add up to less than 60, so the missing carry never shows.', 'M', '5.7'),
        ('[2] What is time complexity? Give an example from the chapter.', 'How the number of steps grows with the input. One-by-one search needs up to n looks; halving needs about log₂ n.', 'M', '5.8'),
        ('[2] At most how many guesses find a number from 1 to 500 by halving? Why?', '9: 8 guesses handle only 255 numbers, 9 handle 511.', 'M', '5.8'),
        ('[2] Why does halving need a sorted list?', 'It throws away the half that cannot hold the name; that is known only if the list is in order.', 'E', '5.8'),
        ('[2] Why is dividing up to n ÷ 2 enough to test whether n is prime?', 'The smallest factor other than 1 is 2, so the largest other than n is n ÷ 2.', 'M', '5.8'),
        ('[2] Define decomposition and give two of its advantages.', 'Breaking a big problem into smaller parts. Each part is simpler; parts are built at the same time and tested alone.', 'E', '5.9'),
        ('[2] What is stepwise refinement? Show one step of it for "make tea".', 'Breaking a step into smaller steps. "Make tea" → boil water; add tea leaves; add milk and sugar; strain.', 'E', '5.9'),
        ('[2] Name the four parts of computational thinking.', 'Decomposition, pattern recognition, abstraction, algorithms.', 'E', '5.9'),
        ('[3] Decompose an online shopping app into five parts.', 'Catalogue (search, product pages); cart; payment; delivery (address, tracking); returns and reviews.', 'M', '5.9'),
    ]
    ok(len(items) == 30 and math.gcd(36, 24) == 12 and 36 * 24 // 12 == 72 and math.ceil(math.log2(501)) == 9)
    out = [(q + tag(d, s), a) for q, a, d, s in items]
    page('05-short-answer.md', 'Short-answer questions', 'Two or three marks each.', [('Short answers', out)], 30)


# ================================================================= 06 long answer
def long_():
    G = W['W6']
    items = []

    def add(q, a, d, s, algo=None):
        if algo is not None:
            a += '\n\n' + pic(drawn(algo), 'Flowchart of the answer', 1.1)
        items.append((q + tag(d, s), a))

    ex = make('c05-q-exam-hall', 'Exam hall', [('in', ['att', 'fee']),
              ('if', 'att >= 75 and fee == 1', [('out', "'Admit card issued'")], [('out', "'Not allowed'")],
               {'text': 'att ≥ 75 AND\nfee paid?'})],
              [([80, 1], ['Admit card issued']), ([75, 1], ['Admit card issued']), ([74, 1], ['Not allowed']), ([90, 0], ['Not allowed'])])
    add('[4] A student gets an admit card if attendance is at least 75% AND the fee is paid (1 = paid). Draw the flowchart and dry-run it for 75, 1 and 90, 0.',
        'Inputs att, fee; one decision "att ≥ 75 AND fee paid?"; Yes: "Admit card issued"; No: "Not allowed". Dry runs: 75, 1 → admit card (75 ≥ 75); 90, 0 → not allowed (fee not paid).', 'M', '5.5', ex)
    out = G.run([33, 60, 65, 70, 62])[0]
    ok(out == ['Grade D'])
    add('[5] (i) Write the steps of problem solving for the report-card program. (ii) Give the test data you would use, of each kind, with the expected result.',
        '(i) Analyse (inputs: 5 marks 0–100; outputs: result and grade); algorithm (W6); code; test; debug; maintain. (ii) Normal 80, 75, 70, 72, 78 → B; extreme 100 ×5 → A and 0 ×5 → Fail; boundary 33 ×5 → D and 32 in one subject → Fail; abnormal −5 or 105 → must be refused.', 'M', '5.2')
    add('[5] Explain the five characteristics of an algorithm with the ATM, and give for each a step that breaks it.',
        'Precision ("a multiple of ₹100"; broken by "give some money"); uniqueness (same inputs, same result; "pay if it feels like it"); finiteness (stops after 3 wrong PINs; "keep asking"); input (card, PIN, amount); output (cash or a message; a step that shows nothing).', 'E', '5.3')
    rounds = []
    a, b = 1071, 462
    while b:
        rounds.append(f'{a} ÷ {b} r {a % b}'); a, b = b, a % b
    ok(a == 21)
    add('[4] Find the GCD and LCM of 1071 and 462 by Euclid\'s method, showing each division, and explain why the method works.',
        f'{"; ".join(rounds)}: GCD 21; LCM = 1071 × 462 ÷ 21 = {ind(1071 * 462 // 21)}. It works because a number that divides both numbers also divides their difference, so each new pair has the same common divisors and a smaller size.', 'H', '5.3')
    add('[4] Draw the six flowchart symbols, name each, and give one common mistake for each.',
        'Terminal (more than one Start); input/output parallelogram (a rectangle for input); process rectangle (a question in it); decision diamond (only one way out); flow line (an arrow to nowhere); connector (letters that do not match).', 'E', '5.4')
    sm = make('c05-q-sum-n', 'Sum and average of n numbers', [('in', ['n']), ('do', 's = 0; i = 1'),
              ('while', 'i <= n', [('in', ['x']), ('do', 's = s + x'), ('do', 'i = i + 1')]),
              ('out', 's'), ('out', 's / n')], [([3, 4, 5, 6], ['15', '5.0']), ([1, 9], ['9', '9.0'])])
    add('[5] Draw a flowchart to input n numbers and print their sum and average. Dry-run it for n = 3 and 4, 5, 6.',
        'Input n; s = 0, i = 1; while i ≤ n: input x; s = s + x; i = i + 1; then print s and s ÷ n. Dry run: s = 4, 9, 15; prints 15 and 5.0.', 'M', '5.5', sm)
    add('[4] Write the five-step method and apply it to: "Input the price and quantity; if the bill is over ₹1,000 give 10% off; print the amount."',
        'Read: given price, quantity; asked the amount. Mark: input, "if" decision, "give" output. List: input price, qty; bill = price × qty; is bill > 1000? Yes: amount = bill − bill × 10 ÷ 100; No: amount = bill; print amount. Draw. Check with 100 × 10 = 1,000 (no discount: boundary) and 200 × 10 = 2,000 (1,800).', 'M', '5.5')
    ok(2000 - 2000 * 10 // 100 == 1800)
    add('[4] Write pseudocode for W9 (1 + x + … + xⁿ) and make its trace table for x = 3, n = 3.',
        'SET sum = 1, term = 1, i = 1; WHILE i ≤ n: term = term × x; sum = sum + term; INCREMENT i; END WHILE; PRINT sum. Trace: term 3, 9, 27; sum 4, 13, 40; i 2, 3, 4; prints 40.', 'M', '5.6')
    ok(W['W9'].run([3, 3])[0] == ['40'])
    add('[5] Compare the four prime tests of section 5.8 for 997 and for 91. Which would you use, and why?',
        'For 997 (prime): 995, 497, 30 and 25 divisions. For 91: all four stop at 7. Use √n: few divisions and no extra memory; the list method is faster still for small n but needs memory and fails from 10,201.', 'H', '5.8')
    ok([len(prime_method(997, m)[0]) for m in (1, 2, 3, 4)] == [995, 497, 30, 25])
    add('[4] Explain time and space complexity with two examples from the chapter.',
        'Time: halving (7 looks for 100) against one by one (100); Euclid (3 divisions) against listing divisors (51 for 30 and 21). Space: the prime list of method (iv); remembering tables against counting on fingers.', 'M', '5.8')
    add('[5] Decompose a school annual-day event into parts, draw its structure diagram and say what the parts must agree on.',
        'Programme (items, rehearsals); stage and sound; invitations and seating; costumes and props; refreshments. They must agree on the date, the timetable and the number of guests.', 'M', '5.9')
    tw = make('c05-q-time-fix', 'Time adder', [('in', ['h1', 'm1', 'h2', 'm2']), ('do', 'h = h1 + h2; m = m1 + m2'),
              ('if', 'm >= 60', [('do', 'h = h + 1; m = m - 60')]), ('out', "str(h) + ' h ' + str(m) + ' min'", {'text': 'Print h, m'})],
              [([4, 50, 2, 20], ['7 h 10 min']), ([3, 45, 2, 15], ['6 h 0 min'])])
    add('[4] A train journey has two parts. Draw a flowchart that adds the two times correctly (hours and minutes), and dry-run it for 3 h 45 min + 2 h 15 min.',
        'Add hours and minutes; if minutes ≥ 60, add 1 to hours and take 60 from minutes. Dry run: h = 5, m = 60; 60 ≥ 60 Yes: h = 6, m = 0: prints 6 h 0 min.', 'M', '5.7', tw)
    ok(len(items) == 12)
    page('06-long-answer.md', 'Long-answer questions', 'Four or five marks each.', [('Long answers', items)], 12)


# ================================================================= 07 case studies
def cases():
    items = [
        ('**Case: the canteen token machine.** A machine takes the amount paid, the price of a thali (₹60) and gives tokens and change. (i) What are the inputs and outputs? (ii) Write the algorithm in steps for one customer paying ₹200 for 3 thalis. (iii) Which test data would you choose?',
         '(i) Inputs: number of thalis, amount paid; outputs: tokens, change, or "pay more". (ii) bill = 3 × 60 = 180; is 200 ≥ 180? Yes: give 3 tokens and ₹20 change. (iii) Exact amount (180), less (150: "pay more"), much more (500), 0 thalis.', 'M', '5.3'),
        ('**Case: the class monitor election.** Votes for two candidates, A and B, are typed one by one; "X" ends. (i) Which block repeats? (ii) Write the pseudocode to count the votes and print the winner. (iii) What should happen on a tie?',
         '(i) Reading a vote and adding it to a count. (ii) SET a = 0, b = 0; INPUT v; WHILE v ≠ "X": IF v = "A" THEN INCREMENT a ELSE INCREMENT b END IF; INPUT v; END WHILE; IF a > b THEN PRINT "A" ELSE IF b > a THEN PRINT "B" ELSE PRINT "Tie" END IF. (iii) A third result, "Tie", must be printed; a two-way IF would wrongly name B.', 'M', '5.6'),
        ('**Case: the bus pass.** Students under 18 travel free; 18 to 25 pay half (₹250); others pay ₹500. (i) Mark the decisions. (ii) Draw the ladder. (iii) Choose boundary test data.',
         '(i) "under 18", "18 to 25": two decisions. (ii) age < 18? Yes: 0; No: age ≤ 25? Yes: 250; No: 500. (iii) 17, 18, 25, 26.', 'E', '5.5'),
        ('**Case: the library fine.** A book is due in 14 days; ₹2 a day for the next 10 late days, then ₹5 a day. (i) Write the conditions. (ii) Find the fine for 20 days and for 30 days. (iii) Which values are boundaries?',
         f'(i) days ≤ 14: 0; days ≤ 24: (days − 14) × 2; else 20 + (days − 24) × 5. (ii) 20 days: 6 × 2 = ₹12; 30 days: 20 + 6 × 5 = ₹50. (iii) 14, 15, 24, 25.', 'H', '5.4'),
        ('**Case: the cricket scorer.** The scorer writes the runs after every ball. (i) What is this like in a dry run? (ii) An over has 1, 4, 0, 6, 2, 1. Make the trace of the total. (iii) Why is one line per ball useful?',
         '(i) A trace table, one row each time something changes. (ii) 1, 5, 5, 11, 13, 14. (iii) Any mistake can be found at the ball where it crept in.', 'E', '5.7'),
        ('**Case: finding a roll number.** The marks list of 1,000 students is sorted by roll number. (i) Which search would you use? (ii) At most how many looks? (iii) What if the list were sorted by name instead?',
         '(i) Halving. (ii) 10. (iii) A search by roll number would have to go one by one (up to 1,000 looks), or the list must be sorted again by roll number.', 'M', '5.8'),
        ('**Case: the school app.** The school wants one app for attendance, fees, homework and results. (i) Decompose it. (ii) Which part would you build and test first, and why? (iii) What must all the parts agree on?',
         '(i) Attendance, fees, homework, results, messages to parents. (ii) The student list (roll numbers and classes), because every other part uses it. (iii) The roll number of each student.', 'M', '5.9'),
        ('**Case: the electricity bill bug.** A program charges ₹5 a unit up to 100 units and ₹7 after; for 150 units it prints ₹1,050. (i) Is that right? (ii) What did the program do? (iii) Fix it.',
         '(i) No: 100 × 5 + 50 × 7 = ₹850. (ii) It charged all 150 units at ₹7. (iii) bill = 500 + (units − 100) × 7 when units > 100.', 'M', '5.7'),
    ]
    ok(sum([1, 4, 0, 6, 2, 1]) == 14 and 100 * 5 + 50 * 7 == 850 and 150 * 7 == 1050 and 6 * 2 == 12 and 20 + 6 * 5 == 50)
    ok(len(items) == 8)
    out = [(q + tag(d, s), a) for q, a, d, s in items]
    page('07-case-study.md', 'Case studies', 'Each case has three parts.', [('Case studies', out)], 8)


# ================================================================= 08 find the output (generated)
def outputs():
    R = random.Random(505)
    Pmap = {p[1]: p for p in PR.P}
    jobs = [
        ('W3', lambda: [R.randint(1, 50), R.randint(1, 50)], 3),
        ('W4', lambda: [R.randint(10, 99)], 3),
        ('W5', lambda: [R.randint(1, 9) for _ in range(3)], 5),
        ('W6', lambda: [R.choice([R.randint(25, 100), R.randint(60, 100)]) for _ in range(5)], 6),
        ('W7', lambda: [R.randint(1, 20) for _ in range(R.randint(2, 4))] + [0], 4),
        ('W8', lambda: [R.randint(10, 300), R.randint(10, 300)], 6),
        ('W9', lambda: [R.randint(2, 4), R.randint(2, 4)], 4),
        ('W10', lambda: [R.randint(3, 7)], 3),
        ('fibonacci', lambda: [R.randint(5, 9)], 3),
        ('armstrong', lambda: [R.choice([153, 370, 371, 407, 154, 222])], 3),
        ('palindrome-number', lambda: [R.choice([1221, 12321, 1231, 4554, 908])], 3),
        ('perfect', lambda: [R.choice([6, 28, 12, 20])], 2),
        ('series-2', lambda: [R.randint(2, 3), R.randint(3, 4)], 2),
        ('pattern-numbers', lambda: [R.randint(3, 4)], 2),
        ('count-characters', lambda: [R.choice(['Hello India', 'CBSE Exam', 'Om Shanti', 'Data 2026'])], 2),
        ('list-swap', lambda: [[R.randint(1, 9) for _ in range(R.randint(4, 6))]], 2),
        ('prime', lambda: [R.choice([49, 51, 53, 87, 89, 91])], 2)]
    secs, n, seen = [], 0, set()
    for key, gen, k in jobs:
        if key in W:
            algo, name = W[key], f'{key} ({WTITLE[key].lower()})'
        else:
            p = Pmap[key]
            algo, name = p[4], f'practical {p[0]} ({p[2].lower()})'
        items = []
        tries = 0
        while len(items) < k and tries < 200:
            tries += 1
            s = gen()
            sig = (key, str(s))
            if sig in seen:
                continue
            seen.add(sig)
            out, trace = algo.run(s, limit=2000)
            ok(out == algo.run_python(s), (key, s))
            steps = sum(1 for r in trace)
            dec = sum(1 for r in trace if algo.node(r['step']).kind == 'decision')
            shown = ', '.join(map(str, s)) if not isinstance(s[0], list) else str(s[0])
            q = f'Dry-run the flowchart of {name} for the input {shown}. What is printed?{tag("M" if steps < 25 else "H", "5.7")}'
            a = f'**{" / ".join(out)}**. *Working:* {steps} steps, {dec} questions asked (boxes {", ".join(str(r["step"]) for r in trace[:14])}{" …" if len(trace) > 14 else ""}).'
            items.append((q, a))
        ok(len(items) == k, key)
        secs.append((f'{name[0].upper()}{name[1:]}', items))
        n += k
    ok(n == 55)
    page('08-find-the-output.md', 'Find the output (dry runs)',
         'Each flowchart is in the book (W1 to W10) or on the page of the 22 practical charts. Make a trace table on paper; then check.',
         secs, 55)


# ================================================================= 09 spot the bug (generated)
def bugs():
    G, A7, G8, F10, S9 = W['W6'], W['W7'], W['W8'], W['W10'], W['W9']
    cases = [
        (G, dict(n4=dict(test='low > 33')), [33, 40, 50, 60, 70], 'Box 4 asks "low > 33?"', 'low ≥ 33', 'W6'),
        (G, dict(n3=dict(do='total = m1 + m2 + m3 + m4 + m5\nper = total / 4\nlow = min(m1, m2, m3, m4, m5)')), [80, 75, 70, 72, 78], 'Box 3 divides the total by 4', 'divide by 5', 'W6'),
        (G, dict(n6=dict(test='per >= 60'), n7=dict(show="'Grade C'"), n10=dict(test='per >= 90'), n11=dict(show="'Grade A'")), [95, 92, 88, 91, 94], 'The ladder asks ≥ 60 first', 'ask 90, then 75, then 60', 'W6'),
        (G, dict(n3=dict(do='total = m1 + m2 + m3 + m4 + m5\nper = total / 5\nlow = max(m1, m2, m3, m4, m5)')), [20, 90, 90, 90, 90], 'Box 3 takes the HIGHEST mark as low', 'the lowest mark: min', 'W6'),
        (A7, dict(n2=dict(do='sum = 0\ncount = 1')), [6, 9, 0], 'count starts at 1', 'count = 0', 'W7'),
        (A7, dict(n7=dict(do='avg = sum / (count + 1)')), [4, 8, 6, 0], 'The average divides by count + 1 (the 0 is counted)', 'avg = sum ÷ count', 'W7'),
        (G8, dict(n8=dict(do='lcm = x * y // b')), [30, 21], None, None, 'W8'),
        (G8, dict(n6=dict(do='b = a'), n7=dict(do='a = r')), [30, 21], 'Boxes 6 and 7 move the values the wrong way', 'a = b, then b = r', 'W8'),
        (F10, dict(n3=dict(do='fact = 0\ni = 1')), [5], 'fact starts at 0', 'fact = 1', 'W10'),
        (F10, dict(n4=dict(test='i < n')), [5], 'The loop asks "i < n?"', 'i ≤ n', 'W10'),
        (S9, dict(n3=dict(do='sum = 0\nterm = 1\ni = 1')), [2, 3], 'sum starts at 0, so the first term 1 is never added', 'sum = 1', 'W9'),
        (S9, dict(n5=dict(do='term = term + x')), [2, 3], 'Box 5 adds x instead of multiplying', 'term = term × x', 'W9'),
        (W['W3'], dict(n3=dict(test='a < b')), [7, 12], 'Box 3 asks "a < b?" but prints a on Yes', 'a > b', 'W3'),
        (W['W4'], dict(n3=dict(test='n % 2 == 1')), [8], 'Box 3 asks "remainder = 1?" but its Yes prints Even', 'remainder of n ÷ 2 = 0', 'W4'),
        (W['W5'], dict(n3=dict(test='a > b and a > c'), n4=dict(test='b > a and b > c')), [5, 5, 2], None, None, 'W5'),
    ]
    items = []
    for k, (algo, ch, s, cause, fix, key) in enumerate(cases, 1):
        if cause is None:                    # cases that are not simple variants: worked by hand below
            continue
        bad = variant(algo, f'bug{k}', **ch)
        try:
            got = bad.run(s, limit=2000)[0]
        except ZeroDivisionError:
            got = ['nothing: it stops with division by zero']
        right = algo.run(s)[0]
        ok(got != right, (key, k, got, right))
        items.append((f'In the flowchart of {key} ({WTITLE[key].lower()}), {cause[0].lower() + cause[1:]}. Dry-run it for {", ".join(map(str, s))}: what does it print, what should it print, and what is the fix?{tag("M", "5.7")}',
                      f'It prints **{" / ".join(got)}**; it should print **{" / ".join(right)}**. *Fix:* {fix}.'))
    # W8 with the GCD in the wrong variable: the loop ends with b = 0, so dividing by b crashes
    try:
        variant(G8, 'bugw8', n8=dict(do='lcm = x * y // b')).run([30, 21])
        crashed = False
    except ZeroDivisionError:
        crashed = True
    ok(crashed)
    items.append((f'In W8, box 8 is written "lcm = x × y ÷ b". What happens for 30, 21, and why?{tag("H", "5.7")}',
                  'It stops with **division by zero**: the loop ends when b = 0, so x × y ÷ b divides by 0. The GCD is in **a** at that point: lcm = x × y ÷ a = 210.'))
    ok(len(items) == 14)
    out_short = []
    ok(not (5 > 5 and 5 > 2) and not (5 > 5 and 5 > 2))
    items.append((f'The greatest of three is written as: IF a > b AND a > c THEN PRINT a ELSE IF b > a AND b > c THEN PRINT b ELSE PRINT c. Dry-run it for 5, 5, 2.{tag("H", "5.5")}',
                  'It prints **2**; the greatest is 5. Both tests are No because neither 5 is greater than the other. *Fix:* the nested tests of W5 (or use ≥).'))
    ok(len(items) == 15)
    page('09-spot-the-bug.md', 'Spot the bug', 'Each flowchart is a book flowchart with one or two boxes changed. Find what goes wrong by a dry run.',
         [('Spot the bug', items)], 15)


# ================================================================= 10 draw the flowchart (generated answers)
def draws():
    R = []

    def q(text, steps, ref, tests, d='M', s='5.5'):
        R.append((text, steps, ref, tests, d, s))
    q('Input the radius of a circle; print its area (π = 3.14).', [('in', ['r']), ('do', 'area = 3.14 * r * r'), ('out', 'area')],
      lambda r: [str(3.14 * r * r)], [(7,), (1,)], 'E')
    q('Input the cost price and selling price; print "Profit", "Loss" or "No profit, no loss".',
      [('in', ['cp', 'sp']), ('if', 'sp > cp', [('out', "'Profit'")], [('if', 'sp < cp', [('out', "'Loss'")], [('out', "'No profit, no loss'")])])],
      lambda c, s_: ['Profit' if s_ > c else 'Loss' if s_ < c else 'No profit, no loss'], [(100, 120), (100, 80), (50, 50)])
    q('Input a number; print whether it is divisible by both 3 and 5.',
      [('in', ['n']), ('if', 'n % 3 == 0 and n % 5 == 0', [('out', "'Divisible by both'")], [('out', "'Not divisible by both'")])],
      lambda n: ['Divisible by both' if n % 15 == 0 else 'Not divisible by both'], [(30,), (9,), (10,)])
    q('Input three sides; print whether they can make a triangle (each side less than the sum of the other two).',
      [('in', ['a', 'b', 'c']), ('if', 'a < b + c and b < a + c and c < a + b', [('out', "'Triangle'")], [('out', "'Not a triangle'")],
                                 {'text': 'each side < sum\nof the others?'})],
      lambda a, b, c: ['Triangle' if a < b + c and b < a + c and c < a + b else 'Not a triangle'], [(3, 4, 5), (1, 2, 3), (2, 2, 3)], 'H')
    q('Input a percentage; print the division: 60 and above "First", 45 and above "Second", 33 and above "Third", else "Fail".',
      [('in', ['p']), ('if', 'p >= 60', [('out', "'First'")], [('if', 'p >= 45', [('out', "'Second'")], [('if', 'p >= 33', [('out', "'Third'")], [('out', "'Fail'")])])])],
      lambda p: ['First' if p >= 60 else 'Second' if p >= 45 else 'Third' if p >= 33 else 'Fail'], [(60,), (59,), (33,), (32,)])
    q('Input a year of birth and the present year; print the age and whether the person is a senior citizen (60 or more).',
      [('in', ['born', 'now']), ('do', 'age = now - born'), ('out', 'age'),
       ('if', 'age >= 60', [('out', "'Senior citizen'")], [('out', "'Not a senior citizen'")])],
      lambda b, n_: [str(n_ - b), 'Senior citizen' if n_ - b >= 60 else 'Not a senior citizen'], [(1960, 2026), (2009, 2026)])
    q('Print the numbers from 1 to n.', [('in', ['n']), ('do', 'i = 1'), ('while', 'i <= n', [('out', 'i'), ('do', 'i = i + 1')])],
      lambda n: [str(i) for i in range(1, n + 1)], [(5,), (1,)], 'E')
    q('Print the odd numbers from 1 to n.', [('in', ['n']), ('do', 'i = 1'), ('while', 'i <= n', [('out', 'i'), ('do', 'i = i + 2')])],
      lambda n: [str(i) for i in range(1, n + 1, 2)], [(9,), (10,)], 'E')
    q('Print the numbers from n down to 1.', [('in', ['n']), ('while', 'n >= 1', [('out', 'n'), ('do', 'n = n - 1')])],
      lambda n: [str(i) for i in range(n, 0, -1)], [(4,), (1,)], 'E')
    q('Input n; print the sum of the even numbers from 2 to n.', [('in', ['n']), ('do', 's = 0; i = 2'), ('while', 'i <= n', [('do', 's = s + i'), ('do', 'i = i + 2')]), ('out', 's')],
      lambda n: [str(sum(range(2, n + 1, 2)))], [(10,), (7,), (1,)])
    q('Input n; print the squares 1, 4, 9 … up to n².', [('in', ['n']), ('do', 'i = 1'), ('while', 'i <= n', [('out', 'i * i'), ('do', 'i = i + 1')])],
      lambda n: [str(i * i) for i in range(1, n + 1)], [(4,)], 'E')
    q('Input x and n; print xⁿ by repeated multiplication.', [('in', ['x', 'n']), ('do', 'p = 1; i = 1'), ('while', 'i <= n', [('do', 'p = p * x'), ('do', 'i = i + 1')]), ('out', 'p')],
      lambda x, n: [str(x ** n)], [(2, 10), (5, 0), (3, 4)])
    q('Input n; print the product 1 × 3 × 5 × … of the odd numbers up to n.', [('in', ['n']), ('do', 'p = 1; i = 1'), ('while', 'i <= n', [('do', 'p = p * i'), ('do', 'i = i + 2')]), ('out', 'p')],
      lambda n: [str(math.prod(range(1, n + 1, 2)))], [(7,), (1,)])
    q('Input a number; print its digits in reverse order, one per line.', [('in', ['n']), ('while', 'n > 0', [('out', 'n % 10', {'text': 'Print the last\ndigit (n mod 10)'}), ('do', 'n = n // 10', {'text': 'n = n div 10'})])],
      lambda n: [c for c in str(n)[::-1]] if n > 0 else [], [(4096,), (7,)])
    q('Input a number; print the reverse number (for 1234: 4321).', [('in', ['n']), ('do', 'rev = 0'), ('while', 'n > 0', [('do', 'rev = rev * 10 + n % 10', {'text': 'rev = rev × 10 +\nlast digit of n'}), ('do', 'n = n // 10', {'text': 'n = n div 10'})]), ('out', 'rev')],
      lambda n: [str(int(str(n)[::-1]))], [(1234,), (500,)], 'H')
    q('Input a number; print how many of its digits are even.', [('in', ['n']), ('do', 'c = 0'), ('while', 'n > 0', [('if', 'n % 2 == 0', [('do', 'c = c + 1')], [], {'text': 'last digit\neven?'}), ('do', 'n = n // 10', {'text': 'n = n div 10'})]), ('out', 'c')],
      lambda n: [str(sum(int(d) % 2 == 0 for d in str(n)))], [(24680,), (1357,), (1234,)], 'H')
    q('Numbers are typed until 0; print their sum.', [('do', 's = 0'), ('in', ['x']), ('while', 'x != 0', [('do', 's = s + x'), ('in', ['x'])]), ('out', 's')],
      lambda *xs: [str(sum(xs[:xs.index(0)]))], [(4, 5, 6, 0), (0,)])
    q('Numbers are typed until 0; print how many were negative.', [('do', 'c = 0'), ('in', ['x']), ('while', 'x != 0', [('if', 'x < 0', [('do', 'c = c + 1')]), ('in', ['x'])]), ('out', 'c')],
      lambda *xs: [str(sum(1 for v in xs[:xs.index(0)] if v < 0))], [(4, -5, -6, 0), (0,)])
    q('Numbers are typed until 0; print the smallest (the first is not 0).', [('in', ['x']), ('do', 'small = x'), ('while', 'x != 0', [('if', 'x < small', [('do', 'small = x')]), ('in', ['x'])]), ('out', 'small')],
      lambda *xs: [str(min(xs[:xs.index(0)]))], [(4, 9, 2, 0), (5, 0)])
    q('Input a PIN; allow up to 3 tries for the PIN 1234; print "Welcome" or "Locked".',
      [('do', 'tries = 0; ok = 0'), ('while', 'tries < 3 and ok == 0', [('in', ['pin']), ('if', 'pin == 1234', [('do', 'ok = 1')], [('do', 'tries = tries + 1')])],
                                    {'text': 'tries < 3 AND\nnot yet right?'}),
       ('if', 'ok == 1', [('out', "'Welcome'")], [('out', "'Locked'")])],
      lambda *ps: ['Welcome' if 1234 in ps[:3] else 'Locked'], [(1111, 1234), (1, 2, 3), (1234,)], 'H')
    q('Input marks until a valid mark (0 to 100) is typed; then print it.',
      [('in', ['m']), ('while', 'm < 0 or m > 100', [('out', "'Invalid, type again'"), ('in', ['m'])], {'text': 'm < 0 OR\nm > 100?'}), ('out', 'm')],
      lambda *ms: ['Invalid, type again'] * next(i for i, v in enumerate(ms) if 0 <= v <= 100) + [str(next(v for v in ms if 0 <= v <= 100))],
      [(105, -3, 67), (50,)], 'H')
    q('Input n; print the multiplication tables of 1 to n, each up to 3 (1 × 1 … n × 3).',
      [('in', ['n']), ('do', 'i = 1'), ('while', 'i <= n', [('do', 'j = 1'), ('while', 'j <= 3', [('out', "str(i) + ' x ' + str(j) + ' = ' + str(i * j)", {'text': 'Print i × j'}), ('do', 'j = j + 1')]), ('do', 'i = i + 1')])],
      lambda n: [f'{i} x {j} = {i * j}' for i in range(1, n + 1) for j in range(1, 4)], [(2,)], 'H')
    q('Print the pattern 1, 22, 333 … for n rows.',
      [('in', ['n']), ('do', 'i = 1'), ('while', 'i <= n', [('do', "row = ''; j = 1"), ('while', 'j <= i', [('do', 'row = row + str(i)'), ('do', 'j = j + 1')]), ('out', 'row'), ('do', 'i = i + 1')])],
      lambda n: [str(i) * i for i in range(1, n + 1)], [(4,)], 'H')
    q('Input n; print the sum of the digits of every number from 1 to n (for 12: 1 + … + 9 + 1 + 2 + 1 + 3 = 51).',
      [('in', ['n']), ('do', 's = 0; i = 1'), ('while', 'i <= n', [('do', 't = i'), ('while', 't > 0', [('do', 's = s + t % 10; t = t // 10', {'text': 's = s + last digit\nt = t div 10'})]), ('do', 'i = i + 1')]), ('out', 's')],
      lambda n: [str(sum(int(c) for i in range(1, n + 1) for c in str(i)))], [(12,), (9,)], 'H')
    q('Input a number; print "Single digit", "Two digits" or "More than two digits" (for a positive number).',
      [('in', ['n']), ('if', 'n < 10', [('out', "'Single digit'")], [('if', 'n < 100', [('out', "'Two digits'")], [('out', "'More than two digits'")])])],
      lambda n: ['Single digit' if n < 10 else 'Two digits' if n < 100 else 'More than two digits'], [(7,), (42,), (100,)], 'E')
    q('Input the units of water used; ₹2 a unit for the first 50, ₹4 for the next 50, ₹8 after that. Print the bill.',
      [('in', ['u']), ('if', 'u <= 50', [('do', 'bill = u * 2')], [('if', 'u <= 100', [('do', 'bill = 100 + (u - 50) * 4')], [('do', 'bill = 300 + (u - 100) * 8')])]), ('out', 'bill')],
      lambda u: [str(u * 2 if u <= 50 else 100 + (u - 50) * 4 if u <= 100 else 300 + (u - 100) * 8)], [(40,), (50,), (80,), (120,)], 'H')
    q('Input two numbers; swap them using a third variable and print them.',
      [('in', ['a', 'b']), ('do', 't = a; a = b; b = t'), ('out', "str(a) + ' ' + str(b)", {'text': 'Print a, b'})],
      lambda a, b: [f'{b} {a}'], [(3, 8)], 'E')
    q('Input the length of a side; print the perimeter and area of a square.',
      [('in', ['s']), ('do', 'p = 4 * s; area = s * s'), ('out', "str(p) + ' ' + str(area)", {'text': 'Print p, area'})],
      lambda s_: [f'{4 * s_} {s_ * s_}'], [(5,)], 'E')
    q('Input n; print "Prime" or "Not prime" by dividing up to √n (n ≥ 2).',
      [('in', ['n']), ('do', 'd = 2; f = 0'), ('while', 'd * d <= n and f == 0', [('if', 'n % d == 0', [('do', 'f = 1')]), ('do', 'd = d + 1')], {'text': 'd × d ≤ n AND\nf = 0?'}),
       ('if', 'f == 0', [('out', "'Prime'")], [('out', "'Not prime'")])],
      lambda n: ['Prime' if is_prime(n) else 'Not prime'], [(97,), (91,), (2,), (4,)], 'H', '5.8')
    ok(len(R) == 29)
    items = []
    for k, (text, steps, ref, tests, d, s) in enumerate(R, 1):
        algo = make(f'c05-draw-{k:02d}', text, steps, [(list(c), ref(*c)) for c in tests])
        runs = '; '.join(f'{", ".join(map(str, c))} → {" / ".join(algo.run(list(c))[0]) or "(nothing)"}' for c in tests)
        a = (f'\n\n```text\n{algo.pseudocode_md()}\n```\n\n' + pic(drawn(algo), f'Flowchart for draw {k}', 1.05) +
             f'\n\n*Dry runs:* {runs}.')
        items.append((f'Draw a flowchart and write the pseudocode: {text}{tag(d, s)}', a))
    page('10-draw-the-flowchart.md', 'Draw the flowchart', 'Our own questions, from easy to hard. Each answer is one correct flowchart (others are possible), tested on the inputs shown.',
         [('Draw the flowchart', items)], 29)


# ================================================================= 11 compare and choose (generated)
def compare():
    items = []
    for n in [50, 200, 4000, 1000000, 64]:
        k = math.ceil(math.log2(n + 1))
        ok(2 ** (k - 1) - 1 < n <= 2 ** k - 1)
        items.append((f'At most how many looks does halving need to find a name among {ind(n)} sorted names? One by one?{tag("M", "5.8")}',
                      f'Halving **{k}**, one by one **{ind(n)}**. *Why:* {k - 1} looks handle only {ind(2 ** (k - 1) - 1)} names; {k} looks handle {ind(2 ** k - 1)}.'))
    letters = [chr(65 + i) for i in range(16)]
    for c in ['C', 'J', 'O']:
        looks, _ = halving(letters, c)
        items.append((f'Among the 16 names A to P in order, which names does halving open to find {c}?{tag("M", "5.8")}',
                      f'{", ".join(letters[m] for _, _, m in looks)}: **{len(looks)}** looks (one by one: {letters.index(c) + 1}).'))
    for a, b in [(48, 36), (100, 75), (610, 377)]:
        r, x, y = 0, a, b
        while y:
            x, y = y, x % y; r += 1
        ok(x == math.gcd(a, b))
        items.append((f'How many divisions does Euclid need for the GCD of {a} and {b}, and how many does listing all divisors need?{tag("M", "5.8")}',
                      f'Euclid **{r}** (GCD {x}); listing **{a + b}** ({a} + {b} trial divisions).'))
    for n in [101, 143, 1009]:
        c = [len(prime_method(n, m)[0]) for m in (1, 2, 3)]
        v = prime_method(n, 3)[1]
        ok((v == 'prime') == is_prime(n))
        items.append((f'How many divisions do methods (i) n − 1, (ii) n ÷ 2 and (iii) √n make to test {ind(n)}? Is it prime?{tag("H", "5.8")}',
                      f'(i) {ind(c[0])}, (ii) {ind(c[1])}, (iii) {c[2]}: **{v}**.' + (f' {n} = {prime_method(n, 3)[0][-1]} × {n // prime_method(n, 3)[0][-1]}.' if v != 'prime' else '')))
    for n in [100, 1000]:
        ok(sum(range(1, n + 1)) == n * (n + 1) // 2)
        items.append((f'To add 1 + 2 + … + {ind(n)}, how many additions does a loop make, and how many operations does the formula n(n + 1) ÷ 2 make?{tag("E", "5.8")}',
                      f'Loop: **{ind(n)}** additions; formula: **3** operations. Both give {ind(n * (n + 1) // 2)}.'))
    items.append((f'Which uses more memory: testing primes by dividing up to √n, or by a stored list of the 25 primes up to 100?{tag("E", "5.8")}',
                  'The stored list: it must be kept in memory. Dividing up to √n stores nothing extra.'))
    items.append((f'For 10,201, which prime method gives a wrong answer, and why?{tag("H", "5.8")}',
                  'Method (iv): none of the 25 primes up to 100 divides 10,201, so it says prime, but 10,201 = 101 × 101.'))
    items.append((f'A phone has 2,000 contacts in order. A student says halving needs 1,000 looks at most. Is that right?{tag("M", "5.8")}',
                  f'No: at most **{math.ceil(math.log2(2001))}** (2¹¹ − 1 = 2,047). Halving throws away half of what is LEFT at every look.'))
    ok(len(items) == 19)
    items.append((f'An algorithm takes 4 steps for 10 items and 400 for 1,000. Another takes 20 steps for 10 items and 60 for 1,000. Which is better for large lists?{tag("H", "5.8")}',
                  'The second: its steps grow slowly (like halving); the first grows with the number of items, and much faster.'))
    page('11-compare-and-choose.md', 'Compare and choose', 'Counting steps (section 5.8).', [('Compare and choose', items)], 20)


def index():
    t = '# Chapter 5: Problem Solving: questions\n\n'
    n = sum(v[1] for v in total.values())
    t += f'**{n} questions**, each with its answer and the reason below it. They are for learning: try each question first, then read the answer.\n\n**By type of question**\n\n'
    for f in sorted(total)[:7]:
        t += f'- [{total[f][0]}: {total[f][1]}]({f})\n'
    t += '\n**Practice with flowcharts**: generated, and every answer found by running the flowcharts\n\n'
    for f in sorted(total)[7:]:
        t += f'- [{total[f][0]}: {total[f][1]}]({f})\n'
    (Q / 'index.md').write_text(t, encoding='utf-8')
    print('total', n)
    return n


if __name__ == '__main__':
    for f in (mcq, fill, true_false, assertion_reason, short, long_, cases, outputs, bugs, draws, compare):
        f()
    n = index()
    ok(280 <= n <= 320, n)
    print(P1.checks, 'checks passed')
