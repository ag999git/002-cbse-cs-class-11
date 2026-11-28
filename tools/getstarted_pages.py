"""The website's "Get started: set up Python" section (28 Nov 2026; plan setup-section-plan-v2.md, S1-S9 and F1-F8
approved). Pages in book/get-started/:
  index.md (G1 start here, with Thonny)  install-python.md (G2)  first-program-in-idle.md (G3)  vs-code.md (G5)
  jupyter.md (G6)  google-colab.md (G7)  when-things-go-wrong.md (G8, index of problems)  where-does-my-code-run.md (G9)
Every install page: the whole flow at the top (flowchart + numbered links), then each step with a picture, a key to its
labelled parts, do / don't / watch out / you should now see, and a link to its problem in "If things go wrong" on the
same page. Pictures: simplified drawings by program (every label exact); real screenshots are added when they arrive
(list: 01-all-chapters-of-cbse-11/ch06-getting-started-with-python/get-started-screenshot-list-v1.md).
Checks: flowcharts by algo_lib (no crossings); every link and every #anchor on these pages exists; the commands that
can safely be run here are run (python --version, pip, a first program).
Run from the repository root:  python tools/getstarted_pages.py"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent.parent
sys.path.insert(0, str(PROJECT / '50-tools'))
from flow_layout import Builder  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

D = ROOT / 'book' / 'get-started'
D.mkdir(exist_ok=True)
IMG = ROOT / 'book' / 'assets' / 'images' / 'get-started'
IMG.mkdir(parents=True, exist_ok=True)
REL = '../assets/images/get-started'
CH6 = PROJECT / '01-all-chapters-of-cbse-11' / 'ch06-getting-started-with-python'
checks = 0

INK, OR, OR2, OR3, GREY, LG = '#262626', '#C55A11', '#F8CBAD', '#FDF1E9', '#7F7F7F', '#E7E6E6'
BLUE = '#1F6FB2'
plt.rcParams['font.family'] = ['Calibri', 'Segoe UI Symbol']
MONO = 'Consolas'


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8')
    return (r.stdout + r.stderr).strip()


# ================================================================= drawing "screens" (simplified, labelled)
class Screen:
    """A simplified drawing of a window. Units are inches; drawn at 300 dpi (sharp on screen and in print)."""

    def __init__(self, name, title, w=6.4, h=3.4, kind='window'):
        self.name, self.w, self.h = name, w, h
        self.fig = plt.figure(figsize=(w, h))
        ax = self.fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis('off')
        self.ax = ax
        ax.add_patch(Rectangle((0.05, 0.05), w - 0.1, h - 0.1, fc='#1E1E1E' if kind == 'dark' else 'white', ec=INK, lw=1.4))
        bar = '#3C3C3C' if kind == 'dark' else ('#DEE3EA' if kind == 'browser' else OR2)
        ax.add_patch(Rectangle((0.05, h - 0.38), w - 0.1, 0.33, fc=bar, ec=INK, lw=1.4))
        ax.text(0.18, h - 0.215, title, va='center', fontsize=9.5, weight='bold', color='white' if kind == 'dark' else INK)
        for k, c in enumerate(['#E06C5A', '#E0B85A', '#6CB86C'] if kind != 'window' else []):
            pass
        ax.text(w - 0.18, h - 0.215, '–  ☐  ✕', va='center', ha='right', fontsize=9, color='white' if kind == 'dark' else INK)
        self.labels = []

    def text(self, x, y, s, fs=9, **kw):
        kw.setdefault('va', 'center')
        self.ax.text(x, y, s, fontsize=fs, **kw)

    def mono(self, x, y, s, fs=9, color=INK, **kw):
        self.ax.text(x, y, s, fontsize=fs, family=MONO, color=color, va='center', **kw)

    def box(self, x, y, w, h, fc='white', ec=INK, lw=1.1, r=0.05):
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}', fc=fc, ec=ec, lw=lw))

    def button(self, x, y, w, h, s, primary=False, fs=9):
        self.box(x, y, w, h, fc=BLUE if primary else '#F3F3F3', ec=BLUE if primary else GREY)
        self.ax.text(x + w / 2, y + h / 2, s, ha='center', va='center', fontsize=fs, color='white' if primary else INK,
                     weight='bold' if primary else 'normal')

    def check(self, x, y, s, on=True, fs=9):
        self.ax.add_patch(Rectangle((x, y - 0.07), 0.14, 0.14, fc=BLUE if on else 'white', ec=INK, lw=1))
        if on:
            self.ax.text(x + 0.07, y, '✓', ha='center', va='center', fontsize=8, color='white', weight='bold')
        self.ax.text(x + 0.22, y, s, va='center', fontsize=fs)

    def terminal(self, x, y, w, h, lines):
        self.box(x, y, w, h, fc='#1E1E1E', ec=INK, r=0.03)
        for k, (s, c) in enumerate(lines):
            self.ax.text(x + 0.12, y + h - 0.2 - k * 0.22, s, fontsize=8.6, family=MONO, color=c, va='center')

    def label(self, x, y, ch):
        self.ax.add_patch(plt.Circle((x, y), 0.12, fc=OR, ec=INK, lw=0.9, zorder=10))
        self.ax.text(x, y - 0.005, ch, ha='center', va='center', fontsize=9, weight='bold', color='white', zorder=11)
        self.labels.append(ch)

    def save(self):
        p = IMG / f'{self.name}.png'
        self.fig.savefig(p, dpi=300, facecolor='white')
        plt.close(self.fig)
        return p.name


def pic(name, alt, width=640):
    ok((IMG / name).exists(), name)
    return f'![{alt}]({REL}/{name}){{ width="{width}" }}'


def chart(name, title, steps):
    a = Builder(name, title, steps).build()
    a.check()
    ok(not a.crossings(), name)
    p, w, h = a.draw(IMG)
    return a, p.name


# ================================================================= the step-page renderer
def step_page(title, label, intro, flow_img, flow_links, before, steps, check_md, problems, tail=''):
    """steps: dicts(id, title, pic, alt, key[(L, text)], do, dont, watch, see, prob[ids]); problems: dict id -> (head, symptom, cause, fix)."""
    a, img = flow_img
    t = f'# {title}\n\n*{label}. {intro}*\n\n'
    t += '!!! abstract "The whole flow"\n\n'
    t += '    ' + pic(img, 'The whole flow', 360).replace('\n', '\n    ') + '\n\n'
    t += '    The numbers in the circles are the flowchart\'s box numbers (Start is box 1). Each step below says its box:\n\n'
    boxes = {}
    for n, (prefix, anchor, txt) in enumerate(flow_links, 1):
        if prefix:
            box = [nd.num for nd in a.nodes if nd.text.replace('\n', ' ').startswith(prefix)]
            ok(len(box) == 1, f'{title}: box "{prefix}" found {len(box)} times')
            boxes[anchor] = box[0]
            t += f'    {n}. **Box {box[0]}** → [Step {n}: {txt}](#{anchor})\n'
        else:
            t += f'    {n}. [Step {n}: {txt}](#{anchor})\n'
    t += '\n    **Something went wrong?** [Go to "If things go wrong"](#if-things-go-wrong)\n\n'
    t += before + '\n\n'
    for n, s in enumerate(steps, 1):
        b = f' (box {boxes[s["id"]]})' if s['id'] in boxes else ''
        t += f'## Step {n}{b}: {s["title"]} {{#{s["id"]}}}\n\n'
        if s.get('pic'):
            t += pic(s['pic'], s['alt']) + '\n\n'
            t += '*A simplified drawing; your screen may look a little different.*\n\n'
        if s.get('key'):
            t += '| Part | What it is |\n|:-:|---|\n' + ''.join(f'| **{L}** | {txt} |\n' for L, txt in s['key']) + '\n'
        if s.get('body'):
            t += s['body'] + '\n\n'
        lines = []
        if s.get('do'):
            lines.append(f'- ✅ **Do:** {s["do"]}')
        if s.get('dont'):
            lines.append(f'- ❌ **Don\'t:** {s["dont"]}')
        if s.get('watch'):
            lines.append(f'- ⚠️ **Watch out:** {s["watch"]}')
        if s.get('see'):
            lines.append(f'- 👀 **You should now see:** {s["see"]}')
        t += '\n'.join(lines) + '\n\n'
        for pid in s.get('prob', []):
            t += f'*Problem at this step?* [{problems[pid][0]}](#{pid})\n\n'
    t += check_md + '\n\n'
    t += '## If things go wrong {#if-things-go-wrong}\n\n'
    for pid, (head, symptom, cause, fix) in problems.items():
        t += f'### {head} {{#{pid}}}\n\n- **What you see:** {symptom}\n- **Why:** {cause}\n- **Fix:** {fix}\n\n'
    t += tail
    return t


def check_links(name, text):
    """Every #anchor link on the page must exist on it; every relative .md link must exist."""
    anchors = set(re.findall(r'\{#([a-z0-9-]+)\}', text))
    for a in re.findall(r'\]\(#([a-z0-9-]+)\)', text):
        ok(a in anchors, f'{name}: missing anchor #{a}')
    for l in re.findall(r'\]\(([^)#:]+\.md)(?:#([a-z0-9-]+))?\)', text):
        target = (D / l[0]).resolve()
        ok(target.exists(), f'{name}: missing page {l[0]}')
        if l[1]:
            ok('{#' + l[1] + '}' in target.read_text(encoding='utf-8') if target.name != name else l[1] in anchors,
               f'{name}: missing anchor {l[0]}#{l[1]}')


