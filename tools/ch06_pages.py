"""Chapter 6 online pages, part 1: the explanation pages (27 Nov 2026; online plan v2 approved, O1-O8).
0602 story and versions · 0603 limits · 0604 install Python, VS Code, Jupyter · 0605 five tools, one program ·
0606 where does my code run? · 0607 when things go wrong · 0608 AI assistants · 0610 reading an error message ·
0611 statements over several lines · 0613 all 35 keywords · 0615 PEP 8 and PEPs · 0616 literals up close ·
0619 notes for people.
Every output, error message, keyword list and drill answer on these pages is made here by running Python; flowcharts
are drawn and checked by 50-tools/flow_layout + algo_lib (no crossings); drawn pictures by matplotlib.
Run from the repository root:  python tools/ch06_pages.py"""
import ast
import contextlib
import io
import keyword
import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent.parent
sys.path.insert(0, str(PROJECT / '50-tools'))
from flow_layout import Builder  # noqa: E402

D = ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python'
IMG = ROOT / 'book' / 'assets' / 'images' / 'ch06'
IMG.mkdir(parents=True, exist_ok=True)
REL = '../../assets/images/ch06'
PYV = sys.version.split()[0]
checks = 0


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def head(title, label, intro):
    return f'# {label}: {title}\n\n*Chapter 6 · {label}. {intro}*\n\n'


def write(name, text):
    (D / name).write_text(text, encoding='utf-8')
    print('wrote', name)


def pic(name, alt, scale=1.25, cap=720):
    from PIL import Image
    w = min(cap, int(Image.open(IMG / name).width * 96 * scale / 300))
    return f'![{alt}]({REL}/{name}){{ width="{w}" }}'


def chart(name, title, steps):
    a = Builder(name, title, steps).build()
    a.check()
    ok(not a.crossings(), name)
    p, w, h = a.draw(IMG)
    return a, p.name


def numbered(a):
    out = []
    for nd in sorted(a.nodes, key=lambda n: n.num):
        t = nd.text.replace('\n', ' ')
        if nd.kind == 'decision':
            t += f' Yes: go to {nd.yes}. No: go to {nd.no}.'
        elif nd.next and nd.next != nd.num + 1:
            t += f'; go to {nd.next}.'
        elif not t.endswith(('.', '?', '!')):
            t += '.'
        out.append(f'{nd.num}. {t}')
    return '\n'.join(out)


def run_script(src):
    """Run a script in a fresh Python; return (stdout, last line of stderr)."""
    r = subprocess.run([sys.executable, '-I', '-c', src], capture_output=True, text=True, encoding='utf-8')
    err = r.stderr.strip().splitlines()
    return r.stdout, (err[-1] if err else '')


def run_ok(src):
    out, err = run_script(src)
    ok(err == '', f'{src!r} gave {err}')
    return out


def code(src, lang='python'):
    return f'```{lang}\n{src.rstrip()}\n```\n'


def cell(src):
    """Code for a table cell: each line in backticks, lines joined by <br>, indentation as &nbsp; outside the code."""
    parts = []
    for ln in src.split('\n'):
        n = len(ln) - len(ln.lstrip(' '))
        if not ln.strip():
            parts.append('&nbsp;')
            continue
        parts.append('&nbsp;' * n + '`' + ln.lstrip(' ').replace('|', '\\|') + '`')
    return '<br>'.join(parts)


def run_block(src):
    """A code block followed by its real output."""
    out = run_ok(src)
    return code(src) + '\n*Output:*\n\n' + code(out, 'text')


# ================================================================= 0602
def story():
    out, err = run_script('print "Hi"')
    ok(err.startswith('SyntaxError'), err)
    t = head('Python\'s story and versions', 'Helps you understand',
             'The printed chapter has a timeline of Python\'s life. Here is the story behind it, why old Python 2 '
             'programs fail today, and how to find your own version.')
    t += f'''## The story in short

| When | What happened |
|---|---|
| Dec 1989 | Guido van Rossum, a Dutch programmer, starts Python during the Christmas holidays as a hobby project |
| Feb 1991 | The first public release, version 0.9.0 |
| 1994 | Version 1.0 |
| 2000 | Python 2.0 |
| Dec 2008 | **Python 3.0**: a big clean-up; some old programs no longer run |
| 1 Jan 2020 | **Python 2 retired**: no more fixes, even for security |
| Oct 2024 | Python 3.13, with a new, coloured shell |
| Oct 2026 | **Python 3.15**, the latest at the time of this book |

**Where the ideas came from.** Python grew out of **ABC**, a teaching language Guido worked on in the 1980s: easy to
read, with indentation instead of brackets. It also borrowed ideas from **Modula-3**. The name comes from the British
comedy show *Monty Python's Flying Circus*, not from the snake.

## Python 2 vs Python 3: why an old program fails

Many old books and websites still show Python 2. The most visible difference is `print`. In Python 2 it was a
statement; in Python 3 it is a **function**, so it needs brackets.

{code('print "Hi"        # Python 2: no brackets')}
Python 3 refuses it at once:

{code(err, 'text')}
| Basis of difference | Python 2 (retired 2020) | Python 3 (today) |
|---|---|---|
| `print` | a statement: `print "Hi"` | a function: `print("Hi")` |
| `7 / 2` | `3` (whole-number division) | `3.5` (true division); `7 // 2` gives `3` |
| Text | ASCII by default | **Unicode** by default: `"नमस्ते"` works everywhere |
| Support | none since 1 Jan 2020 | new version every October |

*If a program from a book or website will not run, look first for `print` without brackets.*

## Which version do I have?

In a terminal (Command Prompt or PowerShell on Windows):

{code('python --version', 'text')}
Inside Python (the shell, a script or a Colab cell):

{code('import sys' + chr(10) + 'print(sys.version)')}
On the computer that checked this page, it printed `{PYV}`. **This book needs Python 3.12 or later.** Every program in it
was run on 3.12; newer versions may word a few error messages slightly differently.

## Why the version numbers matter in the exam

They do not, except two facts: **Python 3** is the Python of the syllabus, and **Guido van Rossum** created it.
'''
    write('helps-story-and-versions.md', t)


