# Task 12 – Day-4 Design Challenge – Re-evaluate and Adapt

Decision: modify wired/office design and redesign wireless for moving equipment. Per AGV: command 0.16 Mbps + status 0.08 Mbps + camera 4 Mbps=4.24 Mbps; 50 AGVs=212 Mbps (12 Mbps commands/status). Plant continuous CCTV+50 AGVs=1,477.92 Mbps (148% of 1 Gbps); motion-triggered CCTV+AGVs=748.32 Mbps (74.8%); devices=1,550.

Original Wi-Fi: 39 handovers, 5.85 s dark time, 585 missed commands/AGV; 50 AGVs=29,250 misses. 802.11r assumed 50 ms still means 195 misses/AGV. Redesign: private 5G URLLC/eMBB/mMTC slices, local core, 5 overlapping gNBs, make-before-break/dual connectivity/packet duplication; Wi-Fi 6 offices only; redundant 10G fibre; Cat6A fixed cells; LoRaWAN slow temperature; local motion CCTV; 1–2 Gbps head-office path with ≥335-frame SR; watchdog stops AGV after 3 missed commands. Pilot-test because 20 ms handover still exceeds 10 ms.

## Source note
Organized from the supplied Computer Networks Assignment 1 PDF.
