"""Chapter 2 questions by type, online (QR 0218) (27 Nov 2026; online plan v1 approved).

Pages 01-07 and 11 are written here by hand (each answer with its reason; no printed question is repeated). Pages 08-10
are generated from three checked tables: SOFTWARE (each program and its group, following the syllabus's three groups),
STATEMENTS (each statement and the translator it is true of) and SCENES (each situation and the OS function or the
interface it shows). Run from the repository root:  python tools/ch02_typed_questions.py"""
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
Q = ROOT / 'book' / 'unit-1' / '002-ch02-software-and-os' / 'questions'
TOOL = 'tools/ch02_typed_questions.py'
total = {}
checks = 0


def ok(c, m=''):
    global checks
    assert c, m
    checks += 1


def tag(d, s):
    return f' *({d} · {s})*'


def page(fname, title, intro, sections, count):
    t = (f'# Chapter 2: Software and Operating Systems: {title} ({count})\n\n*Chapter 2 · Questions (online). {intro} '
         f'Try each one first. The difficulty (E easy, M medium, H hard) and the section of the book are given in '
         f'brackets. The answers of the generated pages come from checked tables in a program (`{TOOL}`).*\n\n')
    n = 0
    for head, items in sections:
        t += f'## {head}\n\n'
        for q, a in items:
            n += 1
            t += f'**Q{n}.** {q}\n\n**Answer.** {a}\n\n'
    ok(n == count, (fname, n, count))
    (Q / fname).write_text(t, encoding='utf-8')
    total[fname] = (title, n)
    print('wrote', fname, n)


# ================================================================= the checked tables
# (program, group, kind, why)
SYS, TR, APP = 'system software', 'a programming tool or language translator', 'application software'
SOFTWARE = [
    ('Windows 11', SYS, 'operating system', 'it runs the whole computer'), ('Android', SYS, 'operating system', 'it runs the phone'),
    ('Linux (Ubuntu)', SYS, 'operating system', 'it runs the computer'), ('iOS', SYS, 'operating system', 'it runs the iPhone'),
    ('BOSS Linux', SYS, 'operating system', 'an Indian Linux that runs the computer'), ('macOS', SYS, 'operating system', 'it runs a Mac'),
    ('a printer driver', SYS, 'device driver', 'it lets the OS work one printer'), ('a graphics-card driver', SYS, 'device driver', 'it lets the OS work the display card'),
    ('a webcam driver', SYS, 'device driver', 'it lets the OS work the webcam'), ('an antivirus', SYS, 'utility', 'it protects the computer'),
    ('a backup program', SYS, 'utility', 'it keeps safe copies'), ('a file compressor (zip)', SYS, 'utility', 'it makes files smaller'),
    ('a disk defragmenter', SYS, 'utility', 'it speeds up a hard disk'), ('disk cleanup', SYS, 'utility', 'it removes unneeded files'),
    ('Python\'s interpreter', TR, 'interpreter', 'it translates and runs Python one statement at a time'),
    ('a C++ compiler', TR, 'compiler', 'it translates a whole C++ program into object code'),
    ('an assembler', TR, 'assembler', 'it translates assembly language into machine code'),
    ('IDLE', TR, 'IDE (programming tool)', 'it is the editor and error window for Python'),
    ('a code editor', TR, 'programming tool', 'it is used to type source code'),
    ('WhatsApp', APP, 'general-purpose', 'it does a job for the user: messages'), ('Google Chrome', APP, 'general-purpose', 'it opens websites for the user'),
    ('MS Word', APP, 'general-purpose', 'a word processor'), ('MS Excel', APP, 'general-purpose', 'a spreadsheet'),
    ('VLC media player', APP, 'general-purpose', 'it plays videos'), ('a photo editor', APP, 'general-purpose', 'it edits pictures'),
    ('IRCTC', APP, 'customised', 'it was made for the railways\' bookings'), ('DigiLocker', APP, 'customised', 'it was made for government documents'),
    ('a school\'s fee app', APP, 'customised', 'it was made for one school'), ('a company\'s payroll system', APP, 'customised', 'it was made for one company\'s salaries'),
    ('a hospital\'s patient system', APP, 'customised', 'it was made for one hospital'),
]
# (statement, true of)
STATEMENTS = [
    ('translates the whole program before anything runs', 'compiler'), ('translates and runs one statement at a time', 'interpreter'),
    ('lists all the errors together', 'compiler'), ('stops at the first error', 'interpreter'),
    ('makes an object-code file', 'compiler'), ('must be present every time the program runs', 'interpreter'),
    ('is not needed after the object file is made', 'compiler'), ('stays in memory while the program runs', 'interpreter'),
    ('the program runs faster afterwards', 'compiler'), ('lets you see each result at once while learning', 'interpreter'),
    ('is used by Python (as the syllabus says)', 'interpreter'), ('is used for C and C++', 'compiler'),
    ('translates assembly language into machine code', 'assembler'), ('translates one instruction into one machine instruction', 'assembler'),
    ('turns source code into machine language', 'all three'), ('is a language translator', 'all three'),
    ('works on a high-level language', 'compiler and interpreter'),
    ('a program with errors in lines 2 and 7 shows nothing at all', 'compiler'),
    ('a program with errors in lines 2 and 7 shows the output of line 1', 'interpreter'),
    ('translates the program again each time it is run', 'interpreter'),
    ('the error in line 7 is found only after line 2 is fixed', 'interpreter'),
    ('like dubbing a whole film before release', 'compiler'), ('like live commentary translated ball by ball', 'interpreter'),
    ('like turning station codes into full names, one for one', 'assembler'),
    ('Java first does this, making bytecode', 'compiler'),
]
# (situation, function or interface)
SCENES = [
    ('Music plays while Maps guides you and WhatsApp is open', 'process management'),
    ('An app closes itself in the background because RAM is full', 'memory management'),
    ('You move a photo from Downloads into a folder named "Trip"', 'file management'),
    ('Your earbuds connect and the music plays through them', 'device management'),
    ('An app asks to use your camera and you refuse', 'security'),
    ('The phone locks until your fingerprint is read', 'security'),
    ('A downloaded file is given its place on storage and a name', 'file management'),
    ('Two programs ask to print at once; one waits its turn', 'device management'),
    ('A game gets RAM when it opens and gives it back when it closes', 'memory management'),
    ('The CPU switches between programs every few thousandths of a second', 'process management'),
    ('You type "dir" to see the files', 'command interface (CUI)'),
    ('You click a folder icon with the mouse', 'graphical interface (GUI)'),
    ('You swipe up on the screen to go home', 'touch interface'),
    ('You say "Hey Google, call Amma"', 'voice interface'),
    ('You flip the phone over to silence a call', 'gesture interface'),
    ('You pinch the screen to zoom into a photo', 'touch interface'),
    ('You wave your hand in a VR game to throw a ball', 'gesture interface'),
    ('You type "ls" in a Linux terminal', 'command interface (CUI)'),
    ('You ask a smart speaker for the weather', 'voice interface'),
    ('You double-click an icon to open a program', 'graphical interface (GUI)'),
]
ok(len(SOFTWARE) == 30 and len(STATEMENTS) == 25 and len(SCENES) == 20)


