# Good practice: When things go wrong

*Chapter 6 · Good practice. The printed chapter says: learn on IDLE. Here are the problems beginners meet most often when they set up and run Python, each as symptom → cause → fix.*

| Symptom | Cause | Fix |
|---|---|---|
| `'python' is not recognized as an internal or external command, operable program or batch file.` | Python is not installed, or its folder is not on PATH | Install it (page "Install Python"); say **Yes** to the PATH question. Or type `py` instead of `python` |
| Typing `python` opens the **Microsoft Store** | Windows has a shortcut ("app execution alias") that points to the Store when no Python is found | Install Python. If it still happens: Start → **Manage app execution aliases**, and check the Python entries |
| `python --version` shows an **old version** (for example 3.8) | Two Pythons are installed; the old one is found first | Type `py list` to see all of them; uninstall the old one, or run `py -3.15` (your version) |
| **IDLE is not in the Start menu** | A shortcut was not made | Type `py -m idlelib` in a terminal |
| **VS Code: "Python is not installed"** or Run does nothing | No interpreter selected, or the Python extension is missing | Install the **Python** extension (Microsoft); then Ctrl+Shift+P → `Python: Select Interpreter` |
| The program was saved as **`hello.py.txt`** | Notepad adds `.txt`; Windows hides known extensions | Save from IDLE or VS Code; in File Explorer, View → tick **File name extensions** to see the real name |
| **Colab asks you to sign in** | Colab runs on Google's computers and saves to your Drive | Sign in with a Google account (a school account is fine) |
| **Colab: "Runtime disconnected"** | An idle notebook is stopped after a while to free Google's computers | Reconnect; run the cells again from the top (values are forgotten) |
| `IndentationError: unexpected indent` after pasting code from a website or PDF | Spaces or tabs at the start of lines were copied wrongly | Delete the spaces at the start of the line; indent only where a block needs it (Chapter 9), always with 4 spaces |
| Line numbers or `>>>` copied into a script | Code copied from a book page or the shell | Delete them: a script holds only the statements. Copy code from this website or the notebooks |

## A habit that prevents most problems

Keep **one** Python (the latest, from python.org), save programs in **one** folder (for example `Documents\Python`), and
give files short names without spaces: `marks_total.py`, not `marks total final (2).py`.
