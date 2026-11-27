"""Chapter 2 online pages (27 Nov 2026; online plan v1 approved, O1-O5).
Explanation pages 0202-0206, 0208-0217 and the index 0201. The interactive page 0207 is tools/ch02_translate.py, the
questions tools/ch02_typed_questions.py. Flowcharts are drawn and checked by 50-tools/algo_lib (via flow_layout);
the Python examples are run here and their real output is printed on the page.
Run from the repository root:  python tools/ch02_pages.py"""
import contextlib
import dis
import io
import math
import random
import shutil
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent.parent
CH = PROJECT / '01-all-chapters-of-cbse-11' / 'ch02-software-and-operating-systems'
sys.path.insert(0, str(PROJECT / '50-tools'))
from flow_layout import Builder  # noqa: E402

D = ROOT / 'book' / 'unit-1' / '002-ch02-software-and-os'
IMG = ROOT / 'book' / 'assets' / 'images' / 'ch02'
REL = '../../assets/images/ch02'
checks = 0


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def head(title, label, intro):
    return (f'# {label}: {title}\n\n*Chapter 2 · {label}. {intro}*\n\n')


def write(name, text):
    (D / name).write_text(text, encoding='utf-8')
    print('wrote', name)


def pic(name, alt, scale=1.25, cap=720):
    from PIL import Image
    src = CH / 'images' / name
    if src.exists():
        shutil.copy(src, IMG / name)
    w = min(cap, int(Image.open(IMG / name).width * 96 * scale / 300))
    return f'![{alt}]({REL}/{name}){{ width="{w}" }}'


def chart(name, title, steps):
    """A process flowchart (not run): laid out and checked by flow_layout/algo_lib, drawn into the site's folder."""
    a = Builder(name, title, steps).build()
    a.check()
    ok(not a.crossings(), name)
    p, w, h = a.draw(IMG)
    return a, p.name


def numbered(a):
    """The numbered steps of a chart, in the order of its boxes (the same numbers as the drawing)."""
    out = []
    for nd in sorted(a.nodes, key=lambda n: n.num):
        t = nd.text.replace('\n', ' ')
        if nd.kind == 'decision':
            tgt = lambda n: next(x.num for x in a.nodes if x.num == n)
            t += f' Yes: go to {tgt(nd.yes)}. No: go to {tgt(nd.no)}.'
        elif nd.next and nd.next != nd.num + 1:
            t += f'; go to {nd.next}.'
        else:
            t += '.' if not t.endswith(('.', '?', '!')) else ''
        out.append(f'{nd.num}. {t}')
    return '\n'.join(out)


# ================================================================= 0202
def grouping():
    t = head('Why books group software differently', 'Sometimes asked',
             'The syllabus has three groups of software. Some books and papers have two, three or four, and put the same '
             'program in different groups. Here is the whole picture, and how to answer.')
    t += '''## The groups, book by book

| Source | Groups | Where translators go | Where utilities go |
|---|---|---|---|
| **CBSE syllabus 2026–27** (this book) | system software; programming tools and language translators; application software | their own group | system software |
| NCERT textbook | the same three groups | their own group (programming tools) | system software |
| Some reference books | system software; application software | system software | application software |
| Other reference books | system; application; utility; libraries | system software | their own group |

## Why they differ

- The **meaning** of each kind of software is the same everywhere: an OS runs the computer, a utility looks after it, a
  translator turns source code into machine code, an application does your job.
- Only the **boxes** differ: whether translators and utilities sit inside "system software" or have boxes of their own.
  A translator does not run the computer (so the syllabus gives it its own group), but it is not a job of the user
  either (so some books call it system software).

## How to answer in the exam

1. Follow the grouping of **the question**: if a paper asks "Compiler is an example of (a) application (b) utility
   (c) system software", the expected answer is (c) system software.
2. If the question is open ("Classify the software"), use the syllabus's three groups and add a few words:
   "a compiler: a language translator (some books: system software)".
3. Never call an OS, a driver or a translator application software: every source agrees on that.

*This page is written with the printed tip box "One group or two?" of section 2.1.*
'''
    write('sometimes-asked-grouping-software.md', t)


