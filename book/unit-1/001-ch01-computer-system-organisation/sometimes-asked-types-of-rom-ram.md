# Types of RAM and ROM

**Sometimes asked** · asked in a few school papers · Chapter 1, section 1.6

## Types of RAM

| Point | SRAM (static RAM) | DRAM (dynamic RAM) |
|---|---|---|
| How it keeps a bit | A tiny circuit of a few switches (transistors) | A tiny charge in a capacitor, which leaks |
| Needs refreshing? | No | Yes, thousands of times a second |
| Speed | Faster | Slower |
| Cost and size | Costlier; fewer bits per chip | Cheaper; more bits per chip |
| Used for | Cache memory | Main memory (the RAM modules) |

*Hook:* **S**RAM **S**tays (static); **D**RAM **D**rains (its charge leaks, so it is refreshed).

## Types of ROM

| Type | Full form | Can it be changed? |
|---|---|---|
| **ROM** (mask ROM) | Read Only Memory | No: written when the chip is made |
| **PROM** | Programmable ROM | Written **once** by the user with a special device; then fixed |
| **EPROM** | Erasable Programmable ROM | Erased by **ultraviolet light** through a quartz window, then written again |
| **EEPROM** | Electrically Erasable Programmable ROM | Erased and written **electrically**, without removing the chip |

**Flash memory** (pen drives, SSDs, and the start-up chip of today's computers) is a kind of EEPROM that is erased in
blocks, which makes it fast.

![A ROM / EPROM chip](../../assets/images/ch01/c01-part-rom.png)

## Questions

**Q.** Expand: PROM, EEPROM.
**Answer.** PROM: Programmable Read Only Memory. EEPROM: Electrically Erasable Programmable Read Only Memory.

**Q.** Write two differences between SRAM and DRAM.
**Answer.** SRAM does not need refreshing, DRAM does; SRAM is faster and costlier and is used for cache, DRAM is cheaper
and is used for main memory.

**Q.** How is an EPROM erased?
**Answer.** By shining ultraviolet light through the quartz window on the chip.
