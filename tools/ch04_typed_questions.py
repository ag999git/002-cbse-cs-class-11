"""Chapter 4 online question pages 01-12 (26 Nov 2026; plan ch04-online-plan-v1, approved: about 320 questions).
Every question is followed by its answer and the reason. Every number in every answer is computed here by
numbase_lib.py or by Python's encoders and checked before a page is written. Numbers used in the printed chapter are
not reused (the printed questions are not repeated online).

Run from the repository root:  python tools/ch04_typed_questions.py"""
import random
import sys
import unicodedata
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numbase_lib as nb  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
QD = ROOT / 'book' / 'unit-1' / '004-ch04-number-systems-and-encoding' / 'questions'
QD.mkdir(parents=True, exist_ok=True)
S = '₀₁₂₃₄₅₆₇₈₉'
NAME = {2: 'binary', 8: 'octal', 10: 'decimal', 16: 'hexadecimal'}
R = random.Random(4)
checks = 0
# numbers that appear in the printed chapter (v4): not reused here
PRINTED = {65, 156, 214, 45, 57, 237, 157, 500, 102, 249, 185, 181, 22, 25, 100, 13, 91, 175, 933, 47, 29, 83, 150, 255,
           99, 400, 1000, 690, 4096, 43, 236, 87, 1039, 2989, 750, 300, 12, 9, 53, 55}


def sub(n):
    return ''.join(S[int(c)] for c in str(n))


def num(s, b):
    return f'({s}){sub(b)}'


def ok(c, m=''):
    global checks
    assert c, m
    checks += 1


def conv(s, a, b, maxf=8):
    r = nb.convert(str(s), a, b, max_frac=maxf)
    if '.' not in str(s) or nb.value(r, b) == nb.value(str(s), a):
        ok(nb.value(r, b) == nb.value(str(s), a), (s, a, b, r))
    return r


def fresh(lo, hi):
    while True:
        n = R.randint(lo, hi)
        if n not in PRINTED:
            PRINTED.add(n)
            return n


# ------------------------------------------------------------------ workings
def div_work(n, b):
    rows = nb.div_ladder(n, b)
    rems = ', '.join(nb.DIGITS[r] + (f' ({r})' if r > 9 else '') for _, _, r in rows)
    res = nb.to_base(n, b)
    ok(nb.value(res, b) == n)
    return f'{n} ÷ {b} again and again: remainders {rems}; read upward → {num(res, b)}', res


def pv_work(s, b):
    terms = nb.place_terms(s, b)
    parts = []
    for c, dv, pos, wt in terms:
        if dv == 0:
            continue
        w = wt if wt.denominator == 1 else f'1/{wt.denominator}'
        parts.append(f'{dv} × {w}' if dv != 1 else f'{w}')
    v = nb.value(s, b)
    vs = str(v) if v.denominator == 1 else f'{float(v):g}'
    return ' + '.join(parts) + f' = {vs}', vs


def grp_work(bits, b):
    k = 3 if b == 8 else 4
    gw, gf, res = nb.bin_to(bits, b)
    ok(nb.value(res, b) == nb.value(bits, 2))
    g = ' '.join(gw) + (' . ' + ' '.join(gf) if gf else '')
    return f'groups of {k} from the point: {g} → {num(res, b)}', res


def bits_work(s, b):
    pairs, res = nb.to_bin_by_digit(s, b)
    ok(nb.value(res, 2) == nb.value(s, b))
    return ', '.join('.' if d == '.' else f'{d} → {p}' for d, p in pairs).replace(', ., ', ' . ') + f' → {num(res, 2)}', res


def frac_work(f, b, places=6):
    rows, why = nb.mul_ladder(Fraction(f), b, max_steps=places)
    steps = '; '.join(f'{float(fr):g} × {b} = {float(p):g} → {nb.DIGITS[d]}' for fr, p, d, nf in rows)
    digits = ''.join(nb.DIGITS[r[2]] for r in rows)
    if why == 'repeats':
        # the ladder stopped when a fraction came back: continue the same digits to the places asked
        start = next(i for i, r in enumerate(rows) if r[0] == rows[-1][3])
        cyc = digits[start:]
        while len(digits) < places:
            digits += cyc[(len(digits) - start) % len(cyc)]
        digits = digits[:places]
        ok(abs(float(nb.value('0.' + digits, b)) - float(Fraction(f))) < b ** -places, (f, digits))
        steps += f'; {float(rows[-1][3]):g} came back, so the digits {cyc} repeat'
    return steps, digits, why


# ------------------------------------------------------------------ page writer
def page(fname, title, intro, sections):
    n = sum(len(qs) for _, qs in sections)
    out = [f'# Chapter 4: Number Systems and Encoding Schemes: {title} ({n})\n',
           f'*Chapter 4 · Questions (online). {intro} Try each one first. The difficulty (E easy, M medium, H hard) and the '
           'section of the book are given in brackets. Every number on this page was computed and checked by a program '
           '(`tools/ch04_typed_questions.py`).*\n']
    k = 0
    for head, qs in sections:
        out.append(f'## {head}\n')
        for q, a, tag in qs:
            k += 1
            out.append(f'**Q{k}.** {q} *({tag})*\n\n**Answer.** {a}\n')
    (QD / fname).write_text('\n'.join(out), encoding='utf-8')
    print(f'wrote {fname}: {n}')
    return n