# ================================================================= 0603
def limits():
    for src in ('x = 5' + chr(10) + 'x = "five"', ):
        run_ok(src)
    out, err = run_script('print("5" + 3)')
    ok(err.startswith('TypeError'), err)
    t = head("Python's limits", 'Helps you understand',
             'The printed chapter lists the features of Python. Every language also has limits. Here are Python\'s, '
             'why each one exists, and why it rarely matters at school.')
    t += f'''| Limit | Why it exists | Does it matter at school? |
|---|---|---|
| **Slower than C or C++** for heavy calculation | Python's interpreter reads and runs your statements one at a time while the program runs; a C++ compiler turns the whole program into machine code first | Hardly ever: your programs finish in a blink. Big Python libraries (NumPy, used in science) run their heavy parts in C to get the speed back |
| **Fewer ready-made libraries for some jobs** (for example, fast mobile games or device drivers) | Each language grew where its users were: C for operating systems, Java for Android apps, Python for data, AI and teaching | No |
| **Not easy to convert** to another language | Python's short, flexible statements (no declared types, indentation for blocks) have no one-to-one match in C or Java | No |
| **Types are not fixed on names** (some books: "not strong on type-binding") | This is **dynamic typing** (section 6.7): a name can be tied to an `int` now and a `str` later | Yes, a little: a mix-up of types shows only when that line runs |

## "Not strong on type-binding" is not "weakly typed"

Some books list "not strong on type-binding" as a minus. It means only that a **name** has no fixed type: the box-or-tag
idea of section 6.7. It does **not** mean Python mixes types carelessly. Python refuses to add text to a number:

{code('print("5" + 3)')}
{code(err, 'text')}
So Python is **dynamically** typed (names have no type) but **strongly** typed (values are never mixed quietly). In
the exam: "Python is dynamically typed"; never "Python is weakly typed".
'''
    write('helps-python-limits.md', t)


# ================================================================= 0604
def install():
    a1, i1 = chart('c06-flow-install-python', 'Installing Python with the Python install manager', [
        ('do', 'a = 1', {'text': 'Go to python.org;\nDownloads; Windows'}),
        ('do', 'b = 1', {'text': 'Download the Python\ninstall manager'}),
        ('do', 'c = 1', {'text': 'Open the file;\nselect Install'}),
        ('do', 'd = 1', {'text': 'Open a terminal;\ntype python'}),
        ('do', 'e = 1', {'text': 'Say Yes to the\nPATH question'}),
        ('if', 'v', [('out', 'r', {'text': 'Ready: open IDLE'})],
         [('out', 'h', {'text': 'See "When things\ngo wrong"'})],
         {'text': 'python --version\nshows 3.12+?'})])
    a2, i2 = chart('c06-flow-install-vscode', 'Installing VS Code for Python', [
        ('do', 'a = 1', {'text': 'Download VS Code\nfrom its own site'}),
        ('do', 'b = 1', {'text': 'Install it (keep\n"Add to PATH")'}),
        ('do', 'c = 1', {'text': 'Extensions: install\n"Python" (Microsoft)'}),
        ('do', 'd = 1', {'text': 'Open a folder; new\nfile hello.py'}),
        ('do', 'e = 1', {'text': 'Select the Python\ninterpreter'}),
        ('if', 'v', [('out', 'r', {'text': 'Ready'})],
         [('out', 'h', {'text': 'See "When things\ngo wrong"'})],
         {'text': 'Run shows the\noutput below?'})])
    a3, i3 = chart('c06-flow-install-jupyter', 'Installing and starting Jupyter', [
        ('do', 'a = 1', {'text': 'Open a terminal'}),
        ('do', 'b = 1', {'text': 'Type: py -m pip\ninstall notebook'}),
        ('do', 'c = 1', {'text': 'Type: py -m\nnotebook'}),
        ('do', 'd = 1', {'text': 'The browser opens\nat localhost:8888'}),
        ('do', 'e = 1', {'text': 'New; Python 3:\na notebook opens'}),
        ('if', 'v', [('out', 'r', {'text': 'Ready'})],
         [('out', 'h', {'text': 'See "When things\ngo wrong"'})],
         {'text': 'A cell runs with\nShift+Enter?'})])
    t = head('Install Python, VS Code and Jupyter on Windows', 'Step by step',
             'The printed chapter shows five tools in one table. Here are the three installs, each as numbered steps '
             'and as a flowchart with the same numbers. Google Colab needs no install: only a Google sign-in.')
    t += '''!!! warning "Cyber link (Chapter 18)"
    Download only from the makers' own sites: **python.org**, **code.visualstudio.com**. "Free Python" or "Python
    setup" files on other sites can carry malware.

## 1. Python itself

Since Python 3.14 the makers recommend the **Python install manager**, a small program that installs Python and keeps
it up to date. (The older full installer, a `.exe` with an "Add python.exe to PATH" box on its first screen, is still
offered for Python 3.15 and earlier, and stops with 3.16.) The same install manager is also in the Microsoft Store.

''' + numbered(a1) + '\n\n' + pic(i1, 'Installing Python', 1.0) + '''

**What "PATH" means.** PATH is the list of folders where Windows looks for a command. If Python's folder is on the list,
typing `python` in any terminal finds it; if not, Windows says it does not know the command. Saying **Yes** to the PATH
question saves trouble later.

**Starting IDLE.** Search for **IDLE** in the Start menu. If it is not there, type this in a terminal; it opens IDLE too:

```text
py -m idlelib
```

## 2. VS Code, for bigger projects

''' + numbered(a2) + '\n\n' + pic(i2, 'Installing VS Code', 1.0) + '''

**Selecting the interpreter** tells VS Code which Python to use: press **Ctrl+Shift+P**, type `Python: Select
Interpreter`, and choose the Python you installed in part 1. VS Code itself does not run Python; it hands your file
to that Python, and the output appears in the **terminal** panel at the bottom.

## 3. Jupyter Notebook, for notebooks without the internet

''' + numbered(a3) + '\n\n' + pic(i3, 'Installing Jupyter', 1.0) + '''

**What these commands mean.**

- `pip` is Python's own installer for extra packages; `py -m pip install notebook` asks it to fetch Jupyter Notebook.
- `py -m notebook` starts a small **Jupyter server** on your own computer and opens your browser at
  `http://localhost:8888`. "localhost" means *this computer*: nothing leaves it.
- Keep the terminal window open while you work; closing it stops the server.

## 4. Google Colab: no install

Open **colab.research.google.com** in a browser and sign in with a Google account. Your code runs on Google's
computers, and your notebooks are saved in your Google Drive (folder *Colab Notebooks*). The page "Five places to write
Python" shows how to use it.

## Anaconda: you may hear of it

**Anaconda** is a large "distribution": Python plus hundreds of extra packages, Jupyter and the Spyder editor, in one
download. Scientists like it. **For Class XI we do not recommend it**: it is a very large download, school labs and the
practical exam use the Python from python.org, and it installs a **second** Python beside the first, so a beginner may
not know which one is running.
'''
    write('step-install-python-vscode-jupyter.md', t)