# ================================================================= 0203
def airport():
    t = head('The airport, part by part', 'Explained',
             'The printed chapter uses an airport to picture the operating system. Here is the whole mapping, part by '
             'part, with where it stops working.')
    t += pic('colour-airport-all.jpg', 'The whole chapter at one airport', 1.6) + '\n\n'
    rows = [('A', 'Control tower and airport management', 'Operating system', 'Nothing moves without them; they decide who uses what, and when', 'The tower never takes a holiday; a computer without an OS cannot do anything at all'),
            ('B', 'One runway, planes in turn', 'The CPU, shared by turns (process management)', 'One plane at a time; the others wait in a queue', 'A plane holds the runway for minutes; a program holds the CPU for thousandths of a second'),
            ('C', 'Gates and parking bays', 'Memory (RAM)', 'Given to a plane on arrival, freed after take-off', 'A gate fits one plane; RAM is divided among many programs at once (space sharing)'),
            ('D', 'Records office', 'Files', 'Flight plans and passenger lists stored, found, protected', '—'),
            ('E', 'Aerobridges, baggage belts and their drivers', 'Devices and their device drivers', 'Each machine has an operator who knows only that machine', 'A driver is software, not a person'),
            ('F', 'Security check', 'Security; an antivirus', 'Every bag scanned; only ticket holders allowed in', '—'),
            ('G', 'Cleaning and maintenance crew', 'Utilities', 'Keep the airport fit for work', 'Utilities run when needed or on a schedule'),
            ('H', 'The airlines and their flights', 'Application software', 'What the passengers came for', '—'),
            ('I', 'Check-in counter and kiosk', 'User interface', 'Where passengers tell the airport what they want', 'An airport has one or two ways in; a phone has five kinds of interface')]
    t += '## The mapping\n\n| | At the airport | In the computer | What is the same | Where it stops working |\n|:-:|---|---|---|---|\n'
    for r in rows:
        t += '| ' + ' | '.join(r) + ' |\n'
    ok(len(rows) == 9)
    t += '''
## Several runways: several CPU cores

A big airport has two or three runways, so two or three planes can take off at the same moment. A phone with an
8-core processor is like an airport with 8 runways: 8 programs can really run at the same instant, and each core still
shares its time among many programs.

## Humanware: the passengers

Some books say a computer system has four parts: **hardware**, the **operating system**, **application programs** and
**humanware**, the people who use it. At the airport, the humanware is the passengers and the staff: without them, the
planes have nowhere to go.
'''
    write('explained-airport-part-by-part.md', t)


# ================================================================= 0204
def utilities():
    t = head('Utilities on your phone', 'Explained',
             'The printed chapter names five utilities. Here is where to find each one on a phone or laptop, what it '
             'really does, and the cyber links in full.')
    t += pic('colour-utilities.jpg', 'Five utilities', 1.0) + '\n\n'
    t += '''*Menus differ from one phone maker to another; look for the words in **bold**.*

| Utility | What it does | On an Android phone | On a Windows laptop |
|---|---|---|---|
| Compression | stores a file or folder in less space; "unzips" it back | the **Files** app opens and extracts zip files | right-click a folder → **Compress to ZIP file** |
| Backup | keeps a safe copy elsewhere | Settings → Google → **Backup**; WhatsApp → Settings → Chats → **Chat backup** | Settings → **Windows Backup**, or copy to a pen drive |
| Antivirus | finds and removes malware | Play Store → your profile → **Play Protect** | **Windows Security** → Virus & threat protection |
| Defragmenter | gathers the scattered pieces of files on a hard disk | not needed: phones use flash memory | **Defragment and Optimize Drives** (on an SSD it only "trims") |
| Disk cleanup | deletes files nobody needs | Settings → **Storage**, or the Files app → **Clean** | **Disk Cleanup**, or Settings → Storage → Temporary files |

## Why a defragmenter does not help a phone or an SSD

A hard disk has a spinning plate and a moving arm, like a gramophone record. If a file is broken into pieces all over
the plate, the arm must jump about to read it, which is slow; gathering the pieces makes reading fast again. A phone and
an SSD have no moving parts: every piece is reached equally fast, so gathering them saves nothing (and needless writing
wears flash memory out a little).

## Cyber links, in full (Chapter 18)

- **What an antivirus catches.** The three kinds of **malware** in the syllabus: a **virus** (copies itself into other
  files), a **trojan** (looks like a useful program but does harm in secret) and **adware** (forces unwanted ads on you).
  Like the airport's security check, it checks everything that comes in.
- **Backup against ransomware.** Ransomware locks your files and demands money to unlock them. With a recent backup
  kept somewhere else, you lose nothing: wipe the device, restore the backup, and pay nobody.
- **The fake cleaner.** "Your phone is 87% full of junk: clean now!" pop-ups and unknown "cleaner" or "booster" apps are a
  common disguise for adware and trojans. The utilities above come with the phone; you do not need another one.
'''
    write('explained-utilities-on-your-phone.md', t)


# ================================================================= 0205
def printer():
    a, img = chart('c02-flow-printer', 'Installing a printer', [
        ('in', ['p'], {'text': 'Connect the printer', 'pseudo': 'CONNECT the printer'}),
        ('do', 'n = 1', {'text': 'The OS notices a\nnew device', 'pseudo': 'OS NOTICES a new device'}),
        ('if', 'have', [], [('do', 'g = 1', {'text': "Download the driver\nfrom the maker's site", 'pseudo': 'DOWNLOAD the driver from the maker\'s site'}),
                            ('do', 'i = 1', {'text': 'Install the driver', 'pseudo': 'INSTALL the driver'})],
         {'text': 'Driver already\non the computer?', 'pseudo': 'IF the driver is not on the computer THEN'}),
        ('out', 'x', {'text': 'Print a test page\nthrough the driver', 'pseudo': 'PRINT a test page'}),
        ('if', 'ok', [('out', 'r', {'text': 'Printer ready', 'pseudo': 'SHOW "Printer ready"'})],
         [('out', 'c', {'text': 'Show "check the\ndriver and cable"', 'pseudo': 'SHOW "check the driver and cable"'})],
         {'text': 'Did the page\nprint?', 'pseudo': 'IF the page printed THEN'})])
    t = head('Installing a printer: the device driver at work', 'Step by step',
             'The printed chapter explains drivers with a universal TV remote. Here is the real procedure, as numbered '
             'steps and as a flowchart with the same numbers.')
    t += '## The steps\n\n' + numbered(a) + '\n\n## The flowchart\n\n' + pic(img, 'Installing a printer', 1.2) + '\n\n'
    t += '''## What each step means

- **Steps 2–3.** The OS knows "a printer was connected", but not this model's own signals. Windows and Android carry
  drivers for many common printers; if this one is new or rare, the OS cannot print yet.
- **Steps 4–6.** If the driver is missing, the **only** safe place to get it is the maker's own website (or the OS's own update). A pop-up or a
  link in a message saying "update your driver now" is a common way for a **trojan** to get in (Chapter 18).
- **Steps 7–10.** The test page proves that the OS, the driver and the printer understand each other.

*Where the universal remote fits:* steps 5–6 are like giving the remote the code set for your TV's brand.
'''
    write('step-by-step-installing-a-printer.md', t)