# ================================================================= 01 MCQ (40)
def mcq():
    R = random.Random(7)
    items = []
    hand = [
        ('Which software makes the hardware useful?', ['firmware only', 'software', 'cables', 'a monitor'], 1, 'software tells the hardware what to do', 'E', '2.1'),
        ('A washing machine does a Cotton or a Quick wash because of its:', ['motor', 'drum', 'program', 'pump'], 2, 'the parts are the same; only the program changes', 'E', '2.1'),
        ('How many groups of software does the syllabus name?', ['two', 'three', 'four', 'five'], 1, 'system; programming tools and translators; application', 'E', '2.1'),
        ('Which is the most basic software?', ['a browser', 'the operating system', 'a game', 'a driver'], 1, 'no other program runs without it', 'E', '2.2'),
        ('BOSS Linux was developed by:', ['ISRO', 'C-DAC', 'IIT Bombay', 'NIC'], 1, 'C-DAC made this Indian Linux', 'M', '2.2'),
        ('Which utility is NOT needed on a phone?', ['backup', 'antivirus', 'defragmenter', 'cleanup'], 2, 'phones use flash memory, with no moving parts', 'M', '2.2'),
        ('A device driver is needed because:', ['the OS cannot know every device\'s own signals', 'devices have no power', 'it is an antivirus', 'it speeds up the CPU'], 0, 'each model needs its own exact signals', 'M', '2.2'),
        ('The universal remote in the book stands for:', ['the operating system', 'a device driver', 'a compiler', 'a utility'], 0, 'the remote is the OS; each brand\'s code set is a driver', 'H', '2.2'),
        ('Customised software is made for:', ['everyone', 'one organisation\'s needs', 'games only', 'the OS'], 1, 'like a jersey printed with your name', 'E', '2.3'),
        ('Which can a computer work without?', ['the OS', 'application software', 'drivers', 'system software'], 1, 'it cannot work without system software', 'E', '2.3'),
        ('Machine language is written in:', ['English', 'short codes', '0s and 1s', 'Python'], 2, 'the CPU understands only 0s and 1s', 'E', '2.4'),
        ('ADD, LOAD and STORE are:', ['machine code', 'assembly codes', 'Python keywords', 'OS commands'], 1, 'short codes for machine instructions', 'E', '2.4'),
        ('A program written by the programmer is:', ['object code', 'source code', 'machine code', 'bytecode'], 1, 'object code is the translated version', 'E', '2.4'),
        ('Which translator makes a file that runs without it?', ['assembler only', 'interpreter', 'compiler', 'editor'], 2, 'the compiler makes an object-code file', 'E', '2.4'),
        ('An interpreter meets an error in line 6 of 9. How many lines have run?', ['0', '5', '6', '9'], 1, 'lines 1 to 5 ran; it stops at 6', 'M', '2.4'),
        ('A compiler meets errors in lines 2 and 8. How many lines run?', ['0', '1', '2', '7'], 0, 'nothing runs until every error is fixed', 'M', '2.4'),
        ('Which translator stays in memory while the program runs?', ['compiler', 'interpreter', 'assembler', 'linker'], 1, 'it translates each statement as it runs', 'M', '2.4'),
        ('Python first turns a program into:', ['machine code', 'bytecode', 'assembly', 'HTML'], 1, 'then it runs the bytecode (Beyond syllabus page)', 'H', '2.4'),
        ('IDE stands for:', ['Internal Device Engine', 'Integrated Development Environment', 'Input Data Editor', 'Interpreted Data Entry'], 1, 'editor, translator and errors in one window', 'E', '2.4'),
        ('The OS is called a resource manager because it:', ['manages money', 'shares the CPU, memory, files and devices', 'repairs hardware', 'writes programs'], 1, 'it decides who gets what', 'E', '2.5'),
        ('A running program is a:', ['file', 'process', 'driver', 'folder'], 1, 'a program on storage becomes a process when it runs', 'E', '2.5'),
        ('Giving RAM to a program and taking it back is:', ['process', 'memory', 'file', 'device'], 1, 'memory management', 'E', '2.5'),
        ('App permissions are part of:', ['file management', 'security', 'device management', 'the user interface'], 1, 'they decide what an app may use', 'M', '2.5'),
        ('In the airport analogy, the runway is the:', ['RAM', 'CPU', 'hard disk', 'printer'], 1, 'one plane at a time = one program at a time', 'E', '2.5'),
        ('A phone with 8 cores is like an airport with:', ['8 gates', '8 runways', '8 towers', '8 counters'], 1, '8 programs can really run at the same instant', 'M', '2.5'),
        ('Which interface needs commands to be remembered?', ['GUI', 'touch', 'command (CUI)', 'voice'], 2, 'commands must be typed exactly', 'E', '2.6'),
        ('Pinching to zoom is:', ['gesture', 'touch', 'voice', 'GUI'], 1, 'it is done on the touchscreen', 'M', '2.6'),
        ('Which interface helps a person who cannot see?', ['touch only', 'voice', 'GUI', 'gesture'], 1, 'speaking and listening need no sight', 'E', '2.6'),
        ('Which is malware that pretends to be useful?', ['virus', 'trojan', 'adware', 'utility'], 1, 'like the Trojan horse; Chapter 18', 'M', '2.2'),
        ('The best defence against ransomware is:', ['a faster CPU', 'a recent backup', 'a bigger screen', 'a new driver'], 1, 'restore the files and pay nobody', 'M', '2.2'),
    ]
    for stem, opts, k, why, d, s in hand:
        o = ' '.join(f'({chr(97 + i)}) {x}' for i, x in enumerate(opts))
        items.append((f'{stem} {o}{tag(d, s)}', f'({chr(97 + k)}) {opts[k]}. *Why:* {why}.'))
    # generated: which is system / application / a translator?
    by = {g: [s for s in SOFTWARE if s[1] == g] for g in (SYS, TR, APP)}
    for g, word in [(SYS, 'system software'), (APP, 'application software'), (TR, 'a language translator or programming tool')] * 3 + [(SYS, 'system software')]:
        right = R.choice(by[g])
        wrong = R.sample([s for s in SOFTWARE if s[1] != g], 3)
        opts = wrong + [right]; R.shuffle(opts)
        k = opts.index(right)
        o = ' '.join(f'({chr(97 + i)}) {x[0]}' for i, x in enumerate(opts))
        items.append((f'Which is {word}? {o}{tag("E", "2.1")}', f'({chr(97 + k)}) {right[0]}. *Why:* {right[3]}.'))
    ok(len(items) == 40)
    page('01-mcq.md', 'Multiple-choice questions', 'One mark each.', [('Multiple-choice questions', items)], 40)