# ================================================================= 0605
def five_tools():
    prog = 'name = "Asha"\nmarks = 92\nprint(name, "scored", marks)'
    out = run_ok(prog)
    t = head('Five places to write Python, one program', 'Step by step',
             'The printed chapter compares five tools in Table 6.3. Here is how to use each one, with the same three-line '
             'program in all five, so you can see they give the same answer.')
    t += '## The program\n\n' + run_block(prog) + '''
## IDLE (comes with Python): the exam tool

1. Start **IDLE**: the shell opens.
2. **File → New File**: the editor opens.
3. Type the program; **File → Save** as `asha.py`.
4. **Run → Run Module** (or **F5**). The output appears in the **shell** window.

## Thonny: made for beginners

1. Install Thonny from **thonny.org** (it brings its own Python).
2. Type the program in the top pane; save it.
3. Press the green **Run** button. The output appears in the **Shell** pane below.
4. Try **View → Variables**: Thonny shows `name` and `marks` with their values as the program runs.

## VS Code: for bigger projects

1. **File → Open Folder**: choose a folder for your programs.
2. **New File** → `asha.py`; type the program; save (**Ctrl+S**).
3. Press **Run ▷** (top right). The output appears in the **terminal** panel at the bottom.

## Jupyter Notebook: cells on your own computer

1. Start Jupyter (`py -m notebook`); in the browser, **New → Python 3**.
2. Type the program in the first **cell**.
3. Press **Shift+Enter**: the output appears just below the cell.
4. **File → Save** keeps a `.ipynb` file on your computer.

## Google Colab: cells in the cloud

1. Open **colab.research.google.com**; sign in; **New notebook**.
2. Type the program in the cell; press **Shift+Enter** (or the round ▶ button).
3. The output appears below the cell. The notebook is saved in your Google Drive.
4. **Share** gives a link, like a Google Doc, for your teacher.

## The same answer everywhere

''' + f'All five print exactly:\n\n{code(out, "text")}' + '''
The **tool** only changes where you type and where the output appears; the **Python** underneath is the same.

## Two more you may meet

- **Spyder**: an editor for science, part of Anaconda; an editor pane, a console pane, and a list of variables.
- **A terminal on its own**: in Command Prompt, go to the folder and type `python asha.py`; the output appears in the
  same window. This is how programs are often run on Linux and on servers.

## The Colab trap

In a **cell** (Colab, Jupyter) and in the **shell**, a bare expression on the last line shows its value. In a
**script** (IDLE editor, Thonny, VS Code) it does not: use `print`. (Section 6.3, "the line that prints nothing".)
'''
    write('step-five-tools-one-program.md', t)