# ================================================================= 0206
def kinds():
    t = head('Kinds of application software', 'Helps you understand',
             'The printed chapter separates general-purpose from customised software. Here are the usual kinds by name, '
             'as papers and other books use them, with what each does and an Indian example.')
    gen = [('Word processor', 'writes and formats documents', 'Google Docs, MS Word, LibreOffice Writer'),
           ('Spreadsheet', 'tables of numbers with formulas and charts', 'Google Sheets, MS Excel, LibreOffice Calc'),
           ('Database program (DBMS)', 'stores and searches large organised data', 'MySQL (Class XII), MS Access'),
           ('Presentation', 'slides for a talk', 'Google Slides, PowerPoint, LibreOffice Impress'),
           ('Desktop publishing (DTP)', 'page layouts for books, posters, newspapers', 'Scribus, Adobe InDesign'),
           ('Graphics and photo editing', 'pictures and photos', 'GIMP, Canva, Photoshop'),
           ('Web browser', 'opens websites', 'Chrome, Firefox, Edge'),
           ('Messaging and video calls', 'talk and share', 'WhatsApp, Google Meet'),
           ('Media player', 'plays music and video', 'VLC')]
    cus = [('Payroll', 'works out every employee\'s salary, PF and tax', 'a company\'s own salary system'),
           ('Inventory', 'keeps count of goods in stock', 'a shop\'s or a godown\'s stock system'),
           ('Financial accounting', 'records every rupee in and out', 'a firm\'s accounts system'),
           ('Billing', 'makes bills and receipts', 'a supermarket\'s billing counters'),
           ('Banking', 'accounts, deposits, loans, ATMs', 'a bank\'s core banking system'),
           ('Reservation', 'books seats and berths', 'IRCTC (railways), airline booking'),
           ('School management', 'admissions, fees, marks, report cards', 'your school\'s own system'),
           ('Hospital management', 'patients, doctors, medicines, bills', 'a hospital\'s patient system'),
           ('Government services', 'documents and certificates', 'DigiLocker, Aadhaar services')]
    t += '## General-purpose (ready-made, for anyone)\n\n| Kind | What it does | Examples |\n|---|---|---|\n'
    t += ''.join(f'| {a} | {b} | {c} |\n' for a, b, c in gen)
    t += '\n## Customised (made for one organisation\'s needs)\n\n| Kind | What it does | Examples |\n|---|---|---|\n'
    t += ''.join(f'| {a} | {b} | {c} |\n' for a, b, c in cus)
    ok(len(gen) == 9 and len(cus) == 9)
    t += '''
## Other names you may meet

- **Packages** or **office tools**: general-purpose software sold as a set (word processor + spreadsheet + presentation).
- **Tailor-made** or **domain-specific** software: customised software.
- **Business software**: payroll, inventory and accounting; ready-made versions exist, but large firms often get theirs
  customised.

*In the exam,* "name two kinds of general-purpose software" → word processor, spreadsheet; "two examples of customised
software" → payroll system, a school's fee software.
'''
    write('helps-kinds-of-application-software.md', t)


# ================================================================= 0208
def robot():
    t = head('The robot that knows six commands', 'Challenge',
             'An activity for two students and a classroom. It shows why programs must use exact commands, what a '
             'translator does, and what a syntax error is.')
    cmds = ['MOVE n (steps forward)', 'TURN LEFT', 'TURN RIGHT', 'PICK UP', 'PUT DOWN', 'SAY "words"']
    ok(len(cmds) == 6)
    t += '## The rules\n\nOne student is the **robot**. It understands only these six commands, exactly as written:\n\n'
    t += ''.join(f'{i}. `{c}`\n' for i, c in enumerate(cmds, 1))
    t += '''
The other student is the **programmer**, who wants the robot to "put the book from the table on the chair".

## Round 1: high-level vs low-level

"Put the book on the chair" is a **high-level** instruction: the robot does not understand it. The programmer must break
it into the robot's own commands, for example:

```text
MOVE 3
TURN LEFT
MOVE 2
PICK UP
TURN RIGHT
TURN RIGHT
MOVE 2
PUT DOWN
SAY "Done"
```

This is what a **translator** does: it turns one high-level instruction into many small machine instructions.

## Round 2: compiler or interpreter?

- **Compiler style:** a third student reads the whole list first, checks every line, and only then hands it to the robot.
- **Interpreter style:** the third student reads one line, the robot does it at once, then the next line.

## Round 3: a syntax error

Add the line `FLY TO THE TABLE`. The robot refuses: it is not one of its six commands. In compiler style the robot does
nothing at all until the list is fixed; in interpreter style it carries out the lines before it, then stops.

## Think about it

1. Why must the robot's commands be exact? *(A computer cannot guess what "go near the table" means.)*
2. Write the commands to bring the book back. *(Many answers are right; check by acting it out.)*
'''
    write('challenge-robot-six-commands.md', t)