PAGES = {}


def write(name, text):
    PAGES[name] = text
    (D / name).write_text(text, encoding='utf-8')
    print('wrote', name)


# ================================================================= G2 install Python
def g2():
    # pictures
    s = Screen('gs-py-1-download', 'python.org  –  Download Python for Windows', kind='browser')
    s.box(0.3, 2.62, 5.8, 0.3, fc='#F3F3F3', ec=GREY); s.mono(0.42, 2.77, 'https://www.python.org/downloads/windows/', fs=8.5)
    s.text(0.4, 2.3, 'Downloads   Documentation   Community', fs=9, color=GREY)
    s.text(0.4, 1.9, 'Python for Windows', fs=14, weight='bold')
    s.button(0.4, 1.2, 2.9, 0.45, 'Python install manager (recommended)', primary=True)
    s.text(0.4, 0.85, 'Python 3.15.x  –  Windows installer (64-bit)', fs=9, color=BLUE)
    s.text(0.4, 0.55, 'Python 3.15.x  –  Windows installer (ARM64)', fs=9, color=BLUE)
    s.label(0.22, 2.77, 'A'); s.label(3.5, 1.42, 'B'); s.label(4.6, 0.85, 'C')
    p1 = s.save()

    s = Screen('gs-py-2-install', 'App Installer')
    s.text(0.5, 2.55, 'Install Python install manager?', fs=13, weight='bold')
    s.text(0.5, 2.15, 'Publisher: Python Software Foundation', fs=9.5, color=GREY)
    s.text(0.5, 1.85, 'Capabilities: uses all system resources', fs=9, color=GREY)
    s.check(0.5, 1.35, 'Launch when ready', on=True)
    s.button(4.3, 0.4, 1.6, 0.45, 'Install', primary=True)
    s.label(0.3, 2.15, 'A'); s.label(0.3, 1.35, 'B'); s.label(6.1, 0.62, 'C')
    p2 = s.save()

    s = Screen('gs-py-3-first-run', 'Windows PowerShell (a terminal)', kind='dark')
    s.terminal(0.2, 0.25, 6.0, 2.7, [('PS C:\\Users\\you> python', '#FFFFFF'),
                                     ('  (the install manager installs the latest Python ...)', '#9CDCFE'),
                                     ('  ... a question about adding a folder to PATH:', '#DCDCAA'),
                                     ('  answer  y  (yes)  and press Enter', '#DCDCAA'),
                                     ('Python 3.15.x ...', '#FFFFFF'),
                                     ('>>> exit()', '#FFFFFF')])
    s.label(5.95, 2.75, 'A'); s.label(5.95, 2.53, 'B'); s.label(5.95, 2.2, 'C'); s.label(5.95, 1.65, 'D')
    p3 = s.save()

    s = Screen('gs-py-4-check', 'Windows PowerShell (a terminal)', kind='dark')
    s.terminal(0.2, 0.25, 6.0, 2.7, [('PS C:\\Users\\you> python --version', '#FFFFFF'),
                                     ('Python 3.15.x', '#B5CEA8'),
                                     ('PS C:\\Users\\you> py list', '#FFFFFF'),
                                     ('  3.15   Python 3.15.x   (the * marks the default)', '#B5CEA8'),
                                     ('PS C:\\Users\\you> python -c "print(\'Hello\')"', '#FFFFFF'),
                                     ('Hello', '#B5CEA8')])
    s.label(5.95, 2.75, 'A'); s.label(5.95, 2.53, 'B'); s.label(5.95, 2.31, 'C'); s.label(5.95, 1.87, 'D')
    p4 = s.save()

    s = Screen('gs-py-5-idle', 'Start menu – search')
    s.box(0.4, 2.45, 4.0, 0.36, fc='#F3F3F3', ec=GREY); s.text(0.55, 2.63, '🔍  idle', fs=10)
    s.box(0.4, 1.55, 5.6, 0.7, fc=OR3, ec=OR); s.text(0.6, 2.0, 'IDLE (Python 3.15)', fs=11, weight='bold'); s.text(0.6, 1.72, 'App', fs=9, color=GREY)
    s.text(0.5, 1.0, 'Not there?  Type in a terminal:   py -m idlelib', fs=9.5)
    s.label(0.22, 2.63, 'A'); s.label(6.2, 1.9, 'B'); s.label(0.25, 1.0, 'C')
    p5 = s.save()

    s = Screen('gs-py-6-classic', 'Python 3.15.x (64-bit) Setup')
    s.text(0.5, 2.6, 'Install Python 3.15.x (64-bit)', fs=13, weight='bold')
    s.box(0.5, 1.75, 3.4, 0.6, fc='#EAF2FB', ec=BLUE); s.text(0.65, 2.15, '→  Install Now', fs=11, weight='bold', color=BLUE)
    s.text(0.95, 1.9, 'C:\\Users\\you\\AppData\\Local\\Programs\\Python\\…', fs=7.5, color=GREY)
    s.text(0.65, 1.42, '→  Customize installation', fs=10.5, color=BLUE)
    s.check(0.5, 0.85, 'Use admin privileges when installing py.exe', on=True)
    s.check(0.5, 0.5, 'Add python.exe to PATH', on=True)
    s.label(4.1, 2.05, 'A'); s.label(3.5, 1.42, 'B'); s.label(4.6, 0.85, 'C'); s.label(3.1, 0.5, 'D')
    p6 = s.save()

    a, flow = chart('gs-flow-install-python', 'Installing Python on Windows', [
        ('do', 'b = 1', {'text': 'python.org: download\nthe install manager'}),
        ('do', 'c = 1', {'text': 'Open it; Install'}),
        ('do', 'd = 1', {'text': 'Terminal: type python;\nYes to PATH'}),
        ('if', 'v', [('out', 'r', {'text': 'Open IDLE: ready'})],
         [('out', 'h', {'text': 'If things go wrong'})], {'text': 'python --version\nshows 3.12+?'})])

    ver = run([sys.executable, '--version'])
    ok(ver.startswith('Python 3.'), ver)
    hello = run([sys.executable, '-c', "print('Hello')"])
    ok(hello == 'Hello')

    problems = {
        'p-not-recognized': ('"python is not recognized …"',
                             '`\'python\' is not recognized as an internal or external command, operable program or batch file.`',
                             'Windows does not know where Python is: it is not installed, or its folder is not on PATH (you said No, or closed the window too early).',
                             'Close the terminal and open a **new** one (PATH is read only when a terminal opens). Still the same? Type `py` instead of `python`. Still the same? Run the install manager again and say **Yes** to the PATH question.'),
        'p-store-opens': ('Typing python opens the Microsoft Store',
                          'The Microsoft Store opens a Python page instead of Python starting.',
                          'Windows has a shortcut ("app execution alias") that points to the Store when it cannot find Python.',
                          'Install Python (steps 1–4). If it still happens: Start → type **Manage app execution aliases** → check that the entries for **Python** of the install manager are **On**.'),
        'p-old-version': ('An old version answers',
                          '`python --version` shows an old Python, for example 3.8.',
                          'Two Pythons are installed; Windows finds the old one first.',
                          'Type `py list` to see all of them. Uninstall the old one (Settings → Apps), or run your programs with `py` (the newest).'),
        'p-no-download': ('The download does not start, or is blocked',
                          'Nothing downloads, or the browser warns about the file.',
                          'A school network or an antivirus may block installers.',
                          'Ask your teacher or parent. Download **only** from python.org; never from another site ("free Python setup" files can carry malware).'),
        'p-no-idle': ('IDLE is not in the Start menu',
                      'Searching for "idle" finds nothing.',
                      'The shortcut was not made, or the search has not caught up yet.',
                      'Type `py -m idlelib` in a terminal: it opens IDLE.'),
        'p-admin': ('"You need administrator permission"',
                    'Windows asks for an administrator password.',
                    'On a school or family computer, you may not be allowed to install programs.',
                    'Ask the computer\'s owner. Or use **Google Colab**: nothing to install ([Google Colab](google-colab.md)).'),
    }
    steps = [
        dict(id='step-download', title='Download the Python install manager', pic=p1, alt='python.org download page',
             key=[('A', 'the address bar: it must say **python.org**'), ('B', 'the **Python install manager** button: the way the makers recommend since Python 3.14'),
                  ('C', 'the older full installers (see "Another way" below)')],
             do='type the address yourself: **python.org**, then **Downloads → Windows**.',
             dont='download Python from any other site or from an advertisement.',
             watch='the same install manager is also in the **Microsoft Store** ("Python Install Manager"); either is fine.',
             see='a file in your **Downloads** folder.', prob=['p-no-download']),
        dict(id='step-install', title='Install it', pic=p2, alt='the install dialog',
             key=[('A', 'the publisher: **Python Software Foundation**, the makers of Python'), ('B', 'start it when ready'), ('C', 'the **Install** button')],
             do='double-click the downloaded file, check the publisher (A), then press **Install** (C).',
             dont='install a file whose publisher is not the Python Software Foundation.',
             watch='a school computer may ask for an administrator password.',
             see='the installer finishes in a minute.', prob=['p-admin']),
        dict(id='step-first-run', title='Type python once: it fetches Python', pic=p3, alt='the first run in a terminal',
             key=[('A', 'you type `python` and press Enter'), ('B', 'the install manager downloads and installs the newest Python by itself'),
                  ('C', 'the **PATH question**: answer **y** (yes)'), ('D', 'the `>>>` prompt: Python is running; type `exit()` to leave')],
             body='**Open a terminal:** press the Windows key, type **PowerShell** (or **Terminal**), press Enter.\n\n'
                  '**What "PATH" means:** PATH is the list of folders where Windows looks for a command. Yes adds Python\'s folder to the list, so `python` works in every terminal.',
             do='answer **yes** to the PATH question.',
             dont='close the window while it is downloading.',
             watch='the exact words of the question may differ from the drawing.',
             see='`>>>`, Python\'s prompt.', prob=['p-store-opens', 'p-not-recognized']),
        dict(id='step-check', title='Check that it worked', pic=p4, alt='checking in a terminal',
             key=[('A', '`python --version` asks Python for its version'), ('B', 'the answer: **3.12 or later** is what this book needs'),
                  ('C', '`py list` lists every Python on the computer'), ('D', 'a first one-line program, run from the terminal')],
             body=f'On the computer that checked this page, `python --version` printed `{ver}` and the one-line program printed `{hello}`.',
             do='open a **new** terminal first (a terminal reads PATH only when it opens).',
             see='a version number, and `Hello`.', prob=['p-not-recognized', 'p-old-version']),
        dict(id='step-idle', title='Open IDLE', pic=p5, alt='finding IDLE',
             key=[('A', 'search for **idle**'), ('B', 'IDLE: Python\'s own simple editor, used in the practical exam'), ('C', 'another way to open it')],
             do='pin IDLE to the taskbar (right-click → Pin) so you find it quickly.',
             see='the IDLE shell with `>>>`. Next: [Your first program in IDLE](first-program-in-idle.md).', prob=['p-no-idle']),
    ]
    check_md = ('## Another way: the classic installer {#classic-installer}\n\n'
                'The older full installer (a `.exe` file) is still offered for **Python 3.15 and earlier**; it stops with Python '
                '3.16. If your school uses it:\n\n' + pic(p6, 'the classic installer') + '\n\n'
                '| Part | What it is |\n|:-:|---|\n| **A** | **Install Now**: the usual choice |\n| **B** | Customize: not needed |\n'
                '| **C** | py.exe, Python\'s launcher (keep it ticked) |\n| **D** | **Add python.exe to PATH**: **tick it** before pressing Install Now |\n\n'
                '- ❌ **Don\'t** forget box **D**: without it, `python` is "not recognized" in a terminal.\n'
                '- 👀 At the end, **Setup was successful**. Then check it as in [Step 4](#step-check).\n\n'
                '## Mac and Linux (short) {#mac-linux}\n\n'
                '- **macOS:** download the macOS installer from **python.org → Downloads → macOS**, open the `.pkg` file and '
                'follow it. IDLE is in **Applications → Python 3.x**. In the Terminal, type `python3` (not `python`).\n'
                '- **Linux** (Ubuntu and others): Python 3 is usually already there; check with `python3 --version`. For IDLE: '
                '`sudo apt install idle3`.\n\n'
                '## Already have Python? {#already}\n\nOpen a terminal and type `python --version`. If it shows **3.12 or later**, '
                'you are ready: go to [Step 5](#step-idle).')
    t = step_page('Install Python on Windows, step by step', 'Get started',
                  'Ten minutes, an internet connection and about 100 MB of space. Follow the steps in order; each step '
                  'says what you should see when it is done.',
                  (a, flow), [('python.org', 'step-download', 'Download the Python install manager'),
                              ('Open it', 'step-install', 'Install it'),
                              ('Terminal', 'step-first-run', 'Type python once: it fetches Python'),
                              ('python --version', 'step-check', 'Check that it worked'),
                              ('Open IDLE', 'step-idle', 'Open IDLE')],
                  '**Before you start.** Windows 10 or 11 · an internet connection · about 10 minutes · permission to install '
                  'programs on this computer. On a Mac or Linux? See [Mac and Linux](#mac-linux). Already have Python? '
                  '[Check it in one minute](#already).', steps, check_md, problems)
    write('install-python.md', t)
    return problems