# ================================================================== 01 MCQ
def mcq():
    hand = [
        ('The base of the octal system is: (a) 2 (b) 8 (c) 10 (d) 16', '(b) 8. *Why:* octo = eight; digits 0 to 7.', 'E · 4.1'),
        ('Which symbol is NOT a hexadecimal digit? (a) A (b) F (c) G (d) 9', '(c) G. *Why:* hex stops at F (fifteen).', 'E · 4.1'),
        ('How many digits does the decimal system have? (a) 9 (b) 10 (c) 11 (d) 8', '(b) 10: 0 to 9.', 'E · 4.1'),
        ('A computer works in binary because: (a) binary is the oldest system (b) a switch has two states (c) binary numbers are short (d) people find binary easy',
         '(b). *Why:* telling two states apart is easy and safe; binary numbers are in fact long, not short.', 'E · 4.1'),
        ('Hexadecimal is used by people mainly because it: (a) is a short form of binary (b) has letters (c) is faster for the CPU (d) is the base of ASCII',
         '(a). *Why:* one hex digit stands for 4 bits; the CPU itself works in binary.', 'E · 4.1'),
        ('In 7345, the place value of 3 is: (a) 3 (b) 30 (c) 300 (d) 3000', '(c) 300. *Why:* 3 is in the hundreds place.', 'E · 4.2'),
        ('The weight of the leftmost bit of a 6-bit binary number is: (a) 6 (b) 32 (c) 64 (d) 16',
         '(b) 32. *Why:* positions run 5, 4, … 0, and 2⁵ = 32.', 'M · 4.2'),
        ('The LSB of a binary number is the bit: (a) on the left (b) on the right (c) in the middle (d) with the largest value',
         '(b) on the right: it has the smallest place value.', 'E · 4.2'),
        ('What comes after (77)₈? (a) (78)₈ (b) (80)₈ (c) (100)₈ (d) (88)₈',
         '(c) (100)₈. *Why:* both digits are at the top (7), so both roll over and carry.', 'M · 4.2'),
        ('What comes after (1F)₁₆? (a) (20)₁₆ (b) (1G)₁₆ (c) (110)₁₆ (d) (2F)₁₆', '(a) (20)₁₆. *Why:* F rolls over to 0 and carries 1 into the 16s place.', 'M · 4.2'),
        ('To convert decimal to binary we: (a) multiply by 2 (b) divide by 2 and read the remainders upward (c) divide by 2 and read the remainders downward (d) group in 3s',
         '(b). *Why:* the first remainder is the units digit, so it comes last.', 'E · 4.3'),
        ('Binary is converted to hexadecimal by grouping bits in: (a) 2s (b) 3s (c) 4s (d) 8s', '(c) 4s. *Why:* 16 = 2⁴.', 'E · 4.3'),
        ('The best way to convert octal to hexadecimal is: (a) directly (b) through binary (c) through ASCII (d) it cannot be done',
         '(b) through binary: each octal digit to 3 bits, then regroup in 4s.', 'E · 4.3'),
        ('When a whole binary number is grouped, extra 0s are added: (a) on the right (b) on the left (c) in the middle (d) anywhere',
         '(b) on the left: a 0 on the left adds nothing; on the right it would double the number.', 'M · 4.3'),
        ('When converting a decimal fraction to binary, we: (a) divide by 2 (b) multiply by 2 and read the whole parts downward (c) multiply by 2 and read upward (d) group in 4s',
         '(b). *Why:* the first digit found is the one nearest the point.', 'E · 4.4'),
        ('Which decimal fraction has an exact binary form? (a) 0.1 (b) 0.2 (c) 0.75 (d) 0.3',
         '(c) 0.75 = 3/4. *Why:* its denominator is a power of 2.', 'M · 4.4'),
        ('ASCII stands for: (a) American Standard Code for Information Interchange (b) American Scientific Code for Information Interchange (c) Advanced Standard Code for Internet Interchange (d) American Standard Computer Information Index',
         '(a).', 'E · 4.5'),
        ('How many characters can 8-bit ISCII represent? (a) 128 (b) 255 (c) 256 (d) 512', '(c) 256 = 2⁸, numbered 0 to 255.', 'E · 4.5'),
        ("The ASCII code of the space character is: (a) 0 (b) 20 (c) 32 (d) 48", '(c) 32. *Why:* the first printable code; 0 is NUL.', 'M · 4.5'),
        ('Unicode code points are usually written in: (a) binary (b) octal (c) decimal (d) hexadecimal, after U+', '(d), for example U+0905 for अ.', 'E · 4.5'),
        ('In UTF-8, an English letter takes: (a) 1 byte (b) 2 bytes (c) 3 bytes (d) 4 bytes', '(a) 1 byte, the same as in ASCII.', 'E · 4.5'),
        ('Which encoding is used by almost all web pages? (a) ASCII (b) ISCII (c) UTF-8 (d) UTF-32', '(c) UTF-8.', 'E · 4.5'),
    ]
    gen = []
    for _ in range(5):
        n = fresh(40, 250)
        right = nb.to_base(n, 2)
        rev = right[::-1]
        wrong = [rev if rev != right else right + '0', nb.to_base(n + 1, 2), nb.to_base(n - 2, 2)]
        opts = [right] + wrong
        R.shuffle(opts)
        L = 'abcd'[opts.index(right)]
        gen.append((f'{num(n, 10)} in binary is: ' + ' '.join(f'({l}) {num(o, 2)}' for l, o in zip('abcd', opts)),
                    f'({L}) {num(right, 2)}. *Why:* {div_work(n, 2)[0]}.', 'E · 4.3'))
    for _ in range(4):
        s = nb.to_base(fresh(300, 3000), 16)
        v = nb.value(s, 16)
        opts = [int(v), int(v) + 16, int(nb.value(s[::-1], 16)), int(v) - 1]
        opts = list(dict.fromkeys(opts))
        while len(opts) < 4:
            opts.append(opts[-1] + 3)
        R.shuffle(opts)
        gen.append((f'{num(s, 16)} in decimal is: ' + ' '.join(f'({l}) {o}' for l, o in zip('abcd', opts)),
                    f'({"abcd"[opts.index(int(v))]}) {v}. *Why:* {pv_work(s, 16)[0]}.', 'M · 4.3'))
    for _ in range(5):
        bits = nb.to_base(fresh(64, 1000), 2)
        right = grp_work(bits, 8)[1]
        left_grp = ''.join(nb.DIGITS[int(bits[i:i + 3].ljust(3, '0'), 2)] for i in range(0, len(bits), 3))
        opts = list(dict.fromkeys([right, left_grp, nb.to_base(int(nb.value(right, 8)) + 1, 8), right[::-1]]))
        while len(opts) < 4:
            opts.append(nb.to_base(int(nb.value(opts[-1], 8)) + 2, 8))
        R.shuffle(opts)
        gen.append((f'{num(bits, 2)} in octal is: ' + ' '.join(f'({l}) {num(o, 8)}' for l, o in zip('abcd', opts)),
                    f'({"abcd"[opts.index(right)]}) {num(right, 8)}. *Why:* {grp_work(bits, 8)[0]}. *Trap:* grouping from the left gives {num(left_grp, 8)}.',
                    'M · 4.3'))
    for ch in ['G', 'k', '9', 'Z']:
        c = ord(ch)
        opts = list(dict.fromkeys([c, c + 32 if c < 97 else c - 32, int(ch) if ch.isdigit() else c + 1, c - 1]))
        R.shuffle(opts)
        why = {'G': "A is 65, G is the 7th letter: 65 + 6", 'k': "a is 97, k is the 11th letter: 97 + 10",
               '9': "'0' is 48: 48 + 9", 'Z': "A is 65, Z the 26th letter: 65 + 25"}[ch]
        gen.append((f"The ASCII code of '{ch}' is: " + ' '.join(f'({l}) {o}' for l, o in zip('abcd', opts)),
                    f'({"abcd"[opts.index(c)]}) {c}. *Why:* {why}.', 'E · 4.5'))
    return page('01-mcq.md', 'Multiple-choice questions', 'One mark each.',
                [('Concepts', hand), ('Working it out', gen)])


