# The memory hierarchy in depth

**Beyond syllabus** · not in the CBSE syllabus · Chapter 1, section 1.6

The printed chapter gives the rule: the farther a memory is from the CPU, the bigger, slower and cheaper it is. This page
puts numbers on that rule, shows **why** a small fast memory is enough most of the time, and works out how much time
the cache saves.

![The memory hierarchy](../../assets/images/ch01/c01-fig-pyramid-v2.png)

## Rough sizes and speeds

The numbers below are typical of a laptop today and only show the pattern: each level down is bigger and slower.

| Level | Typical size | Time to reach it (roughly) | Made of | In the kitchen |
|---|---|---|---|---|
| Registers | A few hundred bytes | Less than 1 nanosecond | Circuits inside the CPU | Plate in the hand |
| L1 cache | 32–64 KB per core | About 1 nanosecond | SRAM | Masala dabba |
| L2 cache | About 1 MB per core | A few nanoseconds | SRAM | Spice rack beside the stove |
| L3 cache | 8–32 MB, shared | 10–20 nanoseconds | SRAM | The shelf above the counter |
| RAM | 8–32 GB | 50–100 nanoseconds | DRAM | The kitchen shelf |
| SSD | 256 GB–2 TB | Tens of microseconds | Flash | The store room next door |
| HDD | 1–4 TB | Several milliseconds | Magnetic platters | The godown down the road |

(1 nanosecond = one billionth of a second; 1 microsecond = 1000 nanoseconds; 1 millisecond = 1000 microseconds.)

## If one nanosecond were one second

Nanoseconds are too small to feel. Stretch time so that **1 nanosecond becomes 1 second**:

| The CPU needs something from … | Real time (roughly) | Stretched time |
|---|---|---|
| A register | under 1 ns | under a second: it is already in hand |
| L1 cache | 1 ns | 1 second |
| L3 cache | 15 ns | 15 seconds |
| RAM | 80 ns | about a minute and a half |
| SSD | 50 µs = 50 000 ns | about 14 hours |
| Hard disk | 5 ms = 5 000 000 ns | about two months |

Now you can see why the CPU must never wait for the disk if it can help it, and why a program is first copied into RAM.

## Why does the hierarchy work? Locality

A small cache would be useless if the CPU wanted a different, random piece of data every time. It does not. Programs
behave in two predictable ways, together called **locality**:

- **Locality in time:** what was used just now is likely to be used again soon. A loop runs the same lines many times;
  a total is added to again and again.
- **Locality in place:** what is **near** the thing just used is likely to be needed next. Instructions run one after
  another; the items of a list sit side by side.

So when the CPU fetches one byte from RAM, the cache copies a whole small block around it (typically 64 bytes, called a
**cache line**). The next few needs are then very likely to be hits.

*In the kitchen:* when you cook dal, you take out the haldi, and you also take out the salt and the mirch kept beside it,
because you will need them in a minute.

## Cache hit and cache miss

- **Cache hit**: the CPU finds what it needs in the cache: fast.
- **Cache miss**: it is not there; it must be fetched from RAM (and copied into the cache for next time): slow.
- **Hit rate**: the share of requests that are hits. Good caches have hit rates above 90 %.

### Worked example: how much does the cache save?

Suppose a cache takes 1 ns, RAM takes 100 ns, and the hit rate is 95 %. On a hit the CPU waits 1 ns; on a miss it
waits about 1 + 100 = 101 ns (it looks in the cache first, then goes to RAM).

Average wait = 0.95 × 1 + 0.05 × 101 = 0.95 + 5.05 = **6 ns**.

Without the cache every request would take 100 ns. So the cache makes memory look about **16 times faster** (100 ÷ 6),
even though it is tiny.

| Hit rate | Average wait (ns) | Faster than RAM alone by |
|---|---|---|
| 80 % | 0.80 × 1 + 0.20 × 101 = 21 | about 5 times |
| 90 % | 0.90 × 1 + 0.10 × 101 = 11 | about 9 times |
| 95 % | 0.95 × 1 + 0.05 × 101 = 6 | about 16 times |
| 99 % | 0.99 × 1 + 0.01 × 101 = 2 | about 50 times |

## When RAM runs out: virtual memory

If you open more programs than fit in RAM, the operating system moves parts of programs that are not being used to a
reserved area of the disk (the **page file** or **swap**), and brings them back when needed. This makes RAM look bigger
than it is, and is called **virtual memory**. The price is speed: the disk is thousands of times slower, which is why
a computer with too little RAM becomes slow when many programs are open. (Operating systems are in Chapter 2.)

## Questions with answers

**Q1.** Why is a hierarchy of memories used instead of one large, fast memory?

**Answer.** Fast memory is very costly per byte. A little fast memory near the CPU and a lot of cheap memory farther away give nearly the speed of the fast memory at nearly the cost of the cheap one.

**Q2.** What is locality? Give its two kinds.

**Answer.** The habit of programs to reuse what they used recently (locality in time) and to use what is near what they used (locality in place). It is why a small cache is hit most of the time.

**Q3.** A cache takes 2 ns and RAM 100 ns. The hit rate is 90 %. Find the average wait.

**Answer.** 0.90 × 2 + 0.10 × (2 + 100) = 1.8 + 10.2 = **12 ns**.

**Q4.** What is a cache line?

**Answer.** The block of bytes (typically 64) copied from RAM into the cache together, so that nearby data is ready for the next requests.

**Q5.** Why does a computer with little RAM become slow when many programs are open?

**Answer.** The operating system has to keep moving parts of programs between RAM and the much slower disk (virtual memory), and the CPU waits for the disk.

**Q6.** Arrange by time to reach, shortest first: SSD, L2 cache, RAM, hard disk, register.

**Answer.** Register, L2 cache, RAM, SSD, hard disk.