# ================================================================= 0209
def source_to_run():
    a, img = chart('c02-flow-source-run', 'From source code to a running program', [
        ('in', ['s'], {'text': 'Type the program\nin an editor', 'pseudo': 'TYPE the program in an editor'}),
        ('do', 'e = 1', {'text': 'Translate it\n(compiler)', 'pseudo': 'TRANSLATE it'}),
        ('while', 'e', [('out', 'e', {'text': 'Show the errors', 'pseudo': 'SHOW the errors'}),
                        ('do', 'e = 0', {'text': 'Correct the program\nand translate again', 'pseudo': 'CORRECT and TRANSLATE again'})],
         {'text': 'Syntax errors?', 'pseudo': 'WHILE there are syntax errors'}),
        ('do', 'k = 1', {'text': 'Linker joins library\ncode: executable file', 'pseudo': 'LINK the library code'}),
        ('do', 'l = 1', {'text': 'Loader puts it\ninto RAM', 'pseudo': 'LOAD it into RAM'}),
        ('out', 'r', {'text': 'The program runs', 'pseudo': 'RUN'})])
    t = head('From source code to a running program', 'Sometimes asked',
             'The syllabus names the translators. Some papers and books also ask about the editor, the linker and the '
             'loader: the steps a program goes through before it runs.')
    t += '## The steps\n\n' + numbered(a) + '\n\n## The flowchart\n\n' + pic(img, 'From source code to a running program', 1.15) + '\n\n'
    t += '''## The tools on the way

| Tool | What it does | Like … |
|---|---|---|
| **Editor** | lets you type and save the source code | a notebook |
| **Translator** (compiler) | turns source code into object code; lists syntax errors | the dubbing studio |
| **Linker** | joins your object code with ready-made **library** code into one executable file | binding the chapters of a book with the printed glossary |
| **Loader** | a part of the OS: copies the executable file from storage into RAM and starts it | the usher who takes you to your seat |
| **IDE** | the editor, translator and error messages in one window (IDLE for Python) | a whole studio in one room |

**Errors on the way.** A **syntax error** (grammar) is caught by the translator, before anything runs. A **logical
error** (a wrong formula) is not caught by any tool: the program runs and gives a wrong answer, and only testing finds
it (Chapters 5 and 8).

**And Python?** Python has no separate linker step for your program: its interpreter reads the file, makes bytecode and
runs it, and the `import` statement brings library code in while the program runs (see "How Python really runs").
'''
    write('sometimes-asked-source-to-running-program.md', t)


# ================================================================= 0210
def libraries():
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        print(math.sqrt(144))
        print(math.pi)
        print(math.ceil(4.2), math.floor(4.8))
        print(statistics.mean([82, 75, 91]))
        random.seed(2); print(random.randint(1, 6))
    lines = out.getvalue().split('\n')
    ok(lines[0] == '12.0' and lines[2] == '5 4' and lines[3] == str(statistics.mean([82, 75, 91])))
    t = head('Software libraries', 'Sometimes asked',
             'Both reference books ask "What is a software library? Name some Python libraries." Here is the answer, '
             'with real examples. Python modules are taught fully in Chapter 15.')
    t += f'''## What a library is

A **software library** is a collection of ready-made, tested code (functions) that any programmer can use instead of
writing it again. In Python, each library is a **module** that you bring in with `import`.

*Like:* a reference book on the shelf. You do not work out √144 by hand every time; you look it up.

## Real examples (run on a computer, real output)

```python
import math
print(math.sqrt(144))        # {lines[0]}
print(math.pi)               # {lines[1]}
print(math.ceil(4.2), math.floor(4.8))   # {lines[2]}

import statistics
print(statistics.mean([82, 75, 91]))     # {lines[3]}

import random
print(random.randint(1, 6))  # a dice throw: any number from 1 to 6
```

## Libraries you will meet

| Library | What it gives | Where |
|---|---|---|
| `math` | sqrt, pi, ceil, floor, pow, sin, cos | Class XI syllabus (Chapter 15) |
| `random` | random, randint, randrange | Class XI syllabus (Chapter 15) |
| `statistics` | mean, median, mode | Class XI syllabus (Chapter 15) |
| NumPy | fast arrays and maths on lakhs of numbers | beyond the syllabus |
| Pandas | tables of data (like a spreadsheet in code) | beyond the syllabus (Informatics Practices) |
| Matplotlib | charts and graphs | beyond the syllabus |

## Why libraries help

1. **Saves time:** the code is already written.
2. **Fewer bugs:** it has been tested by thousands of users.
3. **Programs stay short:** one line `math.sqrt(x)` instead of a loop.
'''
    write('sometimes-asked-software-libraries.md', t)