# ================================================================== 02 fill in
def fill():
    hand = [
        ('The number of digits in a number system is called its ______ or radix.', 'base.', 'E · 4.1'),
        ('The largest digit of base 7 would be ______.', '6. *Why:* base b has digits 0 to b − 1.', 'M · 4.1'),
        ('In hexadecimal, the digit E stands for the decimal value ______.', '14.', 'E · 4.1'),
        ('One hexadecimal digit stands for ______ bits.', '4.', 'E · 4.1'),
        ('The bit with the largest place value is called the ______.', 'MSB (most significant bit).', 'E · 4.2'),
        ('(10)₈ is equal to ______ in decimal.', '8. *Why:* "10" in any base is the base itself.', 'E · 4.2'),
        ('The place value of the position −2 in binary is ______.', '¼ = 0.25 (2⁻²).', 'M · 4.2'),
        ('With 6 bits, the largest number is ______.', '63 = 2⁶ − 1.', 'M · 4.2'),
        ('In the division method the remainders are read from ______ to ______.', 'bottom, top.', 'E · 4.3'),
        ('To convert octal to hexadecimal, we first convert to ______.', 'binary.', 'E · 4.3'),
        ('When grouping the fraction part, extra 0s are added on the ______.', 'right (at the far end of the fraction).', 'M · 4.3'),
        ('In the multiplication method for fractions, the whole-number parts are read from ______ to ______.', 'top, bottom.', 'E · 4.4'),
        ('ISCII stands for Indian Script Code for ______ Interchange.', 'Information.', 'E · 4.5'),
        ("The ASCII code of 'a' is ______.", '97.', 'E · 4.5'),
        ('Unicode gives each character a unique number called its ______.', 'code point.', 'E · 4.5'),
        ('UTF-32 is a ______-length encoding.', 'fixed (always 4 bytes).', 'E · 4.5'),
        ('The ₹ sign takes ______ bytes in UTF-8.', '3. *Why:* U+20B9 is between U+0800 and U+FFFF.', 'M · 4.5'),
        ('A capital letter and its small letter differ by ______ in ASCII.', '32.', 'E · 4.5'),
    ]
    gen = []
    for _ in range(4):
        n = fresh(20, 200)
        r = nb.to_base(n, 2)
        gen.append((f'{num(n, 10)} = (______)₂', f'{r}. *Why:* {div_work(n, 2)[0]}.', 'E · 4.3'))
    for _ in range(3):
        s = nb.to_base(fresh(64, 511), 8)
        gen.append((f'{num(s, 8)} = (______)₁₀', f'{nb.value(s, 8)}. *Why:* {pv_work(s, 8)[0]}.', 'E · 4.3'))
    for _ in range(3):
        bits = nb.to_base(fresh(256, 4000), 2)
        r = grp_work(bits, 16)[1]
        gen.append((f'{num(bits, 2)} = (______)₁₆', f'{r}. *Why:* {grp_work(bits, 16)[0]}.', 'E · 4.3'))
    for w in ['GOA', 'Pune']:
        codes = ' '.join(str(ord(c)) for c in w)
        gen.append((f'The ASCII codes of "{w}" are ______.', f'{codes}.', 'E · 4.5'))
    return page('02-fill-in.md', 'Fill in the blanks', 'One mark each.', [('Concepts', hand), ('Working it out', gen)])


# ================================================================== 03 true or false
def tf():
    hand = [
        ('Hexadecimal has 16 digits.', 'True: 0 to 9 and A to F.', 'E · 4.1'),
        ('A computer stores pictures as numbers.', 'True: everything is stored as numbers in binary.', 'E · 4.1'),
        ('(100)₂ is greater than (100)₈.', 'False: (100)₂ = 4 and (100)₈ = 64.', 'E · 4.2'),
        ('The digit 8 can appear in an octal number.', 'False: octal digits are 0 to 7.', 'E · 4.2'),
        ('Adding a 0 on the right of a binary number doubles it.', 'True: every bit moves one place left.', 'M · 4.2'),
        ('The MSB of a binary number is the rightmost bit.', 'False: the MSB is the leftmost bit.', 'E · 4.2'),
        ('In the division method, the first remainder is the most significant digit.', 'False: it is the least significant (units) digit.', 'M · 4.3'),
        ('Octal to hexadecimal is best done through binary.', 'True.', 'E · 4.3'),
        ('Every decimal fraction can be written exactly in binary.', 'False: 0.1, 0.2, 0.3 repeat for ever.', 'M · 4.4'),
        ('0.5 is (0.1)₂.', 'True: the first place after the binary point is worth ½.', 'E · 4.4'),
        ('ASCII can represent Hindi letters.', 'False: ASCII has only 128 codes, for English.', 'E · 4.5'),
        ("The ASCII code of '0' is 0.", "False: it is 48; code 0 is NUL, which prints nothing.", 'M · 4.5'),
        ('ISCII uses 8 bits.', 'True: 256 codes.', 'E · 4.5'),
        ('Unicode includes all the ASCII characters with the same numbers.', 'True: U+0000 to U+007F.', 'E · 4.5'),
        ('In UTF-8 every character takes the same number of bytes.', 'False: 1 to 4 bytes; that is UTF-32 (always 4).', 'E · 4.5'),
        ('The emoji 😀 takes 4 bytes in UTF-8.', 'True: it is U+1F600, above U+FFFF (most emojis are).', 'M · 4.5'),
    ]
    gen = []
    for i in range(14):
        a, b = R.choice([(10, 2), (10, 8), (10, 16), (2, 8), (2, 16), (8, 16)])
        n = fresh(30, 900)
        s = nb.to_base(n, a)
        r = nb.to_base(n, b)
        truth = i % 2 == 0
        shown = r if truth else nb.to_base(n + R.choice([1, 2, b]), b)
        ok((nb.value(shown, b) == n) == truth)
        if truth:
            ans = f'True. *Check:* both are {n} in decimal.'
        else:
            ans = f'False: {num(s, a)} = {num(r, b)}, which is {n}; {num(shown, b)} is {nb.value(shown, b)}.'
        gen.append((f'{num(s, a)} = {num(shown, b)}', ans, 'E · 4.3'))
    return page('03-true-false.md', 'True or false', 'One mark each.', [('Concepts', hand), ('Working it out', gen)])