# ================================================================= G3 first program in IDLE
def g3():
    for f in ('c06-fig-idle-shell.png', 'c06-fig-idle-run.png'):
        shutil.copy(CH6 / 'images' / f, IMG / f)
    prog = 'print("Hello, world!")\nprint("Welcome to Python")'
    out = run([sys.executable, '-c', prog])
    ok(out == 'Hello, world!\nWelcome to Python')
    t = ('# Your first program in IDLE\n\n*Get started. IDLE comes with Python: the exam uses it. First the shell, then a '
         'saved program (section 6.3 of the book).*\n\n'
         '## 1. The shell: one line at a time {#shell}\n\n' + pic('c06-fig-idle-shell.png', 'The IDLE shell', 420) + '\n\n'
         '| Part | What it is |\n|:-:|---|\n| **A** | the shell window |\n| **B** | the prompt `>>>`: Python is waiting |\n'
         '| **C** | the answer to `7 + 5`, at once |\n| **D** | the output of `print("Namaste")` |\n\n'
         '- ✅ **Do:** type `7 + 5` and press Enter; then `print("Namaste")`.\n'
         '- ⚠️ **Watch out:** work in the shell is **not saved**.\n\n'
         '## 2. A saved program: five steps {#script}\n\n' + pic('c06-fig-idle-run.png', 'Running a script in IDLE', 640) + '\n\n'
         '1. **File → New File**: the editor opens.\n2. Type the program.\n3. **File → Save** (Ctrl+S), name it `hello.py`.\n'
         '4. **Run → Run Module** (F5): the file goes to the shell.\n5. Read the output in the **shell**: first IDLE\'s '
         '`= RESTART` line, then your output.\n\n' + f'```python\n{prog}\n```\n\n*Output:*\n\n```text\n{out}\n```\n\n'
         '- ✅ **Do:** save in one folder, for example `Documents\\Python`, with names like `marks_total.py`.\n'
         '- ❌ **Don\'t:** type `>>>` or line numbers into the editor: a script holds only the statements.\n'
         '- 👀 **Why does the output appear in the other window?** The editor only holds the text; F5 hands the file to '
         'the shell, which runs it.\n\nProblems? [When things go wrong](when-things-go-wrong.md).\n')
    write('first-program-in-idle.md', t)


