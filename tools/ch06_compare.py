"""Chapter 6 online, the two "Compare" pages (Anurag H1-H6, 28 Nov 2026; BOOK-METHOD v13 rule 6.14):
0624 compare-python-and-java.md        the same four lines in Python and in Java, step by step
0625 compare-strong-and-weak-typing.md  Python (strong) and JavaScript (weak), the same lines
Every Python output is made by running Python; every Java line is compiled (and run) with the JDK; every JavaScript
result is run with Node.js. The pictures are the chapter's (tools/figures_s67.py), copied here.
Run from the repository root:  python tools/ch06_compare.py"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT.parent.parent
D = ROOT / 'book' / 'unit-2' / '006-ch06-getting-started-with-python'
IMG = ROOT / 'book' / 'assets' / 'images' / 'ch06'
REL = '../../assets/images/ch06'
CHAP_IMG = PROJECT / '01-all-chapters-of-cbse-11' / 'ch06-getting-started-with-python' / 'images'
JDK = next(Path(r'C:\Program Files\Microsoft').glob('jdk-21*')) / 'bin'
checks = 0


def ok(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def py(src):
    """Run a Python program; return its output, or the last line of its error."""
    p = subprocess.run([sys.executable, '-I', '-X', 'utf8', '-c', src], capture_output=True, text=True, encoding='utf-8')
    return p.stdout.rstrip('\n') if p.returncode == 0 else p.stderr.strip().split('\n')[-1]


def java(body, run=False):
    """Compile a Java main() body; return the compiler's first error line (without the file part) or the output."""
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / 'Main.java'
        f.write_text('public class Main {\n    public static void main(String[] args) {\n' +
                     ''.join(f'        {l}\n' for l in body.split('\n')) + '    }\n}\n', encoding='utf-8')
        c = subprocess.run([str(JDK / 'javac.exe'), str(f)], capture_output=True, text=True, cwd=d)
        if c.returncode:
            first = c.stderr.split('\n')[0]
            return 'error: ' + first.split('error: ', 1)[1]
        if run:
            r = subprocess.run([str(JDK / 'java.exe'), '-cp', d, 'Main'], capture_output=True, text=True)
            return r.stdout.rstrip('\n')
        return 'compiles'


def js(expr):
    return subprocess.run(['node', '-e', f'console.log(JSON.stringify({expr}))'], capture_output=True, text=True,
                          shell=True).stdout.strip()


def fence(lang, code):
    return f'```{lang}\n{code}\n```\n'


def head(title, intro):
    return f'# Compare: {title}\n\n*Chapter 6 · Compare. {intro}*\n\n'


for name in ('c06-fig-py-steps.png', 'c06-fig-java-steps.png'):
    shutil.copy(CHAP_IMG / name, IMG / name)

# ------------------------------------------------------------------ 0624 Python and Java
PROG = 'marks = 92\nscore = marks\nmarks = "Ninety two"\nprint(score, marks)'
out1 = py(PROG)
ok(out1 == '92 Ninety two', out1)
CHECK = ('marks = 92\nscore = marks\nprint(id(score) == id(marks))\nmarks = "Ninety two"\n'
         'print(id(score) == id(marks))\nprint(type(score), type(marks))')
out2 = py(CHECK)
ok(out2 == "True\nFalse\n<class 'int'> <class 'str'>", out2)

J_GOOD = 'int marks;\nmarks = 92;\nint score;\nscore = marks;\nmarks = 95;\nSystem.out.println(score + " " + marks);'
ok(java(J_GOOD, run=True) == '92 95')
J_STR = 'int marks;\nmarks = 92;\nmarks = "Ninety two";'
e_str = java(J_STR)
ok(e_str == 'error: incompatible types: String cannot be converted to int', e_str)
J_UNDECL = 'int marks;\nmarks = 92;\nscore = marks;'
e_und = java(J_UNDECL)
ok(e_und == 'error: cannot find symbol', e_und)
J_EMPTY = 'int marks;\nSystem.out.println(marks);'
e_emp = java(J_EMPTY)
ok(e_emp == 'error: variable marks might not have been initialized', e_emp)
J_SCORE_STR = 'int marks = 92;\nint score;\nscore = marks;\nscore = "Ninety two";'
ok(java(J_SCORE_STR) == e_str)
e_py_empty = py('marks = 92\nprint(marks + bonus)')
ok(e_py_empty == "NameError: name 'bonus' is not defined", e_py_empty)

