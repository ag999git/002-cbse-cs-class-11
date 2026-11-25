# Chapter 1: Computer System Organisation: Short-answer questions (25)

*Chapter 1 · Questions (online). 1, 2 and 3 marks. Every question is followed by its answer, the reason and often a tip for the exam. The section of the book is given in brackets after the difficulty (E easy, M medium, H hard).*

## 1 mark

**Q1.** Define data. *(E · 1.1)*

**Answer.** Data is raw facts and figures, such as marks, names or temperatures, before they are processed.

**Q2.** What is a program? *(E · 1.1)*

**Answer.** A set of instructions, in order, that does a whole job.

**Q3.** What is firmware? Give one example. *(M · 1.2)*

**Answer.** Software stored permanently in a hardware chip; for example, the start-up program (BIOS or UEFI) in ROM.

**Q4.** Name two devices that read data from paper. *(E · 1.3)*

**Answer.** Any two: scanner, OMR, OCR (with a scanner), MICR, barcode reader.

**Q5.** What is the work of the ALU? *(E · 1.4)*

**Answer.** It carries out calculations (+ − × ÷) and comparisons (such as 7 > 5).

**Q6.** What is booting? *(E · 1.6)*

**Answer.** Starting a computer: the start-up program in ROM checks the hardware and loads the operating system into RAM.

**Q7.** What is a memory address? *(E · 1.6)*

**Answer.** The number of one memory location (box), by which the CPU finds it.

**Q8.** Why is RAM called "random access"? *(M · 1.6)*

**Answer.** Because any location can be reached directly, in the same time, without going through the others. *Exam tip:* "random" here does not mean "by chance".

**Q9.** How many bytes are there in 1 MB? *(M · 1.7)*

**Answer.** 1024 × 1024 = 1 048 576 bytes.

**Q10.** Arrange in ascending order: GB, KB, PB, MB, TB. *(E · 1.7)*

**Answer.** KB < MB < GB < TB < PB.

## 2 marks

**Q11.** Differentiate between data and information (two points). *(E · 1.1)*

**Answer.**

| Basis of difference | Data | Information |
|---|---|---|
| What it is | Raw facts and figures | Processed data that means something |
| Example | Marks of 40 students | The class average |

**Q12.** Differentiate between hardware and software (two points). *(E · 1.2)*

**Answer.** Hardware is the physical parts and can be touched; software is the programs and cannot be touched. Hardware wears out; software does not wear out, but can have errors (bugs).

**Q13.** Differentiate between impact and non-impact printers, with one example each. *(M · 1.3)*

**Answer.** An impact printer strikes an inked ribbon against the paper, is noisy, and can make carbon copies (dot-matrix). A non-impact printer does not touch the paper, is quiet and gives better quality (inkjet, laser).

**Q14.** Differentiate between soft copy and hard copy. *(E · 1.3)*

**Answer.** A soft copy is output shown on a screen; it cannot be touched and is temporary. A hard copy is output printed on paper; it can be held and kept.

**Q15.** Name the three parts of the CPU and give the task of each. *(E · 1.4)*

**Answer.** Control unit: directs all the parts. ALU: calculates and compares. Registers: hold the data and instruction in use right now.

**Q16.** Differentiate between RAM and ROM (two points). *(E · 1.6)*

**Answer.** RAM can be read and written; ROM can only be read (in normal use). RAM is volatile; ROM is non-volatile. *Exam tip:* the words **volatile** and **non-volatile** carry the marks.

**Q17.** Differentiate between primary and secondary memory (two points). *(E · 1.6)*

**Answer.** The CPU reads primary memory directly; secondary memory is not used directly by the CPU. Primary memory is faster and smaller; secondary memory is slower, bigger and keeps data permanently.

**Q18.** Why is cache memory used? *(M · 1.6)*

**Answer.** The CPU is far faster than RAM. Cache, a small fast memory between them, keeps copies of the data and instructions used most often, so the CPU waits less.

**Q19.** What is the difference between a cache hit and a cache miss? *(M · 1.6)*

**Answer.** Hit: the data the CPU needs is found in the cache. Miss: it is not there and must be fetched from RAM, more slowly.

**Q20.** Differentiate between a hard disk (HDD) and an SSD (two points). *(M · 1.6)*

**Answer.** An HDD stores data magnetically on spinning platters; an SSD uses flash chips with no moving parts. The SSD is faster, quieter and stronger; the HDD is cheaper per GB.

**Q21.** Convert 3 GB into KB. *(E · 1.7)*

**Answer.** 3 × 1024 × 1024 = 3 145 728 KB. *Why:* GB → MB → KB: two steps down, × 1024 each.

**Q22.** A file is 24 576 bits. What is its size in KB? *(M · 1.7)*

**Answer.** 24 576 ÷ 8 = 3072 bytes; 3072 ÷ 1024 = **3 KB**.

## 3 marks

**Q23.** Explain the fetch–decode–execute cycle. *(M · 1.4)*

**Answer.** (1) **Fetch:** the control unit brings the next instruction from RAM into a register. (2) **Decode:** it works out what the instruction means. (3) **Execute:** the instruction is carried out, for example the ALU adds two numbers. The cycle then repeats for the next instruction, millions of times a second.

**Q24.** Why does a computer need so many kinds of memory? *(M · 1.6)*

**Answer.** Fast memory is costly, and cheap memory is slow. So a computer uses a little very fast memory near the CPU (registers, cache), a medium amount of RAM, and a lot of slow, cheap, permanent secondary memory. Together they are both fast and large, at a low cost.

**Q25.** Arrange in descending order: 2 GB, 2100 MB, 2 000 000 KB. Show your working. *(H · 1.7)*

**Answer.** In MB: 2 GB = 2048 MB; 2100 MB; 2 000 000 KB = 2 000 000 ÷ 1024 ≈ 1953 MB. So **2100 MB > 2 GB > 2 000 000 KB**.