# ================================================================= G5 VS Code
def g5():
    s = Screen('gs-vs-1-tasks', 'Setup – Visual Studio Code: Select Additional Tasks')
    s.text(0.4, 2.65, 'Select the additional tasks you would like Setup to perform:', fs=9.5)
    s.check(0.5, 2.25, 'Create a desktop icon', on=True)
    s.check(0.5, 1.95, 'Add "Open with Code" action to the file context menu', on=True)
    s.check(0.5, 1.65, 'Add "Open with Code" action to the folder context menu', on=True)
    s.check(0.5, 1.35, 'Register Code as an editor for supported file types', on=True)
    s.check(0.5, 1.05, 'Add to PATH (requires shell restart)', on=True)
    s.button(4.6, 0.3, 1.4, 0.4, 'Next >', primary=True)
    s.label(0.25, 2.25, 'A'); s.label(0.25, 1.8, 'B'); s.label(4.9, 1.05, 'C'); s.label(6.2, 0.5, 'D')
    v1 = s.save()

    s = Screen('gs-vs-2-extension', 'Visual Studio Code – Extensions', kind='dark')
    s.box(0.12, 0.12, 0.45, 2.85, fc='#333333', ec='#333333', r=0.01)
    for k, ic in enumerate(['📄', '🔍', '⑂', '▷']):
        s.text(0.24, 2.7 - k * 0.42, ic, fs=11, color='#BBBBBB')
    for dx, dy in ((0, 0), (0.11, 0), (0, 0.11), (0.15, 0.15)):            # the Extensions icon: four small squares
        s.ax.add_patch(Rectangle((0.24 + dx, 0.93 + dy), 0.09, 0.09, fc='white', ec='white'))
    s.box(0.7, 2.5, 2.6, 0.32, fc='#3C3C3C', ec='#555555'); s.mono(0.8, 2.66, 'python', fs=9, color='white')
    s.box(0.7, 1.55, 2.6, 0.8, fc='#37373D', ec='#555555')
    s.text(0.85, 2.15, 'Python', fs=10.5, weight='bold', color='white'); s.text(0.85, 1.88, 'Microsoft  ✓ verified', fs=8.5, color='#9CDCFE')
    s.button(2.45, 1.62, 0.75, 0.3, 'Install', primary=True, fs=8.5)
    s.text(3.6, 2.3, 'Python', fs=16, weight='bold', color='white'); s.text(3.6, 1.95, 'Microsoft', fs=10, color='#9CDCFE')
    s.label(0.75, 1.05, 'A'); s.label(3.45, 2.66, 'B'); s.label(1.6, 1.4, 'C'); s.label(3.35, 1.77, 'D')
    v2 = s.save()

    s = Screen('gs-vs-3-run', 'hello.py – Python – Visual Studio Code', kind='dark')
    s.box(0.12, 1.25, 1.6, 1.7, fc='#252526', ec='#252526', r=0.01)
    s.text(0.2, 2.75, 'EXPLORER', fs=8, color='#BBBBBB'); s.text(0.25, 2.45, '📁 PYTHON', fs=8.5, color='white'); s.text(0.4, 2.2, 'hello.py', fs=8.5, color='white')
    s.mono(1.9, 2.6, '1  print("Hello, world!")', fs=9, color='#D4D4D4')
    s.text(5.85, 2.75, '▷', fs=14, color='#89D185')
    s.box(1.85, 0.2, 4.4, 0.95, fc='#1E1E1E', ec='#555555', r=0.01)
    s.text(1.95, 1.0, 'TERMINAL', fs=8, color='#BBBBBB'); s.mono(1.95, 0.7, 'PS C:\\Python> python hello.py', fs=8.5, color='#D4D4D4')
    s.mono(1.95, 0.42, 'Hello, world!', fs=8.5, color='#B5CEA8')
    s.text(0.2, 0.42, '3.15.x', fs=8.5, color='#BBBBBB')
    s.label(1.0, 2.2, 'A'); s.label(4.6, 2.6, 'B'); s.label(5.6, 2.75, 'C'); s.label(4.6, 0.6, 'D'); s.label(0.9, 0.42, 'E')
    v3 = s.save()

    a, flow = chart('gs-flow-vscode', 'Setting up VS Code', [
        ('do', 'a = 1', {'text': 'Install Python first\n(Install Python page)'}),
        ('do', 'b = 1', {'text': 'Download VS Code;\ntick Add to PATH'}),
        ('do', 'c = 1', {'text': 'Extensions: install\nPython (Microsoft)'}),
        ('do', 'd = 1', {'text': 'Open a folder;\nnew file hello.py'}),
        ('if', 'v', [('out', 'r', {'text': 'Ready'})], [('out', 'h', {'text': 'If things go wrong'})],
         {'text': 'Run shows the\noutput below?'})])
    problems = {
        'p-vs-no-python': ('"Python is not installed" or no interpreter to choose',
                           'VS Code says Python is not installed, or the list of interpreters is empty.',
                           'VS Code does not contain Python; it uses the Python you installed.',
                           'Install Python first ([Install Python](install-python.md)); then restart VS Code and choose it: Ctrl+Shift+P → `Python: Select Interpreter`.'),
        'p-vs-run-nothing': ('Run does nothing, or there is no Run button',
                             'Pressing ▷ does nothing, or the button is missing.',
                             'The Python extension is not installed, or the file is not saved as `.py`.',
                             'Install the **Python** extension by **Microsoft** (step 2); save the file with a `.py` name.'),
        'p-vs-path': ('"code" is not recognized in a terminal',
                      'Typing `code .` in a terminal does not open VS Code.',
                      'The **Add to PATH** box was not ticked during setup (part C of step 1).',
                      'Run the VS Code installer again and tick **Add to PATH**; then open a new terminal.'),
        'p-vs-wrong-ext': ('Many extensions with "Python" in the name',
                           'The search shows many extensions.',
                           'Anyone can publish an extension.',
                           'Choose the one named **Python**, published by **Microsoft**, with the verified tick. Install only what you need.'),
    }
    steps = [
        dict(id='vs-install', title='Download and install VS Code', pic=v1, alt='VS Code setup: additional tasks',
             key=[('A', 'a desktop icon (useful)'), ('B', '"Open with Code" on files and folders: lets you right-click a folder and open it'),
                  ('C', '**Add to PATH**: lets you type `code` in a terminal; keep it **ticked**'), ('D', 'go on')],
             body='Download from VS Code\'s own site (**code.visualstudio.com**) and run the installer. Accept the licence, keep '
                  'the suggested folder, and on the **Select Additional Tasks** screen tick the boxes as in the drawing.',
             do='tick **Add to PATH** (C).', dont='download VS Code from any other site.',
             watch='VS Code does not include Python: install Python first.', see='VS Code opens with a Welcome page.',
             prob=['p-vs-path']),
        dict(id='vs-extension', title='Install the Python extension', pic=v2, alt='VS Code extensions',
             key=[('A', 'the **Extensions** icon in the Activity Bar (or Ctrl+Shift+X)'), ('B', 'type **python** in the search box'),
                  ('C', 'the extension named **Python** by **Microsoft** (verified)'), ('D', 'its **Install** button')],
             do='install **Python** by **Microsoft**; it also brings Pylance (better hints) on its own.',
             dont='install many extensions you do not understand.',
             see='the Install button turns into a settings gear.', prob=['p-vs-wrong-ext']),
        dict(id='vs-folder', title='Open a folder and make a file',
             body='1. Make a folder, for example `Documents\\Python`.\n2. In VS Code: **File → Open Folder** → choose it. Answer '
                  '**Yes, I trust the authors** (it is your own folder).\n3. **New File** (the page-with-plus icon in the '
                  'Explorer) → name it `hello.py`.\n4. Type `print("Hello, world!")` and save (**Ctrl+S**).',
             do='keep all your programs of one chapter in one folder.',
             dont='open your whole Documents or C: drive as a folder: VS Code becomes slow.',
             see='`hello.py` in the **Explorer** on the left.'),
        dict(id='vs-run', title='Choose Python and run', pic=v3, alt='running a file in VS Code',
             key=[('A', 'the **Explorer**: your folder and files'), ('B', 'the **editor**: your program'), ('C', 'the **Run Python File** button ▷'),
                  ('D', 'the **terminal**: the output appears here'), ('E', 'the Python in use: click it to change')],
             body='The first time, choose the Python to use: **Ctrl+Shift+P** → type `Python: Select Interpreter` → pick the '
                  'Python you installed. Then press ▷ (C).',
             do='check part **E**: it should show 3.12 or later.',
             see='`Hello, world!` in the terminal (D).', prob=['p-vs-no-python', 'p-vs-run-nothing']),
    ]
    tail = ('## Notebooks inside VS Code (optional) {#notebooks}\n\nVS Code can also open notebooks (`.ipynb`), like Jupyter and '
            'Colab: install the **Jupyter** extension (Microsoft), then open a `.ipynb` file or press Ctrl+Shift+P → '
            '`Create: New Jupyter Notebook`. Choose your Python as the "kernel" when asked. You do not need this for Class '
            'XI.\n\n'
            '## Why learn VS Code? {#why}\n\nVS Code is free, and it is built from open-source code. For several years it has '
            'been the editor most used by programmers in the large yearly developer surveys. Because its code is open, other '
            'editors are built on it, such as Cursor and Google\'s Antigravity, so what you learn here carries over.\n\n'
            '## Not needed in Class XI {#later}\n\n- **Virtual environments** (a separate set of packages for each project): '
            'you will meet them in larger projects.\n- **Pylance settings, Code Runner and other extensions**: the Python '
            'extension is enough.\n- **Git inside VS Code**: for saving versions of a project, later.\n')
    t = step_page('VS Code, step by step', 'Get started',
                  'VS Code is a free editor used for bigger projects. Install Python first; VS Code uses it.',
                  (a, flow), [('Download VS Code', 'vs-install', 'Download and install VS Code'),
                              ('Extensions', 'vs-extension', 'Install the Python extension'),
                              ('Open a folder', 'vs-folder', 'Open a folder and make a file'),
                              ('Run shows', 'vs-run', 'Choose Python and run')],
                  '**Before you start.** Python installed ([Install Python](install-python.md)) · about 400 MB of space · '
                  'about 10 minutes.', steps, '', problems, tail)
    write('vs-code.md', t)
    return problems