# ================================================================== 04 assertion and reason
def ar():
    key = 'For each: (a) both true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.'
    qs = [
        ('A: Octal is a short form of binary. R: 8 = 2³.', '(a). One octal digit is exactly 3 bits.', 'E · 4.1'),
        ('A: Hexadecimal uses letters A to F. R: Hexadecimal is used for memory addresses.', '(b). Both true, but letters are used because 16 digits need 6 more symbols.', 'M · 4.1'),
        ('A: (10)₁₆ = 16. R: "10" in any base is the base itself.', '(a).', 'E · 4.2'),
        ('A: (1001)₂ is odd. R: The LSB of every odd number is 1.', '(a).', 'E · 4.2'),
        ('A: (19)₈ is a valid octal number. R: Octal digits go from 0 to 7.', '(d). 9 is not an octal digit, so A is false.', 'E · 4.2'),
        ('A: In the division method the remainders are read upward. R: The first remainder is the units digit.', '(a).', 'E · 4.3'),
        ('A: Octal can be converted to hexadecimal through binary. R: Both 8 and 16 are powers of 2.', '(a).', 'M · 4.3'),
        ('A: A whole binary number is padded with 0s on the left. R: A 0 on the left of a whole number adds nothing.', '(a).', 'M · 4.3'),
        ('A: 0.1 cannot be written exactly in binary. R: The denominator of 1/10 has the factor 5.', '(a). Only fractions whose denominator is a power of 2 end in binary.', 'H · 4.4'),
        ('A: ASCII uses 7 bits. R: ASCII was made for Indian languages.', '(c). ASCII was made for English.', 'E · 4.5'),
        ("A: The ASCII code of 'b' is 98. R: Small letters are 32 more than capitals.", "(b). Both true; 98 comes from 'a' = 97 + 1, and 'B' = 66 + 32 = 98 also works, so R does explain it partly. *Note:* most keys accept (a); the safer reading is (a).", 'M · 4.5'),
        ('A: ISCII codes 0 to 127 are the same as ASCII. R: ISCII was designed to keep English text unchanged.', '(a).', 'E · 4.5'),
        ('A: UTF-32 wastes space for English text. R: UTF-32 uses 4 bytes for every character.', '(a).', 'E · 4.5'),
        ('A: UTF-8 is used by most web pages. R: UTF-8 is a fixed-length encoding.', '(c). UTF-8 is variable-length.', 'E · 4.5'),
        ('A: In UTF-32 the 100th character can be found directly. R: All characters have the same size in UTF-32.', '(a). It starts at byte 99 × 4 = 396.', 'M · 4.5'),
    ]
    ok(ord('b') == 98 and ord('B') + 32 == 98)
    # Q11 wording simplified to a clean (a)
    qs[10] = ("A: The ASCII code of 'b' is 98. R: A small letter's code is 32 more than its capital's, and 'B' is 66.", '(a). 66 + 32 = 98.', 'M · 4.5')
    out = page('04-assertion-reason.md', 'Assertion and reason', key + ' One mark each.', [('Assertion and reason', qs)])
    return out


# ================================================================== 05 short answer
def short():
    hand = [
        ('Why does a computer use binary and not decimal?', 'A switch or a wire has two states (on/off, high/low voltage). Two states are easy and safe to tell apart; ten voltage levels would be confused whenever the voltage wobbles.', 'E · 4.1'),
        ('Why do people use octal and hexadecimal if the computer uses binary?', 'Long strings of bits are hard to read and copy; one octal digit stands for 3 bits and one hex digit for 4, so the same value is written in a third or a quarter of the length.', 'E · 4.1'),
        ('What is meant by the base of a number system? Give the base of each of the four systems.', 'The number of digits it uses (also called radix): binary 2, octal 8, decimal 10, hexadecimal 16.', 'E · 4.1'),
        ('Why does hexadecimal need letters?', 'It has 16 digits but we have only ten digit symbols (0–9); six single symbols were needed for ten to fifteen, so A–F are used. "15" would be read as two digits.', 'E · 4.1'),
        ('What is place value? Explain with the number (725)₈.', 'What a digit is worth because of its place: digit × base^position. 7 × 64 + 2 × 8 + 5 × 1 = 448 + 16 + 5 = 469.', 'M · 4.2'),
        ('What are the MSB and the LSB? Name them in (101100)₂.', 'The MSB is the leftmost bit (largest place value, here the 1 worth 32); the LSB is the rightmost bit (here the 0 worth 1).', 'E · 4.2'),
        ('Write the next three numbers after (7)₈ in octal.', '(10)₈, (11)₈, (12)₈. *Why:* after 7 the units place rolls over and carries.', 'E · 4.2'),
        ('Why are the remainders read upward in the division method?', 'The first remainder is the units digit, the last digit of the answer; each later remainder belongs one place further left.', 'M · 4.3'),
        ('Why is grouping by 3 bits allowed for octal?', 'Because 8 = 2³: 3 bits have exactly 8 patterns, one for each octal digit, so each group is exactly one octal digit.', 'M · 4.3'),
        ('Why is octal to hexadecimal done through binary and not directly?', '8 and 16 are not powers of each other, so their digits do not match group to group; both are powers of 2, so binary is the bridge.', 'M · 4.3'),
        ('Why are the digits read downward in the multiplication method for fractions?', 'Multiplying by the base moves the digit nearest the point across it first, so the first digit found is the first after the point.', 'M · 4.4'),
        ('When do you stop multiplying when converting a decimal fraction?', 'When the fraction part becomes 0 (exact), when a fraction part repeats (it goes on for ever), or when the question gives the number of places.', 'M · 4.4'),
        ('What is an encoding scheme? Why is it needed?', 'A table that gives every character a fixed number (code) that everyone agrees on. A computer can store only numbers, and everyone must use the same table so that text moves correctly between computers.', 'E · 4.5'),
        ('Differentiate between ASCII and ISCII (two points).', '| Basis of difference | ASCII | ISCII |\n|---|---|---|\n| Bits, codes | 7 bits, 128 | 8 bits, 256 |\n| Scripts | English only | English + ten Indian scripts |', 'E · 4.5'),
        ('What is a code point? Give the code point of A and of ₹.', 'The unique number Unicode gives a character, written U+ and hex: A = U+0041, ₹ = U+20B9.', 'E · 4.5'),
        ('Give two advantages of UTF-8 over UTF-32.', 'English (ASCII) text takes 1 byte per letter instead of 4; old ASCII files are already valid UTF-8.', 'E · 4.5'),
        ('Give one advantage of UTF-32 over UTF-8.', 'Every character has the same size, so the nth character is found directly (it starts at byte 4 × (n − 1)) and characters are counted as bytes ÷ 4.', 'M · 4.5'),
        ('Why could ASCII not become a world standard?', 'It has only 128 codes, enough for English; the 8-bit extensions filled codes 128–255 differently from maker to maker.', 'M · 4.5'),
    ]
    gen = []
    for _ in range(3):
        n = fresh(100, 999)
        w8, r8 = div_work(n, 8)
        w16, r16 = div_work(n, 16)
        gen.append((f'Convert {num(n, 10)} to octal and hexadecimal. [2]', f'{w8}. {w16}. So {num(n, 10)} = {num(r8, 8)} = {num(r16, 16)}.', 'E · 4.3'))
    for _ in range(3):
        bits = nb.to_base(fresh(200, 2000), 2)
        gen.append((f'Convert {num(bits, 2)} to octal and hexadecimal. [2]', f'{grp_work(bits, 8)[0]}; {grp_work(bits, 16)[0]}.', 'E · 4.3'))
    for _ in range(3):
        s = nb.to_base(fresh(100, 3000), 16)
        w, o = None, conv(s, 16, 8)
        bw, bb = bits_work(s, 16)
        gen.append((f'Convert {num(s, 16)} to octal. [2]', f'To bits: {bw}; regroup in 3s: {grp_work(bb, 8)[0]}.', 'M · 4.3'))
    for f in ['0.6875', '0.40625', '0.15625']:
        steps, digits, why = frac_work(f, 2)
        ok(why == 'zero' and nb.value('0.' + digits, 2) == Fraction(f))
        gen.append((f'Convert {num(f, 10)} to binary. [2]', f'{steps}; fraction now 0, so {num(f, 10)} = {num("0." + digits, 2)}.', 'M · 4.4'))
    return page('05-short-answer.md', 'Short-answer questions (1, 2 and 3 marks)', 'Answers as they should be written in the exam.',
                [('Concepts', hand), ('Conversions', gen)])