# ================================================================= 0211
def python_runs():
    src = 'a = 10\nprint(a + 5)\n'
    code = compile(src, '<program>', 'exec')
    out = io.StringIO()
    dis.dis(code, file=out)
    lines = [ln.rstrip() for ln in out.getvalue().split('\n') if ln.strip()]
    ok(any('LOAD_CONST' in ln for ln in lines) and any('STORE_NAME' in ln for ln in lines))
    run = io.StringIO()
    with contextlib.redirect_stdout(run):
        exec(code, {})
    ok(run.getvalue().strip() == '15')
    try:
        compile('a = 10\nprint(a)\nb = a +\n', '<program>', 'exec')
        syn = None
    except SyntaxError as e:
        syn = e.lineno
    ok(syn == 3)
    v = f'{sys.version_info.major}.{sys.version_info.minor}'
    t = head('How Python really runs', 'Beyond syllabus',
             'For the exam, Python is an interpreted language. Inside, it works in two stages. This page shows them, '
             'with the real output of a real Python.')
    t += f'''## Two stages

1. **Compile to bytecode.** Python reads the **whole** file, checks its grammar, and turns it into **bytecode**: short,
   simple instructions for an imaginary machine.
2. **Run the bytecode.** The **Python virtual machine** (a program inside Python) carries out the bytecode one
   instruction at a time, the way an interpreter does.

## The real bytecode of a two-line program

The program:

```python
{src.rstrip()}
```

prints `{run.getvalue().strip()}`. Its bytecode, as Python {v} shows it with the `dis` module:

```text
{chr(10).join(lines)}
```

`LOAD_CONST` puts a value on a stack, `STORE_NAME` saves it in a variable, `BINARY_OP` adds, `CALL` calls `print`.
(The exact names change a little between Python versions.)

## Why it matters

- A **grammar error anywhere** stops Python before **line 1** runs, because stage 1 reads the whole file first. Try
  `b = a +` in line 3: Python reports a SyntaxError in line {syn}, and nothing is printed.
- A **mistake found only while running** (dividing by 0, an unknown name) stops it **at that line**, after the lines
  before it have run.
- Python saves the bytecode of imported modules in a `__pycache__` folder (`.pyc` files), so they start faster next time.

## So, compiler or interpreter?

For the syllabus and the exam: **interpreter**. The full truth: Python compiles to bytecode, then interprets the bytecode.
Java does something similar; C and C++ are compiled all the way to machine code.
'''
    write('beyond-how-python-runs.md', t)


# ================================================================= 0212, 0213
def os_at_work():
    t = head('The OS at work on your phone', 'Explained',
             'The printed chapter lists the functions of an operating system. Here each one is seen on a real phone, '
             'with the extra reasons an OS is needed and two names that some books use.')
    t += '''## Each function, on your phone

*Menus differ between phone makers; look for the words in **bold**.*

| Function | Where to see it | What you will notice |
|---|---|---|
| Process management | the **recent apps** screen; Settings → **Apps** | many apps "open" at once, taking turns on the CPU |
| Memory management | Settings → **Developer options** → **Running services**, or **Memory** | the RAM used by each app; old apps closed when RAM is short |
| File management | the **Files** app | folders, photos, downloads; delete, copy, move |
| Device management | Settings → **Connected devices** | Bluetooth earbuds, a printer, a USB cable |
| Security | Settings → **Security** → **Permission manager** | which apps may use your camera, microphone, contacts, location |
| User interface | the home screen, voice assistant, gestures | touch, voice and gestures |

## More reasons an OS is needed

- **Program execution:** it loads programs into RAM and starts them (see "What happens when you tap an app").
- **Input and output:** every key press, touch, sound and picture passes through it.
- **Error detection:** if an app crashes, the OS closes it and keeps the rest running ("App has stopped").
- **Resource allocation:** it decides who gets the CPU, memory and devices, and for how long.

## Time sharing and space sharing

The OS shares a resource in one of two ways:

| Way | What is shared | At the airport | In the computer |
|---|---|---|---|
| **Time sharing** (time multiplexing) | one resource, used **in turns** | one runway: one plane after another | the CPU; a printer printing one job after another |
| **Space sharing** (space multiplexing) | a resource **divided** into parts used at the same time | gates: many planes parked at once | RAM divided among the running programs |
'''
    write('explained-os-at-work.md', t)

    a, img = chart('c02-flow-tap-app', 'What happens when you tap an app', [
        ('in', ['t'], {'text': 'You tap the app icon', 'pseudo': 'TAP the icon'}),
        ('do', 'f = 1', {'text': 'The OS finds the\nprogram on storage', 'pseudo': 'FIND the program on storage'}),
        ('if', 'free', [], [('do', 'c = 1', {'text': 'Close an app that\nis not in use', 'pseudo': 'CLOSE an unused app'})],
         {'text': 'Enough free RAM?', 'pseudo': 'IF there is not enough free RAM THEN'}),
        ('do', 'm = 1', {'text': 'Load the program\ninto RAM', 'pseudo': 'LOAD the program into RAM'}),
        ('do', 'p = 1', {'text': 'Give it turns\non the CPU', 'pseudo': 'GIVE it turns on the CPU'}),
        ('out', 's', {'text': "Show the app's screen", 'pseudo': 'SHOW its screen'})])
    t = head('What happens when you tap an app', 'Step by step',
             'The printed chapter says that one tap uses four functions of the OS. Here are the steps, and a flowchart '
             'with the same numbers.')
    t += '## The steps\n\n' + numbered(a) + '\n\n## The flowchart\n\n' + pic(img, 'What happens when you tap an app', 1.15) + '\n\n'
    t += '''## Which function does each step use?

| Step | Function of the OS |
|---|---|
| 2 (your tap) | user interface |
| 3 (find the program) | file management |
| 4–6 (free RAM, load it) | memory management |
| 7 (turns on the CPU) | process management |
| 8 (show the screen) | device management (the display) and the user interface |

*Why does an app open faster the second time?* It may still be in RAM from last time, so steps 4–6 are skipped.
'''
    write('step-by-step-tap-an-app.md', t)


