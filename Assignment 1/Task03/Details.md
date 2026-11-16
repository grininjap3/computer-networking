# Task 3 – Frame encapsulation and OSI

Capture: Ethernet II EtherType 0x0800 (L2 frame); IPv4 10.10.1.25→10.10.9.4 TTL 61 (L3 packet); TCP 51522→502 (L4 segment); Modbus write-register, 12 bytes (application). TTL 64→61 means 3 routers. Frame size = 14+20+20+12+4 = 70 bytes; overhead 58 bytes (82.9%). For 1,400-byte data, frame is 1,458 bytes and overhead ~3.98%. Wrong MAC is L2; TTL zero is L3; closed TCP port is L4. Encapsulation example GET /results produces cumulative lengths 19,25,30,40; overhead 28 bytes. Raw Ethernet saves IP/TCP headers but loses routing, TCP reliability, TTL and common security/monitoring.

## Source
Transcribed and organized from the supplied 24-page Assignment 1 PDF. See the PDF for the complete original task wording and any additional figures/tables.
