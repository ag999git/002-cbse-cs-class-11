"""Online question bank for Chapter 1: units of memory and the memory hierarchy (160 questions).
Every answer is computed here; the same seed gives the same questions.
Run from the repository root:  python tools/units_bank.py"""
import random
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QD = ROOT / 'book' / 'unit-1' / '001-ch01-computer-system-organisation' / 'questions'
rnd = random.Random(1024)
UNITS = ['bit', 'byte', 'KB', 'MB', 'GB', 'TB', 'PB']          # the CBSE ladder (nibble handled separately)
BYTES = {'bit': Fraction(1, 8), 'nibble': Fraction(1, 2), 'byte': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3,
         'TB': 1024 ** 4, 'PB': 1024 ** 5}
HEAD = ('*Chapter 1 · Questions (online). Every answer was computed by a program (`tools/units_bank.py`), so it cannot '
        'contain slips. Try each question first; then read the answer and the working below it.*\n')


def fmt(x):
    x = Fraction(x)
    if x.denominator == 1:
        return f'{x.numerator:,}'.replace(',', ' ')
    return f'{float(x):,.2f}'.rstrip('0').rstrip('.').replace(',', ' ')


def steps(a, b):
    """Working from unit a to unit b, one rung of the ladder at a time."""
    ia, ib = UNITS.index(a), UNITS.index(b)
    out = []
    rng = range(ia, ib, -1) if ia > ib else range(ia, ib)
    for i in rng:
        lo, hi = (UNITS[i - 1], UNITS[i]) if ia > ib else (UNITS[i], UNITS[i + 1])
        f = 8 if 'bit' in (lo, hi) else 1024
        out.append(('×' if ia > ib else '÷') + f' {f} ({hi} → {lo})' if ia > ib else f'÷ {f} ({lo} → {hi})')
    return out


def un(v, u):
    """unit name, plural for bit and byte"""
    return u + ('s' if u in ('bit', 'byte') and Fraction(v) != 1 else '')


def size(v, u):
    return Fraction(v) * BYTES[u]


def conversions(n=60):
    qs = []
    while len(qs) < n:
        a, b = rnd.sample(UNITS, 2)
        if abs(UNITS.index(a) - UNITS.index(b)) > 2:
            continue
        if UNITS.index(a) > UNITS.index(b):          # big to small: any whole number gives a whole answer
            v = rnd.choice([1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 32, 64, 100, 128, 256, 512])
        else:                                          # small to big: choose the answer first, so it is whole
            ans = rnd.choice([1, 2, 3, 4, 5, 6, 8, 10, 16, 32, 64])
            v = size(ans, b) / BYTES[a]
            if v > 100000:
                continue
        res = size(v, a) / BYTES[b]
        q = f'Convert {fmt(v)} {un(v, a)} into {b}{"s" if b in ("bit", "byte") else ""}.'
        if q in [x[0] for x in qs]:
            continue
        qs.append((q, f'{fmt(v)} {un(v, a)} = **{fmt(res)} {un(res, b)}**',
                   'Working: ' + ', then '.join(steps(a, b)) + '.'))
    return qs


def ordering(n=40):
    qs = []
    while len(qs) < n:
        items = []
        while len(items) < 4:
            u = rnd.choice(UNITS[2:6])
            v = rnd.choice([1, 2, 4, 8, 10, 16, 32, 100, 256, 512, 1024, 2048, 3000])
            if all(size(v, u) != size(w, x) for w, x in items):
                items.append((v, u))
        asc = sorted(items, key=lambda t: size(*t))
        q = 'Arrange in ascending order: ' + ', '.join(f'{fmt(v)} {u}' for v, u in items) + '.'
        smallest = min(UNITS.index(u) for _, u in items)
        base = UNITS[smallest]
        conv = ', '.join(f'{fmt(v)} {u} = {fmt(size(v, u) / BYTES[base])} {base}' for v, u in items)
        qs.append((q, ' < '.join(f'**{fmt(v)} {u}**' for v, u in asc), f'Working: change all to {base}: {conv}.'))
    return qs


