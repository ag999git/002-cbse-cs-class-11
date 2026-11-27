"""Chapter 6 cheat sheet (QR 0621; cheat sheets approved 27 Nov 2026): one printable A4 page, made by program.
Every code example is RUN here and its real output printed beside it; the keyword grid is Python's own kwlist.
Writes:  book/assets/cheatsheets/ch06-cheat-sheet.html  (A4, printed to PDF by headless Chrome)
         book/assets/cheatsheets/ch06-cheat-sheet.pdf   (must be exactly 1 page: checked with pdfinfo)
         book/unit-2/006-ch06-getting-started-with-python/revise-cheat-sheet.md  (the same content as a web page)
Run from the repository root:  python tools/ch06_cheatsheet.py"""
import html
import keyword
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python'
CS = ROOT / 'book' / 'assets' / 'cheatsheets'
CS.mkdir(parents=True, exist_ok=True)
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PYV = sys.version.split()[0]
checks = 0


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def run(src):
    r = subprocess.run([sys.executable, '-I', '-c', src], capture_output=True, text=True, encoding='utf-8')
    err = r.stderr.strip().splitlines()
    return r.stdout.rstrip('\n'), (err[-1] if err else '')


def ex(src):
    o, e = run(src)
    ok(e == '', (src, e))
    return (src, o)


def er(src):
    o, e = run(src)
    ok(e != '', src)
    return (src, e.split(':')[0] + ':' + ':'.join(e.split(':')[1:])[:60])


KW = sorted(keyword.kwlist, key=str.lower)
ok(len(KW) == 35)

# Each box: (title, list of parts); a part is ('t', text) or ('c', (code, output)) or ('tab', rows)
BOXES = [
    ('Running Python', [
        ('t', '<b>Shell</b> (interactive): <code>&gt;&gt;&gt;</code> one statement, answered at once; not saved.'),
        ('t', '<b>Script</b>: File → New File, save as <code>name.py</code>, <b>F5</b> (Run Module); output in the shell.'),
        ('c', ex('print("Hello", 11)')),
        ('t', 'In a script a bare <code>7 + 5</code> shows nothing; the shell and the last line of a Colab cell show it.'),
        ('t', 'Read an error message: the <b>last line</b> first, then the line number.'),
    ]),
    ('Interactive or script?', [
        ('tab', [('Where', 'the shell, after <code>&gt;&gt;&gt;</code> · the editor, a <code>.py</code> file'),
                 ('Runs', 'one statement at once · the whole file'),
                 ('Saved?', 'no · yes'),
                 ('<code>7 + 5</code>', 'value shown · nothing (use <code>print</code>)'),
                 ('Best for', 'trying a line · programs')]),
    ]),
    ('Expression or statement?', [
        ('t', 'An <b>expression</b> gives a value: <code>7 + 5</code>, <code>price * 2</code>, <code>marks &gt;= 33</code>.'),
        ('t', 'A <b>statement</b> does something: <code>total = price * 2</code>, <code>import math</code>, <code>pass</code>.'),
        ('t', 'Long statement: continue it inside brackets <code>( )</code>; avoid <code>;</code> between statements.'),
    ]),
    ('Tokens: the five kinds', [
        ('tab', [('keyword', '<code>if</code> <code>for</code> <code>True</code> <code>and</code>'),
                 ('identifier', '<code>marks</code> <code>print</code>'),
                 ('literal', '<code>33</code> <code>"Pass"</code> <code>2.5e3</code>'),
                 ('operator', '<code>+ &gt;= = //</code>'),
                 ('punctuator', '<code>( ) [ ] , : .</code>')]),
        ('t', 'A comment is <b>not</b> a token: Python skips it. <code>if marks &gt;= 33: print("Pass")</code> has 9 tokens.'),
    ]),
    ('The 35 keywords', [('kw', KW),
                         ('t', 'Only <code>True</code>, <code>False</code>, <code>None</code> begin with a capital. '
                               '<code>print</code> is <b>not</b> a keyword.')]),
    ('Names (identifiers)', [
        ('t', '<b>Rules</b> (else an error): begin with a letter or <code>_</code>; then letters, digits, <code>_</code> '
              'only (no space, <code>$ - . @</code>); not a keyword; case counts; any length.'),
        ('t', '<b>Conventions</b> (PEP 8): <code>total_marks</code> (snake_case); <code>PASS_MARK</code> for constants; '
              'never <code>l O I</code> alone; 4 spaces per indent.'),
    ]),
    ('Literals', [
        ('c', ex('print(type(33), type("33"))')),
        ('c', ex('print(type(3.5), type(None))')),
        ('c', ex('print(0b101, 0o17, 0x1F, 2.5e3)')),
        ('c', ex('print(len("a\\tb\\n"))')),
        ('t', '<code>\\n</code> new line, <code>\\t</code> tab: one character each.'),
    ]),
    ('Variables: a name tied to an object', [
        ('c', ex('x = 3\ny = x\nx = x + 2\nprint(x, y)')),
        ('c', ex('a = b = 0\nx, y = 5, 7\nx, y = y, x\nprint(a, b, x, y)')),
        ('c', ex('n = 5\nn = "five"\nprint(type(n))')),
        ('t', '<b>L-value</b> (left of <code>=</code>): a name. <b>R-value</b>: anything that gives a value. '
              '<code>=</code> means "becomes", not "equals". Dynamic typing: the <b>object</b> has the type.'),
    ]),
    ('Comments and notes', [
        ('c', ex('# a note for people\nprint("ok")  # an inline comment')),
        ('t', 'Several lines: <code>#</code> on each, or <code>"""</code> … <code>"""</code> (a docstring at the top).'),
    ]),
    ('First errors', [('err', [er('Print("Hi")'), er('print("Hi"'), er('x = 5\n  y = 6'), er('class = 5'),
                               er('print("A" + 1)')])]),
]