# ================================================================= 02 fill in (30)
def fill():
    rows = [('Software that runs the computer itself is ______ software.', 'system', '2.1'),
            ('The ______ is the most basic software: no other program runs without it.', 'operating system', '2.2'),
            ('A ______ keeps a safe copy of your files.', 'backup utility', '2.2'), ('A ______ makes files smaller.', 'compressor (compression utility)', '2.2'),
            ('A ______ lets the OS work one particular device.', 'device driver', '2.2'), ('Harmful software is called ______.', 'malware', '2.2'),
            ('Malware that forces ads on you is ______.', 'adware', '2.2'), ('Ransomware locks your files and demands ______.', 'money', '2.2'),
            ('Software made for one organisation is ______ software.', 'customised', '2.3'), ('A word processor is ______ software.', 'general-purpose application', '2.3'),
            ('IRCTC is an example of ______ software.', 'customised application', '2.3'), ('Machine language uses only ______ and ______.', '0, 1', '2.4'),
            ('Short codes such as ADD are used in ______ language.', 'assembly', '2.4'), ('Python, C++ and Java are ______ languages.', 'high-level', '2.4'),
            ('The translated program is called ______ code.', 'object', '2.4'), ('A ______ translates the whole program at once.', 'compiler', '2.4'),
            ('An ______ translates one statement at a time.', 'interpreter', '2.4'), ('An ______ translates assembly into machine code.', 'assembler', '2.4'),
            ('Python is translated by an ______.', 'interpreter', '2.4'), ('IDLE is an ______ for Python.', 'IDE', '2.4'),
            ('A running program is called a ______.', 'process', '2.5'), ('Sharing the CPU in turns is ______ management.', 'process', '2.5'),
            ('Creating, copying and deleting files is ______ management.', 'file', '2.5'), ('Working the devices through their drivers is ______ management.', 'device', '2.5'),
            ('Screen lock and app permissions belong to the OS function of ______.', 'security', '2.5'), ('The OS is called a ______ manager.', 'resource', '2.5'),
            ('CUI stands for ______ user interface.', 'character', '2.6'), ('GUI stands for ______ user interface.', 'graphical', '2.6'),
            ('"Hey Siri" uses a ______ interface.', 'voice', '2.6'), ('Flipping the phone to silence it is a ______ interface.', 'gesture', '2.6')]
    ok(len(rows) == 30)
    items = [(q + tag('E', s), a + '.') for q, a, s in rows]
    page('02-fill-in.md', 'Fill in the blanks', 'One mark each.', [('Fill in the blanks', items)], 30)


