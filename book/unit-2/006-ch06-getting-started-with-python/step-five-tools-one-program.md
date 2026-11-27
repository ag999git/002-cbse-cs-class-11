# Step by step: Five places to write Python, one program

*Chapter 6 · Step by step. The printed chapter compares five tools in Table 6.3. Here is how to use each one, with the same three-line program in all five, so you can see they give the same answer.*

## The program

```python
name = "Asha"
marks = 92
print(name, "scored", marks)
```

*Output:*

```text
Asha scored 92
```

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

All five print exactly:

```text
Asha scored 92
```

The **tool** only changes where you type and where the output appears; the **Python** underneath is the same.

## Two more you may meet

- **Spyder**: an editor for science, part of Anaconda; an editor pane, a console pane, and a list of variables.
- **A terminal on its own**: in Command Prompt, go to the folder and type `python asha.py`; the output appears in the
  same window. This is how programs are often run on Linux and on servers.

## The Colab trap

In a **cell** (Colab, Jupyter) and in the **shell**, a bare expression on the last line shows its value. In a
**script** (IDLE editor, Thonny, VS Code) it does not: use `print`. (Section 6.3, "the line that prints nothing".)