def html_box(title, parts):
    t = f'<div class="box"><h2>{html.escape(title)}</h2>'
    for kind, p in parts:
        if kind == 't':
            t += f'<p>{p}</p>'
        elif kind == 'c':
            src, o = p
            t += f'<div class="code"><pre>{html.escape(src)}</pre><pre class="out">{html.escape(o)}</pre></div>'
        elif kind == 'tab':
            t += '<table>' + ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a, b in p) + '</table>'
        elif kind == 'kw':
            t += '<div class="kw">' + ''.join(f'<code>{k}</code>' for k in p) + '</div>'
        elif kind == 'err':
            t += '<table class="err">' + ''.join(f'<tr><td><code>{html.escape(s).replace(chr(10), "<br>").replace("  ", "&nbsp;&nbsp;")}</code></td>'
                                                f'<td>{html.escape(e)}</td></tr>' for s, e in p) + '</table>'
    return t + '</div>'


CSS = '''@page { size: A4; margin: 9mm; }
body { font-family: Calibri, "Segoe UI", sans-serif; font-size: 10.2pt; color: #262626; margin: 0; }
h1 { font-size: 15pt; color: #C55A11; margin: 0 0 1mm 0; border-bottom: 1.5pt solid #C55A11; }
.sub { font-size: 8pt; color: #555; margin: 0 0 2mm 0; }
.cols { column-count: 3; column-gap: 4mm; column-fill: balance; }
.box { break-inside: avoid; border: 0.8pt solid #C55A11; border-radius: 2mm; padding: 1.5mm 2mm; margin: 0 0 2.5mm 0; }
h2 { font-size: 11pt; color: #fff; background: #C55A11; margin: -1.5mm -2mm 1.5mm -2mm; padding: 0.8mm 2mm; border-radius: 1.6mm 1.6mm 0 0; }
p { margin: 0 0 1.2mm 0; }
code, pre { font-family: Consolas, monospace; font-size: 9.2pt; }
.code { display: flex; gap: 1.5mm; margin: 0 0 1.2mm 0; }
.code pre { margin: 0; background: #FDF1E9; padding: 1mm 1.5mm; border-radius: 1mm; flex: 3; white-space: pre-wrap; }
.code pre.out { background: #fff; border: 0.6pt solid #bbb; flex: 2; color: #C55A11; }
table { border-collapse: collapse; width: 100%; margin: 0 0 1mm 0; }
td { border-bottom: 0.5pt solid #e0e0e0; padding: 0.4mm 1mm; vertical-align: top; }
.err td:last-child { color: #C55A11; font-size: 8.6pt; }
.kw { display: grid; grid-template-columns: repeat(4, auto); justify-content: space-between; gap: 0.6mm 0.8mm; margin-bottom: 1.2mm; }
.kw code { background: #F8CBAD; padding: 0.3mm 0.8mm; border-radius: 0.8mm; font-size: 8.4pt; }
.foot { font-size: 7.5pt; color: #777; margin-top: 1mm; }'''


