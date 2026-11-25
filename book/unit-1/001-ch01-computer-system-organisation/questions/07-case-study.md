# Chapter 1: Computer System Organisation: Case studies (6 cases, 24 questions)

*Chapter 1 · Questions (online). Read each case, then answer its questions. Every question is followed by its answer and the reason.*

## Case 1: The school computer lab

Ms Iyer is setting up a lab of 20 computers. Each has a keyboard, a mouse, a monitor, 8 GB of RAM and a 512 GB SSD. One printer is shared by the lab; students also bring pen drives.

**1.1** Name the input devices in the lab. *[1 mark]*

**Answer.** Keyboard and mouse.

**1.2** Is the SSD primary or secondary memory? Why? *[1 mark]*

**Answer.** Secondary memory: it keeps files permanently and the CPU does not read it directly.

**1.3** A student switches a computer off without saving her program. What happens, and why? *[1 mark]*

**Answer.** The program is lost, because it was only in RAM, and RAM is volatile.

**1.4** The lab needs prints of 40 report cards with carbon copies. Which kind of printer should it use? *[1 mark]*

**Answer.** An impact printer, such as a dot-matrix printer: only an impact printer can strike through to make carbon copies.

## Case 2: The bank

At a bank branch, cheques are read by one machine, customers sign in with their fingerprint, and the passbook is printed by a noisy printer.

**2.1** Which device reads the cheque numbers? *[1 mark]*

**Answer.** MICR (Magnetic Ink Character Reader).

**2.2** What kind of device reads the fingerprint? *[1 mark]*

**Answer.** A biometric reader (an input device).

**2.3** The passbook printer is noisy. What kind of printer is it? *[1 mark]*

**Answer.** An impact printer (dot-matrix).

**2.4** Why does the bank use MICR rather than OCR for cheques? *[1 mark]*

**Answer.** The magnetic-ink characters can be read even when the cheque is stamped or written over, and they are hard to forge.

## Case 3: Buying a laptop

Rohan compares two laptops. Laptop A: 8 GB RAM, 1 TB HDD. Laptop B: 16 GB RAM, 512 GB SSD.

**3.1** Which laptop can store more files? *[1 mark]*

**Answer.** Laptop A: 1 TB = 1024 GB, twice 512 GB.

**3.2** Which laptop will start up faster, and why? *[1 mark]*

**Answer.** Laptop B: an SSD has no moving parts and is much faster than an HDD, so the operating system loads into RAM sooner.

**3.3** How many GB of RAM does Laptop B have more than Laptop A, in MB? *[1 mark]*

**Answer.** 8 GB more = 8 × 1024 = 8192 MB.

**3.4** Give one reason to prefer an SSD in a laptop that is carried every day. *[1 mark]*

**Answer.** With no moving parts, it is less likely to be damaged when dropped or shaken.

## Case 4: Inside the CPU

A program adds the marks of two tests, 45 and 38, and checks whether the total is more than 80.

**4.1** Which part of the CPU adds the marks? *[1 mark]*

**Answer.** The ALU.

**4.2** Which part decides that the addition must happen before the comparison? *[1 mark]*

**Answer.** The control unit.

**4.3** Where are 45 and 38 kept while they are being added? *[1 mark]*

**Answer.** In registers inside the CPU.

**4.4** Name the three steps the CPU repeats for each instruction of this program. *[1 mark]*

**Answer.** Fetch, decode, execute.

## Case 5: The phone that ran out of space

Meera's phone has 64 GB of storage. Photos average 4 MB and videos 200 MB. She has 2000 photos and 100 videos; the apps and system use 30 GB.

**5.1** How much space do the photos use, in GB? *[1 mark]*

**Answer.** 2000 × 4 = 8000 MB; 8000 ÷ 1024 ≈ **7.8 GB**.

**5.2** How much do the videos use, in GB? *[1 mark]*

**Answer.** 100 × 200 = 20 000 MB; ÷ 1024 ≈ **19.5 GB**.

**5.3** How much space is left, in MB and in GB? *[1 mark]*

**Answer.** Work in MB: 64 GB = 65 536 MB; used 30 × 1024 + 8000 + 20 000 = 58 720 MB; left 65 536 − 58 720 = **6816 MB ≈ 6.7 GB**.

**5.4** How many more 4 MB photos can she take? *[1 mark]*

**Answer.** 6816 ÷ 4 = **1704 photos**. *Tip:* work in MB from the start; rounding to GB first gives a wrong count.

## Case 6: The power cut

During a power cut, the computer in a shop switches off. When the power returns, the computer starts, shows the shop's billing program, but the bill being typed is gone.

**6.1** Which memory held the bill being typed? *[1 mark]*

**Answer.** RAM.

**6.2** Which memory held the instructions that started the computer again? *[1 mark]*

**Answer.** ROM (the BIOS or UEFI firmware).

**6.3** Where was the billing program kept while the computer was off? *[1 mark]*

**Answer.** In secondary memory (the hard disk or SSD).

**6.4** Suggest one way to stop such losses. *[1 mark]*

**Answer.** Any one: save often (or turn on auto-save); use a UPS (battery backup) so the computer keeps running during a power cut.