# ================================================================= 03 true / false (30)
def tf():
    rows = [('Hardware can do useful work without software.', False, 'it needs programs to tell it what to do', '2.1'),
            ('The syllabus puts translators in their own group.', True, '"programming tools and language translators"', '2.1'),
            ('An antivirus is application software.', False, 'it is a utility, a kind of system software', '2.2'),
            ('Utilities can come with the OS.', True, 'disk cleanup and backup usually do', '2.2'),
            ('A defragmenter speeds up an SSD.', False, 'an SSD has no moving parts', '2.2'),
            ('Every device of the same kind uses exactly the same driver.', False, 'each model may need its own', '2.2'),
            ('Drivers should be downloaded only from the maker\'s website.', True, 'fake driver pop-ups carry trojans', '2.2'),
            ('WhatsApp is system software.', False, 'it does a job for the user', '2.3'),
            ('DigiLocker is customised software.', True, 'it was made for government documents', '2.3'),
            ('A computer can run without an OS.', False, 'nothing else can run without it', '2.3'),
            ('Machine language is easy for people to write.', False, 'long strings of 0s and 1s', '2.4'),
            ('Assembly language is a high-level language.', False, 'it is low-level: one code per machine instruction', '2.4'),
            ('A high-level program can run on different kinds of CPU after translation.', True, 'it is translated for each', '2.4'),
            ('A compiler lists all errors at once.', True, 'it reads the whole program first', '2.4'),
            ('An interpreter makes an object-code file.', False, 'a compiler does', '2.4'),
            ('A compiled program runs faster.', True, 'it is already translated', '2.4'),
            ('An interpreter finds a division by 0 before running.', False, 'it is found only while running', '2.4'),
            ('A compiler can find a logical error.', False, 'no translator finds a wrong formula', '2.4'),
            ('IDLE comes with Python.', True, 'it is installed with Python', '2.4'),
            ('A process is a program that is running.', True, 'on storage it is only a file', '2.5'),
            ('The OS shares the CPU in turns.', True, 'process management', '2.5'),
            ('Memory management gives RAM and takes it back.', True, 'when programs start and end', '2.5'),
            ('The home screen is the whole OS.', False, 'it is only the user interface', '2.5'),
            ('A phone has only one CPU core.', False, 'many phones have 8', '2.5'),
            ('A GUI needs more memory than a CUI.', True, 'pictures and windows need memory', '2.6'),
            ('Voice interfaces help people who cannot see.', True, 'they need no screen', '2.6'),
            ('Gesture interfaces are found only in games.', False, 'flip to silence, wave to skip', '2.6'),
            ('A "digital arrest" is allowed by Indian law.', False, 'there is no such thing; it is a fraud', '2.5'),
            ('1930 is the helpline when money has been lost to cyber fraud.', True, 'call at once', '2.5'),
            ('Letting others use your bank account for a fee is harmless.', False, 'it makes you a money mule, a crime', '2.5')]
    ok(len(rows) == 30)
    items = [(q + tag('E', s), f'{"True" if v else "False"}. *Why:* {w}.') for q, v, w, s in rows]
    page('03-true-false.md', 'True or false', 'One mark each.', [('True or false', items)], 30)


