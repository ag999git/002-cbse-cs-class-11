"""The 22 CBSE practical programs of Class XI (suggested practical list, syllabus 2026-27) as flowcharts (27 Nov 2026).

Each program is written once as steps for 50-tools/flow_layout.py, which lays out the flowchart, writes the
pseudocode and the Python program. Each is then run (the flowchart itself, box by box, and its Python program) on
many inputs and compared with a SEPARATE reference function written here in plain Python, so a wrong box cannot pass.
Where one syllabus line asks for two results from one input (larger / smaller; palindrome and change of case),
one chart gives both: 22 charts in all."""
import math
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent.parent / '50-tools'))
from flow_layout import make  # noqa: E402

P = []          # (number, slug, title, syllabus words, algo, walk-through input, note)


def ref_series(kind, x, n):
    if kind == 1:
        return sum(x ** i for i in range(n + 1))
    if kind == 2:
        return sum((-x) ** i for i in range(n + 1))
    total = 0                                  # added one term at a time, in order, as the flowchart does
    for i in range(1, n + 1):                  # (Python 3.12's sum() of floats is more exact, so it may differ in
        total += x ** i / (i if kind == 3 else math.factorial(i))   # the last digit)
    return total


def fmt(v):
    return str(v)


def add(num, slug, title, words, steps, ref, cases, walk, note='', types=None):
    tests = [(list(c), ref(*c)) for c in cases]
    algo = make(f'c05-prac-{num:02d}-{slug}', title, steps, tests, types)
    P.append((num, slug, title, words, algo, walk, note))


R = random.Random(5)

# 1 ---------------------------------------------------------------- welcome message
add(1, 'welcome', 'Display a welcome message', 'Input a welcome message and display it.',
    [('in', ['msg'], 'str'), ('out', 'msg')],
    lambda m: [m], [('Welcome to Class XI',), ('Namaste',)], ['Welcome to Class XI'])

# 2 ---------------------------------------------------------------- larger and smaller of two
add(2, 'larger-smaller', 'The larger and the smaller of two numbers',
    'Input two numbers and display the larger / smaller number.',
    [('in', ['a', 'b']),
     ('if', 'a >= b', [('do', 'big = a; small = b')], [('do', 'big = b; small = a')]),
     ('out', "'Larger: ' + str(big)", {'text': 'Print big'}),
     ('out', "'Smaller: ' + str(small)", {'text': 'Print small'})],
    lambda a, b: [f'Larger: {max(a, b)}', f'Smaller: {min(a, b)}'],
    [(7, 12), (12, 7), (5, 5), (-3, 2)] + [(R.randint(-50, 50), R.randint(-50, 50)) for _ in range(20)], [7, 12],
    'Equal numbers: a ≥ b is Yes, so both lines show the same number, which is right.')

# 3 ---------------------------------------------------------------- largest and smallest of three
add(3, 'largest-smallest-three', 'The largest and the smallest of three numbers',
    'Input three numbers and display the largest / smallest number.',
    [('in', ['a', 'b', 'c']),
     ('do', 'big = a; small = a'),
     ('if', 'b > big', [('do', 'big = b')]),
     ('if', 'c > big', [('do', 'big = c')]),
     ('if', 'b < small', [('do', 'small = b')]),
     ('if', 'c < small', [('do', 'small = c')]),
     ('out', "'Largest: ' + str(big)", {'text': 'Print big'}),
     ('out', "'Smallest: ' + str(small)", {'text': 'Print small'})],
    lambda a, b, c: [f'Largest: {max(a, b, c)}', f'Smallest: {min(a, b, c)}'],
    [(9, 9, 4), (5, 5, 2), (1, 2, 3), (3, 2, 1), (4, 4, 4)] + [tuple(R.randint(-20, 20) for _ in range(3)) for _ in range(30)],
    [5, 5, 2],
    'This is the "champion" method: assume the first is the largest, and let each other number challenge it. It has no '
    'trap with equal numbers (5, 5, 2 gives 5), and it grows easily to more numbers.')

