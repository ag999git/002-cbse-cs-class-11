"""Number-system library for the book (Chapter 4 and its online pages), 26 Nov 2026.

Every conversion, ladder, grouping and place-value expansion printed in the book is computed here, with exact
fractions (no rounding errors). Used by the chapter's figure script, the online question generator and the
conversion checker (check_conversions.py).

    to_base(65, 2) -> '1000001'           value('3A5', 16) -> Fraction(933)
    div_ladder(65, 8) -> [(65, 8, 1), (8, 1, 0), (1, 0, 1)]
    mul_ladder(Fraction(3, 8), 2) -> rows, repeating flag
    groups('11010110', 3) -> ['011', '010', '110']
    convert('12.375', 10, 2) -> '1100.011'
"""
from fractions import Fraction

DIGITS = '0123456789ABCDEF'
SUB = {2: '₂', 8: '₈', 10: '₁₀', 16: '₁₆'}
NAMES = {2: 'binary', 8: 'octal', 10: 'decimal', 16: 'hexadecimal'}


def digit_value(ch):
    v = DIGITS.index(ch.upper())
    return v


def valid(s, b):
    """True if every digit of s (point allowed once) is a digit of base b."""
    s = s.upper()
    if s.count('.') > 1 or s in ('', '.'):
        return False
    return all(c == '.' or (c in DIGITS and DIGITS.index(c) < b) for c in s)


def value(s, b):
    """Exact value of the numeral s in base b (may have a fractional part)."""
    assert valid(s, b), (s, b)
    s = s.upper()
    whole, _, frac = s.partition('.')
    v = Fraction(0)
    for c in whole:
        v = v * b + digit_value(c)
    for k, c in enumerate(frac, 1):
        v += Fraction(digit_value(c), b ** k)
    return v


def to_base(n, b):
    """Whole number n (int >= 0) written in base b."""
    if n == 0:
        return '0'
    out = ''
    while n:
        n, r = divmod(n, b)
        out = DIGITS[r] + out
    return out


def div_ladder(n, b):
    """Rows (dividend, quotient, remainder) of the repeated-division method, top to bottom."""
    rows = []
    while True:
        q, r = divmod(n, b)
        rows.append((n, q, r))
        if q == 0:
            return rows
        n = q


def mul_ladder(f, b, max_steps=8):
    """Rows (fraction, product, integer digit, new fraction) of the repeated-multiplication method.
    Stops when the fraction becomes 0, when a fraction repeats, or after max_steps.
    Returns (rows, reason) with reason 'zero', 'repeats' or 'limit'."""
    f = Fraction(f)
    assert 0 <= f < 1
    rows, seen = [], set()
    while len(rows) < max_steps:
        if f == 0:
            return rows, 'zero'
        if f in seen:
            return rows, 'repeats'
        seen.add(f)
        p = f * b
        d = int(p)
        rows.append((f, p, d, p - d))
        f = p - d
    return rows, ('zero' if f == 0 else 'limit')


def frac_digits(f, b, max_steps=8):
    rows, reason = mul_ladder(f, b, max_steps)
    return ''.join(DIGITS[r[2]] for r in rows), reason


def convert(s, b_from, b_to, max_frac=8):
    """Convert the numeral s from base b_from to base b_to; the fraction is cut after max_frac digits."""
    v = value(s, b_from)
    whole = int(v)
    out = to_base(whole, b_to)
    f = v - whole
    if f:
        d, _ = frac_digits(f, b_to, max_frac)
        out += '.' + d
    return out


def place_terms(s, b):
    """Rows (digit, digit value, position, weight) for the place-value method."""
    s = s.upper()
    whole, _, frac = s.partition('.')
    rows = []
    for i, c in enumerate(whole):
        pos = len(whole) - 1 - i
        rows.append((c, digit_value(c), pos, Fraction(b) ** pos))
    for k, c in enumerate(frac, 1):
        rows.append((c, digit_value(c), -k, Fraction(1, b ** k)))
    return rows


def groups(bits, k, side='left'):
    """Split a bit string into groups of k. side='left' pads zeros on the left (whole part);
    side='right' pads on the right (fraction part)."""
    pad = (-len(bits)) % k
    bits = '0' * pad + bits if side == 'left' else bits + '0' * pad
    return [bits[i:i + k] for i in range(0, len(bits), k)]


def bin_to(bits, b):
    """Binary numeral (point allowed) to octal (b=8) or hex (b=16) by grouping; returns (groups, result)."""
    k = {8: 3, 16: 4}[b]
    whole, _, frac = bits.partition('.')
    gw = groups(whole, k, 'left')
    gf = groups(frac, k, 'right') if frac else []
    res = ''.join(DIGITS[int(g, 2)] for g in gw).lstrip('0') or '0'
    if gf:
        res += '.' + ''.join(DIGITS[int(g, 2)] for g in gf)
    return gw, gf, res


def to_bin_by_digit(s, b):
    """Octal or hex numeral to binary, digit by digit; returns (list of (digit, bits), result)."""
    k = {8: 3, 16: 4}[b]
    s = s.upper()
    parts = [(c, format(digit_value(c), f'0{k}b')) if c != '.' else ('.', '.') for c in s]
    res = ''.join(p[1] for p in parts)
    whole, _, frac = res.partition('.')
    whole = whole.lstrip('0') or '0'
    frac = frac.rstrip('0')
    return parts, whole + ('.' + frac if frac else '')


def show(s, b):
    return f'({s}){SUB[b]}'


if __name__ == '__main__':
    # self-test
    assert to_base(65, 2) == '1000001' and to_base(65, 8) == '101' and to_base(65, 16) == '41'
    assert value('3A5', 16) == 933 and value('605.12', 8) == Fraction(389) + Fraction(5, 32)
    assert convert('12.375', 10, 2) == '1100.011'
    assert bin_to('10101100.01011', 8)[2] == '254.26' and bin_to('10101100.010111', 16)[2] == 'AC.5C'
    assert to_bin_by_digit('23D', 16)[1] == '1000111101'
    rows, why = mul_ladder(Fraction(675, 1000), 2, 12)
    assert why == 'repeats' and ''.join(str(r[2]) for r in rows) == '1010110011'[:len(rows)]
    print('numbase_lib self-test passed')