# ================================================================= 04 assertion-reason (15)
def ar():
    key = 'Choose: (a) both true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.'
    rows = [('The OS is system software.', 'It manages the hardware and runs other programs.', 'a', ''),
            ('A printer needs a driver.', 'The OS does not know every printer\'s own signals.', 'a', ''),
            ('An antivirus is a utility.', 'It does a job such as writing letters.', 'c', 'R is false: it protects the computer'),
            ('Customised software suits one organisation.', 'It is made for that organisation\'s needs.', 'a', ''),
            ('Python runs line by line.', 'Python uses an interpreter.', 'a', ''),
            ('A compiled program runs faster.', 'A compiler stays in memory while it runs.', 'c', 'R is false: the compiler is not needed then'),
            ('An interpreter stops at the first error.', 'It runs each statement before reading the next.', 'a', ''),
            ('Assembly language is easy for beginners.', 'It uses short codes.', 'd', 'A is false: it is close to the machine and hard'),
            ('High-level languages need translators.', 'The CPU understands only machine language.', 'a', ''),
            ('Machine language needs no translator.', 'It is written in 0s and 1s.', 'a', ''),
            ('The OS is a resource manager.', 'It shares the CPU, memory, files and devices.', 'a', ''),
            ('Many apps seem to run at once.', 'The CPU switches between them very fast.', 'a', ''),
            ('A GUI is easy for beginners.', 'A GUI uses little memory.', 'c', 'R is false: a GUI needs more memory'),
            ('A backup protects against ransomware.', 'Ransomware locks your files.', 'a', ''),
            ('A defragmenter helps a hard disk.', 'An SSD has moving parts.', 'c', 'R is false: an SSD has none')]
    ok(len(rows) == 15)
    items = [(f'A: {a} R: {r}{tag("M", "2.2–2.6")}', f'({k}).' + (f' *Why:* {w}.' if w else '')) for a, r, k, w in rows]
    page('04-assertion-reason.md', 'Assertion and reason', 'One mark each. ' + key, [('Assertion and reason', items)], 15)