# 4-6 ------------------------------------------------------------- the three patterns


def ref_p1(n):
    return ['*' * i for i in range(1, n + 1)]


def ref_p2(n):
    return [''.join(str(j) for j in range(1, i + 1)) for i in range(n, 0, -1)]


def ref_p3(n):
    return [''.join(chr(64 + j) for j in range(1, i + 1)) for i in range(1, n + 1)]


add(4, 'pattern-stars', 'Pattern 1: a triangle of stars', 'Generate the patterns using nested loops: Pattern 1.',
    [('in', ['n']), ('do', 'i = 1'),
     ('while', 'i <= n', [('do', "row = ''; j = 1"),
                          ('while', 'j <= i', [('do', "row = row + '*'"), ('do', 'j = j + 1')]),
                          ('out', 'row'), ('do', 'i = i + 1')])],
    ref_p1, [(5,), (1,), (3,)], [3], 'Row i has i stars: the inner loop runs i times.')
add(5, 'pattern-numbers', 'Pattern 2: 12345, 1234 … 1', 'Generate the patterns using nested loops: Pattern 2.',
    [('in', ['n']), ('do', 'i = n'),
     ('while', 'i >= 1', [('do', "row = ''; j = 1"),
                          ('while', 'j <= i', [('do', 'row = row + str(j)'), ('do', 'j = j + 1')]),
                          ('out', 'row'), ('do', 'i = i - 1')])],
    ref_p2, [(5,), (1,), (3,)], [3], 'The outer loop counts DOWN from n, so the rows get shorter.')
add(6, 'pattern-letters', 'Pattern 3: A, AB, ABC …', 'Generate the patterns using nested loops: Pattern 3.',
    [('in', ['n']), ('do', 'i = 1'),
     ('while', 'i <= n', [('do', "row = ''; j = 1"),
                          ('while', 'j <= i', [('do', 'row = row + chr(64 + j)', {'text': 'row = row +\nletter number j'}),
                                               ('do', 'j = j + 1')]),
                          ('out', 'row'), ('do', 'i = i + 1')])],
    ref_p3, [(5,), (1,), (3,)], [3],
    'Letter number j: A is the 1st letter, B the 2nd … In Python, chr(64 + j), because the ASCII code of A is 65 '
    '(Chapter 4).')

# 7-10 ------------------------------------------------------------ the four series
add(7, 'series-1', 'Series 1 + x + x² + … + xⁿ', 'Sum of the series 1 + x + x² + x³ + … + xⁿ.',
    [('in', ['x', 'n']), ('do', 'total = 1; term = 1; i = 1'),
     ('while', 'i <= n', [('do', 'term = term * x'), ('do', 'total = total + term'), ('do', 'i = i + 1')]),
     ('out', 'total')],
    lambda x, n: [fmt(ref_series(1, x, n))], [(2, 3), (2, 5), (3, 0), (1, 10), (-2, 4)], [2, 3],
    'The same as worked example W9: each term is the one before multiplied by x.')
add(8, 'series-2', 'Series 1 − x + x² − … ± xⁿ', 'Sum of the series 1 − x + x² − x³ + … ± xⁿ.',
    [('in', ['x', 'n']), ('do', 'total = 1; term = 1; i = 1'),
     ('while', 'i <= n', [('do', 'term = term * (-x)', {'text': 'term = term × (−x)'}),
                          ('do', 'total = total + term'), ('do', 'i = i + 1')]),
     ('out', 'total')],
    lambda x, n: [fmt(ref_series(2, x, n))], [(2, 3), (2, 4), (3, 0), (1, 5)], [2, 3],
    'Multiplying by −x each time makes the signs take turns: +, −, +, − …')