# ================================================================= 0606
def where_runs_picture():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
    OR, OR2, OR3, INK, GREY = '#C55A11', '#F8CBAD', '#FDF1E9', '#262626', '#7F7F7F'
    plt.rcParams['font.family'] = ['Calibri', 'Segoe UI Symbol']
    fig = plt.figure(figsize=(7.2, 2.5))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 7.2); ax.set_ylim(0, 2.5); ax.axis('off')

    def box(x, y, w, h, text, fc='white', fs=9, weight='normal', ls='-'):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0,rounding_size=0.05',
                                    fc=fc, ec=INK, lw=1.1, ls=ls))
        ax.text(x, y, text, ha='center', va='center', fontsize=fs, weight=weight, linespacing=1.15)

    def arr(p, q):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle='<|-|>', mutation_scale=9, color=INK, lw=1.1))

    heads = ['(a) Desktop IDE', '(b) Browser, local server', '(c) Browser, cloud server']
    for k, h in enumerate(heads):
        ax.text(1.2 + k * 2.4, 2.38, h, ha='center', va='top', fontsize=10, weight='bold', color=OR)
        if k < 2:
            ax.plot([2.4 * (k + 1), 2.4 * (k + 1)], [0.1, 2.3], color='#D9D9D9', lw=1)
    # (a)
    ax.add_patch(FancyBboxPatch((0.2, 0.35), 2.0, 1.65, boxstyle='round,pad=0,rounding_size=0.08', fc=OR3, ec=OR, lw=1.4))
    ax.text(1.2, 1.88, 'your computer', ha='center', fontsize=8.5, color=OR)
    box(1.2, 1.45, 1.6, 0.4, 'IDLE / Thonny / VS Code')
    box(1.2, 0.72, 1.6, 0.4, 'Python runs here', fc=OR2, weight='bold')
    arr((1.2, 1.24), (1.2, 0.93))
    ax.text(1.2, 0.17, 'no internet needed', ha='center', fontsize=8.5, color=GREY)
    # (b)
    ax.add_patch(FancyBboxPatch((2.6, 0.35), 2.0, 1.65, boxstyle='round,pad=0,rounding_size=0.08', fc=OR3, ec=OR, lw=1.4))
    ax.text(3.6, 1.88, 'your computer', ha='center', fontsize=8.5, color=OR)
    box(3.6, 1.45, 1.6, 0.4, 'browser: shows cells')
    box(3.6, 0.72, 1.6, 0.4, 'Jupyter server:\nPython runs here', fc=OR2, weight='bold', fs=8.5)
    arr((3.6, 1.24), (3.6, 0.93))
    ax.text(3.6, 0.17, 'localhost: no internet needed', ha='center', fontsize=8.5, color=GREY)
    # (c)
    ax.add_patch(FancyBboxPatch((5.0, 1.15), 2.0, 0.85, boxstyle='round,pad=0,rounding_size=0.08', fc='white', ec=INK, lw=1.1))
    ax.text(6.0, 1.88, 'your computer or phone', ha='center', fontsize=8.5, color=INK)
    box(6.0, 1.45, 1.6, 0.36, 'browser: shows cells')
    ax.add_patch(FancyBboxPatch((5.0, 0.3), 2.0, 0.62, boxstyle='round,pad=0,rounding_size=0.2', fc=OR3, ec=OR, lw=1.4))
    ax.text(6.0, 0.72, "Google's computer", ha='center', fontsize=8.5, color=OR)
    ax.text(6.0, 0.47, 'Python runs here', ha='center', fontsize=9, weight='bold')
    arr((6.0, 1.15), (6.0, 0.92))
    ax.text(6.22, 1.04, 'internet', fontsize=8.5, color=GREY, va='center')
    ax.text(6.0, 0.12, 'needs the internet and sign-in', ha='center', fontsize=8.5, color=GREY)
    p = IMG / 'c06-online-where-code-runs.png'
    fig.savefig(p, dpi=300, facecolor='white'); plt.close(fig)
    return p.name


def where_runs():
    img = where_runs_picture()
    t = head('Where does my code run?', 'Explained',
             'Table 6.3 in the printed chapter sorts the tools into three kinds. Here is what each kind means, drawn, '
             'and what it needs. (This page follows the author\'s comparison of programming environments in his '
             '*Python Programming* (2026), rewritten for Class XI.)')
    t += pic(img, 'Three kinds of tool', 1.0, 760) + '''

| Kind | Where your code runs | Example tools | Install? | Internet? | Typical use |
|---|---|---|:-:|:-:|---|
| **Desktop IDE** | your own computer | IDLE, Thonny, VS Code, PyCharm | yes | no | learning; the practical exam; projects |
| **Browser-based, local server** | a server program on **your own** computer; the browser only shows the cells | Jupyter Notebook, JupyterLab | yes (Jupyter) | no | notebooks without the internet; data work |
| **Browser-based, cloud server** | a computer of the provider, far away | Google Colab, Replit, Deepnote | no | **yes** | practice anywhere; sharing with a teacher |

## Two words explained

- **Server**: a program that waits for requests and answers them. A Jupyter server waits for "run this cell", runs it
  in Python and sends back the output. It can be on your own computer ("local server", reached at `localhost`) or on
  another computer far away.
- **Cloud**: computers in the provider's data centres, reached through the internet. When you use Colab, your typing
  travels to Google's computer, Python runs there, and only the output comes back to your screen.

## Why it matters

| Question | Desktop IDE | Local server | Cloud |
|---|---|---|---|
| Works when the internet is down? | yes | yes | no |
| Your files are kept | on your computer | on your computer | in your Google Drive (or the provider's store) |
| Works on a phone or a cheap laptop? | needs Python installed | needs Python installed | yes: only a browser |
| Used in the practical exam? | **yes (IDLE)** | no | no |

**Privacy note (Chapter 16).** Whatever you type in a cloud tool is stored by its provider. Do not paste passwords,
phone numbers or other private data into a notebook you share.
'''
    write('explained-where-does-my-code-run.md', t)


# ================================================================= 0607
def things_go_wrong():
    out, err = run_script('x = 5\n  y = 6')
    ok(err.startswith('IndentationError'), err)
    t = head('When things go wrong', 'Good practice',
             'The printed chapter says: learn on IDLE. Here are the problems beginners meet most often when they set '
             'up and run Python, each as symptom → cause → fix.')
    rows = [
        ('`\'python\' is not recognized as an internal or external command, operable program or batch file.`',
         'Python is not installed, or its folder is not on PATH', 'Install it (page "Install Python"); say **Yes** to the PATH question. Or type `py` instead of `python`'),
        ('Typing `python` opens the **Microsoft Store**', 'Windows has a shortcut ("app execution alias") that points to the Store when no Python is found',
         'Install Python. If it still happens: Start → **Manage app execution aliases**, and check the Python entries'),
        ('`python --version` shows an **old version** (for example 3.8)', 'Two Pythons are installed; the old one is found first',
         'Type `py list` to see all of them; uninstall the old one, or run `py -3.15` (your version)'),
        ('**IDLE is not in the Start menu**', 'A shortcut was not made', 'Type `py -m idlelib` in a terminal'),
        ('**VS Code: "Python is not installed"** or Run does nothing', 'No interpreter selected, or the Python extension is missing',
         'Install the **Python** extension (Microsoft); then Ctrl+Shift+P → `Python: Select Interpreter`'),
        ('The program was saved as **`hello.py.txt`**', 'Notepad adds `.txt`; Windows hides known extensions',
         'Save from IDLE or VS Code; in File Explorer, View → tick **File name extensions** to see the real name'),
        ('**Colab asks you to sign in**', 'Colab runs on Google\'s computers and saves to your Drive', 'Sign in with a Google account (a school account is fine)'),
        ('**Colab: "Runtime disconnected"**', 'An idle notebook is stopped after a while to free Google\'s computers', 'Reconnect; run the cells again from the top (values are forgotten)'),
        (f'`{err}` after pasting code from a website or PDF', 'Spaces or tabs at the start of lines were copied wrongly',
         'Delete the spaces at the start of the line; indent only where a block needs it (Chapter 9), always with 4 spaces'),
        ('Line numbers or `>>>` copied into a script', 'Code copied from a book page or the shell', 'Delete them: a script holds only the statements. Copy code from this website or the notebooks'),
    ]
    t += '| Symptom | Cause | Fix |\n|---|---|---|\n' + ''.join(f'| {a} | {b} | {c} |\n' for a, b, c in rows)
    ok(len(rows) == 10)
    t += '''
## A habit that prevents most problems

Keep **one** Python (the latest, from python.org), save programs in **one** folder (for example `Documents\\Python`), and
give files short names without spaces: `marks_total.py`, not `marks total final (2).py`.
'''
    write('good-practice-when-things-go-wrong.md', t)