# ================================================================= G6 Jupyter
def g6():
    pipv = run([sys.executable, '-m', 'pip', '--version'])
    ok(pipv.startswith('pip '), pipv)
    s = Screen('gs-ju-1-pip', 'Windows PowerShell (a terminal)', kind='dark')
    s.terminal(0.2, 0.25, 6.0, 2.7, [('PS C:\\Users\\you> py -m pip install notebook', '#FFFFFF'),
                                     ('Collecting notebook ...', '#9CDCFE'), ('...', '#9CDCFE'),
                                     ('Successfully installed ... notebook-7.x ...', '#B5CEA8'),
                                     ('PS C:\\Users\\you> py -m notebook', '#FFFFFF'),
                                     ('... http://localhost:8888/tree?token=...', '#DCDCAA')])
    s.label(5.95, 2.75, 'A'); s.label(5.95, 2.09, 'B'); s.label(5.95, 1.87, 'C'); s.label(5.95, 1.65, 'D')
    j1 = s.save()
    s = Screen('gs-ju-2-notebook', 'localhost:8888 – Jupyter Notebook', kind='browser')
    s.text(0.3, 2.68, 'File  Edit  View  Run  Kernel  Settings  Help', fs=9)
    s.text(4.9, 2.68, 'Python 3 (ipykernel)', fs=8.5, color=GREY)
    s.box(0.3, 1.75, 5.8, 0.6, fc=OR3, ec=OR); s.mono(0.4, 2.05, '[1]:  print(7 + 5)', fs=9.5)
    s.mono(0.4, 1.5, '      12', fs=9.5, color=OR)
    s.box(0.3, 0.7, 5.8, 0.5, fc='white', ec=GREY); s.mono(0.4, 0.95, '[ ]:', fs=9.5, color=GREY)
    s.label(0.15, 2.05, 'A'); s.label(1.5, 1.5, 'B'); s.label(0.15, 0.95, 'C'); s.label(6.2, 2.68, 'D')
    j2 = s.save()
    a, flow = chart('gs-flow-jupyter', 'Installing and starting Jupyter', [
        ('do', 'a = 1', {'text': 'Install Python first'}),
        ('do', 'b = 1', {'text': 'Terminal: py -m pip\ninstall notebook'}),
        ('do', 'c = 1', {'text': 'Terminal: py -m\nnotebook'}),
        ('do', 'd = 1', {'text': 'Browser: New;\nPython 3'}),
        ('if', 'v', [('out', 'r', {'text': 'Ready'})], [('out', 'h', {'text': 'If things go wrong'})],
         {'text': 'A cell runs with\nShift+Enter?'})])
    problems = {
        'p-ju-pip': ('"pip is not recognized" or "No module named notebook"',
                     'The install command fails, or `py -m notebook` says there is no such module.',
                     'Python is missing, or the install did not finish.',
                     'Check Python first ([Install Python](install-python.md#step-check)). Always write `py -m pip …`, not `pip …`: it installs into the Python that `py` runs.'),
        'p-ju-browser': ('The browser does not open',
                         'The terminal shows addresses, but no browser opens.',
                         'Windows did not start the browser for you.',
                         'Copy the address that starts with `http://localhost:8888/` from the terminal into your browser.'),
        'p-ju-closed': ('"Connection failed" or the notebook stops working',
                        'The page says it cannot connect, or cells do not run any more.',
                        'The terminal window was closed: it was running the Jupyter server.',
                        'Start it again with `py -m notebook`, and keep that window open (minimised) while you work.'),
    }
    steps = [
        dict(id='ju-install', title='Install Jupyter and start it', pic=j1, alt='installing Jupyter in a terminal',
             key=[('A', 'install Jupyter Notebook with Python\'s own installer, **pip**'), ('B', 'success'),
                  ('C', 'start the Jupyter server'), ('D', 'its address: **localhost** means *this computer*, **8888** the "door" (port) it listens at')],
             body=f'Open a terminal and type the two commands. (pip is Python\'s installer for extra packages; on the computer '
                  f'that checked this page it answered `{pipv.split(" from ")[0]}`.)',
             do='keep this terminal open while you work: it **is** the server.',
             dont='close it: the notebook stops working.', see='your browser opens the Jupyter page.',
             prob=['p-ju-pip', 'p-ju-browser']),
        dict(id='ju-notebook', title='Make a notebook and run a cell', pic=j2, alt='a Jupyter notebook',
             key=[('A', 'a **code cell**: type Python here'), ('B', 'its output, just below'), ('C', 'the next, empty cell'),
                  ('D', 'the **kernel**: the Python that runs your cells')],
             body='In the Jupyter page: **New → Notebook**, choose **Python 3 (ipykernel)**. Type `print(7 + 5)` in the first '
                  'cell and press **Shift + Enter**.',
             do='save with **File → Save** (Ctrl+S): the notebook is a `.ipynb` file on your computer.',
             watch='the last line of a cell shows its value even without print, unlike a script ("the Colab trap", section 6.3).',
             see='`12` under the cell.', prob=['p-ju-closed']),
    ]
    tail = ('## How Jupyter works: client and server {#how}\n\nJupyter has two parts on your own computer. The **server** '
            '(started in the terminal) runs Python. The **client** is your browser: it only shows the cells and sends them to '
            'the server. The address `http://localhost:8888` means: this computer (**localhost**), door number **8888** '
            '(the **port**). Nothing goes on the internet. See [Where does my code run?](where-does-my-code-run.md).\n\n'
            '## Anaconda: you may hear of it {#anaconda}\n\nAnaconda is a large download that brings Python, Jupyter and '
            'hundreds of packages together. **For Class XI we do not recommend it**: it is very large, school labs do not '
            'use it, and it installs a **second** Python beside the first, so you may not know which one is running.\n\n'
            '## Not needed in Class XI {#later}\n\n- **Virtual environments**, **JupyterLab** (a bigger form of Jupyter): '
            'later.\n')
    t = step_page('Jupyter Notebook, step by step', 'Get started',
                  'Notebooks on your own computer, without the internet: cells of code and text, each run on its own.',
                  (a, flow), [('Terminal: py -m pip', 'ju-install', 'Install Jupyter and start it'),
                              ('Browser: New', 'ju-notebook', 'Make a notebook and run a cell')],
                  '**Before you start.** Python installed ([Install Python](install-python.md)) · an internet connection for '
                  'the install only · about 5 minutes.', steps, '', problems, tail)
    write('jupyter.md', t)
    return problems