def compare(n=20):
    qs = []
    while len(qs) < n:
        u1, u2 = rnd.sample(UNITS[2:6], 2)
        v1 = rnd.choice([1, 2, 4, 8, 16, 512, 1024, 2048])
        v2 = rnd.choice([1, 2, 4, 8, 16, 512, 1024, 2048])
        a, b = size(v1, u1), size(v2, u2)
        rel = 'equal to' if a == b else 'more than' if a > b else 'less than'
        q = f'Is {fmt(v1)} {u1} more than, less than or equal to {fmt(v2)} {u2}?'
        if q in [x[0] for x in qs]:
            continue
        qs.append((q, f'{fmt(v1)} {u1} is **{rel}** {fmt(v2)} {u2}.',
                   f'Working: in bytes, {fmt(a)} and {fmt(b)}.'))
    return qs


def files_fit(n=20):
    things = [('photos', 'MB', [2, 3, 4, 5, 6]), ('songs', 'MB', [3, 4, 5, 8]), ('films', 'GB', [1, 2, 3, 4]),
              ('documents', 'KB', [200, 256, 500, 512])]
    disks = [('a 16 GB pen drive', 16, 'GB'), ('a 32 GB memory card', 32, 'GB'), ('a 1 TB hard disk', 1, 'TB'),
             ('a 512 GB SSD', 512, 'GB'), ('a 4 GB pen drive', 4, 'GB'), ('a 700 MB CD', 700, 'MB')]
    qs = []
    while len(qs) < n:
        what, u, sizes = rnd.choice(things)
        s = rnd.choice(sizes)
        dname, dv, du = rnd.choice(disks)
        if BYTES[du] * dv < BYTES[u] * s:
            continue
        cnt = (size(dv, du) / size(s, u))
        whole = cnt.numerator // cnt.denominator
        q = f'How many {what} of {s} {u} each can be stored on {dname}?'
        if q in [x[0] for x in qs]:
            continue
        qs.append((q, f'**{whole:,}**'.replace(',', ' ') + f' {what}.',
                   f'Working: {dv} {du} = {fmt(size(dv, du) / BYTES[u])} {u}; ÷ {s} = {fmt(cnt)}'
                   + ('' if cnt.denominator == 1 else f'; only whole {what} fit, so {fmt(whole)}') + '.'))
    return qs


SPEED = ['registers', 'cache', 'RAM', 'SSD', 'hard disk']     # fastest first; also costliest per byte first


def hierarchy(n=20):
    qs = []
    asks = [('in order of speed, fastest first', SPEED, 'the closer to the CPU, the faster'),
            ('in order of size (capacity), smallest first', SPEED, 'the faster the memory, the smaller it is in a computer'),
            ('in order of cost per byte, cheapest first', SPEED[::-1], 'the slower the memory, the cheaper each byte'),
            ('in order of distance from the CPU, nearest first', SPEED, 'registers are inside the CPU; storage is farthest')]
    while len(qs) < n:
        what, order, why = rnd.choice(asks)
        pick = rnd.sample(SPEED, rnd.choice([3, 4]))
        shown = pick[:]
        rnd.shuffle(shown)
        q = f'Arrange {what}: ' + ', '.join(shown) + '.'
        if q in [x[0] for x in qs]:
            continue
        ans = [m for m in order if m in pick]
        qs.append((q, ', '.join(f'**{m}**' for m in ans) + '.', f'Why: {why} (the memory pyramid, section 1.6).'))
    return qs


def page(fname, title, intro, qs, start=1):
    lines = [f'# Chapter 1: {title} ({len(qs)} questions)\n', HEAD, intro + '\n']
    for k, (q, a, w) in enumerate(qs, start):
        lines += [f'**Q{k}.** {q}\n', f'**Answer.** {a}\n', f'*{w}*\n']
    (QD / fname).write_text('\n'.join(lines), encoding='utf-8')
    return len(qs)


if __name__ == '__main__':
    QD.mkdir(parents=True, exist_ok=True)
    n = page('08-unit-conversions.md', 'converting units of memory',
             '**Rule** (section 1.7): going to a smaller unit, multiply (× 1024 for each step, × 8 from bytes to bits); '
             'going to a bigger unit, divide.', conversions())
    n += page('09-arrange-and-compare.md', 'arranging and comparing sizes',
              '**Rule:** change every size to one unit before comparing.', ordering() + compare())
    n += page('10-how-many-fit.md', 'how many files fit', '**Rule:** change both sizes to one unit, divide, and keep only the whole number.', files_fit())
    n += page('11-memory-hierarchy.md', 'the memory hierarchy', '**Rule:** read the pyramid: registers → cache → RAM → SSD → hard disk.', hierarchy())
    print(n, 'questions')
