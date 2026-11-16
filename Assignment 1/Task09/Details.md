# Task 9 – Sliding-window size and link utilisation

Frame=1,500 B=12,000 bits; 400 km at 2×10⁸ m/s; link=1 Gbps. Transmission=12 µs; one-way propagation=2 ms; a=166.67. Stop-and-wait utilisation=0.299%, throughput≈2.99 Mbps. Full-utilisation window W=1+2a=334.33→335 frames (~502 KB). Go-Back-N needs 9 sequence bits; Selective Repeat needs 10. SR retransmits only lost frame but buffers out-of-order frames (~502.5 KB); GBN may resend up to 335 frames. HDLC bit-stuffs after five 1s; PPP byte-stuffs 0x7E as 0x7D 0x5E. Prefer Selective Repeat/TCP SACK with window scaling.

## Source
Transcribed and organized from the supplied 24-page Assignment 1 PDF. See the PDF for the complete original task wording and any additional figures/tables.