def build_html():
    t = ('<!doctype html><html><head><meta charset="utf-8"><title>Chapter 6 cheat sheet</title>'
         f'<style>{CSS}</style></head><body>'
         '<h1>Chapter 6 · Getting Started with Python · Cheat sheet</h1>'
         f'<p class="sub">Computer Science with Python, CBSE Class XI. Every example was run in Python {PYV}; the output is '
         'shown on the right of each code box.</p><div class="cols">')
    t += ''.join(html_box(a, b) for a, b in BOXES)
    t += ('</div><p class="foot">© 2026 Anurag Gupta · Online companion: ag999git.github.io/002-cbse-cs-class-11 · '
          'Print on one A4 sheet.</p></body></html>')
    (CS / 'ch06-cheat-sheet.html').write_text(t, encoding='utf-8')


def build_pdf():
    pdf = CS / 'ch06-cheat-sheet.pdf'
    import tempfile                                  # Chrome's profile: never inside the repository
    prof = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.gettempdir()) / 'ch06-chrome-prof'
    r = subprocess.run([CHROME, '--headless=new', f'--user-data-dir={prof}', '--no-first-run', '--disable-gpu',
                        '--no-pdf-header-footer', f'--print-to-pdf={pdf}', (CS / 'ch06-cheat-sheet.html').as_uri()],
                       capture_output=True, text=True, timeout=90)
    ok(pdf.exists(), r.stderr[-300:])
    info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
    pages = int(next(l.split()[-1] for l in info.splitlines() if l.startswith('Pages:')))
    ok(pages == 1, f'the cheat sheet has {pages} pages')
    return pages


def build_page():
    t = ('# Revise: Chapter 6 cheat sheet\n\n*Chapter 6 · Revise. The whole chapter on one A4 page, to print and keep. '
         'Every example on it was run in Python.*\n\n'
         '[Download the printable A4 sheet (PDF)](../../assets/cheatsheets/ch06-cheat-sheet.pdf){ .md-button .md-button--primary }\n\n')
    for title, parts in BOXES:
        t += f'## {title}\n\n'
        for kind, p in parts:
            if kind == 't':
                txt = p.replace('<b>', '**').replace('</b>', '**').replace('<code>', '`').replace('</code>', '`')
                txt = txt.replace('&gt;', '>').replace('&lt;', '<')
                t += f'{txt}\n\n'
            elif kind == 'c':
                src, o = p
                t += f'```python\n{src}\n```\n\n*Output:* `{o}`\n\n'
            elif kind == 'tab':
                t += '| Kind | Examples |\n|---|---|\n' + ''.join(
                    f'| {a} | {b.replace("<code>", "`").replace("</code>", "`").replace("&gt;", ">")} |\n' for a, b in p) + '\n'
            elif kind == 'kw':
                t += ' '.join(f'`{k}`' for k in p) + '\n\n'
            elif kind == 'err':
                t += '| Program | Python says |\n|---|---|\n' + ''.join(
                    '| ' + '<br>'.join(f'`{l.strip()}`' if l.strip() else '' for l in s.split('\n')) + f' | `{e}` |\n' for s, e in p) + '\n'
    (D / 'revise-cheat-sheet.md').write_text(t, encoding='utf-8')


if __name__ == '__main__':
    build_html()
    build_page()
    n = build_pdf()
    print(f'cheat sheet: {n} page; {checks} checks, 0 wrong (Python {PYV})')