# ================================================================= 0608
def ai():
    t = head('AI assistants: learn first', 'Good practice',
             'The printed chapter says in one line: learn first; there is no AI help in the practical exam. Here is '
             'what AI assistants are, and how to use them honestly once you can program.')
    t += '''## What they are

VS Code and Google Colab can show an **AI assistant**: a program trained on very large amounts of text and code. You type
a comment such as `# add the marks of three subjects` and it suggests the code; or you ask it in plain words why your
program fails. Examples: GitHub Copilot in VS Code, Gemini in Google Colab.

## Why learn without them first

| Reason | What it means for you |
|---|---|
| The **practical exam** (30 marks) has no AI and no internet | You must write, run and correct programs on your own in IDLE |
| Programming is a skill of the **mind**, like arithmetic | If a calculator always does your sums, you never learn tables; if an assistant always writes your loops, you never learn loops |
| AI suggestions are **sometimes wrong** | Only someone who understands the code can see the mistake |
| Your **practical file** and **project** must be your own work | Code you cannot explain in the viva costs marks |

## How to use one honestly, later

1. Write the program yourself first; run it; correct it.
2. Then ask the assistant to **explain** an error message or **review** your program, not to write it.
3. Read every suggestion and run it; never paste code you do not understand.
4. In a project, say where you used an assistant.

*Teachers: in this book, every program was written and checked by running it; the online notebooks have automatic
checks so that students can test their own work without an assistant.*
'''
    write('good-practice-ai-assistants.md', t)


# ================================================================= 0610
ERRORS = [
    ('SyntaxError', 'print("Hello"', 'a bracket opened but never closed', 'close the bracket: `print("Hello")`'),
    ('SyntaxError', 'print "Hello"', 'Python 2 style, without brackets', '`print("Hello")`'),
    ('NameError', 'Print("Hello")', 'capital P: `Print` is not a known name', '`print`, small letters'),
    ('NameError', 'print(totl)', 'a name used before it is given a value (often a spelling mistake)', 'spell it as created: `total`'),
    ('IndentationError', 'x = 5\n    print(x)', 'a line starts with spaces for no reason', 'start the line at the left edge'),
    ('TypeError', 'print("Marks: " + 92)', 'text and a number joined with `+`', '`print("Marks:", 92)`'),
    ('ZeroDivisionError', 'print(10 / 0)', 'division by zero', 'check the divisor before dividing (Chapter 9)'),
    ('SyntaxError', 'class = "XI-A"', 'a keyword used as a name', 'another name: `section = "XI-A"`'),
]


def error_messages():
    t = head('Reading an error message', 'Explained',
             'The printed chapter says: look at the line number and the last line. Here is a whole error message, part by '
             'part, and the eight errors beginners meet first, each made by running Python.')
    src = 'marks = 92\ntotal = marks + bonus\nprint(total)'
    r = subprocess.run([sys.executable, '-I', '-c', src], capture_output=True, text=True, encoding='utf-8')
    tb = r.stderr.strip()
    ok('NameError' in tb and 'line 2' in tb, tb)
    t += '## A whole error message\n\n' + code(src) + '\n*Python prints:*\n\n' + code(tb, 'text') + '''
| Part | What it tells you |
|---|---|
| `Traceback (most recent call last):` | "Here is where things went wrong", printed before every error |
| `File "<string>", line 2` | **the line number** (in IDLE you see your file name); go to that line first |
| the line itself, sometimes with `^` marks | the statement Python was running, and where |
| **the last line** | **the kind of error and its cause**: read this first |

## The first eight errors

| # | Program | The last line Python prints | Why | Correct it |
|:-:|---|---|---|---|
'''
    for k, (kind, prog, why, fix) in enumerate(ERRORS, 1):
        out, last = run_script(prog)
        ok(last.startswith(kind), f'{prog!r}: {last}')
        t += f'| {k} | {cell(prog)} | {cell(last)} | {why} | {fix} |\n'
    t += f'''
*Messages made by Python {PYV}; other versions may word them a little differently.*

## Three habits

1. Read the **last line** first, then go to the **line number**.
2. Correct **one** error, save, run again: the next error may be a different one.
3. A `SyntaxError` stops the program **before** any line runs; most other errors stop it **at** the line, after the
   lines above have run. Chapter 8 explains why, and the three kinds of error (syntax, run-time, logical).
'''
    write('explained-reading-an-error-message.md', t)