# ================================================================= 05 short (30)
def short():
    rows = [('[2] Why is software needed? Use the washing machine.', 'Hardware cannot decide what to do; the program (Cotton, Quick wash) tells the same parts what to do and when.', '2.1'),
            ('[2] Name the three groups of software with one example each.', 'System (Windows); programming tools and translators (a compiler); application (WhatsApp).', '2.1'),
            ('[2] Why do some books put a compiler under system software?', 'It is not a job of the user; the syllabus gives translators a group of their own.', '2.1'),
            ('[2] Give two functions of utility software.', 'Protect the computer (antivirus); keep safe copies (backup).', '2.2'),
            ('[2] Why can the OS not work a new printer without its driver?', 'It knows "print a page" but not that model\'s own signals; the driver knows them.', '2.2'),
            ('[2] Name two operating systems for computers and two for phones.', 'Windows, Linux; Android, iOS.', '2.2'),
            ('[2] What is malware? Name its three kinds in the syllabus.', 'Harmful software: virus, trojan, adware.', '2.2'),
            ('[2] Give two safe habits about drivers and apps.', 'Drivers only from the maker\'s site; apps only from the official store.', '2.2'),
            ('[2] Differentiate general-purpose and customised software with examples.', 'Ready-made for anyone (a spreadsheet) vs made for one organisation (a school\'s fee app).', '2.3'),
            ('[2] Name two general-purpose and two customised applications.', 'Word processor, browser; payroll system, IRCTC.', '2.3'),
            ('[2] What is the difference between source code and object code?', 'Source code is as written; object code is the same program in machine language.', '2.4'),
            ('[2] What is assembly language? Why is it called low-level?', 'Short codes for machine instructions, one for one; it is close to the machine and works on one kind of CPU.', '2.4'),
            ('[2] Give two advantages of high-level languages.', 'Easy to write and correct; work on many CPUs once translated.', '2.4'),
            ('[2] What does an assembler do?', 'Translates assembly language into machine code, one instruction for one.', '2.4'),
            ('[2] Why does a compiled program run faster than an interpreted one?', 'It is translated once, before running; an interpreter translates as it runs, every time.', '2.4'),
            ('[2] Why is an interpreter handy while learning?', 'You see each line\'s result at once, and the first error stops it where it is.', '2.4'),
            ('[2] What is an IDE? Name one.', 'Editor, translator and error messages in one window; IDLE.', '2.4'),
            ('[2] What is a software library? Name two Python libraries.', 'Ready-made tested code you can use; math, random.', '2.4'),
            ('[2] What do a linker and a loader do?', 'The linker joins library code into one executable file; the loader puts it into RAM to run.', '2.4'),
            ('[2] What is a process? How is it different from a program?', 'A program that is running; a program on storage is only a file.', '2.5'),
            ('[2] Explain process management with an example.', 'The OS gives each running program turns on the CPU: music, Maps and WhatsApp at once.', '2.5'),
            ('[2] Explain memory management.', 'The OS gives RAM to a program when it starts and takes it back when it ends.', '2.5'),
            ('[2] Explain file management.', 'Creating, naming, storing, finding, copying, deleting and protecting files in folders.', '2.5'),
            ('[2] How does the OS keep your phone secure? Two ways.', 'Screen lock or fingerprint; app permissions.', '2.5'),
            ('[2] Differentiate time sharing and space sharing.', 'One resource used in turns (CPU) vs one resource divided among programs (RAM).', '2.5'),
            ('[3] What happens when you tap an app icon? Name the functions used.', 'The OS finds it (file), gives memory and loads it (memory), gives CPU turns (process), shows its screen (device, UI).', '2.5'),
            ('[2] What is a user interface? Name its five kinds.', 'The way you give commands and see results: command, graphical, touch, voice, gesture.', '2.6'),
            ('[2] Give one advantage and one drawback of a CUI.', 'Uses little memory and is fast for experts; commands must be remembered.', '2.6'),
            ('[2] How do voice interfaces help people with disabilities?', 'People who cannot see or use their hands can give commands by speaking.', '2.6'),
            ('[3] What is the "digital arrest" fraud and what should you do?', 'A fake officer frightens a person on a video call into paying; hang up, tell family, report on 1930 or cybercrime.gov.in.', '2.5')]
    ok(len(rows) == 30)
    items = [(q + tag('E' if '[2]' in q else 'M', s), a) for q, a, s in rows]
    page('05-short-answer.md', 'Short-answer questions', 'Two or three marks each.', [('Short answers', items)], 30)


