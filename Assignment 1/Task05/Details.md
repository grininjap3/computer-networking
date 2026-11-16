# Task 5 – Wi-Fi 6 versus private 5G for AGVs

AGV trip: 1,200 m at 2 m/s = 600 s. Wi-Fi 30 m cells mean 39 handovers at 150 ms = 5.85 s unreachable, 11.7 m travel disconnected and 585 missed 10 ms commands. Private 5G 300 m cells mean 3 handovers at 20 ms = 60 ms unreachable, 12 cm and 6 missed commands. Even 20 ms exceeds the 10 ms deadline; use make-before-break, dual connectivity or packet duplication. 5G: URLLC for AGVs, eMBB for CCTV, mMTC for sensors. LoRaWAN cannot carry 600 sensors at 50 B/s (240 kbps demand versus ~5 kbps/gateway); slow temperature readings can fit.

## Source
Transcribed and organized from the supplied 24-page Assignment 1 PDF. See the PDF for the complete original task wording and any additional figures/tables.