# ================================================================= 0214
def os_types():
    rows = [('Single-user, single-task', 'one user, one program at a time', 'MS-DOS (old)', 'a basic calculator'),
            ('Single-user, multitasking', 'one user, many programs in turns', 'Windows or macOS on a laptop', 'you, with music and a document open'),
            ('Multi-user', 'many users share one computer, each with an account', 'Linux on a server', 'railway reservation counters all over India using one central system'),
            ('Batch', 'jobs collected and run together, without the user waiting', 'old mainframes', 'all salary slips of a company printed overnight'),
            ('Time-sharing', 'many users get the CPU in short turns, so each seems to have it alone', 'UNIX in a computer lab', 'thirty students on one big computer'),
            ('Real-time', 'must answer within a fixed, very short time, every time', 'the computer in a car\'s airbag, a rocket\'s guidance', 'an airbag that opens within a fraction of a second'),
            ('Multiprocessing', 'several processors (cores) work at the same instant', 'Android on an 8-core phone', 'an airport with several runways'),
            ('Distributed', 'many computers work together as if they were one', 'the systems behind UPI or a search engine', 'lakhs of payments handled at once'),
            ('Mobile', 'made for phones and tablets: touch, battery, sensors', 'Android, iOS', 'your phone'),
            ('Embedded', 'a small OS inside a machine that does one job', 'washing machines, smart TVs, ATMs', 'the wash program of section 2.1')]
    ok(len(rows) == 10)
    t = head('Types of operating system', 'Beyond syllabus',
             'The syllabus asks for the functions of an OS, not its types. Both reference books list the types, and '
             'they are sometimes asked. Here they are, each with an example from daily life.')
    t += '| Type | What it means | Example OS | Daily-life example |\n|---|---|---|---|\n'
    t += ''.join('| ' + ' | '.join(r) + ' |\n' for r in rows)
    t += '''
*One OS can be several types at once:* Windows is single-user and multitasking; Android is mobile, multitasking and
multiprocessing.
'''
    write('beyond-types-of-os.md', t)


# ================================================================= 0215
def report_crime():
    t = head('How to report a cyber crime', 'Explained',
             'The printed chapter tells the story of the "digital arrest" fraud. Here is what to do, step by step, and '
             'where to report. Every address on this page was checked before it was published.')
    t += '''## Where to report

| When | Where | Run by |
|---|---|---|
| **Money has been lost** (UPI, card, bank transfer) | call **1930** at once, the same day if possible: the bank can try to stop the money | the national cyber-crime helpline |
| Any cyber crime: fraud, hacking, bullying, a fake profile | **[cybercrime.gov.in](https://cybercrime.gov.in/)**, the National Cyber Crime Reporting Portal | Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs; about the portal: [i4c.mha.gov.in](https://i4c.mha.gov.in/ncrp.aspx) |
| A **suspected** fraud call, SMS or WhatsApp message, before any money is lost | **[Chakshu on Sanchar Saathi](https://sancharsaathi.gov.in/sfc/)** | Department of Telecommunications |
| Anything urgent and dangerous | **112** or the nearest police station | the police |

## What to keep ready

- the phone numbers, email or social-media IDs used by the criminal;
- screenshots of messages, calls and payment screens;
- the transaction ID, date, time and amount of every payment;
- your bank account and the account the money went to.

## The "digital arrest" fraud, in full

1. **The call.** Someone says they are from the police, customs, the narcotics bureau or a central agency: "a parcel in
   your name contains drugs" or "your Aadhaar is linked to a crime".
2. **The fear.** You are told you are under "digital arrest", must stay on a video call, must not tell anyone. Fake
   uniforms, fake offices and fake documents are shown.
3. **The money.** You are told to transfer money "for verification" or "to clear your name".
4. **The mule accounts.** The money goes to bank accounts opened in the names of poor people, who are paid a little for
   their account and card; the criminals take the rest.
5. **How the police trace it:** the bank trail from account to account, the ATMs where cash was withdrawn and their CCTV
   footage, the phone numbers and the IP addresses used (digital footprints, Chapter 16).

**Remember:** there is **no such thing as a "digital arrest"** in Indian law. No real officer arrests anyone, or asks for
money, on a video call. **Hang up, tell your family, and report it.**

## Never

- share an OTP, a PIN, a password or a screen with anyone, even someone who says they are from your bank;
- install an app or click a link because a caller asks you to;
- let anyone use your bank account or card "for a small fee": that makes you a **money mule**, and that is a crime.
'''
    write('explained-report-a-cyber-crime.md', t)


