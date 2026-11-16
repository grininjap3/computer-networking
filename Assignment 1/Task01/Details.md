# Task 1 – Traffic sizing

Per line: robots 40×500 commands/s×200 B×8 = 32 Mbps; 600 vibration sensors×50 B/s×8 = 0.24 Mbps; 24 CCTV×4 Mbps = 96 Mbps; office 150×2 Mbps×10% = 30 Mbps. Total 158.24 Mbps/line; 8-line plant = 1,265.92 Mbps (1.27 Gbps). CCTV is largest (60.7%); robots have strictest 10 ms deadline. A 1 Gbps uplink supports one line but not the whole plant. A 1 MB queue adds 8 ms; 2 MB adds 16 ms. Use VLANs and strict-priority 802.1p/DSCP EF for robots. Motion-triggered CCTV at 5% reduces plant load to 536.32 Mbps; five plants aggregate to 2.68 Gbps. Local continuous CCTV storage is about 1.04 TB/line/day.

## Source
Transcribed and organized from the supplied 24-page Assignment 1 PDF. See the PDF for the complete original task wording and any additional figures/tables.
