# Task 8 Questions

1. For a 16-bit data word, calculate the number of Hamming check bits required using (2^r \ge m+r+1). Find the total codeword length and overhead.
2. Calculate the minimum Hamming distance of the code set `{00000, 01011, 10101, 11110}`.
3. State how many errors this code can detect and correct based on its minimum distance.
4. Decode received Hamming(7,4) word `0110111`: calculate the three syndrome bits, identify the error position, correct the codeword and extract the data bits.
5. Compare forward error correction (FEC) and automatic repeat request (ARQ) when retransmission takes 40 ms and the control deadline is 10 ms.
6. Explain why FEC is useful for time-critical/noisy radio links and live video, and describe the role of FEC and HARQ in 5G.
7. Complete the supplied Hamming decoder function.
8. Show how two flipped bits can cause the single-error-correcting Hamming(7,4) decoder to miscorrect.
9. Compare Hamming FEC (21,16) with detect-and-ARQ for BER (10^{-3}), a 16-bit reading and 40 ms retransmission. Compare failure probability, average bits, average extra delay and worst-case delay.
10. Recommend FEC or ARQ for slow trending readings versus vibration alarms or traffic near the 10 ms deadline.

**Complete the Task 8 Python example** and include the program output.