# ================================================================= 06 long (12)
def long_():
    rows = [('[4] Explain the three groups of software with two examples each, and say why the OS is the most basic.', 'System (Windows, a printer driver); programming tools and translators (a compiler, IDLE); application (WhatsApp, IRCTC). The OS runs the hardware and gives every other program a place to run, so without it nothing works.'),
            ('[5] Explain utility software. Describe four utilities and say where each is found on a phone or laptop.', 'Utilities keep the computer healthy. Compression (zip), backup (Google/WhatsApp backup), antivirus (Play Protect, Windows Security), disk cleanup (Storage, Files → Clean); the defragmenter only for hard disks.'),
            ('[4] What is a device driver? Explain with the universal remote, and give the steps of installing a printer.', 'A program that lets the OS work one device. The remote works a TV only with its brand\'s codes. Steps: connect; OS notices; driver present? if not, download from the maker\'s site and install; test page.'),
            ('[5] Explain machine, assembly and high-level languages with the self-driving car, and give one difference each.', 'High-level: one sentence ("take me to India Gate"); assembly: turn-by-turn steps, one code per instruction; machine: the exact signals (0s and 1s). High-level is easy and portable; low-level is hard and tied to one CPU.'),
            ('[5] Differentiate between a compiler and an interpreter (five points), with the dubbed film and live commentary.', 'Whole program vs one statement; all errors listed vs stops at the first; object file vs none; faster vs slower; needed once vs every run. Dubbed once and shown many times vs translated live every match.'),
            ('[4] A program has an error in line 3 and a division by 0 in line 6. What happens with a compiler and with an interpreter?', 'Compiler: reports line 3, runs nothing; after the fix, the file is made and runs until line 6 stops it. Interpreter: runs lines 1–2, stops at line 3; after the fix, runs up to line 6 and stops there.'),
            ('[5] Explain the functions of an operating system with the airport.', 'Process (runway, planes in turn); memory (gates given and freed); file (records office); device (aerobridges, belts and their operators); security (security check). Plus the user interface (check-in counter).'),
            ('[4] Explain the five kinds of user interface with "play my favourite song".', 'Type a command (CUI); click the song (GUI); tap it (touch); say "play my song" (voice); wave a hand (gesture).'),
            ('[5] Describe the path from source code to a running program.', 'Editor → compiler (syntax errors fixed) → linker joins library code into an executable file → loader puts it into RAM → it runs; logical errors are found by testing.'),
            ('[4] Explain the cyber links of the chapter: antivirus, backup, drivers, apps and permissions.', 'Antivirus catches viruses, trojans, adware; backup defeats ransomware; drivers only from the maker; apps only from the official store; refuse permissions an app does not need.'),
            ('[4] Write about the "digital arrest" fraud: how it works, how it is traced, and how to report it.', 'Fake officer, fear, payment to mule accounts; traced through the bank trail, ATM CCTV, phone numbers and IP addresses; report on 1930, cybercrime.gov.in, Chakshu.'),
            ('[4] Name the types of operating system with an example of each (beyond the syllabus).', 'Single-user (MS-DOS); multitasking (Windows); multi-user (a server); batch (overnight payslips); time-sharing (UNIX lab); real-time (airbag); multiprocessing (8-core phone); distributed (UPI systems); mobile (Android); embedded (washing machine).')]
    ok(len(rows) == 12)
    items = [(q + tag('M', '2.1–2.6'), a) for q, a in rows]
    page('06-long-answer.md', 'Long-answer questions', 'Four or five marks each.', [('Long answers', items)], 12)


# ================================================================= 07 case (8)
def cases():
    rows = [('**Case: the new laptop.** Riya buys a laptop with Windows. (i) Which software came with it? (ii) She installs WhatsApp and a game: which group? (iii) Her old printer does not print: why?', '(i) The OS, drivers and utilities. (ii) Application software. (iii) The printer\'s driver is missing; get it from the maker\'s site.'),
            ('**Case: the slow phone.** Arjun\'s phone is slow and full. (i) Which utility helps? (ii) An app says "Clean now: 87% junk!". Should he install it? (iii) Which OS function closes apps when RAM is full?', '(i) Disk cleanup (Storage, Files → Clean). (ii) No: such "cleaners" are often adware or trojans. (iii) Memory management.'),
            ('**Case: the school app.** A school wants an app for fees and marks. (i) General-purpose or customised? (ii) Name one general-purpose program the office also uses. (iii) Why not buy a ready-made one?', '(i) Customised. (ii) A spreadsheet. (iii) Its fee rules and report cards are its own.'),
            ('**Case: the coding class.** Students write Python in IDLE. (i) What is IDLE? (ii) Which translator runs their programs? (iii) A program has an error in line 4: what do they see?', '(i) An IDE. (ii) An interpreter (via bytecode). (iii) For a spelling error, Python stops before running anything; for a run-time error, lines 1–3 run and it stops at 4.'),
            ('**Case: the game studio.** A studio writes a game in C++. (i) Which translator? (ii) Why does it run fast? (iii) Do players need the translator?', '(i) A compiler. (ii) It is translated once into machine code. (iii) No: only the object (executable) file.'),
            ('**Case: the busy airport.** (i) Which part is the OS? (ii) What do planes waiting for one runway show? (iii) A second runway opens: what is that in a phone?', '(i) Air-traffic control. (ii) Programs taking turns on the CPU (process management). (iii) A second CPU core.'),
            ('**Case: the video call.** A caller in a uniform says Dadi is under "digital arrest". (i) Is this real? (ii) What should the family do? (iii) Where should they report it?', '(i) No: there is no such thing. (ii) Hang up; never pay or share OTPs. (iii) Chakshu on sancharsaathi.gov.in; if money was paid, 1930 and cybercrime.gov.in.'),
            ('**Case: the accessible lab.** A student who cannot see joins the computer lab. (i) Which interface helps most? (ii) Name a software aid. (iii) Which chapter discusses this?', '(i) Voice. (ii) A screen reader. (iii) Chapter 19 (technology and society).')]
    ok(len(rows) == 8)
    items = [(q + tag('M', '2.1–2.6'), a) for q, a in rows]
    page('07-case-study.md', 'Case studies', 'Each case has three parts.', [('Case studies', items)], 8)