# ================================================================= G7 Colab
def g7():
    s = Screen('gs-co-1-notebook', 'Untitled0.ipynb – Colab', kind='browser')
    s.text(0.3, 2.68, 'File  Edit  View  Insert  Runtime  Tools  Help', fs=9)
    s.button(5.05, 2.53, 0.9, 0.3, 'Share', primary=True, fs=8.5)
    s.text(0.3, 2.3, '+ Code   + Text', fs=9.5, color=BLUE)
    s.box(0.3, 1.45, 5.8, 0.6, fc=OR3, ec=OR); s.text(0.42, 1.75, '▶', fs=12, color=INK); s.mono(0.75, 1.75, 'print("Namaste")', fs=9.5)
    s.mono(0.75, 1.15, 'Namaste', fs=9.5, color=OR)
    s.text(4.6, 0.55, 'Connected  ✓  RAM ▮▮', fs=8.5, color='#2E7D32')
    s.label(0.15, 2.68, 'A'); s.label(6.2, 2.68, 'B'); s.label(1.7, 2.3, 'C'); s.label(0.15, 1.75, 'D'); s.label(2.2, 1.15, 'E'); s.label(6.2, 0.55, 'F')
    c1 = s.save()
    a, flow = chart('gs-flow-colab', 'Starting Google Colab', [
        ('do', 'a = 1', {'text': 'Open\ncolab.research.google.com'}),
        ('do', 'b = 1', {'text': 'Sign in with a\nGoogle account'}),
        ('do', 'c = 1', {'text': 'New notebook'}),
        ('do', 'd = 1', {'text': 'Type code; press\nShift+Enter'}),
        ('if', 'v', [('out', 'r', {'text': 'Ready'})], [('out', 'h', {'text': 'If things go wrong'})],
         {'text': 'Output under\nthe cell?'})])
    problems = {
        'p-co-signin': ('It asks me to sign in, or a school account is blocked',
                        'Colab will not open a notebook without signing in, or your school account has Colab switched off.',
                        'Colab saves notebooks in your Google Drive, so it needs a Google account; schools can switch it off.',
                        'Sign in with a personal Google account (with a parent\'s permission), or ask your teacher.'),
        'p-co-disconnected': ('"Runtime disconnected"',
                              'A message says the runtime disconnected; your names and values are gone.',
                              'An idle notebook is stopped after a while to free Google\'s computers.',
                              'Press **Connect**, then **Runtime → Run all** to run every cell again from the top.'),
        'p-co-nameerror': ('NameError for a name you made',
                           'A cell says a name is not defined, though you made it in another cell.',
                           'The cell that makes the name was not run (or was run before a disconnect).',
                           'Run the cells in order from the top (**Runtime → Run all**).'),
    }
    steps = [
        dict(id='co-start', title='Open Colab and sign in',
             body='Open **colab.research.google.com** in Chrome, Edge or Firefox (on a laptop, a Chromebook or even a phone). '
                  'Sign in with a Google account. Press **New notebook**.',
             do='use a Google account you can sign in to again: your notebooks are kept in its Drive.',
             dont='type passwords, phone numbers or other private data into a notebook you share.',
             see='a page with one empty code cell.', prob=['p-co-signin']),
        dict(id='co-run', title='Run your first cell', pic=c1, alt='a Colab notebook',
             key=[('A', 'the menus: **Runtime → Run all** runs every cell'), ('B', '**Share**, like a Google Doc: send a link to your teacher'),
                  ('C', 'add a **code** cell or a **text** cell'), ('D', 'the ▶ button runs the cell (or Shift + Enter)'),
                  ('E', 'the output, under the cell'), ('F', 'connected to Google\'s computer')],
             body='Type `print("Namaste")` and press ▶ (or **Shift + Enter**). The first run takes a few seconds: Colab connects '
                  'to one of Google\'s computers.',
             watch='the last line of a cell shows its value even without print, unlike a script ("the Colab trap").',
             see='`Namaste` under the cell.', prob=['p-co-disconnected', 'p-co-nameerror']),
        dict(id='co-save', title='Save, share, and open the book\'s notebooks',
             body='- **Save:** Colab saves to your Google Drive (folder *Colab Notebooks*) by itself; **File → Save** saves '
                  'now.\n- **Open this book\'s notebooks:** each chapter\'s notebook page has an **Open in Colab** link; it '
                  'opens the notebook from GitHub. Then **File → Save a copy in Drive** to keep your own copy.\n'
                  '- **Download:** **File → Download → Download .py** gives the code as a Python script for IDLE.',
             do='save a copy before you change a book notebook.',
             see='your notebook in Google Drive → *Colab Notebooks*.'),
    ]
    tail = ('## Not needed in Class XI {#later}\n\n- **GPU and TPU** (Runtime → Change runtime type): for training AI '
            'models, later.\n- **Installing extra libraries** (`!pip install …`): not needed for this book.\n')
    t = step_page('Google Colab, step by step', 'Get started',
                  'Python in your browser, on Google\'s computers: nothing to install. Good on a Chromebook, a phone, or a '
                  'computer where you may not install programs.',
                  (a, flow), [('Open colab', 'co-start', 'Open Colab and sign in'),
                              ('Type code', 'co-run', 'Run your first cell'),
                              (None, 'co-save', 'Save, share, and open the book\'s notebooks')],
                  '**Before you start.** An internet connection · a Google account · a browser.', steps, '', problems, tail)
    write('google-colab.md', t)
    return problems


