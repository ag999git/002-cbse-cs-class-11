# Chapter 1: the memory hierarchy (20 questions)

*Chapter 1 · Questions (online). Every answer was computed by a program (`tools/units_bank.py`), so it cannot contain slips. Try each question first; then read the answer and the working below it.*

**Rule:** read the pyramid: registers → cache → RAM → SSD → hard disk.

**Q1.** Arrange in order of speed, fastest first: RAM, registers, SSD.

**Answer.** **registers**, **RAM**, **SSD**.

*Why: the closer to the CPU, the faster (the memory pyramid, section 1.6).*

**Q2.** Arrange in order of speed, fastest first: SSD, registers, RAM, cache.

**Answer.** **registers**, **cache**, **RAM**, **SSD**.

*Why: the closer to the CPU, the faster (the memory pyramid, section 1.6).*

**Q3.** Arrange in order of distance from the CPU, nearest first: RAM, registers, SSD, hard disk.

**Answer.** **registers**, **RAM**, **SSD**, **hard disk**.

*Why: registers are inside the CPU; storage is farthest (the memory pyramid, section 1.6).*

**Q4.** Arrange in order of cost per byte, cheapest first: registers, hard disk, SSD.

**Answer.** **hard disk**, **SSD**, **registers**.

*Why: the slower the memory, the cheaper each byte (the memory pyramid, section 1.6).*

**Q5.** Arrange in order of distance from the CPU, nearest first: registers, RAM, SSD, cache.

**Answer.** **registers**, **cache**, **RAM**, **SSD**.

*Why: registers are inside the CPU; storage is farthest (the memory pyramid, section 1.6).*

**Q6.** Arrange in order of distance from the CPU, nearest first: registers, hard disk, RAM, SSD.

**Answer.** **registers**, **RAM**, **SSD**, **hard disk**.

*Why: registers are inside the CPU; storage is farthest (the memory pyramid, section 1.6).*

**Q7.** Arrange in order of size (capacity), smallest first: cache, SSD, registers, hard disk.

**Answer.** **registers**, **cache**, **SSD**, **hard disk**.

*Why: the faster the memory, the smaller it is in a computer (the memory pyramid, section 1.6).*

**Q8.** Arrange in order of distance from the CPU, nearest first: hard disk, RAM, SSD, cache.

**Answer.** **cache**, **RAM**, **SSD**, **hard disk**.

*Why: registers are inside the CPU; storage is farthest (the memory pyramid, section 1.6).*

**Q9.** Arrange in order of cost per byte, cheapest first: SSD, registers, RAM.

**Answer.** **SSD**, **RAM**, **registers**.

*Why: the slower the memory, the cheaper each byte (the memory pyramid, section 1.6).*

**Q10.** Arrange in order of distance from the CPU, nearest first: registers, cache, hard disk, SSD.

**Answer.** **registers**, **cache**, **SSD**, **hard disk**.

*Why: registers are inside the CPU; storage is farthest (the memory pyramid, section 1.6).*

**Q11.** Arrange in order of size (capacity), smallest first: registers, SSD, hard disk.

**Answer.** **registers**, **SSD**, **hard disk**.

*Why: the faster the memory, the smaller it is in a computer (the memory pyramid, section 1.6).*

**Q12.** Arrange in order of cost per byte, cheapest first: cache, registers, SSD, hard disk.

**Answer.** **hard disk**, **SSD**, **cache**, **registers**.

*Why: the slower the memory, the cheaper each byte (the memory pyramid, section 1.6).*

**Q13.** Arrange in order of distance from the CPU, nearest first: RAM, registers, cache, SSD.

**Answer.** **registers**, **cache**, **RAM**, **SSD**.

*Why: registers are inside the CPU; storage is farthest (the memory pyramid, section 1.6).*

**Q14.** Arrange in order of size (capacity), smallest first: registers, hard disk, cache, SSD.

**Answer.** **registers**, **cache**, **SSD**, **hard disk**.

*Why: the faster the memory, the smaller it is in a computer (the memory pyramid, section 1.6).*

**Q15.** Arrange in order of size (capacity), smallest first: cache, hard disk, SSD, registers.

**Answer.** **registers**, **cache**, **SSD**, **hard disk**.

*Why: the faster the memory, the smaller it is in a computer (the memory pyramid, section 1.6).*

**Q16.** Arrange in order of distance from the CPU, nearest first: SSD, registers, cache.

**Answer.** **registers**, **cache**, **SSD**.

*Why: registers are inside the CPU; storage is farthest (the memory pyramid, section 1.6).*

**Q17.** Arrange in order of speed, fastest first: cache, RAM, registers.

**Answer.** **registers**, **cache**, **RAM**.

*Why: the closer to the CPU, the faster (the memory pyramid, section 1.6).*

**Q18.** Arrange in order of size (capacity), smallest first: registers, RAM, hard disk, SSD.

**Answer.** **registers**, **RAM**, **SSD**, **hard disk**.

*Why: the faster the memory, the smaller it is in a computer (the memory pyramid, section 1.6).*

**Q19.** Arrange in order of speed, fastest first: SSD, hard disk, cache, RAM.

**Answer.** **cache**, **RAM**, **SSD**, **hard disk**.

*Why: the closer to the CPU, the faster (the memory pyramid, section 1.6).*

**Q20.** Arrange in order of cost per byte, cheapest first: hard disk, RAM, registers, SSD.

**Answer.** **hard disk**, **SSD**, **RAM**, **registers**.

*Why: the slower the memory, the cheaper each byte (the memory pyramid, section 1.6).*
