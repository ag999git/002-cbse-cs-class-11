"""Boolean expressions in the book's notation, computed instead of typed (24 Nov 2026).

Notation: A' NOT (prime after a letter or a bracket), · AND (also *, or letters side by side: AB), + OR, ⊕ XOR,
brackets. Precedence: brackets, NOT, AND, OR (B-N-A-O); XOR at OR level.

    e = parse("(A·B + C')'")
    show(e)                     -> "(A·B + C')'"
    rows(e)                     -> [(inputs tuple, value), ...] in counting order
    complement_steps(e)         -> list of lines: F' = ..., = ... (De Morgan, one level at a time), final
    dual(e)                     -> the dual (swap + and ·, swap 0 and 1)
    equal(e1, e2)               -> True if they agree in every row
    draw(e, path)               -> logic circuit PNG (Schemdraw)
"""
import itertools
import re


# ------------------------------------------------------------------ tree
class Var:
    def __init__(self, n): self.n = n
class Const:
    def __init__(self, v): self.v = v
class Not:
    def __init__(self, a): self.a = a
class And:
    def __init__(self, *xs): self.xs = list(xs)
class Or:
    def __init__(self, *xs): self.xs = list(xs)
class Xor:
    def __init__(self, *xs): self.xs = list(xs)


def parse(s):
    toks = re.findall(r"[A-Za-z]|[01]|[()+·*⊕']", s.replace('.', '·'))
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def eat(t=None):
        tok = toks[pos[0]]
        assert t is None or tok == t, (tok, t, s)
        pos[0] += 1
        return tok

    def expr():
        xs, ops = [term()], []
        while peek() in ('+', '⊕'):
            ops.append(eat()); xs.append(term())
        if not ops:
            return xs[0]
        # group: XOR and OR at the same level, left to right
        node = xs[0]
        for op, x in zip(ops, xs[1:]):
            if op == '+':
                node = Or(*(node.xs if isinstance(node, Or) else [node]), x)
            else:
                node = Xor(*(node.xs if isinstance(node, Xor) else [node]), x)
        return node

    def term():
        xs = [factor()]
        while peek() is not None and (peek() in ('·', '*') or peek().isalpha() or peek() in '(01'):
            if peek() in ('·', '*'):
                eat()
            xs.append(factor())
        return xs[0] if len(xs) == 1 else And(*xs)

    def factor():
        t = peek()
        if t == '(':
            eat('('); node = expr(); eat(')')
        elif t in ('0', '1'):
            eat(); node = Const(int(t))
        else:
            node = Var(eat().upper())
        while peek() == "'":
            eat(); node = Not(node)
        return node

    e = expr()
    assert pos[0] == len(toks), ('unparsed', s)
    return e


def names(e):
    if isinstance(e, Var): return {e.n}
    if isinstance(e, Const): return set()
    if isinstance(e, Not): return names(e.a)
    return set().union(*(names(x) for x in e.xs))


def ev(e, env):
    if isinstance(e, Var): return env[e.n]
    if isinstance(e, Const): return e.v
    if isinstance(e, Not): return 1 - ev(e.a, env)
    vals = [ev(x, env) for x in e.xs]
    if isinstance(e, And): return int(all(vals))
    if isinstance(e, Or): return int(any(vals))
    return sum(vals) % 2


PREC = {Or: 1, Xor: 1, And: 2}


def show(e, parent=0, dot=True):
    """Book notation. dot=True writes A·B; dot=False writes AB."""
    if isinstance(e, Var): return e.n
    if isinstance(e, Const): return str(e.v)
    if isinstance(e, Not):
        inner = show(e.a, 3, dot)
        return (inner if isinstance(e.a, (Var, Const, Not)) else f'({show(e.a, 0, dot)})') + "'"
    p = PREC[type(e)]
    sep = {Or: ' + ', Xor: ' ⊕ ', And: '·' if dot else ''}[type(e)]
    txt = sep.join(show(x, p, dot) for x in e.xs)
    return f'({txt})' if p < parent else txt


def rows(e, order=None):
    vs = order or sorted(names(e))
    return [(combo, ev(e, dict(zip(vs, combo)))) for combo in itertools.product((0, 1), repeat=len(vs))]


def equal(a, b):
    vs = sorted(names(a) | names(b))
    return all(ev(a, dict(zip(vs, c))) == ev(b, dict(zip(vs, c))) for c in itertools.product((0, 1), repeat=len(vs)))