# ================================================================== 06 long answer
def long_():
    qs = []
    for _ in range(4):
        n = fresh(300, 2000)
        b2 = div_work(n, 2)
        o = grp_work(b2[1], 8)
        h = grp_work(b2[1], 16)
        back = pv_work(h[1], 16)
        qs.append((f'(i) Convert {num(n, 10)} to binary. (ii) From your answer, write it in octal and hexadecimal without dividing again. (iii) Check the hexadecimal answer by converting it back to decimal. [4]',
                   f'(i) {b2[0]}. (ii) {o[0]}; {h[0]}. (iii) {back[0]}. ✓', 'M · 4.3'))
    for whole, frac in [(23, '0.375'), (41, '0.8125'), (13, '0.6')]:
        b = div_work(whole, 2)
        steps, digits, why = frac_work(frac, 2, places=6)
        tail = ', exact' if why == 'zero' else ' (to 6 places)'
        val = f'{b[1]}.{digits}'
        qs.append((f'Convert {num(f"{whole}{frac[1:]}", 10)} to binary{" (to 6 places if it does not end)" if why != "zero" else ""}, then to octal and hexadecimal. [4]',
                   f'Whole part: {b[0]}. Fraction: {steps}{tail}. So {num(val, 2)}. Octal: {grp_work(val, 8)[0]}. Hex: {grp_work(val, 16)[0]}.', 'H · 4.4'))
    for s, b in [('6357.42', 8), ('A9F.C8', 16)]:
        to = 16 if b == 8 else 8
        bw, bb = bits_work(s, b)
        res = grp_work(bb, to)
        qs.append((f'Convert {num(s, b)} to {NAME[to]}. Show every step. [3]', f'To bits: {bw}. Regroup: {res[0]}.', 'H · 4.3'))
    qs += [
        ('Explain the place-value method of converting a number in base b to decimal. Convert (2B.4)₁₆ to decimal. [3]',
         'Multiply each digit by b to the power of its position (0, 1, 2 … left of the point; −1, −2 … right of it) and add. ' + pv_work('2B.4', 16)[0] + '.', 'M · 4.2'),
        ('What is an encoding scheme? Compare ASCII, ISCII and Unicode in a table (four points). [4]',
         'A table giving each character a fixed number that everyone uses.\n\n| Basis of difference | ASCII | ISCII | Unicode |\n|---|---|---|---|\n| Bits | 7 | 8 | 8 to 32 per unit (UTF-8, UTF-32) |\n| Characters | 128 | 256 | 159,801 (17.0) |\n| Scripts | English | English + ten Indian | every script |\n| First 128 codes | — | same as ASCII | same as ASCII |', 'M · 4.5'),
        ('Explain UTF-8 and UTF-32 with the parking-lot example. Which would you choose for a website, and why? [4]',
         'UTF-8: slots cut to size, 1 to 4 bytes per character; small, but the 100th character is found by counting from the start. UTF-32: every slot bus-size, always 4 bytes; large, but the 100th character starts at byte 396. A website should use UTF-8: English and HTML stay 1 byte per character, old ASCII files work, and every script can still be stored.', 'M · 4.5'),
        ('How many bytes does "भारत 2047" take in UTF-8 and in UTF-32? Show the count. [3]', None, 'H · 4.5'),
        ('Encode the word "Kerala" in ASCII (decimal and 7-bit binary) and find its size in bytes in ASCII, UTF-8 and UTF-32. [4]', None, 'M · 4.5'),
    ]
    s = 'भारत 2047'
    dev = [c for c in s if 'ऀ' <= c <= 'ॿ']
    asc = [c for c in s if ord(c) < 128]
    u8 = len(s.encode('utf-8'))
    ok(u8 == 3 * len(dev) + len(asc))
    qs[-2] = (qs[-2][0], f'Code points: {len(dev)} Devanagari (भ, ा, र, त: the vowel sign ा is a code point of its own) and {len(asc)} ASCII (the space and 2, 0, 4, 7). UTF-8: {len(dev)} × 3 + {len(asc)} × 1 = **{u8} bytes**. UTF-32: {len(s)} × 4 = **{len(s) * 4} bytes**.', qs[-2][2])
    w = 'Kerala'
    rows = ' | '.join(f'{c} {ord(c)} {format(ord(c), "07b")}' for c in w)
    ok(len(w.encode('utf-8')) == 6)
    qs[-1] = (qs[-1][0], f'{rows}. Capital K is 75; the small letters are 32 more than their capitals (e 101, r 114, a 97, l 108). Size: ASCII 6 bytes, UTF-8 6 bytes, UTF-32 24 bytes.', qs[-1][2])
    return page('06-long-answer.md', 'Long-answer questions (3, 4 and 5 marks)', 'Answers with full working, as they should be written in the exam.', [('Long answers', qs)])