p1 = head('Python and Java, step by step',
          'The printed section 6.7 explains static and dynamic typing in words. This page shows the same four lines in '
          'Python and in Java, one step at a time, with the real answers of Python and of the Java compiler. You do not '
          'need to learn Java: read its lines for the idea.')
p1 += ('## The program in Python\n\n' + fence('python', PROG) + '\nOutput:\n\n' + fence('text', out1) +
       '\nAfter each line, every name and the object it is tied to:\n\n'
       f'![Python: the state after each line]({REL}/c06-fig-py-steps.png){{ width="720" }}\n\n'
       '- **Line 1** makes the object 92 (an `int`), makes the name `marks` and ties it to the object.\n'
       '- **Line 2** makes **no new object**: `score` is tied to the same 92. One object, two tags.\n'
       '- **Line 3** makes a new object, the string, and moves only the tag `marks` to it. `score` stays on 92.\n\n'
       'You can watch this happen with `id()` (the identity of an object) and `type()`:\n\n' + fence('python', CHECK) +
       '\nOutput:\n\n' + fence('text', out2) +
       '\nThe first `True`: after line 2, both names share one object. The `False`: after line 3, `marks` has moved. '
       'And `type()` reports the type of the **object**; the names have none.\n\n')
p1 += ('## The same steps in Java\n\n'
       'In Java, a variable is a **box with a type**. Each step below was compiled with the Java compiler (JDK 21); '
       'the messages are the compiler\'s own, shortened to their first line.\n\n'
       '| Step | Java | What happens | Python, for comparison |\n|---|---|---|---|\n'
       '| 1 | `int marks;` | a **declaration**: a box for whole numbers is made, before any value exists | no such step: a name exists only when it is tied to an object |\n'
       '| 2 | `marks = 92;` | 92 is put into the box | `marks = 92` makes the object and the name and ties them |\n'
       f'| 3 | `score = marks;` before `int score;` | refused: `{e_und}` | no declaration needed |\n'
       '| 4 | `int score;` then `score = marks;` | a second box; a **copy** of 92 is put into it | a second **tag** on the **same** object; nothing is copied |\n'
       f'| 5 | `marks = "Ninety two";` | refused before the program runs: `{e_str}` | allowed: `marks` simply moves to a string |\n'
       f'| 6 | `score = "Ninety two";` | refused in the same way | allowed |\n\n'
       f'![Java: the same steps with typed boxes]({REL}/c06-fig-java-steps.png){{ width="720" }}\n\n'
       '**Two boxes, two copies.** In Java, after `score = marks;` the boxes are separate. This complete Java program '
       'changes `marks` afterwards and prints both:\n\n' + fence('java', J_GOOD) +
       '\nOutput (compiled and run):\n\n' + fence('text', '92 95') +
       '\n`score` kept its own copy, 92. In Python the end result for numbers looks the same (`score` stays 92), but '
       'for a different reason: nothing was copied; only the tag `marks` moved.\n\n'
       '**A name with no value.** Java can declare a box and leave it empty; using it is refused by the compiler: '
       f'`{e_emp}`. In Python a name cannot exist without an object, so a name never given a value is a '
       f'`NameError` when its line runs: `print(marks + bonus)` gives `{e_py_empty}`.\n\n')
p1 += ('## In one table\n\n'
       '| Basis of difference | Java (static typing) | Python (dynamic typing) |\n|---|---|---|\n'
       '| What a variable is | a box with a type | a name (tag) tied to an object |\n'
       '| Declaration | needed before use: `int marks;` | none |\n'
       '| `score = marks` | copies the value into a second box | ties a second tag to the same object |\n'
       '| Wrong type later | refused by the compiler, before the program runs | allowed: the tag moves |\n'
       '| Name used before a value | compiler error | `NameError` when the line runs |\n'
       '| Who checks types, and when | the compiler, before running | Python, while running |\n\n'
       'C and C++ work like Java here. The printed chapter puts this in one sentence: *in Java the type belongs to the '
       'box; in Python it belongs to the object.*\n\n'
       '[Back to Chapter 6](index.md)\n')