# ================================================================= 0611
def several_lines():
    a = 'total = (90 + 85 + 78\n         + 92 + 88)\nprint("Total:", total)'
    b = 'total = 90 + 85 + 78 \\\n        + 92 + 88\nprint("Total:", total)'
    c = 'a = 1; b = 2; print(a + b)'
    out_a, out_b = run_ok(a), run_ok(b)
    ok(out_a == out_b, 'both ways give the same')
    o3, e3 = run_script('total = 90 + 85\n        + 78')
    ok(e3.startswith('IndentationError'), e3)
    t = head('Statements over several lines', 'Helps you understand',
             'The printed chapter shows one statement written over two lines. Here are the two names for lines, both '
             'ways to continue a statement, and why `;` is poor style.')
    t += '''## Physical and logical lines

- A **physical line** is a line you see on the screen, ending where you pressed Enter.
- A **logical line** is one whole statement, as Python reads it.

Usually they are the same. When a statement is long, one **logical** line may run over several **physical** lines.

## Way 1 (better): inside brackets

Python does not end a statement while a bracket `(`, `[` or `{` is still open.

''' + run_block(a) + '''
## Way 2: a backslash at the very end of a line

''' + code(b) + f'''
Same output. The `\\` must be the **last** character of the line (not even a space after it).

## What goes wrong without either

{code('total = 90 + 85' + chr(10) + '        + 78')}
{code(e3, 'text')}
The first line is a complete statement, so Python ends it there; the second line then starts with spaces for no reason.

## The opposite: several statements on one line

{run_block(c)}
Legal, but poor style (PEP 8): one statement per line is easier to read and to correct, because an error message gives
one line number.

| Basis of difference | Brackets | Backslash `\\` | Semicolon `;` |
|---|---|---|---|
| What it does | one statement over several lines | one statement over several lines | several statements on one line |
| Style | preferred | allowed, easy to break | avoid |
'''
    write('helps-statements-over-several-lines.md', t)


# ================================================================= 0613
KW = {  # keyword: (meaning, tiny example, chapter)
    'False': ('the Boolean value "no"', 'passed = False', '7'),
    'None': ('"no value yet"', 'result = None', '7'),
    'True': ('the Boolean value "yes"', 'ready = True', '7'),
    'and': ('both must be true', 'age >= 18 and has_id', '7'),
    'as': ('a second name, in imports', 'import math as m', '15'),
    'assert': ('stop if a condition is false (a check)', 'assert marks <= 100', 'Class XII'),
    'async': ('starts a task that can wait (advanced)', '(not in school Python)', 'beyond'),
    'await': ('waits for such a task (advanced)', '(not in school Python)', 'beyond'),
    'break': ('leave a loop at once', 'break', '10'),
    'class': ('defines a new kind of object (not in the syllabus)', '(not in your syllabus)', 'beyond'),
    'continue': ('skip to the next turn of a loop', 'continue', '10'),
    'def': ('defines a function', 'def area(r):', 'Class XII'),
    'del': ('deletes a name or an item', 'del marks[0]', '12'),
    'elif': ('"else if": another test', 'elif marks >= 60:', '9'),
    'else': ('what to do otherwise', 'else:', '9'),
    'except': ('what to do when an error happens', 'except ValueError:', 'Class XII'),
    'finally': ('runs at the end, error or not', 'finally:', 'Class XII'),
    'for': ('repeat for each item', 'for i in range(5):', '10'),
    'from': ('take something from a module', 'from math import pi', '15'),
    'global': ('use a name from outside a function', 'global count', 'Class XII'),
    'if': ('test a condition', 'if marks >= 33:', '9'),
    'import': ('bring in a module', 'import math', '15'),
    'in': ('is it a member? / each item of', "'a' in 'cat'", '7, 10'),
    'is': ('the same object?', 'x is None', '7'),
    'lambda': ('a one-line function without a name', 'lambda x: x * 2', 'Class XII'),
    'nonlocal': ('use a name from the enclosing function', 'nonlocal total', 'beyond'),
    'not': ('the opposite', 'not passed', '7'),
    'or': ('at least one must be true', 'rain or homework', '7'),
    'pass': ('do nothing (a placeholder)', 'pass', '9'),
    'raise': ('cause an error on purpose', 'raise ValueError', 'Class XII'),
    'return': ('give a value back from a function', 'return area', 'Class XII'),
    'try': ('try something that may fail', 'try:', 'Class XII'),
    'while': ('repeat while a condition is true', 'while n > 0:', '10'),
    'with': ('open something and close it safely', 'with open("a.txt") as f:', 'Class XII'),
    'yield': ('give values one at a time (advanced)', '(advanced)', 'beyond'),
}


def keywords():
    ok(set(KW) == set(keyword.kwlist) and len(KW) == 35, set(KW) ^ set(keyword.kwlist))
    ok(sorted(k for k in KW if k[0].isupper()) == ['False', 'None', 'True'])
    out = run_ok('import keyword\nprint(len(keyword.kwlist))\nprint(keyword.softkwlist)')
    soft = eval(out.splitlines()[1])
    ok(set(soft) >= {'match', 'case', '_'}, soft)
    t = head('All 35 keywords', 'Helps you understand',
             'The printed chapter groups the 35 keywords by purpose. Here is each one with a one-line meaning, a tiny '
             'example and the chapter where you meet it. You do not need to learn them all now.')
    t += '| Keyword | What it does | Tiny example | Chapter |\n|---|---|---|:-:|\n'
    for k in keyword.kwlist:
        m, ex, ch = KW[k]
        exs = ex if ex.startswith('(') else f'`{ex}`'
        t += f'| `{k}` | {m} | {exs} | {ch} |\n'
    t += f'''
*The list is Python's own (`keyword.kwlist`, Python {PYV}), sorted as Python sorts it: capital letters come before small
ones.*

## Why do `True`, `False` and `None` begin with a capital?

They are **values**, not instructions, and Python's makers gave the three built-in values capital first letters, as
names of special things often have in English. So `true` and `none` are ordinary names you may use (but should not),
while `True` and `None` are keywords.

## Soft keywords: not in your syllabus

Newer Pythons also have a few **soft keywords** (`{"`, `".join(soft)}`): words that act as keywords only in one special
statement and are ordinary names everywhere else. They are not in your syllabus, and older books do not list them; if
you see them, you can ignore them.
'''
    write('helps-all-35-keywords.md', t)


