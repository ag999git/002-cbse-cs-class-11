"""Chapter 4 online pages (26 Nov 2026, Anurag: plan ch04-online-plan-v1 approved): Helps you understand (H4-H6),
Sometimes asked (S1-S7), Beyond syllabus (B1-B3, B6, B7) and Challenge (C1, C2). Every number in every table is
computed here by numbase_lib.py or by Python's own encoders, and checked before the page is written.
The interactive pages (H1-H3) and B4 (floating point), B5 (joining characters) come in the next revision.

Run from the repository root:  python tools/ch04_pages.py"""
import sys
import unicodedata
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numbase_lib as nb  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'book' / 'unit-1' / '004-ch04-number-systems-and-encoding'
S = '₀₁₂₃₄₅₆₇₈₉'
checks = 0


def sub(n):
    return ''.join(S[int(c)] for c in str(n))


def num(s, b):
    return f'({s}){sub(b)}'


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def conv(s, a, b):
    r = nb.convert(s, a, b)
    ok(nb.value(r, b) == nb.value(s, a), (s, a, b, r))
    return r


def head(title, label, intro):
    return (f'# {label}: {title}\n\n*Chapter 4 · {label}. {intro}*\n\n'
            '*Every number and code on this page was computed by a program (`tools/ch04_pages.py`) and checked.*\n\n')


def ladder_md(n, b):
    rows = nb.div_ladder(n, b)
    out = ['| Divide | Quotient | Remainder |', '|:-:|:-:|:-:|']
    for d, q, r in rows:
        out.append(f'| {d} ÷ {b} | {q} | **{nb.DIGITS[r]}**' + (f' ({r})' if r > 9 else '') + ' |')
    res = nb.to_base(n, b)
    ok(nb.value(res, b) == n)
    return '\n'.join(out) + f'\n\nRead the remainders upward: {num(n, 10)} = {num(res, b)}.'


def write(name, text):
    (D / name).write_text(text, encoding='utf-8')
    print('wrote', name)


# ================================================================= H4 why the methods work
def h4():
    t = head('why the methods work', 'Helps you understand',
             'The printed book shows each method and gives the reason in a "Why?" box; this page shows the reason step by step, with algebra you already know.')
    n, b = 45, 2
    q, r = divmod(n, b)
    t += f'''## 1. Why does dividing give the digits?

Any whole number n, divided by the base b, gives a quotient q and a remainder r:

**n = q × b + r**, and r is always smaller than b, so r is one digit of base b.

- The part **q × b** is a whole number of "b's": it fills the places from the b's place leftwards.
- The part **r** is what is left over for the **units** place.

So the first remainder is the **units digit**. Now do the same with q: its remainder is the next digit, in the b's place,
and so on. That is why the remainders are read **upward**: the first one found is the last digit written.

Example: {n} = {q} × {b} + {r}, so the units digit of {n} in binary is **{r}**. The whole ladder:

{ladder_md(n, b)}

## 2. Why does multiplying give the fraction digits?

A fraction f in base b looks like 0.d₁d₂d₃…, which means f = d₁/b + d₂/b² + d₃/b³ + …

Multiply both sides by b: **f × b = d₁ + d₂/b + d₃/b² + …**

The whole-number part of f × b is exactly **d₁**, the first digit after the point. What is left over (the fraction part) is
0.d₂d₃…, so multiplying again gives d₂. The digits come out **in order**, nearest the point first: read **downward**.

'''
    f = Fraction(13, 16)
    rows, why = nb.mul_ladder(f, 2)
    t += '| Fraction × 2 | Whole part (digit) | Fraction left |\n|:-:|:-:|:-:|\n'
    for fr, p, d, nf in rows:
        t += f'| {float(fr):g} × 2 = {float(p):g} | **{d}** | {float(nf):g} |\n'
    res = '0.' + ''.join(str(r[2]) for r in rows)
    ok(nb.value(res, 2) == f)
    t += f'\nSo {num(float(f), 10)} = {num(res, 2)}. Check: ½ + ¼ + 1/16 = 0.8125. ✓\n\n'
    t += '''## 3. Which fractions end in binary, and which go on for ever?

A fraction ends in base b only if, written in its lowest terms, its denominator has **no prime factor other than those of b**.
For binary (b = 2) the denominator must be a power of 2: 2, 4, 8, 16 …

| Decimal | As a fraction | Denominator | In binary |
|:-:|:-:|:-:|---|
'''
    for x in ['0.5', '0.25', '0.375', '0.625', '0.1', '0.2', '0.3', '0.75']:
        fr = Fraction(x)
        rows, why = nb.mul_ladder(fr, 2, max_steps=12)
        digits = ''.join(str(r[2]) for r in rows)
        ends = why == 'zero'
        pw = fr.denominator & (fr.denominator - 1) == 0
        ok(ends == pw, x)
        t += f'| {x} | {fr.numerator}/{fr.denominator} | {fr.denominator} {"(a power of 2)" if pw else "(has a factor 5)"} | ' \
             f'{"(0." + digits + ")₂, ends" if ends else "(0." + digits + "…)₂, repeats for ever"} |\n'
    t += '''
This is why 0.1, a very ordinary decimal, cannot be stored exactly in a computer: its denominator 10 = 2 × 5 has a 5.

## 4. Why can we group bits for octal and hex, but not for decimal?

- 8 = 2³: one octal place is worth exactly three binary places. A group of 3 bits has 2³ = 8 patterns, one for each octal digit.
- 16 = 2⁴: one hex place is worth exactly four binary places; 4 bits have 16 patterns.
- 10 is **not** a power of 2: no whole number of bits matches one decimal digit (3 bits make 8 patterns, too few; 4 bits make
  16, too many). That is why decimal must go by division or place values.

| Base | A power of 2? | Method |
|:-:|:-:|---|
| 8 = 2³ | yes | group the bits in 3s |
| 16 = 2⁴ | yes | group the bits in 4s |
| 10 | no | divide, or use place values |
'''
    write('helps-why-methods-work.md', t)


# ================================================================= H5 the full ASCII table
CTRL = {0: 'NUL (null)', 7: 'BEL (bell)', 8: 'BS (backspace)', 9: 'TAB (horizontal tab)', 10: 'LF (line feed: new line)',
        13: 'CR (carriage return: back to the start of the line)', 27: 'ESC (escape)', 127: 'DEL (delete)'}