# ================================================================= 0216
def ui_timeline():
    rows = [('1970s–80s', 'Command line (CUI)', 'type exact commands', 'MS-DOS, UNIX', 'computers had little memory; text was all they could show'),
            ('1984–95', 'Graphical (GUI)', 'click icons and menus with a mouse', 'Apple Macintosh, Windows 95', 'anyone could use a computer without learning commands'),
            ('2007 onwards', 'Touch', 'tap, swipe, pinch', 'iPhone, Android', 'phones had no room for a keyboard and mouse'),
            ('2011 onwards', 'Voice', 'speak', 'Siri, Google Assistant, Alexa', 'hands-free use; help for people who cannot see or type'),
            ('2010s onwards', 'Gesture', 'move a hand, tilt or shake', 'motion-sensing game consoles, VR headsets, "flip to silence"', 'natural movement; games and VR')]
    t = head('From typed commands to voice and gestures', 'Beyond syllabus',
             'The printed chapter shows the five kinds of user interface. Here they are in the order they came, and why '
             'each one came.')
    t += pic('colour-ui.jpg', 'Five interfaces', 1.0) + '\n\n'
    t += '| When | Interface | You … | Early examples | Why it came |\n|---|---|---|---|---|\n'
    t += ''.join('| ' + ' | '.join(r) + ' |\n' for r in rows)
    ok(len(rows) == 5)
    t += '''
*Older ways never disappear:* programmers still use the command line every day, because one typed command can do what
many clicks do (see "Ten safe commands to try").
'''
    write('beyond-ui-timeline.md', t)


# ================================================================= 0217
def commands():
    rows = [('See the files in this folder', 'dir', 'ls'), ('Show which folder you are in', 'cd', 'pwd'),
            ('Show your user name', 'whoami', 'whoami'), ('Show the date', 'date /t', 'date'),
            ('Show the computer\'s name', 'hostname', 'hostname'), ('Print a message', 'echo Namaste', 'echo Namaste'),
            ('Show the OS version', 'ver', 'uname -a'), ('Show the folders as a tree', 'tree', 'ls -R'),
            ('Show the network address', 'ipconfig', 'ip addr'), ('Clear the screen', 'cls', 'clear')]
    ok(len(rows) == 10)
    t = head('Ten safe commands to try', 'Challenge',
             'The command-line interface (CUI) of section 2.6, tried for real. These ten commands only **show** '
             'information: they change nothing.')
    t += '''**How to open the command line:** on Windows, press the Windows key, type **cmd** and press Enter. On Linux
(or a Chromebook's Linux terminal, or a Raspberry Pi), open **Terminal**.

| What it does | Windows (cmd) | Linux |
|---|---|---|
'''
    t += ''.join(f'| {a} | `{b}` | `{c}` |\n' for a, b, c in rows)
    t += '''
## Three rules

1. **Never type a command you do not understand**, and never paste one sent by a stranger: a single line can delete
   files or install malware.
2. Commands that **delete or format** (`del`, `rd`, `format`; `rm`) are not for practice.
3. Try them at school with your teacher, or on your own computer.

**Challenge:** which command would you use to find out which folder you are in, and which to see what is in it? Why does
a programmer find this faster than clicking?
'''
    write('challenge-safe-commands.md', t)


# ================================================================= 0201
def index():
    t = '''# Chapter 2: Software and Operating Systems

The online pages of Chapter 2 of *Computer Science with Python, CBSE Class XI*. The label under each QR code in the
printed book says what you will find: **Explained**, **Step by step**, **See it** (interactive), **Helps you
understand**, **Sometimes asked**, **Beyond syllabus**, **Challenge**, **Practice** and **Revise**.

| Page | Label | Section of the book |
|---|---|---|
| [Why books group software differently](sometimes-asked-grouping-software.md) | Sometimes asked | 2.1 |
| [The airport, part by part](explained-airport-part-by-part.md) | Explained | 2.2 |
| [Utilities on your phone](explained-utilities-on-your-phone.md) | Explained | 2.2 |
| [Installing a printer: the device driver at work](step-by-step-installing-a-printer.md) | Step by step | 2.2 |
| [Kinds of application software](helps-kinds-of-application-software.md) | Helps you understand | 2.3 |
| [Compiler vs interpreter, step by step](see-it-compiler-interpreter.md) | See it | 2.4 |
| [The robot that knows six commands](challenge-robot-six-commands.md) | Challenge | 2.4 |
| [From source code to a running program](sometimes-asked-source-to-running-program.md) | Sometimes asked | 2.4 |
| [Software libraries](sometimes-asked-software-libraries.md) | Sometimes asked | 2.4 |
| [How Python really runs](beyond-how-python-runs.md) | Beyond syllabus | 2.4 |
| [The OS at work on your phone](explained-os-at-work.md) | Explained | 2.5 |
| [What happens when you tap an app](step-by-step-tap-an-app.md) | Step by step | 2.5 |
| [Types of operating system](beyond-types-of-os.md) | Beyond syllabus | 2.5 |
| [How to report a cyber crime](explained-report-a-cyber-crime.md) | Explained | 2.5 |
| [From typed commands to voice and gestures](beyond-ui-timeline.md) | Beyond syllabus | 2.6 |
| [Ten safe commands to try](challenge-safe-commands.md) | Challenge | 2.6 |
| [Questions with answers, by type](questions/index.md) | Practice | the whole chapter |
| [Flashcards](flashcards.md) and [glossary](glossary.md) | Revise | the whole chapter |
| [Concept map](concept-map.md) | Revise | the whole chapter |
'''
    t += COLOUR_SECTION
    write('index.md', t)