# ================================================================= 0615
PEP8 = [  # (rule, poor, good)
    ('Meaningful names', 'tm = 450', 'total_marks = 450'),
    ('snake_case for variables', 'TotalMarks = 450', 'total_marks = 450'),
    ('CAPITALS for constants', 'pass_mark = 33', 'PASS_MARK = 33'),
    ('Never `l`, `O`, `I` as one-letter names', 'l = 1', 'count = 1'),
    ('4 spaces per indent level', 'if True:\n  x = 1', 'if True:\n    x = 1'),
    ('One statement per line', 'a = 1; b = 2', 'a = 1\nb = 2'),
    ('Spaces around `=` and operators', 'total=a+b*2', 'total = a + b * 2'),
    ('No space inside brackets', 'print( total )', 'print(total)'),
    ('A space after a comma', 'print(a,b)', 'print(a, b)'),
    ('Lines of at most 79 characters', 'x = 1  # ' + 'a very long comment ' * 4, 'x = 1  # a short comment'),
    ('Comments: `# ` and a space, saying why', 'x = x + 1 #add 1', 'x = x + 1  # one more student'),
    ('Blank lines to separate parts', 'a = 1\nprint(a)\nb = 2\nprint(b)', 'a = 1\nprint(a)\n\nb = 2\nprint(b)'),
    ('Names do not hide built-ins', 'print = 5', 'points = 5'),
    ('Comparisons with `None` use `is`', 'x = None\nprint(x == None)', 'x = None\nprint(x is None)'),
    ('No `\\` where brackets will do', 'total = 1 + \\\n    2', 'total = (1 +\n         2)'),
]


def pep8():
    for rule, poor, good in PEP8:                 # both forms must be legal Python: style is not syntax
        compile(poor, '<poor>', 'exec')
        compile(good, '<good>', 'exec')
        ok(True)
    ok(len(PEP8) == 15)
    ok(max(len(l) for l in PEP8[9][1].splitlines()) > 79 and len(PEP8[9][2]) <= 79, 'line-length example')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        import this  # noqa: F401  (prints The Zen of Python)
    zen = [l for l in buf.getvalue().splitlines() if l.strip()]
    ok(zen[0] == 'The Zen of Python, by Tim Peters' and len(zen) == 20, len(zen))
    t = head('PEP 8 for Class XI, and what a PEP is', 'Good practice',
             'The printed chapter names six conventions from PEP 8. Here are fifteen, each with a poor and a good '
             'example, and what a PEP is. Every example on this page is legal Python: style is about reading, not about '
             'running.')
    t += '''## What is a PEP?

**PEP = Python Enhancement Proposal**: a numbered document that proposes a change to Python, or records a rule or a
decision. Anyone may write one; Python's core team accepts or rejects it. Two are famous:

- **PEP 8**: *Style Guide for Python Code*, the rules for writing Python that is easy to read.
- **PEP 20**: *The Zen of Python*, nineteen short sayings about good programs.

## Fifteen PEP 8 rules

| # | Rule | Poor | Good |
|:-:|---|---|---|
'''
    for k, (rule, poor, good) in enumerate(PEP8, 1):
        poor_s = 'a line of more than 79 characters' if k == 10 else cell(poor)
        t += f'| {k} | {rule} | {poor_s} | {cell(good)} |\n'
    t += '''
## The Zen of Python (PEP 20)

Type `import this` in the shell. Python prints nineteen sayings; the first four are:

```text
''' + '\n'.join(zen[1:5]) + '''
```

## What the examiner looks for (practical exam)

The lab test is marked **60% logic, 20% documentation, 20% code quality**.

| Under | The examiner looks for |
|---|---|
| Documentation | a comment at the top (what the program does); comments that say **why**; clear prompts and output messages |
| Code quality | meaningful snake_case names; 4-space indents; one statement per line; no needless repetition |
'''
    write('good-practice-pep8-and-peps.md', t)


# ================================================================= 0616
ESC = [('\\n', 'new line'), ('\\t', 'tab (a jump to the next column)'), ('\\\\', 'one backslash'),
       ("\\'", 'a single quote inside \'...\''), ('\\"', 'a double quote inside "..."')]
LIT_DRILLS = ['25', '-7', '0b101', '0o17', '0o28', '0x1F', '0xG1', '3.14', '.5', '7.', '2.5e3', '1.7E', '0.17E2.3',
              '1,234', '17,225E02', '"Pass"', "'A'", '"Asha\'s"', "'Hi\"", '"""Hi"""', 'True', 'true', 'None',
              '2+3j', '1_000_000', '012', '00', '1e-3', '"5"', '5.0']


WHY_INVALID = {'0o28': '8 is not an octal digit (only 0–7)', '0xG1': 'G is not a hexadecimal digit (only 0–9, A–F)',
               '1.7E': 'no digits after E', '0.17E2.3': 'the power after E must be a whole number',
               '\'Hi"': 'the opening and closing quotes are different', '012': 'a whole number may not begin with 0'}


def literal_answer(lit):
    try:
        tree = ast.parse(lit, mode='eval')
    except SyntaxError:
        return 'invalid', WHY_INVALID[lit]
    node = tree.body
    if isinstance(node, ast.Name):
        return 'a name, not a literal', 'Python looks for a variable of this name'
    if isinstance(node, ast.Tuple):
        return 'a tuple, not a number', 'the comma makes two values: ' + repr(eval(lit))
    if isinstance(node, ast.UnaryOp):
        v = ast.literal_eval(lit)
        return type(v).__name__, f'value {v!r}; strictly, `-` is an operator in front of the literal {lit.lstrip("-+")}'
    if isinstance(node, ast.BinOp):
        v = eval(lit)
        return f'{type(v).__name__}', f'value {v!r}'
    v = ast.literal_eval(lit)
    return type(v).__name__ if v is not None else 'NoneType (the special literal)', f'value {v!r}'