def h5():
    t = head('the full ASCII table, explained', 'Helps you understand',
             'The printed book has the ASCII chart and the codes to remember (section 4.5); this page has every code with its binary and hex, and the patterns in the bits.')
    t += '''## 1. The patterns in the bits

| Characters | Codes | 7-bit pattern | What the pattern says |
|---|:-:|---|---|
'''
    groups = [('control codes', 0, 31), ('space and signs', 32, 47), ("digits '0'–'9'", 48, 57),
              ('capitals A–Z', 65, 90), ('small letters a–z', 97, 122)]
    for name, a, b in groups:
        t += f'| {name} | {a}–{b} | {format(a, "07b")} to {format(b, "07b")} | '
        t += {'control codes': 'the two leftmost bits are 00',
              'space and signs': 'starts 010',
              "digits '0'–'9'": "starts 011 0: the last 4 bits are the digit itself ('7' = 011 0111)",
              'capitals A–Z': 'starts 10: the last 5 bits count the letter (A = 1, B = 2 …)',
              'small letters a–z': 'starts 11: the same last 5 bits as the capital; only the bit worth 32 differs'}[name] + ' |\n'
    ok(format(ord('7'), '07b')[3:] == format(7, '04b'))
    ok(all((ord(c) & 31) == i + 1 for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
    ok(all(ord(c.lower()) - ord(c) == 32 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    t += '''
**Two tricks that follow:** to change a capital to a small letter, add 32 (switch on the bit worth 32); to get the value of
a digit character, subtract 48 (or keep only its last 4 bits).

## 2. All 128 codes

| Code | Binary (7 bits) | Hex | Character |
|:-:|:-:|:-:|---|
'''
    for n in range(128):
        if n < 32 or n == 127:
            ch = CTRL.get(n, 'control code')
        elif n == 32:
            ch = 'space'
        elif chr(n) in '|':
            ch = '\\|'
        else:
            ch = '`' + chr(n) + '`' if chr(n) != '`' else '`` ` ``'
        t += f'| {n} | {format(n, "07b")} | {n:02X} | {ch} |\n'
    t += '\nThe control codes 1–31 not named above were used for old teleprinters and are rarely seen today.\n'
    write('helps-full-ascii-table.md', t)


# ================================================================= H6 how many bits
def h6():
    t = head('how many bits does a number need?', 'Helps you understand',
             'The printed book says n inputs give 2ⁿ patterns (Chapter 3) and seven bits reach 127 (section 4.2); this page turns that into a rule you can use.')
    t += '''## 1. The rule

With **n bits** there are **2ⁿ patterns**, so they can stand for the numbers **0 to 2ⁿ − 1**.

| Bits n | Patterns 2ⁿ | Numbers | Where you meet it |
|:-:|:-:|:-:|---|
'''
    where = {1: 'one switch: on or off', 3: 'one octal digit', 4: 'one hex digit (a nibble)', 7: 'ASCII', 8: 'one byte; ISCII',
             10: 'about a thousand (1024 = 1 KB)', 16: 'two bytes; UTF-16 unit', 32: 'UTF-32; four bytes'}
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 32]:
        t += f'| {n} | {2 ** n:,} | 0 to {2 ** n - 1:,} | {where.get(n, "")} |\n'
    t += '''
## 2. How many bits for a given number?

Find the smallest n with 2ⁿ greater than the number. Or convert the number to binary and count the bits.

| Number | Smallest power of 2 above it | Bits needed | Check in binary |
|:-:|:-:|:-:|---|
'''
    for x in [5, 31, 32, 100, 255, 256, 1000, 100000, 10000000]:
        n = x.bit_length()
        ok(2 ** (n - 1) <= x < 2 ** n)
        t += f'| {x:,} | 2^{n} = {2 ** n:,} | **{n}** | {nb.to_base(x, 2)} |\n'
    t += '''
**One crore (1,00,00,000) needs 24 bits**, because 2²⁴ = 1,67,77,216 is the first power of 2 above it.

## 3. The same in octal and hex

n octal digits reach 8ⁿ − 1; n hex digits reach 16ⁿ − 1. Each octal digit is 3 bits and each hex digit 4 bits, so the
number of hex digits is about a quarter of the number of bits (rounded up).

| Digits | Largest octal | = decimal | Largest hex | = decimal |
|:-:|:-:|:-:|:-:|:-:|
'''
    for k in [1, 2, 3, 4]:
        o, h = '7' * k, 'F' * k
        ok(nb.value(o, 8) == 8 ** k - 1 and nb.value(h, 16) == 16 ** k - 1)
        t += f'| {k} | {num(o, 8)} | {8 ** k - 1:,} | {num(h, 16)} | {16 ** k - 1:,} |\n'
    ok((10 ** 7).bit_length() == 24)
    write('helps-how-many-bits.md', t)


# ================================================================= S1 binary arithmetic
def add_working(a, b):
    """Column addition of two binary strings, with the carry row; returns markdown."""
    n = max(len(a), len(b)) + 1
    A, B = a.rjust(n, '0'), b.rjust(n, '0')
    carry, res, carries = 0, [], [' '] * n
    for i in range(n - 1, -1, -1):
        s = int(A[i]) + int(B[i]) + carry
        res.append(str(s % 2))
        carry = s // 2
        if i > 0:
            carries[i - 1] = '1' if carry else ' '
    r = ''.join(reversed(res)).lstrip('0') or '0'
    ok(int(r, 2) == int(a, 2) + int(b, 2))
    c = ''.join(carries)
    w = max(len(a), len(b), len(r)) + 2
    return (f'```\ncarry  {c.rjust(w)}\n       {a.rjust(w)}\n     + {b.rjust(w)}\n       {"-" * w}\n       {r.rjust(w)}\n```\n'
            f'Check in decimal: {int(a, 2)} + {int(b, 2)} = {int(r, 2)}. ✓\n'), r


def s1():
    t = head('binary arithmetic', 'Sometimes asked',
             'Not in the syllabus wording, but school papers set it now and then. The printed book points here at the end of section 4.4.')
    t += '''## 1. The four rules of binary addition

| Sum | Result | Write | Carry | Like in decimal |
|:-:|:-:|:-:|:-:|---|
| 0 + 0 | 0 | 0 | 0 | 0 + 0 |
| 0 + 1 | 1 | 1 | 0 | 0 + 1 |
| 1 + 0 | 1 | 1 | 0 | 1 + 0 |
| 1 + 1 | (10)₂ = 2 | 0 | 1 | 9 + 1 = 10: write 0, carry 1 |
| 1 + 1 + 1 | (11)₂ = 3 | 1 | 1 | (with a carry coming in) |

*Why a carry at 1 + 1?* Binary has no digit 2. Two in binary is "10": one in the twos place, nothing in the units. It is
the meter rolling over (section 4.2).

## 2. Worked examples

'''
    for a, b in [('1011', '110'), ('11011', '1101'), ('111111', '1')]:
        w, r = add_working(a, b)
        t += f'**Add {num(a, 2)} and {num(b, 2)}.**\n\n{w}\n'
    t += '''## 3. Subtraction with borrowing

| Difference | Result | Note |
|:-:|:-:|---|
| 0 − 0 | 0 | |
| 1 − 0 | 1 | |
| 1 − 1 | 0 | |
| 0 − 1 | 1, borrow 1 | borrow from the next place: (10)₂ − 1 = 1 |

'''
    for a, b in [('1101', '110'), ('10000', '1')]:
        r = format(int(a, 2) - int(b, 2), 'b')
        ok(int(r, 2) == int(a, 2) - int(b, 2))
        t += f'- {num(a, 2)} − {num(b, 2)} = **{num(r, 2)}**. Check: {int(a, 2)} − {int(b, 2)} = {int(r, 2)}. ✓\n'
    t += '''
Computers do not subtract this way: they add the **2's complement** instead (next page).

## 4. Common mistakes

| Mistake | Why it is wrong | Correct |
|---|---|---|
| 1 + 1 = 2 | there is no digit 2 in binary | 1 + 1 = (10)₂: write 0, carry 1 |
| forgetting the carry in the last column | the carry is a new leftmost digit | 1 + 1 at the left end gives a new 1 in front |
| 1 + 1 + 1 = 10 | three is (11)₂ | write 1, carry 1 |

## 5. Practice (answers below each)

'''
    qs = [('101', '11'), ('1110', '1011'), ('10101', '1111'), ('110110', '101101'), ('1111', '1111')]
    for i, (a, b) in enumerate(qs, 1):
        r = format(int(a, 2) + int(b, 2), 'b')
        ok(int(r, 2) == int(a, 2) + int(b, 2))
        t += f'**Q{i}.** {num(a, 2)} + {num(b, 2)}\n\n**Answer.** {num(r, 2)}. *Check:* {int(a, 2)} + {int(b, 2)} = {int(r, 2)}.\n\n'
    for i, (a, b) in enumerate([('1100', '101'), ('10010', '111'), ('11111', '10101'), ('100000', '1'), ('1011', '1011')], 6):
        r = format(int(a, 2) - int(b, 2), 'b')
        t += f'**Q{i}.** {num(a, 2)} − {num(b, 2)}\n\n**Answer.** {num(r, 2)}. *Check:* {int(a, 2)} − {int(b, 2)} = {int(r, 2)}.\n\n'
    write('sometimes-asked-binary-arithmetic.md', t)


# ================================================================= S2 complements
def ones(s):
    return ''.join('1' if c == '0' else '0' for c in s)


def twos(s):
    n = len(s)
    r = format((int(ones(s), 2) + 1) % 2 ** n, f'0{n}b')
    ok((int(s, 2) + int(r, 2)) % 2 ** n == 0)
    return r


def s2():
    t = head("1's and 2's complement", 'Sometimes asked',
             'Not in the syllabus wording, but asked in some school papers and needed for "how does a computer subtract?".')
    t += '''## 1. What they are

- **1's complement:** turn every bit round: 0 becomes 1, 1 becomes 0. (Like NOT in Chapter 3, on every bit.)
- **2's complement:** the 1's complement, **plus 1**.
- **Shortcut for the 2's complement:** from the right, copy the bits up to and including the first 1; turn round all the
  bits after it.

Always work with a **fixed number of bits** (here 8): the complement of a number depends on how many bits it has.

| Number (8 bits) | 1's complement | 2's complement | Check: number + 2's complement |
|:-:|:-:|:-:|---|
'''
    for x in [5, 12, 40, 100, 1, 127]:
        s = format(x, '08b')
        t += f'| {s} ({x}) | {ones(s)} | {twos(s)} | {int(s, 2)} + {int(twos(s), 2)} = {int(s, 2) + int(twos(s), 2)} = 2⁸: the carry leaves 8 zeros |\n'
    t += '''
## 2. Why computers use the 2's complement

In 8 bits, the 2's complement of a number behaves exactly like its **negative**: adding it gives 0 (the carry out of the
eighth bit is dropped). So a computer can **subtract by adding**: A − B = A + (2's complement of B). One adding circuit does
both jobs.

## 3. Subtraction by adding

'''
    for a, b in [(13, 6), (45, 20), (100, 37)]:
        A, B = format(a, '08b'), format(b, '08b')
        tb = twos(B)
        s = (int(A, 2) + int(tb, 2)) % 256
        ok(s == a - b)
        t += (f'**{a} − {b}:** {A} + {tb} (the 2\'s complement of {B}) = 1 {format(s, "08b")}; drop the carry: '
              f'**{format(s, "08b")}** = {s}. ✓\n\n')
    t += '''## 4. Signed numbers in 8 bits

With the 2's complement, 8 bits hold **−128 to +127**. The leftmost bit tells the sign: 0 for positive, 1 for negative.
More on the "Beyond syllabus: signed numbers" page.

## 5. Practice (answers below each)

'''
    for i, x in enumerate([9, 25, 64, 77, 120], 1):
        s = format(x, '08b')
        t += f'**Q{i}.** Find the 1\'s and 2\'s complement of {s} (8 bits).\n\n**Answer.** 1\'s: {ones(s)}; 2\'s: {twos(s)}.\n\n'
    for i, (a, b) in enumerate([(20, 7), (50, 18), (91, 45), (64, 1), (99, 99)], 6):
        A, B = format(a, '08b'), format(b, '08b')
        s = (int(A, 2) + int(twos(B), 2)) % 256
        ok(s == a - b)
        t += (f'**Q{i}.** Using the 2\'s complement in 8 bits, find {a} − {b}.\n\n**Answer.** {A} + {twos(B)} → drop the carry → '
              f'{format(s, "08b")} = {s}.\n\n')
    write('sometimes-asked-complements.md', t)


# ================================================================= S3 double dabble
def dd_rows(bits, b=2):
    v, rows = 0, []
    for d in bits:
        nv = v * b + nb.digit_value(d)
        rows.append((v, d, nv))
        v = nv
    ok(v == nb.value(bits, b))
    return rows


def s3():
    t = head('double dabble: a second way from binary to decimal', 'Sometimes asked',
             'The printed book uses place values (Road 2) and points here for the second method that some teachers and books use.')
    t += '''## 1. The method

Start with 0. Take the bits **from the left**. For each bit: **double what you have, then add the bit.**
When the bits are used up, you have the number in decimal.

'''
    bits = '110101'
    t += f'**Example:** {num(bits, 2)}\n\n| Have | Next bit | Double, then add | New value |\n|:-:|:-:|---|:-:|\n'
    for v, d, nv in dd_rows(bits):
        t += f'| {v} | {d} | 2 × {v} + {d} | **{nv}** |\n'
    t += f'\nSo {num(bits, 2)} = {num(nb.value(bits, 2), 10)}. Check by place values: 32 + 16 + 4 + 1 = 53. ✓\n\n'
    t += '''## 2. Why it works

Doubling moves everything one place to the **left** (every place is worth twice the place to its right), and adding the
new bit fills the units place. After the last bit, every bit has been doubled the right number of times: the leftmost bit
of a 6-bit number is doubled 5 times, so it is worth 2⁵ = 32, exactly its place value.

## 3. It works in any base

For octal, multiply by 8 instead of 2; for hex, by 16:

'''
    for s, b in [('357', 8), ('2F9', 16)]:
        t += f'**{num(s, b)}:** '
        t += '; '.join(f'{v} × {b} + {nb.digit_value(d)} = {nv}' for v, d, nv in dd_rows(s, b))
        t += f' → **{nb.value(s, b)}**.\n\n'
    t += '''## 4. Which method should I use in the exam?

Either is correct. The **place-value** method (Road 2) shows the working most clearly and is what most marking schemes
expect; double dabble is quicker in your head for long binary numbers. Use one to work, the other to check.

## 5. Practice (answers below each)

'''
    for i, s in enumerate(['1011', '11100', '100101', '1111111', '10110110', '110011001'], 1):
        rows = dd_rows(s)
        t += f'**Q{i}.** Convert {num(s, 2)} to decimal by double dabble.\n\n**Answer.** ' + ' → '.join(str(r[2]) for r in rows) + \
             f'; so {num(s, 2)} = **{nb.value(s, 2)}**.\n\n'
    for i, (s, b) in enumerate([('76', 8), ('1234', 8), ('BAD', 16), ('7E5', 16)], 7):
        rows = dd_rows(s, b)
        t += f'**Q{i}.** Convert {num(s, b)} to decimal by "multiply and add".\n\n**Answer.** ' + ' → '.join(str(r[2]) for r in rows) + \
             f'; so **{nb.value(s, b)}**.\n\n'
    write('sometimes-asked-double-dabble.md', t)


# ================================================================= S4 extended ASCII and garbled text
def s4():
    t = head('extended ASCII and garbled text', 'Sometimes asked',
             'The printed book gives one line on extended ASCII (section 4.5); this page has the full story and the garbled-text puzzle.')
    rupee = '₹'.encode('utf-8')
    wrong = rupee.decode('cp1252')
    ok(wrong == 'â‚¹')
    e_acute = 'é'.encode('utf-8').decode('cp1252')
    t += f'''## 1. Extended ASCII

ASCII uses 7 bits (codes 0 to 127). A byte has 8 bits, so 128 more codes (128 to 255) were free. Computer makers filled
them with accented letters (é, ü, ñ), lines for drawing boxes, and symbols. But **each maker filled them differently**:
these sets are called **code pages**. Code 233 was é in one code page and a different letter in another. Text that used
codes above 127 came out wrong on a computer with another code page: the "two registers" problem of the printed book.

| Fact | |
|---|---|
| Codes 0 to 127 | the same everywhere (plain ASCII) |
| Codes 128 to 255 | different in each code page (Windows-1252, ISO 8859-1, Indian code pages …) |
| Why it could not become a world standard | 128 extra places cannot hold the world's scripts, and nobody agreed which 128 |
| What replaced it | Unicode |

## 2. The garbled-text puzzle: "{wrong}" instead of ₹

You may have seen "{wrong}" in a message where ₹ should be. Here is what happened:

1. The sender's phone stored ₹ in **UTF-8**: three bytes, {' '.join(f'{x:02X}' for x in rupee)}.
2. The receiving program wrongly read the text with an old one-byte table (Windows-1252), where **each byte is one
   character**.
3. In that table E2 is "â", 82 is "‚" and B9 is "¹". So one ₹ became three wrong characters.

The bytes were right; the **table** used to read them was wrong. The same happens to é, which becomes "{e_acute}".
This kind of garbled text even has a name, **mojibake** (Japanese for "changed characters").

**The cure:** both sides must use the same encoding, and today that is almost always UTF-8. In a browser or editor,
choosing "UTF-8" as the encoding usually brings the text back.
'''
    write('sometimes-asked-extended-ascii-garbled-text.md', t)


# ================================================================= S5 typing Indian languages
def s5():
    t = head('typing Hindi and other Indian languages', 'Sometimes asked',
             'NCERT has an activity on it and some books describe it. The printed book points here from section 4.5.')
    t += '''## 1. Three ways to type in an Indian script

| Way | How it works | Good for |
|---|---|---|
| **InScript keyboard** | each key of an ordinary keyboard gives one letter or sign of the script; the same layout serves all Indian scripts | fast typing after practice; the Government of India standard |
| **Phonetic (transliteration) typing** | you type in English letters as it sounds ("namaste") and the program shows नमस्ते | beginners; phones |
| **Handwriting or voice** | write on the screen with a finger, or speak | phones |

Whatever way you type, what is stored is the same: **Unicode code points**, usually in **UTF-8**.

## 2. InScript, the standard keyboard

- The first InScript layout was part of the ISCII standard **IS 13194:1991** (section 4.5 of the book).
- Today's **Enhanced InScript** is the Bureau of Indian Standards standard **IS 16350:2016**. It is built to work with
  Unicode and covers the scripts of all 22 official languages of India.
- Because ISCII gave the same sound the same place in every script, InScript puts the same sound on the same key in
  every script: learn it once for Hindi and you can type Bengali or Tamil on the same keys.

## 3. Activity (about 20 minutes)

1. On a computer, add the Hindi language and its keyboard in the language settings; on a phone, add Hindi to the
   keyboard languages.
2. Type your name in Devanagari (or in your own state's script).
3. Count its characters, then use the chapter's notebook to see its code points and its size in UTF-8 and UTF-32.
4. Compare with your name in English: which takes more bytes in UTF-8, and why? (Each English letter takes 1 byte;
   each Devanagari code point takes 3.)

## 4. Unicode in Indian e-governance

Indian government websites and documents use Unicode for Indian languages, so that text typed in one office can be read
in any other, on any device. This is the "one register for the whole school" of the printed book, at the scale of a
country.
'''
    write('sometimes-asked-typing-indian-languages.md', t)


# ================================================================= S6 UTF-16
def s6():
    t = head('UTF-16, the third way', 'Sometimes asked',
             'The syllabus names UTF-8 and UTF-32; some books also describe UTF-16, which sits between them.')
    t += '''## 1. How UTF-16 works

UTF-16 stores a code point in **2 bytes** (one 16-bit unit) if it fits, and in **4 bytes** (two units, called a
**surrogate pair**) if it does not. Every character of the common scripts, including all Indian scripts, fits in 2 bytes;
emojis and rare scripts take 4.

| Character | Code point | UTF-8 bytes | UTF-16 bytes | UTF-32 bytes |
|:-:|:-:|:-:|:-:|:-:|
'''
    for ch in ['A', 'é', '₹', 'अ', 'ஆ', '😀']:
        u8, u16, u32 = len(ch.encode('utf-8')), len(ch.encode('utf-16-le')), len(ch.encode('utf-32-le'))
        ok(u32 == 4 and u16 in (2, 4))
        t += f'| {ch} | U+{ord(ch):04X} | {u8} | {u16} | {u32} |\n'
    s = 'हम सब एक'
    a, b, c = len(s.encode('utf-8')), len(s.encode('utf-16-le')), len(s.encode('utf-32-le'))
    ok((a, b, c) == (20, 16, 32))
    t += f'''
**हम सब एक** (the printed worked example): UTF-8 {a} bytes, UTF-16 **{b} bytes**, UTF-32 {c} bytes.

## 2. The three compared

| Basis of difference | UTF-8 | UTF-16 | UTF-32 |
|---|---|---|---|
| Bytes per character | 1 to 4 | 2 or 4 | always 4 |
| English text | smallest (1 byte) | 2 bytes | 4 bytes |
| Hindi text | 3 bytes | **2 bytes** (smallest) | 4 bytes |
| Old ASCII files | read unchanged | must be converted | must be converted |
| Where used | the web, e-mail, Python files | inside Windows, Java and JavaScript | inside some programs |

So for a text that is mostly Hindi, UTF-16 is smaller than UTF-8; for English or mixed web pages, UTF-8 is smaller. The
web chose UTF-8 because most of its markup (HTML tags) is plain ASCII.
'''
    write('sometimes-asked-utf16.md', t)


# ================================================================= S7 Unicode code charts
BLOCKS = [('Devanagari (Hindi, Marathi, Sanskrit, Nepali …)', 0x0900, 0x097F), ('Bengali and Assamese', 0x0980, 0x09FF),
          ('Gurmukhi (Punjabi)', 0x0A00, 0x0A7F), ('Gujarati', 0x0A80, 0x0AFF), ('Oriya (Odia)', 0x0B00, 0x0B7F),
          ('Tamil', 0x0B80, 0x0BFF), ('Telugu', 0x0C00, 0x0C7F), ('Kannada', 0x0C80, 0x0CFF), ('Malayalam', 0x0D00, 0x0D7F)]


def s7():
    t = head('Unicode code points of Indian scripts', 'Sometimes asked',
             'The printed book gives the Devanagari block and a few code points (section 4.5); this page has every Indian script block and how to look up any character.')
    t += '| Script | Block | First letter "a" of the script | Its code point |\n|---|:-:|:-:|:-:|\n'
    for name, a, b in BLOCKS:
        ch = chr(a + 5)
        nm = unicodedata.name(ch)
        ok(nm.endswith('LETTER A'), nm)
        t += f'| {name} | U+{a:04X} to U+{b:04X} | {ch} | U+{a + 5:04X} |\n'
    t += '''
Each Indian script has a block of 128 places, and the letters sit in **the same order** in every block (the order of
ISCII). So "a" is always the 6th place (…05), and ka is always …15:

| Script | ka | Code point |
|---|:-:|:-:|
'''
    for name, a, b in BLOCKS[:6]:
        ch = chr(a + 0x15)
        ok(unicodedata.name(ch).endswith('LETTER KA'))
        t += f'| {name.split(" (")[0]} | {ch} | U+{a + 0x15:04X} |\n'
    t += '''
## How to look up any character

- **On the web:** the Unicode Consortium publishes a code chart for every block (search "Unicode code charts").
- **In Python** (Chapter 6 onward): `ord('क')` gives 2325 and `hex(ord('क'))` gives '0x915'; `chr(0x20B9)` gives '₹'.
- **In a word processor:** type the hex code point and press Alt+X (in Microsoft Word): 20b9 then Alt+X gives ₹.

## A few facts

- The **₹** sign (U+20B9) was added in Unicode 6.0, in **2010**, the year India adopted it.
- Unicode 17.0 (September 2025) has 159,801 characters from 172 scripts.
- The Hindi digits ० to ९ are U+0966 to U+096F; they are different characters from 0 to 9 (U+0030 to U+0039).
'''
    ok(ord('०') == 0x966 and ord('९') == 0x96F and ord('क') == 2325)
    write('sometimes-asked-unicode-indian-scripts.md', t)


# ================================================================= B1 how UTF-8 packs bits
def utf8_working(ch):
    cp = ord(ch)
    by = ch.encode('utf-8')
    n = len(by)
    pat = {1: ['0xxxxxxx'], 2: ['110xxxxx', '10xxxxxx'], 3: ['1110xxxx', '10xxxxxx', '10xxxxxx'],
           4: ['11110xxx', '10xxxxxx', '10xxxxxx', '10xxxxxx']}[n]
    free = sum(p.count('x') for p in pat)
    bits = format(cp, f'0{free}b')
    out, k = [], 0
    for p in pat:
        c = p.count('x')
        out.append(p.replace('x' * c, bits[k:k + c]))
        k += c
    ok([int(o, 2) for o in out] == list(by), ch)
    return cp, n, pat, bits, out, by


def b1():
    t = head('how UTF-8 packs the bits', 'Beyond syllabus',
             'The printed book says UTF-8 uses 1 to 4 bytes (section 4.5); this page shows exactly how the bits are placed.')
    t += '''## 1. The patterns

| Code points | Bytes | Byte patterns (x = a bit of the code point) | Free bits |
|---|:-:|---|:-:|
| U+0000 to U+007F | 1 | 0xxxxxxx | 7 |
| U+0080 to U+07FF | 2 | 110xxxxx 10xxxxxx | 11 |
| U+0800 to U+FFFF | 3 | 1110xxxx 10xxxxxx 10xxxxxx | 16 |
| U+10000 to U+10FFFF | 4 | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx | 21 |

- The **first byte** says how many bytes the character has: it starts with as many 1s as there are bytes (110 = 2,
  1110 = 3, 11110 = 4). A byte starting with 0 is a whole ASCII character on its own.
- Every **following byte** starts with 10. So a program can always find where a character starts, even in the middle of
  a text: this is the "board on every vehicle" of the printed parking-lot picture.

## 2. Worked examples

'''
    for ch in ['é', '₹', 'अ', '😀']:
        cp, n, pat, bits, out, by = utf8_working(ch)
        t += (f'**{ch}** (U+{cp:04X}): {n} bytes. Code point in binary, filled to {len(bits)} bits: {bits}. '
              f'Into the pattern {" ".join(pat)} → {" ".join(out)} → **{" ".join(f"{x:02X}" for x in by)}** in hex.\n\n')
    t += '''## 3. Decoding: from bytes back to the character

Take E0 A4 85. In binary: 1110 0000 · 10 100100 · 10 000101. The first byte starts with 1110, so 3 bytes. Remove the
markers (1110, 10, 10) and join what is left: 0000 100100 000101 = 0000 1001 0000 0101 = 0905 in hex → **U+0905 = अ**.

## 4. Why is it designed like this?

- ASCII text is unchanged (one byte, starting with 0).
- No byte of a long character can be mistaken for an ASCII character (they all start with 1).
- A damaged byte spoils only one character; the reader finds the next start and carries on.
'''
    cp, n, pat, bits, out, by = utf8_working('अ')
    ok(by.hex().upper() == 'E0A485')
    write('beyond-utf8-bits.md', t)


# ================================================================= B2 other codes
def b2():
    t = head('other codes: BCD, Excess-3, Gray code, EBCDIC and parity', 'Beyond syllabus',
             'Not in the Class XI syllabus; taught in engineering courses on digital circuits, and asked now and then in olympiads.')
    t += '| Decimal | Binary | BCD (8421) | Excess-3 | Gray code |\n|:-:|:-:|:-:|:-:|:-:|\n'
    for n in range(10):
        g = n ^ (n >> 1)
        t += f'| {n} | {format(n, "04b")} | {format(n, "04b")} | {format(n + 3, "04b")} | {format(g, "04b")} |\n'
    for n in range(15):
        ok(bin((n ^ (n >> 1)) ^ ((n + 1) ^ ((n + 1) >> 1))).count('1') == 1)
    bcd = ' '.join(format(int(d), '04b') for d in '259')
    t += f'''
## 1. BCD (binary-coded decimal)

Each **decimal digit** is written in 4 bits, separately: 259 in BCD is {bcd}, not the binary of 259
({nb.to_base(259, 2)}). Used where numbers are shown digit by digit: calculators, digital clocks, meters. The 4-bit
patterns 1010 to 1111 are not used.

## 2. Excess-3

BCD plus 3 for each digit. Its trick: the 9's complement of a digit is found by turning every bit round (4 → 0111, and
9 − 4 = 5 → 1000). Used in old calculating machines.

## 3. Gray code

Counting in Gray code, **only one bit changes** from one number to the next (see the table: 3 → 4 is 0010 → 0110).
In ordinary binary, 7 → 8 changes all four bits (0111 → 1000), and a sensor reading the bits at slightly different
moments could see a wrong number in between. Gray code is used in **rotary encoders** (the knob of a volume control,
the position sensor of a motor) for this reason. To get it: copy the leftmost bit, then each next Gray bit is the XOR
(Chapter 3) of two neighbouring binary bits.

## 4. EBCDIC

**Extended Binary Coded Decimal Interchange Code**: IBM's 8-bit code for its mainframe computers (1960s), different
from ASCII. 'A' is C1 in hex (193) in EBCDIC but 41 (65) in ASCII. Still used on some bank and government mainframes.

## 5. Parity bit: a simple check for errors

An extra bit is added so that the number of 1s is **even** (even parity) or **odd** (odd parity). If one bit is
flipped on the way, the count is wrong and the error is noticed (though not corrected).

| Data (7 bits) | Number of 1s | Even-parity bit | Sent (8 bits) |
|:-:|:-:|:-:|:-:|
'''
    for ch in 'AC7':
        d = format(ord(ch), '07b')
        p = d.count('1') % 2
        ok((d.count('1') + p) % 2 == 0)
        t += f"| {d} ('{ch}') | {d.count('1')} | {p} | {p}{d} |\n"
    ok('A'.encode('cp500') == b'\xc1')
    write('beyond-other-codes.md', t)


# ================================================================= B3 signed numbers
def b3():
    t = head('signed numbers: how a computer stores −5', 'Beyond syllabus',
             'Not in the Class XI syllabus; it follows on from the "1\'s and 2\'s complement" page and prepares for data types (Chapter 7).')
    t += '| Number | Sign and magnitude | 1\'s complement | 2\'s complement |\n|:-:|:-:|:-:|:-:|\n'
    for x in [5, -5, 1, -1, 127, -127, 0]:
        if x >= 0:
            sm = oc = tc = format(x, '08b')
        else:
            sm = '1' + format(-x, '07b')
            oc = ones(format(-x, '08b'))
            tc = format((256 + x) % 256, '08b')
        ok(int(tc, 2) == x % 256)
        t += f'| {x:+d} | {sm} | {oc} | {tc} |\n'
    t += '''
- **Sign and magnitude:** the leftmost bit is the sign (0 +, 1 −), the rest is the size. Simple, but it has two zeros
  (+0 and −0) and adding needs special rules.
- **1's complement:** a negative number is its positive turned round. Still two zeros.
- **2's complement:** a negative number is the 2's complement of its positive. **One zero**, and adding works with the
  ordinary adding circuit. Almost every computer uses it.

| Bits | Range in 2's complement |
|:-:|---|
'''
    for n in [8, 16, 32, 64]:
        t += f'| {n} | −{2 ** (n - 1):,} to +{2 ** (n - 1) - 1:,} |\n'
    t += '''
**Overflow:** in 8 bits, 127 + 1 gives 1000 0000, which reads as −128: the result did not fit. Programs in languages with
fixed-size numbers must watch for this. **Python's whole numbers have no fixed size**: Python simply uses more bytes when a
number grows, so `2 ** 100` is exact.
'''
    ok(int('10000000', 2) - 256 == -128)
    write('beyond-signed-numbers.md', t)


# ================================================================= B6 where octal and hex appear
def b6():
    t = head('where you meet octal and hex', 'Beyond syllabus',
             '"Why learn hex?" The printed book says hex and octal are short forms of binary; here is where people actually use them.')
    r, g, b = 0xC5, 0x5A, 0x11
    t += f'''## 1. Colours on screens and web pages

A colour is written **#RRGGBB**: two hex digits each for red, green and blue, each from 00 (none) to FF (255, full).
This book's orange is **#C55A11**: red C5 = {r}, green 5A = {g}, blue 11 = {b}.

| Colour | Hex | Red, green, blue |
|---|:-:|:-:|
| black | #000000 | 0, 0, 0 |
| white | #FFFFFF | 255, 255, 255 |
| pure red | #FF0000 | 255, 0, 0 |
| this book's orange | #C55A11 | {r}, {g}, {b} |
| saffron of the national flag (often given as) | #FF9933 | 255, 153, 51 |

Each colour uses 3 bytes = 24 bits, so a screen can show 2²⁴ = {2 ** 24:,} colours.

## 2. File permissions in octal

On Linux and Android, who may read (r = 4), write (w = 2) and run (x = 1) a file is written as three octal digits, for the
owner, the group and everyone else. **755** means rwx r-x r-x: 7 = 4 + 2 + 1 for the owner, 5 = 4 + 1 for the others.
Each octal digit is exactly 3 bits: one bit for each permission. That is why octal is used here.

| Octal | Bits | Permission |
|:-:|:-:|:-:|
'''
    for d in range(8):
        bits = format(d, '03b')
        perm = ''.join(c if bit == '1' else '-' for c, bit in zip('rwx', bits))
        t += f'| {d} | {bits} | {perm} |\n'
    t += '''
## 3. Memory addresses and network addresses

- Memory addresses are shown in hex (0x7FFE…): 64 bits become 16 hex digits instead of 64 bits.
- A network card's **MAC address** is 48 bits written as 6 pairs of hex digits, such as 3C:52:82:1A:7F:09.
- **IPv6** internet addresses are 128 bits, written as 8 groups of 4 hex digits.

## 4. Unicode charts

Every code point is written in hex (U+20B9), because the blocks start at round hex numbers (U+0900) and the charts are
laid out in rows of 16.
'''
    ok(int('C5', 16) == r and int('5A', 16) == g and 0xFF9933 == (255 << 16) + (153 << 8) + 51)
    write('beyond-where-octal-and-hex.md', t)


# ================================================================= B7 history
def b7():
    t = head('number systems in history, and in India', 'Beyond syllabus',
             'For the curious reader and the teacher: where the ideas of this chapter came from.')
    t += '''## 1. Place value and zero in India

- The Indian way of writing numbers, with **ten digits whose worth depends on their place** and a sign for an empty
  place, developed in India in the first centuries CE.
- **Brahmagupta**, in the *Brahmasphutasiddhanta* (628 CE), gave rules for calculating with zero as a number: a number
  plus zero is the number; a number times zero is zero.
- The system travelled to the Arab world and then to Europe, which is why the digits are called **Hindu–Arabic numerals**.

## 2. Pingala and patterns of two kinds

**Pingala's** *Chandaḥśāstra*, a work on the metres of Sanskrit poetry (dated by different scholars between about the
5th and the 2nd century BCE), lists every pattern of **light (laghu)** and **heavy (guru)** syllables for a line of a given
length, in a fixed order, and gives a method to find a pattern's place in the list. Scholars have pointed out that this
listing works like counting in binary, with light and heavy in place of 0 and 1. Pingala did not write numbers in binary;
the likeness is in the method.

## 3. Binary in Europe

**Gottfried Leibniz** described binary arithmetic in a paper of 1703. Binary became central to computing in the 20th
century, when **Claude Shannon** (1937) showed that switching circuits could do Boolean logic (Chapter 3).

## 4. Other bases still with us

| Base | Where | Why |
|:-:|---|---|
| 60 | 60 seconds in a minute, 60 minutes in an hour; 360° in a circle | from ancient Mesopotamia; 60 divides by 2, 3, 4, 5, 6 |
| 12 | a dozen; 12 inches in a foot | 12 divides by 2, 3, 4, 6 |
| 20 | a "score" (English); counting on fingers and toes in some cultures | |

## 5. Lakh and crore

The Indian way of grouping digits (1,00,00,000 = one crore) is a different way of **reading** a decimal number, not a
different base: the places are the same powers of 10, only the commas are placed differently (in twos after the
thousands).
'''
    write('beyond-history-and-india.md', t)


# ================================================================= C1 puzzles
def c1():
    t = head('puzzles with bases', 'Challenge', 'For students who like a puzzle. Each answer is below its question; try first.')
    qs = []
    # find the base
    for s, v in [('121', 49), ('144', 81), ('1000', 343)]:
        b = next(b for b in range(2, 17) if nb.valid(s, b) and nb.value(s, b) == v)
        qs.append((f'In which base b does "{s}" mean {v}?', f'b = {b}. *Why:* {s} in base {b} = ' +
                   ' + '.join(f'{nb.digit_value(d)} × {b}^{len(s) - 1 - i}' for i, d in enumerate(s)) + f' = {v}.'))
    qs.append(('Which is the largest: (777)₈, (1FF)₁₆, (111111111)₂?',
               f'All are 511! (777)₈ = {nb.value("777", 8)}, (1FF)₁₆ = {nb.value("1FF", 16)}, (111111111)₂ = {nb.value("111111111", 2)}. '
               '*Why:* each is "all top digits", and 8³ = 2⁹ = 512, and 1FF = 1 0000 0000 − 1 in binary terms.'))
    ok(nb.value('777', 8) == nb.value('1FF', 16) == nb.value('111111111', 2) == 511)
    qs.append(('With four weights of 1, 3, 9 and 27 kg on a balance (a weight may go on either pan), every whole number of '
               'kilograms from 1 to 40 can be weighed. Why 40, and why these weights?',
               '1 + 3 + 9 + 27 = 40. Each weight can be on the left pan, the right pan, or off: three choices, like the digits '
               '−1, 0, 1 of a base-3 system ("balanced ternary"). For example 5 = 9 − 3 − 1: 9 with the load on one side, 3 and 1 '
               'with the load on the other.'))
    qs.append(('A number is 2-digit in decimal and 7-digit in binary. Which numbers can it be?',
               'Seven bits cover 64 to 127; two decimal digits cover 10 to 99. So **64 to 99**.'))
    ok(all(len(nb.to_base(x, 2)) == 7 for x in range(64, 100)))
    qs.append(('Why does every odd number end in 1 in binary, and why does a multiple of 8 end in 000?',
               'The last bit is the units place; odd means one unit is left over. A multiple of 8 = 2³ has nothing in the 1, 2 '
               'and 4 places, so its last three bits are 0 (just as a multiple of 1000 ends in 000 in decimal).'))
    qs.append(('Without converting to decimal, is (3A7)₁₆ even or odd?',
               'Odd. *Why:* 16 is even, so only the last digit decides; 7 is odd.'))
    ok(nb.value('3A7', 16) % 2 == 1)
    qs.append(('How many digits does 2¹⁰⁰ have in binary, octal and hexadecimal?',
               '2¹⁰⁰ is 1 followed by 100 zeros in binary: **101 bits**. 100 = 3 × 33 + 1, so in octal it is 2 followed by 33 '
               'zeros: **34 digits**. 100 = 4 × 25, so in hex it is 1 followed by 25 zeros: **26 digits**.'))
    ok(len(nb.to_base(2 ** 100, 2)) == 101 and len(nb.to_base(2 ** 100, 8)) == 34 and len(nb.to_base(2 ** 100, 16)) == 26)
    t += '\n'.join(f'**Q{i}.** {q}\n\n**Answer.** {a}\n' for i, (q, a) in enumerate(qs, 1))
    write('challenge-puzzles-with-bases.md', t)


# ================================================================= C2 mind-reading cards
def c2():
    t = head('the binary mind-reading cards', 'Challenge',
             'A classroom trick that is binary in disguise. Print the six cards, try it on a friend, then explain how it works.')
    for k in range(6):
        w = 2 ** k
        nums = [n for n in range(1, 64) if n & w]
        ok(nums[0] == w and len(nums) == 32)
        rows = [nums[i:i + 8] for i in range(0, 32, 8)]
        t += f'**Card {k + 1}** (first number {w})\n\n| | | | | | | | |\n|---|---|---|---|---|---|---|---|\n'
        t += '\n'.join('| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows) + '\n\n'
    t += '''## How to do the trick

1. Ask a friend to think of a number from 1 to 63.
2. Show the six cards; the friend says only "yes" or "no": is the number on this card?
3. Add the **first numbers** of the "yes" cards. That is the number.

## Why it works

Card 1 has every number whose **1s bit** is 1; card 2 every number whose **2s bit** is 1; card 3 the **4s bit**; and so on
up to 32. The friend's yes/no answers are the bits of the number, and adding the first numbers adds the place values of
the 1 bits: the cake trays of the printed book. For 45 = 32 + 8 + 4 + 1: yes, no, yes, yes, no, yes (cards 1 to 6).
'''
    ok(45 == 32 + 8 + 4 + 1)
    write('challenge-mind-reading-cards.md', t)


# ================================================================= B4 floating point
def b4():
    import struct
    from decimal import Decimal
    t = head('why 0.1 + 0.2 is not 0.3 in Python', 'Beyond syllabus',
             "The printed book shows that 0.1 repeats for ever in binary (section 4.4); this page shows what that does to a computer's arithmetic. Useful again in Chapter 7 (data types).")
    s = 0.1 + 0.2
    ok(repr(s) == '0.30000000000000004' and s != 0.3 and round(s, 2) == 0.3)
    exact = str(Decimal(0.1))
    ok(exact.startswith('0.1000000000000000055511151231257827'))
    d = format(struct.unpack('>Q', struct.pack('>d', 0.1))[0], '064b')
    f = format(struct.unpack('>I', struct.pack('>f', 0.1))[0], '032b')
    ok(d[1:12] == '01111111011' and f[1:9] == '01111011')
    digits = ''
    fr = Fraction(1, 10)
    for _ in range(12):
        p_ = fr * 2
        digits += str(int(p_))
        fr = p_ - int(p_)
    ok(digits == '000110011001')
    t += f"""## 1. The surprise

Type this in Python (Chapter 6 onward):

```python
>>> 0.1 + 0.2
{s!r}
>>> 0.1 + 0.2 == 0.3
False
```

Python is not broken. The reason is in section 4.4 of the book.

## 2. The reason: 0.1 never ends in binary

Multiply by 2 again and again (the book's method): 0.1 → 0.{digits}… The block **0011** repeats for ever, because the
denominator of 1/10 has the factor 5 (see "Why the methods work"). A computer has only a fixed number of bits, so it must
**cut 0.1 off**, and the number it stores is very slightly different from 0.1:

> 0.1 is stored as **{exact}**

The same happens to 0.2 and to 0.3. When the slightly-wrong 0.1 and 0.2 are added, the tiny errors add up to a number
that is not the stored 0.3; Python shows it as {s!r}.

## 3. How a computer stores numbers with a point

Like scientific notation (6.02 × 10²³), but in binary: a **sign**, a **fraction** (the significant bits) and an
**exponent** (where the point goes). This is the international standard **IEEE 754**. Python's `float` uses 64 bits:

| Part | Bits | 0.1 in Python |
|---|:-:|---|
| sign | 1 | {d[0]} (positive) |
| exponent | 11 | {d[1:12]} |
| fraction | 52 | {d[12:]} |

Look at the fraction: **1001 1001 1001 …**, the repeating pattern of 0.1, cut off after 52 bits (the last bits are
rounded). A shorter 32-bit version (single precision) has 1 + 8 + 23 bits: {f[0]} {f[1:9]} {f[9:]}.

## 4. What to do about it in Python

| Need | Use | Example |
|---|---|---|
| show a few decimal places | `round(x, n)` | `round(0.1 + 0.2, 2)` gives 0.3 |
| compare two floats | `math.isclose(a, b)` | `math.isclose(0.1 + 0.2, 0.3)` gives True |
| exact money (rupees and paise) | whole paise, or the `decimal` module | store ₹10.50 as 1050 paise |
| exact fractions | the `fractions` module | `Fraction(1, 10)` |

**Rule of thumb:** never test two floats with `==`; never store money as a float.

## 5. Questions

**Q1.** Why can 0.5 + 0.25 be stored exactly, but not 0.1 + 0.2?

**Answer.** 0.5 = ½ and 0.25 = ¼ have denominators that are powers of 2, so they end in binary ((0.1)₂ and (0.01)₂);
0.1 and 0.2 have the factor 5 in their denominators and repeat for ever, so they are cut off.

**Q2.** Will `0.75 + 0.125 == 0.875` be True in Python?

**Answer.** True: all three end in binary (3/4, 1/8, 7/8), so they are stored exactly.
"""
    import math
    ok(0.75 + 0.125 == 0.875 and 0.5 + 0.25 == 0.75 and math.isclose(0.1 + 0.2, 0.3))
    write('beyond-floating-point.md', t)


# ================================================================= B5 joining characters
def mark(c):
    return c if unicodedata.category(c).startswith('L') else '◌' + c


def b5():
    t = head('characters that join: why नमस्ते is 6 code points', 'Beyond syllabus',
             'The printed book counts नमस्ते as 6 code points (question 24); this page explains why. Useful again in Chapter 11 (strings).')
    w = 'नमस्ते'
    ok(len(w) == 6 and len(w.encode('utf-8')) == 18)
    t += """## 1. What you see and what is stored

On the screen नमस्ते looks like three letters: न, म, स्ते. In the computer it is **six code points**:

| # | Character | Code point | Name | Bytes in UTF-8 |
|:-:|:-:|:-:|---|:-:|
"""
    for i, c in enumerate(w, 1):
        t += f'| {i} | {mark(c)} | U+{ord(c):04X} | {unicodedata.name(c).lower()} | {len(c.encode("utf-8"))} |\n'
    t += f"""
- **्** (the halant, or virama) is a character of its own: it removes the vowel of the letter before it and joins it to
  the next letter, so स + ् + त is drawn as स्त.
- **े** (the vowel sign e) is also a character of its own; the font draws it on top of त.
- The **font** decides how the joined shapes look. The text stores only the code points, in the order they are spoken.

So in Python `len('{w}')` gives **{len(w)}**, and the word takes **{len(w.encode('utf-8'))} bytes** in UTF-8 (6 × 3).

## 2. More joined letters

| What you see | Code points | How many | UTF-8 bytes |
|:-:|---|:-:|:-:|
"""
    for s in ['क्ष', 'त्र', 'ज्ञ', 'श्री', 'कि']:
        ok(all('ऀ' <= c <= 'ॿ' for c in s))
        t += f'| {s} | ' + ' + '.join(f'{mark(c)} (U+{ord(c):04X})' for c in s) + f' | {len(s)} | {len(s.encode("utf-8"))} |\n'
    fam = '\U0001F468‍\U0001F469‍\U0001F467'
    flag = '\U0001F1EE\U0001F1F3'
    ok(len(fam) == 5 and len(fam.encode('utf-8')) == 18 and len(flag) == 2 and len(flag.encode('utf-8')) == 8)
    t += f"""
In **कि** the vowel sign ि is drawn **before** क, but it is stored **after** it: the stored order is the spoken order.

## 3. Emojis join too

| What you see | Stored as | Code points | UTF-8 bytes |
|:-:|---|:-:|:-:|
| {fam} (a family) | man + zero-width joiner + woman + zero-width joiner + girl | {len(fam)} | {len(fam.encode('utf-8'))} |
| {flag} (the flag of India) | regional indicator I + regional indicator N | {len(flag)} | {len(flag.encode('utf-8'))} |

The **zero-width joiner** (U+200D) is an invisible character that asks the phone to draw its two neighbours as one
picture. A phone that does not know the joined picture shows the separate emojis instead.

## 4. Why it matters

- **Counting:** "how many letters?" has two answers: the code points (what `len()` counts) and what a reader sees as
  one letter (called a *grapheme*).
- **Storage:** a short Hindi word can take many bytes (नमस्ते: 18 bytes in UTF-8, 24 in UTF-32).
- **Cutting text:** cutting a string after 3 code points gives {w[:3]}, which reads differently: never cut in the middle
  of a joined letter.

## 5. Questions

**Q1.** How many code points and how many UTF-8 bytes does "क्षमा" have?

**Answer.** {len('क्षमा')} code points (क, ्, ष, म, ा) and {len('क्षमा'.encode('utf-8'))} bytes (5 × 3).

**Q2.** Why does the vowel sign of कि come after क in memory, though it is drawn before it?

**Answer.** Unicode stores characters in the order they are spoken (k, then i); the font draws ि on the left.
"""
    ok(len('क्षमा') == 5 and len('क्षमा'.encode('utf-8')) == 15 and len(w.encode('utf-32-le')) == 24)
    write('beyond-joining-characters.md', t)


if __name__ == '__main__':
    h4(); h5(); h6(); s1(); s2(); s3(); s4(); s5(); s6(); s7(); b1(); b2(); b3(); b6(); b7(); c1(); c2(); b4(); b5()
    print(f'{checks} checks passed')