# ================================================================== 07 case studies
def cases():
    qs = []
    # 1 the scoreboard
    n = 147
    qs.append(('**Case: the school scoreboard.** A digital scoreboard shows runs in binary lights. The score is 147. (i) Which lights are on? (ii) How many lights are needed for scores up to 300? (iii) Write 147 in hexadecimal for the scorer\'s app.',
               f'(i) {nb.to_base(n, 2)} (128 + 16 + 2 + 1). (ii) 9, because 2⁸ = 256 is too few and 2⁹ = 512 is enough. (iii) {num(nb.to_base(n, 16), 16)}.', 'M · 4.3'))
    ok(nb.value(nb.to_base(n, 2), 2) == 147 and nb.to_base(147, 16) == '93')
    # 2 file permissions
    qs.append(('**Case: file permissions.** On a Linux computer, a teacher gives a file the permission 750 (octal). (i) Write 750 in binary. (ii) Each group of 3 bits is read (r), write (w), run (x) for the owner, the group and others: what may each do? (iii) Why is octal convenient here?',
               '(i) 111 101 000. (ii) owner rwx (read, write, run); group r-x (read, run); others --- (nothing). (iii) Each octal digit is exactly 3 bits, one bit for each permission.', 'M · 4.3'))
    ok(conv('750', 8, 2) == '111101000')
    # 3 colours
    qs.append(('**Case: the school website colour.** The designer chooses the colour #2E8B57. (i) What are the red, green and blue values in decimal? (ii) How many bits does one colour need? (iii) How many colours can be made?',
               f'(i) red 2E = {int("2E", 16)}, green 8B = {int("8B", 16)}, blue 57 = {int("57", 16)}. (ii) 24 bits (3 bytes). (iii) 2²⁴ = 16,777,216.', 'M · 4.3'))
    ok(int('2E', 16) == 46 and int('8B', 16) == 139 and int('57', 16) == 87)
    # 4 message decode
    msg = 'SWACHH'
    codes = ' '.join(str(ord(c)) for c in msg)
    qs.append((f'**Case: a secret note.** Riya sends Arjun the numbers {codes}. (i) Decode them in ASCII. (ii) Write the first code in binary. (iii) How would the note change if every number were 32 more?',
               f'(i) {msg}. (ii) {ord(msg[0])} = {format(ord(msg[0]), "07b")}. (iii) every letter would become small: "{msg.lower()}".', 'E · 4.5'))
    # 5 Hindi SMS
    s = 'नमस्ते भारत'
    u8, u16, u32 = len(s.encode('utf-8')), len(s.encode('utf-16-le')), len(s.encode('utf-32-le'))
    qs.append((f'**Case: a Hindi message.** A phone sends "{s}". It has {len(s)} code points: all Devanagari except one space. (i) How many bytes in UTF-8? (ii) In UTF-32? (iii) Which should the app use, and why?',
               f'(i) {len(s) - 1} × 3 + 1 = **{u8} bytes**. (ii) {len(s)} × 4 = **{u32} bytes**. (iii) UTF-8: smaller here, used by the web, and the same app can send English cheaply.', 'M · 4.5'))
    ok(u8 == (len(s) - 1) * 3 + 1)
    # 6 garbled
    qs.append(('**Case: garbled text.** A shop\'s bill shows "â‚¹ 250" where "₹ 250" should be. (i) What has gone wrong? (ii) How many bytes does ₹ take in UTF-8? (iii) How can it be fixed?',
               '(i) The ₹ was stored in UTF-8 but read with an old one-byte table, so its 3 bytes became 3 characters. (ii) 3 (E2 82 B9). (iii) Read the text as UTF-8 (both sides must use the same encoding).', 'M · 4.5'))
    # 7 storage
    qs.append(('**Case: storing roll numbers.** A school has 1,800 students. (i) How many bits are needed for each roll number? (ii) How many hexadecimal digits? (iii) Write roll number 1,500 in hex.',
               f'(i) 11, because 2¹⁰ = 1024 is too few and 2¹¹ = 2048 is enough. (ii) 3 (11 bits fit in 3 × 4 = 12). (iii) {num(nb.to_base(1500, 16), 16)}.', 'M · 4.2'))
    ok((1800).bit_length() == 11 and nb.to_base(1500, 16) == '5DC')
    # 8 ISCII to Unicode
    qs.append(('**Case: an old Hindi file.** A government office has documents typed in ISCII in the 1990s. (i) How many codes does ISCII have? (ii) Why can such a file not hold Hindi and Tamil together? (iii) Why should the office convert them to Unicode?',
               '(i) 256 (8 bits). (ii) All Indian scripts share the same upper 96 places, so a file holds one Indian script at a time. (iii) Unicode gives every script its own block, works on every device and is the standard used for e-governance.', 'M · 4.5'))
    return page('07-case-study.md', 'Case studies', 'Each case has three parts.', [('Case studies', qs)])


