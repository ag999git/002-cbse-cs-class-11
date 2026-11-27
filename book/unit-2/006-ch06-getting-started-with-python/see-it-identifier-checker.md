# See it: Identifier checker

*Chapter 6 · See it. Section 6.5 has the rules Python enforces and the conventions good programmers follow. Type a name (or press an example) to see whether Python accepts it, and whether it follows the conventions.*

<div class="c6box" markdown="0">
<p><label>A name: <input id="id-input" size="24" spellcheck="false" value="total_marks"></label></p>
<p>Examples: <button class="c6light" data-ch06-name="total_marks">total_marks</button> <button class="c6light" data-ch06-name="2nd_rank">2nd_rank</button> <button class="c6light" data-ch06-name="my marks">my marks</button> <button class="c6light" data-ch06-name="sum$">sum$</button> <button class="c6light" data-ch06-name="class">class</button> <button class="c6light" data-ch06-name="TotalMarks">TotalMarks</button> <button class="c6light" data-ch06-name="PASS_MARK">PASS_MARK</button> <button class="c6light" data-ch06-name="print">print</button> <button class="c6light" data-ch06-name="l">l</button> <button class="c6light" data-ch06-name="नाम">नाम</button> </p>
<div id="id-result"></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var show = Ch06.namePage({input: 'id-input', result: 'id-result'});
  document.querySelectorAll('[data-ch06-name]').forEach(function (b) {
    b.onclick = function () { document.getElementById('id-input').value = b.getAttribute('data-ch06-name'); show(); };
  });
});
</script>

## The rules and the conventions

| Rules Python enforces (break one: the program does not run) | Conventions (break one: it runs, but reads badly) |
|---|---|
| 1. Begin with a letter or `_`, never a digit | meaningful names: `total_marks`, not `tm` |
| 2. Then only letters, digits and `_`: no space, `$`, `-`, `.`, `@` | snake_case: small letters joined by `_` |
| 3. Not a keyword | CAPITALS only for constants: `PASS_MARK` |
| 4. Capital and small letters differ | never `l`, `O`, `I` as one-letter names |
| 5. Any length | do not reuse Python's own names: `print`, `len`, `sum` |

**Names in Indian scripts.** Python accepts letters of every language, so `नाम = "Asha"` is legal. In the exam and in
code you share, use English names: everyone can type and read them.

## Variable vs identifier

The two words are often mixed up. An **identifier** is a **name**; a **variable** is a name **tied to an object**.

| Basis of difference | Identifier | Variable |
|---|---|---|
| What it is | a name, made by the rules above | a name tied to an object (section 6.7) |
| Names what? | anything with a name: a variable, a function, a module | a value the program keeps and uses |
| Examples | `marks`, `print` (a function), `math` (a module) | `marks` after `marks = 92` |
| Has a value? | not by itself | yes: through its object |
| Has a type? | no | **no**: in Python the **object** has the type, not the name (box or tag, section 6.7) |

- Every variable has an identifier (its name); not every identifier is a variable (`print` names a function, `math` a
  module).
- In C++ and Java a variable is a box with a fixed type, so books for those languages describe a variable as "a name, a
  value and a type". In Python the type belongs to the object; the name only points to it.
- A name also has a **scope**, the part of the program where it can be used; you meet scope with functions in Class XII.

*The checker was tested on 5,007 names against Python's own `str.isidentifier()` and `keyword.iskeyword()`, including
names in Devanagari and Tamil: it agrees with Python on every one.*