add(9, 'series-3', 'Series x + x²/2 + x³/3 + … + xⁿ/n', 'Sum of the series x + x²/2 + x³/3 + … + xⁿ/n.',
    [('in', ['x', 'n']), ('do', 'total = 0; power = 1; i = 1'),
     ('while', 'i <= n', [('do', 'power = power * x'), ('do', 'total = total + power / i'), ('do', 'i = i + 1')]),
     ('out', 'total')],
    lambda x, n: [fmt(ref_series(3, x, n))], [(2, 3), (1, 4), (3, 1)], [2, 3],
    'Keep the power xⁱ and the divisor i apart: the power is multiplied by x, the divisor is just i.')
add(10, 'series-4', 'Series x + x²/2! + x³/3! + … + xⁿ/n!', 'Sum of the series x + x²/2! + x³/3! + … + xⁿ/n!.',
    [('in', ['x', 'n']), ('do', 'total = 0; power = 1; fact = 1; i = 1'),
     ('while', 'i <= n', [('do', 'power = power * x; fact = fact * i'), ('do', 'total = total + power / fact'),
                          ('do', 'i = i + 1')]),
     ('out', 'total')],
    lambda x, n: [fmt(ref_series(4, x, n))], [(2, 3), (1, 4), (3, 1)], [2, 3],
    'The factorial i! is built up as the loop goes (as in W10), so nothing is worked out twice.')

# 11-13 ----------------------------------------------------------- perfect, Armstrong, palindrome number


def ref_perfect(n):
    return [f'{n} is perfect' if n > 1 and sum(d for d in range(1, n) if n % d == 0) == n else f'{n} is not perfect']


add(11, 'perfect', 'Is the number perfect?', 'Determine whether a number is a perfect number.',
    [('in', ['n']), ('do', 's = 0; d = 1'),
     ('while', 'd < n', [('if', 'n % d == 0', [('do', 's = s + d')]), ('do', 'd = d + 1')]),
     ('if', 's == n and n > 1', [('out', "str(n) + ' is perfect'", {'text': 'Print "perfect"'})],
      [('out', "str(n) + ' is not perfect'", {'text': 'Print "not perfect"'})])],
    ref_perfect, [(6,), (28,), (12,), (1,), (27,)], [6],
    'A perfect number equals the sum of its divisors other than itself: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14.')


def ref_arm(n):
    k = len(str(n))
    return [f'{n} is an Armstrong number' if sum(int(c) ** k for c in str(n)) == n else f'{n} is not an Armstrong number']


add(12, 'armstrong', 'Is it an Armstrong number?', 'Determine whether a number is an Armstrong number.',
    [('in', ['n']), ('do', 'k = len(str(n)); s = 0; t = n', {'text': 'k = number of digits\ns = 0, t = n'}),
     ('while', 't > 0', [('do', 'd = t % 10', {'text': 'd = last digit of t\n(t mod 10)'}),
                         ('do', 's = s + d ** k', {'text': 's = s + dᵏ'}),
                         ('do', 't = t // 10', {'text': 't = t div 10\n(drop the last digit)'})]),
     ('if', 's == n', [('out', "str(n) + ' is an Armstrong number'", {'text': 'Print "Armstrong"'})],
      [('out', "str(n) + ' is not an Armstrong number'", {'text': 'Print "not Armstrong"'})])],
    ref_arm, [(153,), (370,), (9474,), (123,), (7,), (10,)], [153],
    'An Armstrong number equals the sum of its digits, each raised to the number of digits: '
    '153 = 1³ + 5³ + 3³ = 1 + 125 + 27.')


def ref_pal(n):
    return [f'{n} is a palindrome' if str(n) == str(n)[::-1] else f'{n} is not a palindrome']


