# Task 12 Questions

Use the Day-4 challenge assumptions in the assignment, including 50 AGVs and the requirement that AGVs must never miss a command.

### A. Impact Analysis (2 marks)
1. Identify how the new requirement affects transmission media, wireless choice, error control and backbone Ethernet.
2. Recalculate traffic for one AGV (200-byte command every 10 ms, 100-byte status every 10 ms and one 4 Mbps camera) and for all 50 AGVs.
3. Compare continuous-CCTV plant traffic plus 50 AGVs with motion-triggered CCTV plus 50 AGVs. State whether 1 Gbps is sufficient.

### B. Test the Original Design (2 marks)
4. For 50 AGVs using the original Wi-Fi 6 design with 30 m AP spacing, calculate hand-overs, unreachable time and missed 10 ms commands per AGV trip.
5. Calculate the missed commands across all 50 AGVs and the plant-wide hand-over rate.
6. Recalculate the missed-command impact using the assignment's 802.11r assumption (50 ms hand-over).
7. Explain why the original design fails the requirement and discuss contention and welding-noise effects.

### C. Adaptation or Redesign (2 marks)
8. Propose the wireless redesign, including private 5G service slices, local core, cell overlap, make-before-break/dual connectivity and packet duplication.
9. State what should remain on Wi-Fi 6, fibre, Cat6A S/FTP and LoRaWAN.
10. Specify the head-office link, redundancy and AGV safety-watchdog action.

### D. Evidence-Based Defence (2 marks)
11. Compare Wi-Fi 6, Wi-Fi 6 with 802.11r, private 5G and private 5G with make-before-break using the assignment's hand-over, dark-time, missed-command and blind-distance figures.
12. Defend the final design by discussing cost, latency guarantees, pilot testing, security and why 5G does not replace the wired backbone.

**Complete the Task 12 Python example** and include the program output.