def literals():
    for e, _ in ESC:
        ok(len(eval('"' + e + '"')) == 1, e)
    ok(len('ab\nc') == 4 and len('Asha\'s') == 6 and len('C:\\temp') == 7)
    sizes = [('"ab\\nc"', 4, 'a, b, new line, c'), ('"Asha\\\'s"', 6, 'the escape counts as one character'),
             ('"C:\\\\temp"', 7, 'C, :, one backslash, t, e, m, p'), ('"\\t5"', 2, 'tab, 5'),
             ('"""Hi\nAll"""', 6, 'H, i, new line, A, l, l: the Enter inside triple quotes is a new-line character')]
    for s, n, _ in sizes:
        ok(len(eval(s)) == n, s)
    t = head('Literals up close', 'Sometimes asked',
             'The printed chapter lists the kinds of literal in one table; Chapter 7 studies each kind. Here are the '
             'details some papers ask: escape sequences, the size of a string, other ways to write numbers, and 30 '
             '"valid or invalid?" drills, every answer decided by Python.')
    t += '## Escape sequences: characters you cannot type directly inside quotes\n\n| Sequence | Means |\n|:-:|---|\n'
    t += ''.join(f'| `{e}` | {m} |\n' for e, m in ESC)
    t += '\n' + run_block('print("Name:\\tAsha\\nClass:\\tXI")') + '''
**An escape sequence is one character**, though you type two. So:

| String | `len()` | Why |
|---|:-:|---|
'''
    for s, n, why in sizes:
        t += f'| `{s.replace(chr(10), "↵")}` | {n} | {why} |\n'
    t += '''
## Numbers written other ways

| Kind | Written as | Value |
|---|---|---|
'''
    for lit in ['0b101', '0o17', '0x1F', '2.5e3', '1e-3', '1_000_000', '2+3j']:
        v = eval(lit)
        t += f'| {type(v).__name__} | `{lit}` | `{v!r}` |\n'
        ok(True)
    t += '''
`0b` = binary, `0o` = octal, `0x` = hexadecimal (Chapter 4); `e` = "times ten to the power"; `_` only for reading
(one million); `j` marks the imaginary part of a complex number.

## 30 drills: valid or invalid? what type?

*Cover the answer column, decide, then check. Every answer was made by Python.*

| # | Literal | Answer | Why |
|:-:|---|---|---|
'''
    for k, lit in enumerate(LIT_DRILLS, 1):
        ans, why = literal_answer(lit)
        t += f'| {k} | `{lit}` | **{ans}** | {why} |\n'
    ok(len(LIT_DRILLS) == 30)
    ok({l for l in LIT_DRILLS if literal_answer(l)[0] == 'invalid'} == set(WHY_INVALID), 'every invalid drill has its reason')
    ok(literal_answer('0o28')[0] == 'invalid' and literal_answer('1,234')[0].startswith('a tuple')
       and literal_answer('012')[0] == 'invalid' and literal_answer('00')[0] == 'int')
    t += '''
**Two traps from the drills.** `012` is invalid in Python 3 (a leading zero is not allowed, except for zero itself:
old Python 2 read it as octal). And `1,234` is legal but is **two** numbers in a tuple, not one thousand two hundred and
thirty-four.
'''
    write('sometimes-asked-literals-up-close.md', t)


# ================================================================= 0619
def notes():
    s_src = 's = """Line 1\nLine 2\nLine 3"""\nprint(s)\nprint(len(s))'
    out = run_ok(s_src)
    ok(out.splitlines()[-1] == '20', out)
    doc_src = '"""Report card: reads marks, prints the total.\nClass XI-A, Term 1."""\nprint(__doc__.splitlines()[0])'
    t = head('Notes for people', 'Good practice',
             'The printed chapter shows two ways to write a note over several lines. Here are comments that help, '
             'docstrings, and triple quotes used for a string you keep and print.')
    t += '''## Comments that help

| Program part | A comment that helps |
|---|---|
| The top of every program | what it does, for whom, and the date: `# Total and grade for one student; Asha, Class XI-A` |
| A line whose reason is not obvious | `# 22/7 because the question asks for it, not math.pi` |
| A value with a meaning | `PASS_MARK = 33  # CBSE pass mark, out of 100` |
| A part of a long program | `# --- read the marks ---`, `# --- print the result ---` |

| Avoid | Because |
|---|---|
| `x = x + 1  # add 1 to x` | it repeats the code |
| a comment on every line | the useful ones get lost |
| a comment that is no longer true | worse than none: change it with the code |

## Docstrings

A triple-quoted note as the **first statement** of a program is its **docstring**: a description for **users**.
Python keeps it, and other tools can show it:

''' + run_block(doc_src) + '''
In Class XII you will write a docstring as the first line of every function.

## Triple quotes for a string you keep

The same triple quotes can make a **string over several lines** that you store in a name and print. This is not a
note: the string is kept and used.

''' + run_block(s_src) + '''
The length is 20: 18 letters, digits and spaces, plus 2 new-line characters (one for each Enter inside the quotes).
Chapter 11 (Strings) uses these strings.

| Basis of difference | A triple-quoted **note** | A triple-quoted **string** |
|---|---|---|
| Written | on its own line | after `=`, or inside `print(...)` |
| Python | makes the string, then throws it away | keeps it under a name |
| Used for | notes and docstrings | text over several lines: addresses, poems, menus |
'''
    write('good-practice-notes-for-people.md', t)


if __name__ == '__main__':
    for f in (story, limits, install, five_tools, where_runs, things_go_wrong, ai, error_messages, several_lines,
              keywords, pep8, literals, notes):
        f()
    print(f'{checks} checks, 0 wrong (Python {PYV})')