add(13, 'palindrome-number', 'Is the number a palindrome?', 'Determine whether a number is a palindrome.',
    [('in', ['n']), ('do', 'rev = 0; t = n'),
     ('while', 't > 0', [('do', 'rev = rev * 10 + t % 10', {'text': 'rev = rev × 10 +\nlast digit of t'}),
                         ('do', 't = t // 10', {'text': 't = t div 10'})]),
     ('if', 'rev == n', [('out', "str(n) + ' is a palindrome'", {'text': 'Print "palindrome"'})],
      [('out', "str(n) + ' is not a palindrome'", {'text': 'Print "not palindrome"'})])],
    ref_pal, [(121,), (1221,), (123,), (7,), (10,)], [121],
    'The loop builds the number backwards, one digit at a time: 121 → 1, 12, 121.')


def ref_prime(n):
    if n < 2:
        return [f'{n} is neither prime nor composite']
    return [f'{n} is prime' if all(n % d for d in range(2, math.isqrt(n) + 1)) else f'{n} is composite']


add(14, 'prime', 'Prime or composite', 'Input a number and check if the number is a prime or composite number.',
    [('in', ['n']),
     ('if', 'n < 2', [('out', "str(n) + ' is neither prime nor composite'", {'text': 'Print "neither"'})],
      [('do', 'd = 2; found = 0'),
       ('while', 'd * d <= n and found == 0', [('if', 'n % d == 0', [('do', 'found = 1')]), ('do', 'd = d + 1')],
        {'text': 'd × d ≤ n AND\nfound = 0?'}),
       ('if', 'found == 1', [('out', "str(n) + ' is composite'", {'text': 'Print "composite"'})],
        [('out', "str(n) + ' is prime'", {'text': 'Print "prime"'})])])],
    ref_prime, [(n,) for n in [0, 1, 2, 3, 4, 9, 25, 29, 91, 97, 100, 997]], [91],
    'Method (iii) of section 5.8: divide only while d × d ≤ n, and stop at the first divisor. 0 and 1 are neither '
    'prime nor composite.')


def ref_fib(n):
    a, b, out = 0, 1, []
    for _ in range(n):
        out.append(str(a)); a, b = b, a + b
    return out


add(15, 'fibonacci', 'The first n terms of the Fibonacci series', 'Display the terms of a Fibonacci series.',
    [('in', ['n']), ('do', 'a = 0; b = 1; i = 1'),
     ('while', 'i <= n', [('out', 'a'), ('do', 'c = a + b; a = b; b = c'), ('do', 'i = i + 1')])],
    ref_fib, [(7,), (1,), (2,), (10,)], [6],
    'Each term is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8 … The box "c = a + b, a = b, b = c" moves the pair '
    'one step along.')


def ref_gcd(a, b):
    return [f'{math.gcd(a, b)} {a * b // math.gcd(a, b)}']


add(16, 'gcd-lcm', 'GCD and LCM of two numbers (Euclid)', 'Compute the greatest common divisor and least common '
    'multiple of two integers.',
    [('in', ['a', 'b']), ('do', 'x = a; y = b'),
     ('while', 'b != 0', [('do', 'r = a % b', {'text': 'r = remainder\nof a ÷ b'}), ('do', 'a = b'), ('do', 'b = r')]),
     ('do', 'lcm = x * y // a', {'text': 'lcm = x × y ÷ a'}),
     ('out', "str(a) + ' ' + str(lcm)", {'text': 'Print a, lcm'})],
    ref_gcd, [(30, 21), (54, 45), (84, 36), (1071, 462), (17, 5), (12, 18), (8, 8)], [30, 21],
    'Worked example W8 of the book; every round is drawn on the page "Euclid step by step".')


def ref_count(s):
    v = sum(c in 'aeiouAEIOU' for c in s)
    c = sum(ch.isalpha() and ch not in 'aeiouAEIOU' for ch in s)
    return [f'Vowels {v}, consonants {c}, upper {sum(ch.isupper() for ch in s)}, lower {sum(ch.islower() for ch in s)}']