# ================================================================== 08 conversion drill
def drill():
    secs = []
    for a, b, lo, hi, cnt in [(10, 2, 30, 600, 10), (10, 8, 100, 3000, 7), (10, 16, 200, 9000, 8)]:
        qs = []
        for _ in range(cnt):
            n = fresh(lo, hi)
            w, r = div_work(n, b)
            qs.append((f'Convert {num(n, 10)} to {NAME[b]}.', f'{num(r, b)}. *Working:* {w}.', 'E · 4.3'))
        secs.append((f'Decimal to {NAME[b]} (divide)', qs))
    qs = []
    for b, lo, hi, cnt in [(2, 30, 500, 6), (8, 64, 4000, 5), (16, 256, 60000, 5)]:
        for _ in range(cnt):
            s = nb.to_base(fresh(lo, hi), b)
            w, v = pv_work(s, b)
            qs.append((f'Convert {num(s, b)} to decimal.', f'{v}. *Working:* {w}.', 'E · 4.3'))
    secs.append(('Binary, octal or hexadecimal to decimal (place values)', qs))
    qs = []
    for b in [8, 16] * 5:
        bits = nb.to_base(fresh(100, 30000), 2)
        w, r = grp_work(bits, b)
        qs.append((f'Convert {num(bits, 2)} to {NAME[b]}.', f'{num(r, b)}. *Working:* {w}.', 'E · 4.3'))
    secs.append(('Binary to octal or hexadecimal (group)', qs))
    qs = []
    for b in [8, 16] * 4:
        s = nb.to_base(fresh(64, 20000), b)
        w, r = bits_work(s, b)
        qs.append((f'Convert {num(s, b)} to binary.', f'{num(r, 2)}. *Working:* {w}.', 'E · 4.3'))
    secs.append(('Octal or hexadecimal to binary (each digit to bits)', qs))
    qs = []
    for b in [8, 16] * 3:
        to = 16 if b == 8 else 8
        s = nb.to_base(fresh(64, 40000), b)
        bw, bb = bits_work(s, b)
        w, r = grp_work(bb, to)
        qs.append((f'Convert {num(s, b)} to {NAME[to]}.', f'{num(r, to)}. *Working:* to bits: {bw}; regroup: {w}.', 'M · 4.3'))
    secs.append(('Octal and hexadecimal (through binary)', qs))
    return page('08-conversion-drill.md', 'Conversion drill with workings', 'Whole numbers, every road of section 4.3.', secs)


# ================================================================== 09 fractions
def fractions():
    secs = []
    qs = []
    for s, b in [('110.011', 2), ('1011.101', 2), ('0.1101', 2), ('11.0011', 2), ('37.4', 8), ('125.24', 8), ('0.71', 8),
                 ('A.8', 16), ('1F.4', 16), ('3C.28', 16)]:
        w, v = pv_work(s, b)
        qs.append((f'Convert {num(s, b)} to decimal.', f'{v}. *Working:* {w}.', 'M · 4.4'))
    secs.append(('To decimal (place values after the point)', qs))
    qs = []
    for f in ['0.4375', '0.84375', '0.09375', '0.71875', '0.5625']:
        steps, d, why = frac_work(f, 2)
        ok(why == 'zero')
        qs.append((f'Convert {num(f, 10)} to binary.', f'{num("0." + d, 2)}. *Working:* {steps}; fraction 0: stop.', 'M · 4.4'))
    for f in ['0.2', '0.7', '0.45']:
        steps, d, why = frac_work(f, 2, places=6)
        qs.append((f'Convert {num(f, 10)} to binary, to 6 places.', f'≈ {num("0." + d + "…", 2)}. *Working:* {steps}; it does not end ({"a fraction came back" if why == "repeats" else "6 places reached"}).', 'H · 4.4'))
    for f, b in [('0.828125', 8), ('0.9375', 16), ('0.3125', 8), ('0.6484375', 16)]:
        steps, d, why = frac_work(f, b)
        ok(why == 'zero')
        qs.append((f'Convert {num(f, 10)} to {NAME[b]}.', f'{num("0." + d, b)}. *Working:* {steps}.', 'H · 4.4'))
    secs.append(('From decimal (multiply)', qs))
    qs = []
    for s, b in [('101.011', 8), ('1101.1011', 16), ('10.01101', 8), ('111001.101', 16), ('0.10111', 8), ('11101.01', 16)]:
        w, r = grp_work(s, b)
        qs.append((f'Convert {num(s, 2)} to {NAME[b]}.', f'{num(r, b)}. *Working:* {w}.', 'M · 4.4'))
    for s, b in [('5.36', 8), ('B.A', 16)]:
        w, r = bits_work(s, b)
        qs.append((f'Convert {num(s, b)} to binary.', f'{num(r, 2)}. *Working:* {w}.', 'M · 4.4'))
    secs.append(('Between binary, octal and hexadecimal (group away from the point)', qs))
    return page('09-fractions.md', 'Numbers with a fractional part', 'Section 4.4.', secs)


# ================================================================== 10 encoding
def encoding():
    secs = []
    qs = []
    for w in ['INDIA', 'Delhi', 'CODE', 'Byte', 'KV2', 'ok!', 'Hi 5', 'RAM']:
        codes = ' '.join(str(ord(c)) for c in w)
        bins = ' '.join(format(ord(c), '07b') for c in w)
        qs.append((f'Encode "{w}" in ASCII (decimal and 7-bit binary).', f'{codes}; in binary {bins}.', 'E · 4.5'))
    secs.append(('Encode in ASCII', qs))
    qs = []
    for w in ['MUMBAI', 'Chai', 'BHARAT', 'Data', 'GO 11', 'Taj', 'CPU', 'Yes']:
        codes = ' '.join(str(ord(c)) for c in w)
        qs.append((f'Decode the ASCII codes {codes}.', f'"{w}". *Hint:* A = 65, a = 97, space = 32, \'0\' = 48.', 'E · 4.5'))
    secs.append(('Decode ASCII', qs))
    qs = []
    for s in ['Hello', 'नमस्ते', '₹500', 'India भारत', 'தமிழ்', '😀 OK', 'é', 'क ख ग']:
        u8, u32 = len(s.encode('utf-8')), len(s.encode('utf-32-le'))
        parts = []
        for c in s:
            parts.append(f'{c if c != " " else "space"} {len(c.encode("utf-8"))}')
        qs.append((f'How many bytes does "{s}" take in UTF-8 and in UTF-32?', f'UTF-8 **{u8}**, UTF-32 **{u32}** ({len(s)} code points × 4). *Working (UTF-8 bytes per code point):* ' + ', '.join(parts) + '.', 'M · 4.5'))
    secs.append(('Bytes in UTF-8 and UTF-32', qs))
    qs = []
    for c in ['B', 'z', 'ई', 'ङ', '₹', '©']:
        cp = ord(c)
        qs.append((f'Write the Unicode code point of "{c}" ({unicodedata.name(c).lower()}) and its value in decimal.', f'U+{cp:04X} = {cp}. *Why:* (hex to decimal) {pv_work(f"{cp:X}", 16)[0]}.', 'M · 4.5'))
    secs.append(('Code points', qs))
    return page('10-encoding.md', 'Encoding: ASCII and Unicode', 'Section 4.5.', secs)


