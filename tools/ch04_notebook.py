"""Make notebooks/ch04-number-systems.ipynb (Chapter 4, Colab), 26 Nov 2026. Every code cell is run here once to make
sure it works before the notebook is written. Run from the repository root:  python tools/ch04_notebook.py"""
import contextlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'notebooks' / 'ch04-number-systems.ipynb'

cells = [
    ('md', """# Chapter 4: Number systems and encoding: try it in Python

*Computer Science with Python, CBSE Class XI · online notebook of Chapter 4.*

You meet Python properly in Chapter 6. Here you only **run** the cells: click a cell and press **Shift + Enter**. Change the
numbers and run it again. Nothing can break."""),
    ('md', "## 1. Decimal to binary, octal and hex\n\n`bin()`, `oct()` and `hex()` give the number with a prefix: **0b** for binary, **0o** for octal, **0x** for hex."),
    ('code', "n = 65\nprint(bin(n), oct(n), hex(n))"),
    ('md', "## 2. Back to decimal\n\n`int(text, base)` reads a number written in any base from 2 to 36."),
    ('code', "print(int('1000001', 2), int('101', 8), int('41', 16), int('9C', 16))"),
    ('md', "## 3. The division ladder of the book (Road 1)\n\nThis small program divides again and again and reads the remainders upward, exactly as in section 4.3."),
    ('code', """def ladder(n, b):
    digits = '0123456789ABCDEF'
    remainders = []
    while n > 0:
        q, r = divmod(n, b)
        print(f'{n:>6} ÷ {b} = {q:<6} remainder {digits[r]}')
        remainders.append(digits[r])
        n = q
    print('Read upward:', ''.join(reversed(remainders)))

ladder(156, 8)"""),
    ('md', "## 4. Place values (Road 2)"),
    ('code', """def place_values(text, b):
    total = 0
    for position, digit in enumerate(reversed(text)):
        value = int(digit, 16)
        print(f'{digit} × {b}^{position} = {value * b ** position}')
        total += value * b ** position
    print('Total:', total)

place_values('3A5', 16)"""),
    ('md', "## 5. Fractions: multiply and read down (section 4.4)\n\nWatch 0.375 end, and 0.3 go on for ever."),
    ('code', """from fractions import Fraction

def fraction_to_base(f, b, places=8):
    f = Fraction(f)
    digits, seen = '', []
    while f and len(digits) < places:
        if f in seen:
            print('  this fraction came before: the digits repeat')
            break
        seen.append(f)
        p = f * b
        d = int(p)
        print(f'  {float(f):g} × {b} = {float(p):g} → {d}')
        digits += '0123456789ABCDEF'[d]
        f = p - d
    print('Read down: 0.' + digits)

fraction_to_base('0.375', 2)
fraction_to_base('0.3', 2)"""),
    ('md', "## 6. Characters and their codes\n\n`ord()` gives a character's code (its Unicode code point; for English letters this is the ASCII code). `chr()` goes back."),
    ('code', """print(ord('A'), ord('a'), ord('0'), ord(' '))
print(chr(65), chr(97 + 12))
word = 'RAMAN'
print([ord(c) for c in word])
print([format(ord(c), '07b') for c in word])"""),
    ('md', "## 7. Unicode: code points and bytes\n\n`.encode('utf-8')` gives the bytes that are stored. Compare UTF-8 and UTF-32."),
    ('code', """for text in ['A', '₹', 'अ', '😀', 'हम सब एक']:
    u8 = text.encode('utf-8')
    u32 = text.encode('utf-32-be')
    print(f'{text!r:12} code points: {[hex(ord(c)) for c in text]}')
    print(f'{"":12} UTF-8: {len(u8)} bytes {u8.hex(" ").upper()}   UTF-32: {len(u32)} bytes')"""),
    ('md', """## 8. Try these (answers hidden: click to open)

1. Use `bin()` to write 2026 in binary.
2. Use `int()` to find (7F)₁₆ in decimal.
3. Run `ladder(500, 16)`.
4. Run `fraction_to_base('0.1', 2)`: does it end?
5. What is `chr(ord('g') - 32)`?
6. How many bytes does your name take in UTF-8? Type it in Hindi or your own script too.

<details><summary>Answers</summary>

1. `0b11111101010` 2. 127 3. 500 = (1F4)₁₆ 4. No: 0.1 repeats in binary 5. 'G' 6. 1 byte per English letter, 3 per Devanagari code point.

</details>"""),
    ('code', "# your own experiments here\n"),
]


def to_nb(cells):
    out = []
    for kind, src in cells:
        lines = src.split('\n')
        source = [l + '\n' for l in lines[:-1]] + [lines[-1]]
        if kind == 'md':
            out.append({'cell_type': 'markdown', 'metadata': {}, 'source': source})
        else:
            out.append({'cell_type': 'code', 'metadata': {}, 'execution_count': None, 'outputs': [], 'source': source})
    return {'cells': out, 'metadata': {'colab': {'provenance': []}, 'kernelspec': {'name': 'python3', 'display_name': 'Python 3'},
                                       'language_info': {'name': 'python'}}, 'nbformat': 4, 'nbformat_minor': 0}


env = {}
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    for kind, src in cells:
        if kind == 'code':
            exec(src, env)
out = buf.getvalue()
assert '(1F4)' not in out  # sanity
assert 'Read upward: 234' in out and 'Total: 933' in out and 'Read down: 0.011' in out and 'repeat' in out
assert bin(2026) == '0b11111101010' and int('7F', 16) == 127 and chr(ord('g') - 32) == 'G'
OUT.write_text(json.dumps(to_nb(cells), ensure_ascii=False, indent=1), encoding='utf-8')
print('wrote', OUT.name, len(cells), 'cells; all code cells ran')
