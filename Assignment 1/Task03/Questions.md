# Task 3 Questions

Use the capture details supplied in the assignment:

1. Map the Ethernet II, IPv4, TCP and Modbus write-register lines to their OSI layers and protocol data units (PDUs).
2. From the IPv4 TTL value of 61, assuming an initial TTL of 64, calculate how many routers the packet crossed.
3. Calculate the total Ethernet frame size for the 12-byte Modbus message, including Ethernet, IPv4, TCP and FCS headers.
4. Calculate the header overhead in bytes and as a percentage of the frame.
5. Repeat the calculation for a 1,400-byte camera payload and compare the overhead percentages.
6. Explain why small robot commands are more affected by per-packet overhead than large video packets.
7. Map the three faults (wrong MAC address, TTL reaching zero and closed destination port) to the appropriate layer and describe the result.
8. Map the OSI layers to the TCP/IP model.
9. Complete the supplied `send(message)` function so that each layer adds its header and the final frame is returned.
10. Evaluate the raw-Ethernet alternative (EtherType 0x8892): calculate the header savings and explain what networking capabilities are lost.

**Complete the Task 3 Python example** and include the program output.