# ================================================================= G1 start here (with Thonny)
def g1():
    a, flow = chart('gs-flow-start', 'Which way will you use Python?', [
        ('if', 'own', [('out', 'g2', {'text': 'Install Python,\nthen use IDLE'})],
         [('if', 'lab', [('out', 'lab', {'text': 'It is already there:\nuse IDLE'})],
           [('out', 'co', {'text': 'Use Google Colab'})], {'text': 'In a school lab?'})],
         {'text': 'Your own Windows,\nMac or Linux computer?'})])
    t = ('# Start here: set up Python\n\n*Get started. Before Chapter 6 you need a place to write and run Python. Answer one '
         'question, then follow the page it points to.*\n\n' + pic(flow, 'Which way will you use Python?', 420) + '\n\n'
         '| Your situation | Do this | Then |\n|---|---|---|\n'
         '| Your own **Windows** laptop or desktop | [Install Python](install-python.md) (10 minutes) | [Your first program in IDLE](first-program-in-idle.md) |\n'
         '| A **Mac** or **Linux** computer | [Install Python: Mac and Linux](install-python.md#mac-linux) | [Your first program in IDLE](first-program-in-idle.md) |\n'
         '| A **school lab** | nothing: Python and IDLE are already there | [Your first program in IDLE](first-program-in-idle.md) |\n'
         '| A **phone**, a **Chromebook**, or a computer where you may not install | [Google Colab](google-colab.md): nothing to install | the book\'s Colab notebooks |\n\n'
         '**Later, if you want more:** [VS Code](vs-code.md) for bigger projects · [Jupyter Notebook](jupyter.md) for '
         'notebooks without the internet · [Where does my code run?](where-does-my-code-run.md) · '
         '[When things go wrong](when-things-go-wrong.md).\n\n'
         '## Which tool, for what? {#tools}\n\n| Tool | Kind | Install? | Best for | In the exam? |\n|---|---|:-:|---|:-:|\n'
         '| IDLE | desktop IDE | comes with Python | learning; the exam | **yes** |\n'
         '| Thonny | desktop IDE | yes | beginners: shows each value as it changes | rarely |\n'
         '| VS Code | desktop IDE | yes | bigger projects | rarely |\n'
         '| Jupyter Notebook | browser, local server | yes | notebooks without the internet | no |\n'
         '| Google Colab | browser, cloud | no | practice anywhere | no |\n\n'
         '## Thonny, in short {#thonny}\n\nThonny is a free Python editor made for beginners at the University of Tartu '
         '(Estonia). It installs with its own Python. Its special feature is the **Variables** pane (View → Variables): when '
         'a program runs step by step (the bug button), it shows every name and its value, as on this site\'s "names and '
         'objects" page. Many schools abroad use it; in India most labs and the practical exam use **IDLE**. To try it: '
         '**thonny.org** → download for Windows → install → type a program in the top pane → press the green **Run** '
         'button.\n')
    write('index.md', t)


