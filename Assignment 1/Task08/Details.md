# Task 8 – Hamming code and FEC versus ARQ

For 16 data bits, 2^r≥m+r+1 requires r=5; codeword=21 bits and check-bit overhead=31.25% of data. Code set {00000,01011,10101,11110} has dmin=3, detects 2 errors and corrects 1. Hamming(7,4) received 0110111 gives syndrome (s1,s2,s3)=(1,0,1), error position 5; corrected codeword 0110011 and data 1011. Two-bit errors can be miscorrected. Since 40 ms ARQ exceeds 10 ms control deadline, use FEC/hybrid FEC+CRC for time-critical traffic; ARQ is suitable for slower trending data.

## Source
Transcribed and organized from the supplied 24-page Assignment 1 PDF. See the PDF for the complete original task wording and any additional figures/tables.