COLOUR_SECTION = """
## Full-colour pictures

Large full-colour versions of the pictures of the printed chapter.

**The whole chapter at one airport** (end of the chapter): find each letter, then say what it is in a computer.

![The whole chapter at one airport](../../assets/images/ch02/colour-airport-all.jpg)

**Same machine, different programs** (section 2.1).

![The washing machine](../../assets/images/ch02/colour-washing.jpg)

**Five utilities** (section 2.2): compression, backup, antivirus, defragmenter, disk cleanup.

![Five utilities](../../assets/images/ch02/colour-utilities.jpg)

**The universal remote** (section 2.2): it needs each TV's codes, as the OS needs each device's driver.

![The universal remote](../../assets/images/ch02/colour-remote.jpg)

**Three ways to tell a car where to go** (section 2.4).

![The self-driving car](../../assets/images/ch02/colour-car.jpg)

**Dubbed before release, translated live** (section 2.4): the compiler and the interpreter.

![Dubbed film and live commentary](../../assets/images/ch02/colour-translate.jpg)

**Play your favourite song, five ways** (section 2.6).

![Five interfaces](../../assets/images/ch02/colour-ui.jpg)
"""

ALL = [grouping, airport, utilities, printer, kinds, robot, source_to_run, libraries, python_runs, os_at_work, os_types,
       report_crime, ui_timeline, commands, index]

if __name__ == '__main__':
    IMG.mkdir(parents=True, exist_ok=True)
    only = set(sys.argv[1:])
    for f in ALL:
        if not only or f.__name__ in only:
            f()
    print(checks, 'checks passed')


# ================================================================= concept map (moved online in plan v2)
def concept_map():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch
    INK, OR, OR2, OR3 = '#262626', '#C55A11', '#F8CBAD', '#FDF1E9'
    fig = plt.figure(figsize=(9.0, 5.6))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 9); ax.set_ylim(0, 5.6); ax.axis('off')

    def box(x, y, w, h, t, fc=OR3, bold=False, col=INK, fs=9):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0,rounding_size=0.06', fc=fc, ec=INK, lw=1.1))
        ax.text(x, y, t, ha='center', va='center', fontsize=fs, weight='bold' if bold else 'normal', color=col, linespacing=1.1)

    def line(a, b):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=INK, lw=1.0, zorder=0)
    box(4.5, 5.2, 1.7, 0.42, 'Software', fc=OR, bold=True, col='white', fs=11)
    heads = [(1.5, 'System software'), (4.5, 'Programming tools\nand translators'), (7.5, 'Application software')]
    for x, t in heads:
        line((4.5, 4.99), (x, 4.42))
        box(x, 4.2, 2.2, 0.46, t, fc=OR2, bold=True)
    # system software
    # a side line on the left joins the three kinds; the OS functions hang directly under the OS
    sx = 0.14
    line((1.5, 3.97), (1.5, 3.85)); line((sx, 3.85), (1.5, 3.85)); line((sx, 3.85), (sx, 1.0))
    for y, t, h in [(3.45, 'Operating system\n(the resource manager)', 0.55), (1.95, 'Utilities: compression, backup,\nantivirus, defragmenter, cleanup', 0.55),
                    (1.0, 'Device drivers: one per device', 0.45)]:
        line((sx, y), (0.25, y))
        box(1.6, y, 2.7, h, t)
    xs = [0.55 + i * 0.53 for i in range(5)]
    for x, t in zip(xs, ['process', 'memory', 'file', 'device', 'security']):
        line((x, 3.17), (x, 2.93))
        box(x, 2.78, 0.5, 0.3, t, fs=7.5)
    ax.text(1.6, 2.45, 'the OS functions ("Pilots Must File Daily Safety")', ha='center', fontsize=7.5, style='italic')
    # translators
    lv = [(3.45, 'Machine (0, 1) → assembly → high-level'), (2.6, 'Assembler: assembly → machine, one for one'),
          (1.85, 'Compiler: whole program first,\nall errors, object file'), (1.0, 'Interpreter: one statement at a time,\nstops at the first error (Python)')]
    for y, t in lv:
        line((4.5, 3.97), (4.5, y + 0.28))
        box(4.5, y, 2.7, 0.55, t, fs=8.5)
    # application + UI
    for y, t in [(3.45, 'General-purpose: word processor,\nspreadsheet, browser, WhatsApp'), (2.55, 'Customised: payroll, IRCTC,\nDigiLocker, a school\'s app')]:
        line((7.5, 3.97), (7.5, y + 0.3))
        box(7.5, y, 2.7, 0.55, t, fs=8.5)
    box(7.5, 1.5, 2.7, 0.75, 'User interface (from the OS):\ncommand · graphical · touch ·\nvoice · gesture', fc=OR2, fs=8.5)
    p = IMG / 'c02-concept-map.png'
    fig.savefig(p, dpi=300, facecolor='white'); plt.close(fig)
    t = head('Concept map', 'Revise', 'The whole of Chapter 2 on one page. Cover a box and say what is under it.')
    t += pic('c02-concept-map.png', 'Concept map of Chapter 2', 0.8) + '\n'
    write('concept-map.md', t)


if __name__ == '__main__' and (not sys.argv[1:] or 'concept_map' in sys.argv):
    concept_map()
