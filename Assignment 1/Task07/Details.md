# Task 7 – CRC, parity and checksum

Data 1101011011 with generator 1011 (x³+x+1): append 3 zeros and divide modulo 2; CRC remainder = 100; transmitted frame = 1101011011100. Last-bit-corrupted frame 1101011011101 has remainder 001 and is rejected. All bursts of length ≤3 are detected; error patterns divisible by generator are undetectable (example 0000000001011). Two-dimensional parity misses four-corner rectangle flips. Internet checksum: 4500+0073+0000+4000=8573; one's complement=7A8C; receiver sum=FFFF. CRC-3 is stronger than single parity overall.

## Source
Transcribed and organized from the supplied 24-page Assignment 1 PDF. See the PDF for the complete original task wording and any additional figures/tables.