# ------------------------------------------------------------------ complement and dual
def push(e):
    """NOT pushed all the way in (De Morgan everywhere): the complement of e, with primes only on letters."""
    if isinstance(e, Var): return Not(e)
    if isinstance(e, Const): return Const(1 - e.v)
    if isinstance(e, Not): return strip(e.a)
    if isinstance(e, And): return Or(*[push(x) for x in e.xs])
    if isinstance(e, Or): return And(*[push(x) for x in e.xs])
    raise ValueError('XOR: complement it as XNOR')


def strip(e):
    """e with every NOT of a bracket opened (so double primes vanish): the same function, primes only on letters."""
    if isinstance(e, (Var, Const)): return e
    if isinstance(e, Not): return push(e.a)
    return type(e)(*[strip(x) for x in e.xs])


def flatten(e):
    if isinstance(e, (Var, Const)): return e
    if isinstance(e, Not): return Not(flatten(e.a))
    xs = []
    for x in (flatten(x) for x in e.xs):
        xs += x.xs if type(x) is type(e) else [x]
    return type(e)(*xs)


def one_level(e):
    """(e)' with De Morgan applied once, at the top: (X + Y)' -> X'·Y' where X and Y keep their insides."""
    if isinstance(e, And): return Or(*[Not(x) if not isinstance(x, Not) else x.a for x in e.xs])
    if isinstance(e, Or): return And(*[Not(x) if not isinstance(x, Not) else x.a for x in e.xs])
    if isinstance(e, Not): return e.a
    return Not(e)


def complement_steps(e):
    """Lines of a worked answer: F' = (F)', then De Morgan at the top, then every bracket opened."""
    f = Not(e)
    lines = [show(f)]
    a = one_level(e)
    if show(a) not in lines:
        lines.append(show(a))
    final = flatten(push(e))
    if show(final) not in lines:
        lines.append(show(final))
    assert equal(final, f), 'complement check failed'
    return lines


def dual(e):
    if isinstance(e, Var): return e
    if isinstance(e, Const): return Const(1 - e.v)
    if isinstance(e, Not): return Not(dual(e.a))
    if isinstance(e, And): return Or(*[dual(x) for x in e.xs])
    if isinstance(e, Or): return And(*[dual(x) for x in e.xs])
    raise ValueError('no dual for XOR here')


# ------------------------------------------------------------------ truth table as markdown, with step columns
def steps(e):
    """Sub-expressions in the order they are worked out (inside out), without the plain letters."""
    out = []

    def walk(x):
        if isinstance(x, (Var, Const)):
            return
        if isinstance(x, Not):
            walk(x.a)
        else:
            for y in x.xs:
                walk(y)
        s = show(x)
        if s not in out:
            out.append(s)
    walk(e)
    return out


def table_md(e, out_name='F', include_steps=True):
    vs = sorted(names(e))
    cols = [parse(s) for s in (steps(e) if include_steps else [show(e)])]
    head = vs + [show(c) for c in cols[:-1]] + [f'{out_name} = {show(e)}']
    lines = ['| ' + ' | '.join(head) + ' |', '|' + ':-:|' * len(head)]
    for combo in itertools.product((0, 1), repeat=len(vs)):
        env = dict(zip(vs, combo))
        lines.append('| ' + ' | '.join([str(v) for v in combo] + [str(ev(c, env)) for c in cols]) + ' |')
    return '\n'.join(lines)


# ------------------------------------------------------------------ circuit drawing
def to_schemdraw(e):
    if isinstance(e, Var): return e.n
    if isinstance(e, Const): return str(e.v)
    if isinstance(e, Not):
        return f'(not {to_schemdraw(e.a)})'
    op = {And: ' and ', Or: ' or ', Xor: ' xor '}[type(e)]
    return '(' + op.join(to_schemdraw(x) for x in e.xs) + ')'


def draw(e, path, out_label='F', reveal=True):
    """reveal=False writes only the output name (for 'write the expression of this circuit' questions)."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import schemdraw
    from schemdraw.parsing import logicparse
    schemdraw.config(fontsize=14, lw=1.6)
    d = logicparse(to_schemdraw(e), outlabel=f'{out_label} = {show(e)}' if reveal else out_label, gateH=1.6, gateW=2.2)
    d.save(str(path), dpi=300)
    plt.close('all')


if __name__ == '__main__':
    for s in ["(A·B + C')'", "A + B'C", "(A + B)(A' + C)", "AB + A'C + BC", "(X + Y)'·Z"]:
        e = parse(s)
        print(show(e), '| complement:', ' = '.join(complement_steps(e)), '| dual:', show(dual(e)))