# ================================================================== 11 compare, arrange, find the base
def compare():
    qs = []
    for _ in range(6):
        ns = [fresh(20, 300) for _ in range(4)]
        bases = R.sample([2, 8, 10, 16], 4)
        shown = [num(nb.to_base(n, b), b) for n, b in zip(ns, bases)]
        order = [s for _, s in sorted(zip(ns, shown))]
        qs.append((f'Arrange in increasing order: {", ".join(shown)}.', f'{", ".join(order)}. *Working:* in decimal they are ' + ', '.join(f'{s} = {n}' for s, n in zip(shown, ns)) + '.', 'M · 4.3'))
    for s, v in [('101', 26), ('23', 19), ('110', 42), ('31', 25), ('1000', 125), ('202', 74)]:
        b = next(b for b in range(2, 17) if nb.valid(s, b) and nb.value(s, b) == v)
        qs.append((f'Find the base b if ({s})_b = {v}.', f'b = {b}. *Working:* ' + ' + '.join(f'{nb.digit_value(d)} × {b}^{len(s) - 1 - i}' for i, d in enumerate(s)) + f' = {v}.', 'H · 4.2'))
    for _ in range(4):
        n = fresh(100, 4000)
        h = nb.to_base(n, 16)
        k = R.randrange(len(h))
        blank = h[:k] + 'x' + h[k + 1:]
        qs.append((f'Find the digit x if ({blank})₁₆ = {n}.', f'x = {h[k]}. *Check:* {num(h, 16)} = {pv_work(h, 16)[0]}.', 'H · 4.3'))
    for s, b in [('1010', 2), ('1010', 8), ('1010', 16), ('1010', 10)]:
        qs.append((f'What is "1010" worth if it is in base {b}?', f'{nb.value(s, b)}. *Why:* {pv_work(s, b)[0]}. The same digits mean different numbers in different bases: always write the base.', 'E · 4.2'))
    return page('11-compare-and-find.md', 'Compare, arrange, find the base or the digit', 'Sections 4.2 and 4.3.', [('Compare and find', qs)])


# ================================================================== 12 spot the mistake
def mistakes():
    qs = []
    for _ in range(4):
        n = fresh(30, 250)
        rows = nb.div_ladder(n, 2)
        down = ''.join(str(r[2]) for r in rows)
        right = nb.to_base(n, 2)
        ok(down != right)
        qs.append((f'A student converts {num(n, 10)} to binary: remainders {", ".join(str(r[2]) for r in rows)}, answer {num(down, 2)}. Find the mistake.',
                   f'The remainders were read **downward**. The first remainder is the units digit, so read upward: {num(right, 2)}.', 'M · 4.3'))
    for _ in range(3):
        bits = nb.to_base(fresh(100, 2000), 2)
        if len(bits) % 3 == 0:
            bits = '1' + bits
        wrong = ''.join(nb.DIGITS[int(bits[i:i + 3].ljust(3, '0'), 2)] for i in range(0, len(bits), 3))
        right = grp_work(bits, 8)[1]
        ok(wrong != right)
        qs.append((f'A student converts {num(bits, 2)} to octal by grouping from the left and filling the last group with 0s: answer {num(wrong, 8)}. Find the mistake.',
                   f'Groups must start at the point (the right end) and be padded on the **left**: {grp_work(bits, 8)[0]}.', 'M · 4.3'))
    for _ in range(3):
        while True:
            n = fresh(160, 4000)
            h = nb.to_base(n, 16)
            if any(c in 'ABCDEF' for c in h):
                break
        wrong = ''.join(str(nb.digit_value(c)) for c in h)
        qs.append((f'A student writes {num(n, 10)} in hexadecimal as ({wrong})₁₆. Find the mistake.',
                   f'Remainders 10 to 15 must be written as single letters A to F. {div_work(n, 16)[0]}.', 'E · 4.3'))
    for s in ['1101', '10110', '111001']:
        wrong = sum(int(d) * 2 ** (len(s) - i) for i, d in enumerate(s))
        right = nb.value(s, 2)
        ok(wrong == 2 * right)
        qs.append((f'A student finds {num(s, 2)} = {wrong}, numbering the positions from 1. Find the mistake.',
                   f'Positions start at **0** for the units place, so every place value was doubled. {pv_work(s, 2)[0]}.', 'M · 4.2'))
    f = '0.375'
    steps, d, why = frac_work(f, 2)
    qs.append((f'A student converts {num(f, 10)} to binary and writes {num("0." + d[::-1], 2)}. Find the mistake.',
               f'The whole parts were read upward. In the multiplication method they are read **downward**: {steps} → {num("0." + d, 2)}.', 'M · 4.4'))
    qs.append(("A student writes: the ASCII code of '4' is 4. Find the mistake.", "'4' is a character, not the number four; its code is 48 + 4 = 52.", 'E · 4.5'))
    return page('12-spot-the-mistake.md', 'Spot the mistake', 'Each question shows a worked answer with one mistake: find it, say why it is wrong, and correct it.', [('Spot the mistake', qs)])


def index(counts):
    total = sum(counts.values())
    t = f'''# Chapter 4: Number Systems and Encoding Schemes: questions

**{total} questions**, each with its answer and the reason below it. They are for learning: try each question first, then read the answer.

**By type of question**

- [Multiple-choice questions: {counts["01"]}](01-mcq.md)
- [Fill in the blanks: {counts["02"]}](02-fill-in.md)
- [True or false: {counts["03"]}](03-true-false.md)
- [Assertion and reason: {counts["04"]}](04-assertion-reason.md)
- [Short-answer questions: {counts["05"]}](05-short-answer.md)
- [Long-answer questions: {counts["06"]}](06-long-answer.md)
- [Case studies: {counts["07"]} cases, three parts each](07-case-study.md)

**Practice with numbers and codes**: generated and checked by program

- [Conversion drill with workings: {counts["08"]}](08-conversion-drill.md)
- [Numbers with a fractional part: {counts["09"]}](09-fractions.md)
- [Encoding: ASCII and Unicode: {counts["10"]}](10-encoding.md)
- [Compare, arrange, find the base or the digit: {counts["11"]}](11-compare-and-find.md)
- [Spot the mistake: {counts["12"]}](12-spot-the-mistake.md)
'''
    (QD / 'index.md').write_text(t, encoding='utf-8')
    print('total', total)


if __name__ == '__main__':
    c = {'01': mcq(), '02': fill(), '03': tf(), '04': ar(), '05': short(), '06': long_(), '07': cases(), '08': drill(),
         '09': fractions(), '10': encoding(), '11': compare(), '12': mistakes()}
    index(c)
    print(f'{checks} checks passed')
