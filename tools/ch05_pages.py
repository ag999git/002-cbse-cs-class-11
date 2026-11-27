"""Chapter 5 online pages (27 Nov 2026; plan ch05-online-plan-v2 approved, "12 Online plan decisions 1").
First the sample page, Euclid step by step (QR 0504), for Anurag's approval; the other pages follow the same pattern.

Every number on every page is computed here and checked (ok(...)); flowchart runs come from algo_lib, the same
description that drew the printed flowchart W8. Pictures are drawn here, in the book's style, into
book/assets/images/ch05/.

Run from the repository root:  python tools/ch05_pages.py"""
import math
import shutil
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent.parent
CH = PROJECT / '01-all-chapters-of-cbse-11' / 'ch05-problem-solving'
sys.path.insert(0, str(PROJECT / '50-tools'))
sys.path.insert(0, str(CH / 'tools'))
import figures_v1 as F  # noqa: E402  (the printed flowcharts: F.GCD is W8)

D = ROOT / 'book' / 'unit-2' / '005-ch05-problem-solving'
IMG = ROOT / 'book' / 'assets' / 'images' / 'ch05'
REL = '../../assets/images/ch05'
INK, OR, OR2, OR3 = '#262626', '#C55A11', '#F8CBAD', '#FDF1E9'
plt.rcParams['font.family'] = ['Calibri', 'Segoe UI Symbol']
checks = 0


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def ind(n):
    """Indian grouping: 1533 -> 1,533; 100000 -> 1,00,000."""
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head:
        parts.insert(0, head)
    return ','.join(parts) + ',' + tail


def head(title, label, intro, src='tools/ch05_pages.py'):
    return (f'# {label}: {title}\n\n*Chapter 5 · {label}. {intro}*\n\n'
            f'*Every number on this page was computed by a program (`{src}`) and checked.*\n\n')


def write(name, text):
    (D / name).write_text(text, encoding='utf-8')
    print('wrote', name)


# ================================================================= Euclid: the numbers
def euclid_rounds(a, b):
    """Rounds of Euclid's method exactly as the printed flowchart W8 runs them: while b != 0: r = a mod b; a = b;
    b = r. Each round: (a, b, quotient, remainder)."""
    rounds = []
    while b != 0:
        q, r = divmod(a, b)
        rounds.append((a, b, q, r))
        a, b = b, r
    return rounds, a