# ================================================================= 08 compiler or interpreter? (25)
def sorting():
    items = []
    for st, who in STATEMENTS:
        why = {'compiler': 'a compiler translates the whole program first and makes an object file',
               'interpreter': 'an interpreter translates and runs one statement at a time',
               'assembler': 'an assembler works on assembly language, one code for one instruction',
               'all three': 'every translator turns source code into machine language',
               'compiler and interpreter': 'both translate high-level languages'}[who]
        items.append((f'Compiler, interpreter, assembler, or more than one? "{st}."{tag("M", "2.4")}', f'**{who.capitalize()}**. *Why:* {why}.'))
    ok(len(items) == 25)
    page('08-compiler-or-interpreter.md', 'Compiler or interpreter?', 'Sort each statement (as in some reference books).', [('Sort the statement', items)], 25)


# ================================================================= 09 classify (30)
def classify():
    items = []
    for name, group, kind, why in SOFTWARE:
        items.append((f'Classify **{name}**: which group of software, and which kind?{tag("E", "2.1–2.3")}', f'{group[0].upper() + group[1:]} ({kind}). *Why:* {why}.'))
    ok(len(items) == 30)
    page('09-classify-software.md', 'Classify the software', 'Using the syllabus\'s three groups.', [('Classify', items)], 30)


# ================================================================= 10 which function / interface (20)
def scenes():
    items = [(f'Which OS function, or which kind of user interface? "{s}."{tag("E", "2.5–2.6")}', f'**{f.capitalize()}**.') for s, f in SCENES]
    ok(len(items) == 20)
    page('10-which-function-or-interface.md', 'Which OS function? Which interface?', 'Name the function or the interface each situation shows.', [('Name it', items)], 20)


# ================================================================= 11 NCERT-style, libraries, types of OS (10)
def extra():
    rows = [('Name the two primary services an OS gives to make a computer usable. (NCERT style)', 'Managing the CPU (running programs) and managing memory; it also gives the user an interface.'),
            ('How does a computer understand a program written in a high-level language? (NCERT style)', 'A translator (compiler or interpreter) turns it into machine language, which the CPU runs.'),
            ('Can a computer have RAM but no secondary storage and still have software installed? (NCERT style)', 'Software could be loaded into RAM, but it is lost when the power goes off; installing needs secondary storage.'),
            ('Why is system software needed even when no application is open?', 'It keeps running the hardware, devices, memory and security, and waits for the user.'),
            ('What is a software library? Name three Python libraries in the syllabus.', 'Ready-made tested code; math, random, statistics (Chapter 15).'),
            ('Give two advantages of using a library.', 'Saves writing code again; tested code has fewer bugs.'),
            ('What is a real-time OS? Give an example.', 'One that must answer within a fixed short time every time; a car\'s airbag controller.'),
            ('What is a multi-user OS? Give an example.', 'Many users share one computer through their own accounts; a railway reservation server.'),
            ('What is the difference between a batch OS and a time-sharing OS?', 'Batch runs collected jobs without the user waiting; time-sharing gives many users short turns so each seems alone.'),
            ('What is an embedded OS? Give an example from Chapter 2.', 'A small OS inside a machine that does one job; the washing machine of section 2.1.')]
    ok(len(rows) == 10)
    items = [(q + tag('M', '2.2–2.5'), a) for q, a in rows]
    page('11-ncert-libraries-os-types.md', 'NCERT-style, libraries and types of OS', 'Sometimes asked; two marks each.', [('More questions', items)], 10)


def index():
    t = '# Chapter 2: Software and Operating Systems: questions\n\n'
    n = sum(v[1] for v in total.values())
    t += f'**{n} questions**, each with its answer. They are for learning: try each question first, then read the answer.\n\n**By type of question**\n\n'
    for f in sorted(total)[:7]:
        t += f'- [{total[f][0]}: {total[f][1]}]({f})\n'
    t += '\n**More practice**\n\n'
    for f in sorted(total)[7:]:
        t += f'- [{total[f][0]}: {total[f][1]}]({f})\n'
    (Q / 'index.md').write_text(t, encoding='utf-8')
    print('total', n)
    return n


if __name__ == '__main__':
    for f in (mcq, fill, tf, ar, short, long_, cases, sorting, classify, scenes, extra):
        f()
    n = index()
    ok(n == 250, n)
    print(checks, 'checks passed')
