# Chapter 1: Computer System Organisation: Long-answer questions (10)

*Chapter 1 · Questions (online). 4 and 5 marks. Every question is followed by a model answer and a tip for the exam. The section of the book is given in brackets after the difficulty (E easy, M medium, H hard).*

**Q1.** Draw the block diagram of a computer and explain each unit. *[5 marks] (M · 1.5)*

**Answer.** The diagram: Input unit → CPU (control unit, ALU, registers) → Output unit; the CPU ↔ primary memory ↔ secondary memory; dashed control signals from the control unit to every unit.

- **Input unit:** takes data and instructions from the user and sends them in (keyboard, mouse).
- **CPU:** carries out the instructions. Control unit: directs every part. ALU: calculates and compares. Registers: hold what is in use right now.
- **Primary memory (RAM, ROM):** holds the program and data in use; read directly by the CPU.
- **Secondary memory:** keeps data and programs for later (hard disk, SSD).
- **Output unit:** gives the results to the user (monitor, printer).

*Exam tip:* label every box and draw the arrows; the diagram itself usually carries 2 of the marks.

**Q2.** Explain the four levels of memory with one example each, and say how speed, size and cost change. *[4 marks] (M · 1.6)*

**Answer.** (1) Registers: inside the CPU, a few bytes. (2) Cache: between the CPU and RAM, a few MB (L1, L2, L3). (3) Primary memory: RAM (8–16 GB) and ROM. (4) Secondary memory: hard disk, SSD, pen drive (hundreds of GB to TB). Going down the levels, memory becomes **bigger, slower and cheaper** per byte.

**Q3.** Give four differences between RAM and ROM. *[4 marks] (E · 1.6)*

**Answer.**

| Basis of difference | RAM | ROM |
|---|---|---|
| Full form | Random Access Memory | Read Only Memory |
| Read and write | Read and write | Read only (in normal use) |
| Without power | Volatile: contents lost | Non-volatile: contents stay |
| What it holds | Programs and data in use now | Start-up instructions (firmware) |
| Size | Large (GB) | Small (MB) |

**Q4.** Explain the types of ROM. *[4 marks] (H · 1.6)*

**Answer.** **ROM (mask ROM):** written at the factory; cannot be changed. **PROM:** blank when bought; written once by the user with a special device. **EPROM:** can be erased with ultraviolet light through a small window and written again. **EEPROM:** erased and rewritten electrically, byte by byte, without taking the chip out; **flash memory** is a kind of EEPROM erased in blocks, used in pen drives, SSDs and BIOS chips.

**Q5.** Explain booting with the help of steps. *[4 marks] (M · 1.6)*

**Answer.** (1) The power is switched on. (2) The CPU runs the start-up program in ROM (BIOS or UEFI). (3) It checks the hardware: RAM, keyboard, disks. (4) If a part is not working, it gives a beep or an error message and stops. (5) Otherwise it finds the operating system on secondary memory. (6) It loads the operating system into RAM. (7) The operating system takes over and the home screen appears.

**Q6.** Classify the following as input, output or storage devices and justify any two: scanner, plotter, SSD, microphone, projector, OMR, pen drive, speaker. *[4 marks] (E · 1.3)*

**Answer.** Input: scanner, microphone, OMR. Output: plotter, projector, speaker. Storage: SSD, pen drive. *Justification (any two):* a scanner sends a picture of a page **into** the computer; a speaker gives sound **out**; a pen drive **keeps** data for later.

**Q7.** Explain cache memory: where it is, why it is used, its levels and the terms hit and miss. *[4 marks] (M · 1.6)*

**Answer.** Cache is a small, very fast memory between the CPU and RAM, made of SRAM. It keeps copies of the data and instructions used most often, so the CPU waits less for slow RAM. Levels: L1 (smallest, fastest, inside each core), L2, L3 (largest of the three, shared). A **hit** means the data is found in the cache; a **miss** means it must be fetched from RAM.

**Q8.** (a) Convert 5 GB into bits. (b) A phone has 64 GB of storage. How many 4 MB songs can it hold? *[4 marks] (M · 1.7)*

**Answer.** (a) 5 × 1024 × 1024 × 1024 × 8 = **42 949 672 960 bits**. (b) 64 GB = 64 × 1024 = 65 536 MB; 65 536 ÷ 4 = **16 384 songs**.

**Q9.** Using a kitchen as an example, explain how a computer works. *[5 marks] (E · 1.1–1.6)*

**Answer.** The order window is the input unit; the head chef who directs is the control unit; the cook who measures and tastes is the ALU; the plate in the cook's hand is the registers; the masala dabba on the counter is cache; the kitchen shelf is RAM; the recipe painted on the wall is ROM; the store room is secondary memory; the serving window is the output unit. Like chai being made, data goes in, is processed by following a recipe (program), and the result comes out.

**Q10.** Explain how one key press travels from the keyboard to the screen. *[4 marks] (H · 1.3–1.5)*

**Answer.** (1) Pressing a key closes a switch; the keyboard sends the key's code to the computer. (2) The code travels along a bus into RAM. (3) The CPU, running the program (for example a word processor), fetches the code, decides what to do, and stores the letter in the document in RAM. (4) The CPU sends the new picture of the page to the display, and the letter appears on the monitor.