(D / 'compare-python-and-java.md').write_text(p1, encoding='utf-8')

# ------------------------------------------------------------------ 0625 strong and weak typing
rows = [('"5" + 3', 'int("5") + 3'), ('"5" - 3', None), ('"5" == 5', None)]
res = []
for expr, _ in rows:
    pr = py(f'print(repr({expr}))')
    jr = js(expr)
    res.append((expr, pr, jr))
ok(res[0][1].startswith('TypeError') and res[0][2] == '"53"', res[0])
ok(res[1][1].startswith('TypeError') and res[1][2] == '2', res[1])
ok(res[2][1] == 'False' and res[2][2] == 'true', res[2])
fix1, fix2 = py('print(int("5") + 3)'), py('print("5" + str(3))')
ok(fix1 == '8' and fix2 == '53')
java_plus = java('System.out.println("5" + 3);', run=True)
ok(java_plus == '53', java_plus)
java_minus = java('System.out.println("5" - 3);')
ok(java_minus.startswith('error: bad operand types'), java_minus)


def show(v):
    return '`' + v + '`'


p2 = head('Strong and weak typing',
          'The printed chapter says that Python is strongly typed and JavaScript, the language of web pages, is weakly '
          'typed. Here are the same lines in both, run in Python and in Node.js (a program that runs JavaScript).')
p2 += ('## Two different questions\n\n'
       '- **Static or dynamic?** *When* are types checked: before the program runs (static: Java, C, C++) or while it '
       'runs (dynamic: Python, JavaScript)? See [Python and Java, step by step](compare-python-and-java.md).\n'
       '- **Strong or weak?** *What happens when two types meet*, as in `"5" + 3`? A strongly typed language refuses '
       'to mix them quietly; a weakly typed language converts one of them for you and goes on.\n\n'
       'The two questions are independent. Python is **dynamic and strong**. JavaScript is **dynamic and weak**.\n\n'
       '## The same lines in Python and JavaScript\n\n'
       '| Line | Python | JavaScript | What JavaScript did |\n|---|---|---|---|\n'
       f'| `{res[0][0]}` | {show(res[0][1])} | {show(res[0][2])} | turned 3 into the text "3" and joined |\n'
       f'| `{res[1][0]}` | {show(res[1][1])} | {show(res[1][2])} | turned "5" into the number 5 and subtracted |\n'
       f'| `{res[2][0]}` | {show(res[2][1])} | {show(res[2][2])} | compared after turning "5" into a number |\n\n'
       'JavaScript guessed differently each time: `+` turned the number into text, `-` turned the text into a number. '
       'Such guesses are behind many bugs on web pages: a form field holds the text "5", and adding 3 gives "53".\n\n'
       '**Python makes you say what you mean:**\n\n'
       + fence('python', 'print(int("5") + 3)     # the number 8\nprint("5" + str(3))     # the text "53"') +
       '\nOutput:\n\n' + fence('text', f'{fix1}\n{fix2}') +
       '\n## Where Java stands\n\n'
       'Java is **static and strong**, with one well-known exception: its `+` joins text with anything, so '
       f'`"5" + 3` gives `{java_plus}` in Java too (compiled and run). But `"5" - 3` is refused by the Java compiler '
       f'(`{java_minus}`), as in Python.\n\n'
       '| Language | Types checked | Mixes types quietly? | In short |\n|---|---|---|---|\n'
       '| Python | while running | no | dynamic and strong |\n'
       '| JavaScript | while running | yes | dynamic and weak |\n'
       '| Java | before running (compiler) | no (except `+` with text) | static and strong |\n\n'
       '**Exam point.** "Python is weakly typed" is wrong. Python is **dynamically** typed (a name has no type) and '
       '**strongly** typed (values are never mixed quietly).\n\n'
       '[Back to Chapter 6](index.md)\n')
(D / 'compare-strong-and-weak-typing.md').write_text(p2, encoding='utf-8')
print('wrote compare-python-and-java.md, compare-strong-and-weak-typing.md;', checks, 'checks, 0 wrong')