# ================================================================= G8 index of problems, G9 where code runs
def g8(probs):
    t = ('# When things go wrong\n\n*Get started. Every problem on the set-up pages, in one list. Each link opens the '
         'problem on its own page, with what you see, why, and the fix.*\n\n')
    for page, title, ps in probs:
        t += f'## {title}\n\n' + ''.join(f'- [{v[0]}]({page}#{k})\n' for k, v in ps.items()) + '\n'
    t += ('## While writing programs\n\n- Line numbers or `>>>` copied into a script → delete them; copy code from this '
          'website or the notebooks, not from a book page.\n- `IndentationError` after pasting code → delete the spaces at '
          'the start of the line.\n- A file saved as `hello.py.txt` → save from IDLE or VS Code, not Notepad; in File '
          'Explorer, View → show **File name extensions**.\n- Reading any error message: Chapter 6\'s page [Reading an error '
          'message](../unit-2/006-ch06-getting-started-with-python/explained-reading-an-error-message.md).\n')
    write('when-things-go-wrong.md', t)


def g9():
    shutil.copy(ROOT / 'book' / 'assets' / 'images' / 'ch06' / 'c06-online-where-code-runs.png', IMG / 'where-code-runs.png')
    old = (ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python' / 'explained-where-does-my-code-run.md')
    if old.exists():
        body = old.read_text(encoding='utf-8')
    else:
        body = (D / 'where-does-my-code-run.md').read_text(encoding='utf-8')
    body = body.replace('../../assets/images/ch06/c06-online-where-code-runs.png', f'{REL}/where-code-runs.png')
    body = re.sub(r'^# Explained: ', '# ', body, flags=re.M)
    body = body.replace('*Chapter 6 · Explained. Table 6.3 in the printed chapter sorts', '*Get started. Table 6.3 of the book (Chapter 6) sorts')
    write('where-does-my-code-run.md', body)


def pages_file():
    (D / '.pages').write_text('title: "Get started: set up Python"\nnav:\n    - index.md\n    - install-python.md\n'
                              '    - first-program-in-idle.md\n    - google-colab.md\n    - vs-code.md\n    - jupyter.md\n'
                              '    - where-does-my-code-run.md\n    - when-things-go-wrong.md\n', encoding='utf-8')


if __name__ == '__main__':
    g9()
    p2 = g2()
    g3()
    p5 = g5()
    p6 = g6()
    p7 = g7()
    g8([('install-python.md', 'Installing Python', p2), ('vs-code.md', 'VS Code', p5), ('jupyter.md', 'Jupyter', p6),
        ('google-colab.md', 'Google Colab', p7)])
    g1()
    pages_file()
    for name, text in PAGES.items():
        check_links(name, text)
    n_pics = len(list(IMG.glob('gs-*.png'))) - len(list(IMG.glob('gs-*-grey.png')))
    print(f'{len(PAGES)} pages; {n_pics} drawn pictures and flowcharts; {checks} checks, 0 wrong')
