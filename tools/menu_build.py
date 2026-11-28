"""Write the menu-order files (.pages, read by mkdocs-awesome-pages-plugin) for the website, 26 Nov 2026.

They set the order of the left-hand menu and give every folder a proper name ("Chapter 1: Computer System
Organisation" instead of "001 ch01 computer system organisation"). They never change a web address, so every printed
QR code keeps working. A chapter's menu name is taken from the first heading of its index.md.

Run from the repository root:  python tools/menu_build.py"""
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent / 'book'


def put(folder, text):
    (folder / '.pages').write_text(text, encoding='utf-8')


def h1(md):
    m = re.search(r'^# (.+)$', md.read_text(encoding='utf-8'), re.M)
    return m.group(1).strip()


put(BOOK, """nav:
    - index.md
    - get-started
    - how-to-use.md
    - unit-1
    - unit-2
    - unit-3
    - practical
    - model-papers
    - flashcards
""")
UNITS = {'unit-1': 'Unit I: Computer Systems and Organisation',
         'unit-2': 'Unit II: Computational Thinking and Programming – 1',
         'unit-3': 'Unit III: Society, Law and Ethics',
         'practical': 'Practical work'}
n = 0
for folder, title in UNITS.items():
    put(BOOK / folder, f'title: "{title}"\n')
    for ch in sorted(p for p in (BOOK / folder).iterdir() if p.is_dir()):
        put(ch, f'title: "{h1(ch / "index.md")}"\n')
        n += 1
        if (ch / 'questions').is_dir():
            put(ch / 'questions', 'title: "Questions with answers"\n')
put(BOOK / 'model-papers', 'title: "Model papers"\n')
put(BOOK / 'flashcards', 'title: "Flashcards"\n')
print(f'menu files written: book, {len(UNITS)} units, {n} chapters')
