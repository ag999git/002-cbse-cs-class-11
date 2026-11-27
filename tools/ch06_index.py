"""Chapter 6 index page (QR 0601) and the colour pictures (28 Nov 2026; online plan v2, O5).
Lists every online page of the chapter with its label and section, checks that each linked file exists, copies the
concept map and puts the full-colour pictures (made by OpenAI from prompts-colour-v1.md, resized here) on the page.
Run from the repository root:  python tools/ch06_index.py"""
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent.parent
CH = PROJECT / '01-all-chapters-of-cbse-11' / 'ch06-getting-started-with-python'
D = ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python'
IMG = ROOT / 'book' / 'assets' / 'images' / 'ch06'
REL = '../../assets/images/ch06'

PAGES = [  # (file, title, label, section)
    ('helps-story-and-versions.md', "Python's story and versions", 'Helps you understand', '6.1'),
    ('helps-python-limits.md', "Python's limits", 'Helps you understand', '6.1'),
    ('step-install-python-vscode-jupyter.md', 'Install Python, VS Code and Jupyter on Windows', 'Step by step', '6.2'),
    ('step-five-tools-one-program.md', 'Five places to write Python, one program', 'Step by step', '6.2'),
    ('explained-where-does-my-code-run.md', 'Where does my code run?', 'Explained', '6.2'),
    ('good-practice-when-things-go-wrong.md', 'When things go wrong', 'Good practice', '6.2'),
    ('good-practice-ai-assistants.md', 'AI assistants: learn first', 'Good practice', '6.2'),
    ('see-it-interactive-or-script.md', 'Interactive or script?', 'See it', '6.3'),
    ('explained-reading-an-error-message.md', 'Reading an error message', 'Explained', '6.3'),
    ('helps-statements-over-several-lines.md', 'Statements over several lines', 'Helps you understand', '6.3'),
    ('see-it-token-explorer.md', 'Token explorer', 'See it', '6.4'),
    ('helps-all-35-keywords.md', 'All 35 keywords', 'Helps you understand', '6.5'),
    ('see-it-identifier-checker.md', 'Identifier checker, and variable vs identifier', 'See it', '6.5'),
    ('good-practice-pep8-and-peps.md', 'PEP 8 for Class XI, and what a PEP is', 'Good practice', '6.5'),
    ('sometimes-asked-literals-up-close.md', 'Literals up close', 'Sometimes asked', '6.6'),
    ('see-it-names-and-objects.md', 'Names and objects, step by step', 'See it', '6.7'),
    ('practice-tricky-assignments-and-none.md', 'Tricky assignments and None', 'Practice', '6.7'),
    ('good-practice-notes-for-people.md', 'Notes for people', 'Good practice', '6.8'),
    ('practice-colab-notebooks.md', 'Four Colab notebooks', 'Practice', 'the whole chapter'),
    ('revise-cheat-sheet.md', 'Chapter 6 cheat sheet (printable A4)', 'Revise', 'the whole chapter'),
    ('questions/index.md', '320 questions with answers, by type', 'Practice', 'the whole chapter'),
]

COLOUR = [  # (raw OpenAI picture, jpg name, caption, section)
    ('col-nets', 'colour-nets', '**Interactive mode is like the nets** (section 6.3): one ball, one shot, and you know at once.', '6.3'),
    ('col-match', 'colour-match', '**Script mode is like a match** (section 6.3): played from start to end, from a plan, and kept on record.', '6.3'),
    ('col-tags', 'colour-tags', '**A variable is a price tag** (section 6.7): the tag is not the thing, and it can be tied to another thing.', '6.7'),
    ('col-case-tag', 'colour-case-tag', '**Box or tag?** (section 6.7): a spectacles case takes one kind of thing only (C++, Java); a price tag can be tied to anything (Python).', '6.7'),
    ('col-glasses', 'colour-glasses', '**Swapping two drinks** (section 6.7): you cannot pour lassi into the nimbu paani; you need an empty third glass first.', '6.7'),
]


def colour():
    src = CH / 'images' / 'colour-raw' / 'colour' / 'openai'
    made = []
    for raw, jpg, cap, sec in COLOUR:
        p = src / f'{raw}.png'
        if not p.exists():
            print('missing (not made yet):', p.name)
            continue
        im = Image.open(p).convert('RGB')
        im = im.resize((1800, im.height * 1800 // im.width), Image.LANCZOS)
        out = IMG / f'{jpg}.jpg'
        im.save(out, quality=88, optimize=True)
        made.append((jpg, cap))
        print('made', out.name, im.size, f'{out.stat().st_size // 1024} KB')
    return made


def index(made):
    shutil.copy(CH / 'images' / 'c06-fig-concept-map-v3.png', IMG / 'c06-concept-map.png')
    t = ('# Chapter 6: Getting Started with Python\n\nThe online pages of Chapter 6 of *Computer Science with Python, CBSE '
         'Class XI*. The label under each QR code in the printed book says what you will find:\n\n'
         '- **Helps you understand**: more explanation of a topic of the book;\n'
         '- **Explained**, **Step by step**: a topic in full, with every step;\n'
         '- **Good practice**: not in the syllabus, but what every good programmer does (and examiners reward);\n'
         '- **See it**: interactive: type, choose, press and watch;\n'
         '- **Sometimes asked**: beyond the syllabus wording, but set now and then in school papers;\n'
         '- **Practice**, **Revise**: questions with answers, notebooks, the cheat sheet, flashcards and the glossary.\n\n'
         '| Page | Label | Section of the book |\n|---|---|---|\n')
    for f, title, label, sec in PAGES:
        assert (D / f).exists(), f
        t += f'| [{title}]({f}) | {label} | {sec} |\n'
    t += '| [Flashcards](flashcards.md) and [glossary](glossary.md) | Revise | the whole chapter |\n'
    assert (D / 'flashcards.md').exists() and (D / 'glossary.md').exists()
    t += ('\nEvery output, error message and answer on these pages was made by running Python, and the interactive pages '
          'were tested against Python itself.\n\n## Concept map\n\n'
          f'![Concept map of Chapter 6]({REL}/c06-concept-map.png){{ width="720" }}\n')
    if made:
        t += '\n## Full-colour pictures\n\nLarge full-colour versions of the pictures of the printed chapter, and two more.\n\n'
        for jpg, cap in made:
            t += f'{cap}\n\n![{cap.split("**")[1]}]({REL}/{jpg}.jpg)\n\n'
    (D / 'index.md').write_text(t, encoding='utf-8')
    print('wrote index.md:', len(PAGES) + 1, 'rows,', len(made), 'colour pictures')


if __name__ == '__main__':
    index(colour())