add(17, 'count-characters', 'Vowels, consonants, upper case and lower case in a string',
    'Count and display the number of vowels, consonants, uppercase, lowercase characters in a string.',
    [('in', ['s'], 'str'), ('do', 'v = 0; c = 0; up = 0; lo = 0; i = 0'),
     ('while', 'i < len(s)', [
         ('do', 'ch = s[i]', {'text': 'ch = character\nnumber i of s'}),
         ('if', 'ch.isalpha()', [('if', "ch in 'aeiouAEIOU'", [('do', 'v = v + 1')], [('do', 'c = c + 1')],
                                  {'text': 'ch a vowel?'}),
                                 ('if', 'ch.isupper()', [('do', 'up = up + 1')], [('do', 'lo = lo + 1')],
                                  {'text': 'ch upper case?'})],
          [], {'text': 'ch a letter?'}),
         ('do', 'i = i + 1')]),
     ('out', "'Vowels ' + str(v) + ', consonants ' + str(c) + ', upper ' + str(up) + ', lower ' + str(lo)",
      {'text': 'Print v, c, up, lo'})],
    ref_count, [('Hello World',), ('CBSE 2026',), ('aeiou',), ('',)], ['Hi Om'],
    'Spaces and digits are not letters, so they are counted in none of the four.')


def ref_pal_case(s):
    return [f'{s} is a palindrome' if s == s[::-1] else f'{s} is not a palindrome', s.swapcase()]


add(18, 'palindrome-and-case', 'Is the string a palindrome? Change the case of each letter',
    'Input a string and determine whether it is a palindrome or not; convert the case of characters in a string.',
    [('in', ['s'], 'str'), ('do', "rev = ''; new = ''; i = 0"),
     ('while', 'i < len(s)', [
         ('do', 'rev = s[i] + rev', {'text': 'rev = character i\n+ rev'}),
         ('if', 's[i].isupper()', [('do', 'new = new + s[i].lower()', {'text': 'new = new +\nlower case of it'})],
          [('do', 'new = new + s[i].upper()', {'text': 'new = new +\nupper case of it'})],
          {'text': 'character i\nupper case?'}),
         ('do', 'i = i + 1')]),
     ('if', 'rev == s', [('out', "s + ' is a palindrome'", {'text': 'Print "palindrome"'})],
      [('out', "s + ' is not a palindrome'", {'text': 'Print "not palindrome"'})]),
     ('out', 'new')],
    ref_pal_case, [('madam',), ('Madam',), ('Python',), ('nitin',)], ['Madam'],
    '"Madam" is not a palindrome for the computer: M and m are different characters. Putting each character in FRONT of '
    'rev builds the string backwards.')


def ref_minmax(L):
    return [f'Largest {max(L)}, smallest {min(L)}']


add(19, 'list-largest-smallest', 'The largest and the smallest in a list', 'Find the largest / smallest number in a '
    'list / tuple.',
    [('in', ['L'], 'list'), ('do', 'big = L[0]; small = L[0]; i = 1', {'text': 'big = first item\nsmall = first item\ni = 1'}),
     ('while', 'i < len(L)', [('if', 'L[i] > big', [('do', 'big = L[i]', {'text': 'big = item i'})], [], {'text': 'item i > big?'}),
                              ('if', 'L[i] < small', [('do', 'small = L[i]', {'text': 'small = item i'})], [], {'text': 'item i < small?'}),
                              ('do', 'i = i + 1')]),
     ('out', "'Largest ' + str(big) + ', smallest ' + str(small)", {'text': 'Print big, small'})],
    ref_minmax, [([4, 9, 1, 7],), ([5],), ([-2, -8, -1],), ([3, 3, 3],)], [[4, 9, 1, 7]],
    'The list is typed as [4, 9, 1, 7]. Items are counted from 0, so the first item is L[0].')


def ref_swap(L):
    M = list(L)
    for i in range(0, len(M) - 1, 2):
        M[i], M[i + 1] = M[i + 1], M[i]
    return [str(M)]