def gcd_checked(a, b):
    rounds, g = euclid_rounds(a, b)
    ok(g == math.gcd(a, b), (a, b))
    lcm = a * b // g
    ok(lcm == math.lcm(a, b) and lcm % a == 0 and lcm % b == 0)
    out, _ = F.GCD.run([a, b])                       # the printed flowchart itself, run box by box
    ok(out == [f'{g} {lcm}'], (out, a, b))
    ok(F.GCD.run_python([a, b]) == [f"{g} {lcm}"], F.GCD.run_python([a, b]))
    return rounds, g, lcm


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def img(name, alt):
    """Markdown for a picture at its natural size on screen (a 300 dpi file shown at 96 px per inch), so a small
    picture (8 x 8: one square) is not blown up to the full page width."""
    from PIL import Image
    w = min(720, Image.open(IMG / name).width * 144 // 300)    # 1.5 x natural: labels readable on screen
    return f'![{alt}]({REL}/{name}){{ width="{w}" }}'


# ================================================================= Euclid: the pictures
def tile_panels(a, b, name):
    """One panel per round. The rectangle is a wide and b high. In each round the squares cut are the
    quotient (dark), the squares of earlier rounds are light, and the piece still to be cut (the remainder)
    is dashed. Returns the file name."""
    rounds, g = euclid_rounds(a, b)
    n = len(rounds)
    pw = 2.15                                         # width of one panel, inches
    W = pw * n
    scale = min(0.86 * pw / a, 1.55 / b)
    Hrect = b * scale
    H = Hrect + 0.75
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
    done = []                                         # squares cut in earlier rounds: (x, y, side)
    x, y, w, h = 0.0, 0.0, float(a), float(b)         # the piece still to be cut, in number units
    for k, (A, B, q, r) in enumerate(rounds):
        cut = []
        if q > 0:
            if abs(w - A) < 1e-9 and abs(h - B) < 1e-9:     # A runs across: squares of side B, left to right
                cut = [(x + i * B, y, B) for i in range(q)]
                x, w = x + q * B, r
            else:                                     # A runs up: squares of side B, bottom to top
                cut = [(x, y + i * B, B) for i in range(q)]
                y, h = y + q * B, r
        ox = k * pw + (pw - a * scale) / 2
        oy = 0.12
        ax.add_patch(Rectangle((ox, oy), a * scale, b * scale, fc='white', ec=INK, lw=1.1))
        for (sx, sy, s) in done:
            ax.add_patch(Rectangle((ox + sx * scale, oy + sy * scale), s * scale, s * scale, fc=OR3, ec=INK, lw=0.6))
        for (sx, sy, s) in cut:
            ax.add_patch(Rectangle((ox + sx * scale, oy + sy * scale), s * scale, s * scale, fc=OR2, ec=INK, lw=0.9))
            if s * scale >= 0.42:
                ax.text(ox + (sx + s / 2) * scale, oy + (sy + s / 2) * scale, f'{s} × {s}', ha='center', va='center',
                        fontsize=8.5)
        if r > 0 and w > 0 and h > 0:
            ax.add_patch(Rectangle((ox + x * scale, oy + y * scale), w * scale, h * scale, fc='none', ec=OR, lw=1.3,
                                   ls=(0, (3, 2))))
        done += cut
        title = f'Round {k + 1}: {A} ÷ {B} = {q} r {r}'
        note = ('no square fits: the numbers swap' if q == 0 else
                (f'{q} square{"s" if q > 1 else ""} of {B} × {B}; ' + (f'{r} left' if r else 'nothing left')))
        ax.text(k * pw + pw / 2, oy + Hrect + 0.42, title, ha='center', fontsize=9.5, weight='bold', color=INK)
        ax.text(k * pw + pw / 2, oy + Hrect + 0.2, note, ha='center', fontsize=8.5, color=OR)
    ok(sum(s * s for (_, _, s) in done) == a * b, ('tiles do not fill', a, b))   # the squares fill the rectangle
    p = IMG / f'{name}.png'
    fig.savefig(p, dpi=300, facecolor='white'); plt.close(fig)
    return p.name


WORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
GREY, GREY2 = '#E6E6E6', '#9A9A9A'


def round_panels(a, b, name):
    """27 Nov (approved R1-R6, d-f): one panel per round of the flowchart, all at ONE scale (smaller squares look
    smaller); side lengths on the piece being cut; this round's squares numbered 1, 2, 3 ... (the quotient is a
    count); the left-over strip white and dashed with a "remainder" arrow; earlier rounds grey, marked "done"; a curved
    arrow "the strip is the next rectangle"; the last square marked "side g = GCD". A round with quotient 0 (smaller
    number first) cuts nothing and swaps the numbers. If the last squares are too small to see, one more panel shows the
    last piece enlarged, marked so. At most three panels in a row."""
    import figures_v4 as F4                            # the same cutting rule as the printed figure
    from matplotlib.patches import FancyArrowPatch
    rounds, g = euclid_rounds(a, b)
    geo = F4.euclid_cuts(a, b)
    ok([(R['big'], R['small'], R['q'], R['r']) for R in geo] == [(A, B, q, r) for A, B, q, r in rounds if q > 0],
       ('flowchart and picture disagree', a, b))
    s = min(2.55 / a, 1.9 / b)                         # inches per unit, the same in every panel
    tiny = geo[-1]['small'] * s < 0.2
    panels = [(A, B, q, r) for A, B, q, r in rounds] + ([None] if tiny else [])
    n = len(panels)
    ncol = min(n, 3)
    nrow = -(-n // ncol)
    pw, ph, gap = a * s + 1.1, b * s + 2.0, 0.8
    W, H = ncol * pw + (ncol - 1) * gap, nrow * ph
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
    F4.INK = INK
    gi = 0                                              # index into geo (rounds that cut squares)
    for k, pan in enumerate(panels):
        col, row = k % ncol, k // ncol
        ox, oy = col * (pw + gap) + 0.45, (nrow - 1 - row) * ph + 0.62
        top = oy + b * s + 0.55
        P = lambda u, v, ox=ox, oy=oy, sc=s: (ox + u * sc, oy + v * sc)
        if pan is None:                                 # R5: the last piece, enlarged
            R = geo[-1]
            px, py, w_, h_ = R['piece']
            se = min(a * s / w_, b * s / h_)
            Q = lambda u, v: (ox + (u - px) * se, oy + (v - py) * se)
            top = oy + h_ * se + 0.55
            for j, (u, v, side) in enumerate(R['sq']):
                last = j == len(R['sq']) - 1
                ax.add_patch(Rectangle(Q(u, v), side * se, side * se, fc=OR if last else OR2, ec=INK, lw=1.4 if last else 1))
                ax.text(*Q(u + side / 2, v + side / 2), f'{j + 1}', ha='center', va='center', fontsize=8, weight='bold',
                        color='white' if last else INK)
            F4.dim(ax, Q(px, py + h_), Q(px + w_, py + h_), str(w_), 'top', off=0.14)
            F4.dim(ax, Q(px + w_, py), Q(px + w_, py + h_), str(h_), 'right', off=0.14)
            ax.text(ox + a * s / 2, top + 0.4, f'Round {len(rounds)}, enlarged', ha='center', fontsize=11, weight='bold')
            ax.text(ox + a * s / 2, top + 0.16, f'the {w_} × {h_} strip, drawn {se / s:.0f} times larger', ha='center',
                    fontsize=9.5, color=OR)
            lx, ly = Q(R['sq'][-1][0] + R['small'] / 2, R['sq'][-1][1])
            ax.annotate(f'side {g} = GCD', xy=(lx, ly), xytext=(lx - 0.3, oy - 0.32), fontsize=9.5, weight='bold',
                        ha='center', va='center', arrowprops=dict(arrowstyle='->', color=INK, lw=1))
            continue
        A, B, q, r = pan
        # earlier rounds: grey, "done"
        for R in geo[:gi]:
            for (u, v, side) in R['sq']:
                ax.add_patch(Rectangle(P(u, v), side * s, side * s, fc=GREY, ec=GREY2, lw=0.6))
        if gi:
            u, v, side = geo[0]['sq'][0]
            if side * s > 0.5:
                ax.text(*P(u + side / 2, v + side / 2), 'done', ha='center', va='center', fontsize=10, color='#7A7A7A',
                        style='italic')
        if q == 0:                                      # smaller number first: nothing is cut, the numbers swap
            ax.add_patch(Rectangle(P(0, 0), a * s, b * s, fc=OR3, ec=INK, lw=1.3))
            F4.dim(ax, P(0, b), P(a, b), str(a), 'top', off=0.14)
            F4.dim(ax, P(0, 0), P(0, b), str(b), 'left', off=0.14)
            sub = f'quotient 0: no {B} × {B} square fits; swap'
        else:
            R = geo[gi]
            for j, (u, v, side) in enumerate(R['sq']):
                last = r == 0 and j == q - 1
                ax.add_patch(Rectangle(P(u, v), side * s, side * s, fc=OR if last else OR2, ec=INK,
                                       lw=1.5 if last else 1))
                if side * s >= 0.45:
                    lab = f'{j + 1}\n{side} × {side}'
                elif side * s >= 0.13:
                    lab = f'{j + 1}'
                else:
                    lab = ''
                if lab:
                    ax.text(*P(u + side / 2, v + side / 2), lab, ha='center', va='center',
                            fontsize=10 if '\n' in lab else 8, weight='bold', color='white' if last else INK,
                            linespacing=1.1)
            px, py, w_, h_ = R['piece']
            if r:
                if w_ >= h_:
                    lu, lv, lw_, lh_ = px + q * B, py, r, h_
                else:
                    lu, lv, lw_, lh_ = px, py, w_, r
                ax.add_patch(Rectangle(P(lu, lv), lw_ * s, lh_ * s, fc='white', ec=OR, lw=1.3, ls='--'))
                cx, cy = P(lu + lw_ / 2, lv + lh_ / 2)
                ax.annotate(f'remainder {r}\n(left over)', xy=(cx, cy), xytext=(P(a, 0)[0] - 0.75, oy - 0.3),
                            fontsize=8.5, color=OR, weight='bold', ha='left', va='center',
                            arrowprops=dict(arrowstyle='->', color=OR, lw=0.9))
            elif not tiny:
                u, v, side = R['sq'][-1]
                lx, ly = P(u + side / 2, v)
                ax.annotate(f'side {g} = GCD', xy=(lx, ly), xytext=(lx - 0.35, oy - 0.32), fontsize=9.5, weight='bold',
                            ha='center', va='center', arrowprops=dict(arrowstyle='->', color=INK, lw=1))
            small_last = tiny and gi == len(geo) - 1      # the enlarged panel shows its sides
            if w_ * s >= 0.25 and not small_last:
                F4.dim(ax, P(px, py + h_), P(px + w_, py + h_), str(w_), 'top', off=0.14)
            if h_ * s >= 0.25 and not small_last:
                if gi == 0:
                    F4.dim(ax, P(px, py), P(px, py + h_), str(h_), 'left', off=0.14)
                else:
                    F4.dim(ax, P(px + w_, py), P(px + w_, py + h_), str(h_), 'right', off=0.14)
            sub = (f'quotient {q} = {WORD[q]} {B} × {B} square{"s" if q > 1 else ""} fit{"" if q > 1 else "s"}')
            gi += 1
        ax.add_patch(Rectangle(P(0, 0), a * s, b * s, fc='none', ec=INK, lw=1.3))
        ax.text(ox + a * s / 2, top + 0.4, f'Round {k + 1}: {A} ÷ {B} = {q} r {r}', ha='center', fontsize=11,
                weight='bold')
        ax.text(ox + a * s / 2, top + 0.16, sub, ha='center', fontsize=9.5, color=OR)
        if k < n - 1 and col < ncol - 1:                # D: the left-over piece is the next rectangle
            x1 = ox + a * s + 0.55
            yA = oy + b * s * 0.8
            ax.add_patch(FancyArrowPatch((x1 - 0.1, yA), (x1 + gap + 0.1, yA), connectionstyle='arc3,rad=-0.35',
                                         arrowstyle='-|>', mutation_scale=11, color=INK, lw=1.0))
            nxt = 'the numbers\nswap' if q == 0 else ('the same strip,\nenlarged' if panels[k + 1] is None
                                                       else 'the strip is\nthe next\nrectangle')
            ax.text(x1 + gap / 2, yA + 0.3, nxt, ha='center', va='bottom', fontsize=7.5, linespacing=1.05)
    ok(sum(t[2] ** 2 for R in geo for t in R['sq']) == a * b, ('tiles do not fill', a, b))
    p = IMG / f'{name}.png'
    fig.savefig(p, dpi=300, facecolor='white'); plt.close(fig)
    return p.name


def grid_picture(a, b, g, name):
    """The a × b rectangle covered by g × g squares: g fits both sides exactly."""
    s = 2.4 / a
    fig = plt.figure(figsize=(a * s + 0.5, b * s + 0.45))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(-0.35, a * s + 0.15); ax.set_ylim(-0.1, b * s + 0.35); ax.axis('off')
    for i in range(a // g):
        for j in range(b // g):
            ax.add_patch(Rectangle((i * g * s, j * g * s), g * s, g * s, fc=OR3 if (i + j) % 2 else OR2, ec=INK, lw=0.7))
    ax.text(a * s / 2, b * s + 0.12, f'{a}', ha='center', fontsize=9.5, weight='bold')
    ax.text(-0.18, b * s / 2, f'{b}', ha='center', va='center', rotation=90, fontsize=9.5, weight='bold')
    ok(a % g == 0 and b % g == 0)
    p = IMG / f'{name}.png'
    fig.savefig(p, dpi=300, facecolor='white'); plt.close(fig)
    return p.name


def rounds_table(a, b):
    rounds, g = euclid_rounds(a, b)
    rows = ['| Round | Divide | Quotient | Remainder | Next pair |', '|:-:|:-:|:-:|:-:|:-:|']
    for k, (A, B, q, r) in enumerate(rounds):
        nxt = f'({B}, {r})' + (' : stop, the remainder is 0' if r == 0 else '')
        rows.append(f'| {k + 1} | {A} ÷ {B} | {q} | **{r}** | {nxt} |')
        ok(A == q * B + r and 0 <= r < B)
    return '\n'.join(rows)


# ================================================================= the page
def euclid_page():
    IMG.mkdir(parents=True, exist_ok=True)
    shutil.copy(CH / 'images' / 'c05-flow-gcd-lcm.png', IMG / 'c05-flow-gcd-lcm.png')

    r30, g30, l30 = gcd_checked(30, 21)
    ok((g30, l30) == (3, 210) and len(r30) == 3)
    r54, g54, l54 = gcd_checked(54, 45)
    ok((g54, l54) == (9, 270) and len(r54) == 2)
    common = [sorted(set(divisors(x)) & set(divisors(y))) for x, y in [(30, 21), (21, 9), (9, 3)]]
    ok(common[0] == common[1] == common[2] == [1, 3])
    ok(30 - 21 == 9 == r30[0][3] and 21 - 2 * 9 == 3 == r30[1][3])

    t = head('Euclid\'s GCD', 'Step by step',
             'The printed book (section 5.3 and worked example W8) shows Euclid\'s method for 30 and 21 in one tile '
             'picture. This page shows every round, for seven pairs of numbers, with a picture of each round, and '
             'explains why the method always gives the right answer.')

    t += """## 1. The idea in one line

> **Divide the larger number by the smaller. Then divide the last divisor by the last remainder, again and again,
> until the remainder is 0. The last divisor (the last remainder that was not 0) is the GCD.**

The **GCD** (greatest common divisor, also called the HCF, highest common factor) of two numbers is the largest number
that divides both of them exactly. Euclid of Alexandria wrote this method down about 2,300 years ago, and every phone
still uses it (for example, inside the arithmetic that keeps online payments secret).

## 2. The tile picture: what one division means

Think of a floor **30 units long and 21 units wide** that must be covered with **square tiles, all of the same size, as
large as possible, with no tile cut**. The side of the largest such tile is the GCD of 30 and 21.

Euclid's method finds it by cutting squares. All three pictures are drawn to the **same scale**, so a 9 × 9 square
really is smaller than the 21 × 21 square:

"""
    t += img(round_panels(30, 21, 'c05-euclid-30-21'), 'Euclid for 30 and 21, round by round') + '\n\n'
    t += rounds_table(30, 21) + '\n\n'
    t += f"""- **Round 1.** 30 ÷ 21 = 1, remainder 9: the largest square that fits is 21 × 21, and **one** of it fits.
  A strip **9 wide** is left over (white, dashed).
- **Round 2.** Now only that strip, 21 by 9, is left. 21 ÷ 9 = 2, remainder 3: **two** squares of 9 × 9 fit, and a
  strip **3 tall** is left over.
- **Round 3.** The strip is 9 by 3. 9 ÷ 3 = 3, remainder 0: **three** squares of 3 × 3 fill it exactly.
- Nothing is left, so we stop. The last square has side **3**, so **GCD (30, 21) = {g30}**.

*Reading the pictures:* the numbers on the arrows are the lengths of the sides. The squares of each round are numbered
1, 2, 3 … because the **quotient is a count**: how many squares fit. The white dashed strip is the **remainder**, and
the curved arrow shows that it becomes the next rectangle. Grey, marked "done", is what earlier rounds already cut.

### A pair that finishes in two rounds: 54 and 45

The remainder can become 0 sooner. For 54 and 45, five 9 × 9 squares fill the first strip exactly:

"""
    t += img(round_panels(54, 45, 'c05-euclid-54-45'), 'Euclid for 54 and 45, round by round') + '\n\n'
    t += rounds_table(54, 45) + '\n\n'
    t += f"""**GCD (54, 45) = {g54}**; LCM = 54 × 45 ÷ {g54} = **{l54}**.

## 3. Why does it work?

Two facts are enough.

1. **A number that divides both 30 and 21 also divides their difference, 30 − 21 = 9.** If 30 and 21 are both made of
   3's, then taking 21 away from 30 leaves a number made of 3's too.
2. **A number that divides both 21 and 9 also divides 30**, because 30 = 21 + 9.

So the pair (30, 21) and the pair (21, 9) have **exactly the same common divisors**, and so has the next pair (9, 3):
the program found all three to be {", ".join(map(str, common[0]))}. Their largest is the same, so
GCD (30, 21) = GCD (21, 9) = GCD (9, 3) = 3.

Each round replaces the pair by a smaller pair with the same GCD. The numbers keep getting smaller, so the method must
stop, and when the remainder is 0, the last divisor divides the one before it exactly: it is the GCD.

*A division is only quick subtraction:* 21 ÷ 9 = 2 r 3 is "take 9 away from 21 twice". 1071 ÷ 462 = 2 r 147 is "take
462 away twice". That is why fact 1 (about the difference) is enough.

In the tile picture: a 3 × 3 tile covers the whole floor exactly, **10 across and 7 up**, so 3 divides both 30 and 21.
No larger square can: a 4 × 4 or 5 × 5 tile does not fit 21 exactly, and neither does anything else above 3.

"""
    t += img(grid_picture(30, 21, 3, 'c05-euclid-grid-30-21'), '30 by 21 covered by 3 by 3 tiles') + '\n\n'
    ok(30 // 3 == 10 and 21 // 3 == 7 and all(30 % d or 21 % d for d in range(4, 22)))

    t += '## 4. More pairs, round by round\n\n'
    pairs = [
        (84, 36, 'The pair in the printed Check yourself: two rounds.'),
        (1071, 462, 'Three rounds with large numbers. The 21 × 21 squares of the last round are tiny at this scale, so a fourth picture shows the last strip enlarged.'),
        (17, 5, 'The GCD can be 1: then the two numbers have no common factor except 1 (they are *co-prime*).'),
        (8, 8, 'Equal numbers: one round, and the GCD is the number itself.'),
        (12, 18, 'The smaller number first. Round 1 gives quotient 0 and simply swaps the numbers, so you need not '
                 'put the larger number first: the method does it for you.'),
    ]
    for a, b, why in pairs:
        rounds, g, lcm = gcd_checked(a, b)
        t += f'### {a} and {b}\n\n{why}\n\n'
        t += img(round_panels(a, b, f'c05-euclid-{a}-{b}'), f'Euclid for {a} and {b}') + '\n\n'
        t += rounds_table(a, b) + '\n\n'
        t += f'**GCD ({a}, {b}) = {g}**; LCM = {a} × {b} ÷ {g} = **{ind(lcm)}**.\n\n'
    ok(euclid_rounds(17, 5)[1] == 1 and euclid_rounds(12, 18)[0][0][2] == 0)

    # the printed flowchart and its full walk-through
    t += f'''## 5. The flowchart (worked example W8) and every step of it

The printed flowchart, with its numbered boxes. Box 3 keeps a copy of a and b (as x and y), because the loop changes a
and b, and the LCM needs the original numbers.

{img('c05-flow-gcd-lcm.png', 'Flowchart W8: GCD and LCM by Euclid’s method')}

The book prints the walk-through for a = 30, b = 21. Here it is for **a = 1071, b = 462**, every step, nothing left out:

| Step (box) | Pseudocode | What happens |
|:-:|---|---|
'''
    rows = F.GCD.walkthrough_rows([1071, 462], telling=False)
    for step, code, what in rows:
        t += f'| {step} | `{code}` | {what} |\n'
    out, _ = F.GCD.run([1071, 462])
    ok(out == ['21 23562'])
    t += '\nThe loop (boxes 4 to 7) ran three times, once for each round of the table in section 4.\n\n'

    # listing divisors vs Euclid
    t += '''## 6. Why not just list the divisors?

Listing every divisor of both numbers and picking the largest common one also works, but it needs one trial division
for every number from 1 up to each number. Euclid needs one division per round.

| Numbers | Trial divisions to list all divisors | Divisions by Euclid |
|:-:|:-:|:-:|
'''
    for a, b in [(30, 21), (54, 45), (84, 36), (1071, 462), (987, 610), (100000, 75000)]:
        rounds, g, _ = gcd_checked(a, b)
        t += f'| {ind(a)} and {ind(b)} | {ind(a + b)} | {len(rounds)} |\n'
    ok(len(euclid_rounds(987, 610)[0]) == 14)
    t += '''
*Beyond the syllabus:* 987 and 610 are two neighbouring numbers of the Fibonacci series (… 377, 610, 987 …), and such
pairs are the slowest of all for Euclid. Even so, it needs only 14 divisions.

'''

    # LCM
    small = [m for m in range(1, 210) if m % 30 == 0 and m % 21 == 0]
    ok(small == [] and 210 % 30 == 0 and 210 % 21 == 0 and 30 * 21 == 630)
    t += f'''## 7. The LCM from the GCD

**LCM = a × b ÷ GCD.** For 30 and 21: 30 × 21 = {30 * 21}, and {30 * 21} ÷ 3 = **210**.

*Check:* 210 ÷ 30 = 7 and 210 ÷ 21 = 10, both exact, so 210 is a common multiple; and the program tried every number
below 210: none is a multiple of both.

*Why it works:* 30 = 3 × 10 and 21 = 3 × 7. The product 30 × 21 = 3 × 10 × 3 × 7 counts the common part, 3, **twice**;
dividing by the GCD once leaves 3 × 10 × 7 = 210, which has each part just once.

## 8. Common mistakes

| Mistake | Why it is wrong | Right |
|---|---|---|
| Stopping when the remainder is 0 and giving **0** (or the last quotient) as the GCD | 0 is what tells you to stop; it is not the answer | the **last divisor** (the last non-zero remainder) |
| Dividing the remainder by the divisor (9 ÷ 21) | the roles must move one place to the left each round | divide the **last divisor** by the **last remainder** (21 ÷ 9) |
| Giving the GCD when the LCM is asked | the GCD is the largest common **divisor**, the LCM the smallest common **multiple** | LCM = a × b ÷ GCD |
| Forgetting to keep a and b for the LCM in the flowchart | the loop changes a and b | keep copies first (box 3 of W8) |

## 9. Try it yourself

'''
    for a, b in [(48, 18), (391, 299), (35, 64)]:
        rounds, g, lcm = gcd_checked(a, b)
        steps = '; '.join(f'{A} ÷ {B} = {q} r {r}' for A, B, q, r in rounds)
        t += f'**Find the GCD and LCM of {a} and {b}.**\n\n??? success "Answer"\n    {steps}. '
        t += f'**GCD = {g}**, LCM = {a} × {b} ÷ {g} = **{ind(lcm)}**.\n\n'
    write('step-by-step-euclid-gcd.md', t)


if __name__ == '__main__':
    euclid_page()
    print(checks, 'checks passed')