add(20, 'list-swap', 'Swap the items at even and odd places', 'Input a list of numbers and swap elements at the even '
    'location with the elements at the odd location.',
    [('in', ['L'], 'list'), ('do', 'i = 0'),
     ('while', 'i + 1 < len(L)', [('do', 't = L[i]; L[i] = L[i + 1]; L[i + 1] = t',
                                   {'text': 'swap item i and\nitem i + 1 (with t)'}),
                                  ('do', 'i = i + 2')]),
     ('out', 'L')],
    ref_swap, [([1, 2, 3, 4, 5, 6],), ([10, 20, 30],), ([7],), ([],)], [[1, 2, 3, 4, 5]],
    'i jumps by 2 (0, 2, 4 …), so each pair is swapped once. With an odd number of items, the last one stays.')


def ref_search(L, x):
    return [f'{x} found at position {L.index(x)}' if x in L else f'{x} not found']


add(21, 'list-search', 'Search for an item in a list', 'Input a list / tuple of elements, search for a given element '
    'in the list / tuple.',
    [('in', ['L'], 'list'), ('in', ['x']), ('do', 'i = 0; pos = -1'),
     ('while', 'i < len(L) and pos == -1', [('if', 'L[i] == x', [('do', 'pos = i')], [], {'text': 'item i = x?'}),
                                             ('do', 'i = i + 1')],
      {'text': 'i < length AND\npos = −1?'}),
     ('if', 'pos == -1', [('out', "str(x) + ' not found'", {'text': 'Print "not found"'})],
      [('out', "str(x) + ' found at position ' + str(pos)", {'text': 'Print "found at" pos'})])],
    ref_search, [([4, 9, 1, 7], 1), ([4, 9, 1, 7], 5), ([3, 3], 3), ([], 2)], [[4, 9, 1, 7], 1],
    'The search stops at the first match (pos is no longer −1). This is the one-by-one search of section 5.8.')


def ref_dict(n, *rows):
    out = []
    for k in range(n):
        roll, name, marks = rows[3 * k: 3 * k + 3]
        if marks > 75:
            out.append(name)
    return out


add(22, 'dictionary-marks', 'Students with marks above 75', 'Create a dictionary with the roll number, name and marks '
    'of n students in a class and display the names of students who have marks above 75.',
    [('in', ['n']), ('do', 'd = {}; i = 1', {'text': 'd = empty dictionary\ni = 1'}),
     ('while', 'i <= n', [('in', ['roll', 'name', 'marks'], {'text': 'Input roll,\nname, marks'}),
                          ('do', 'd[roll] = [name, marks]', {'text': 'd[roll] =\n[name, marks]'}),
                          ('do', 'i = i + 1')]),
     ('do', 'keys = list(d); k = 0', {'text': 'keys = the roll\nnumbers in d\nk = 0'}),
     ('while', 'k < len(keys)', [('if', 'd[keys[k]][1] > 75', [('out', 'd[keys[k]][0]', {'text': 'Print the name'})],
                                  [], {'text': 'marks of student\nk > 75?'}),
                                 ('do', 'k = k + 1')])],
    ref_dict, [(3, 1, 'Asha', 82, 2, 'Ravi', 75, 3, 'Meena', 91), (1, 7, 'Om', 40), (2, 1, 'A', 76, 2, 'B', 100)],
    [3, 1, 'Asha', 82, 2, 'Ravi', 75, 3, 'Meena', 91],
    'Ravi has exactly 75, which is not ABOVE 75. The roll number is the key, so no two students share an entry.',
    types={'n': 'int', 'roll': 'int', 'name': 'str', 'marks': 'int'})

assert [p[0] for p in P] == list(range(1, 23))

if __name__ == '__main__':
    for num, slug, title, words, algo, walk, note in P:
        print(num, algo.name, len(algo.nodes), 'boxes;', len(algo.tests), 'tests passed')
