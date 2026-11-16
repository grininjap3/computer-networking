# Task 10 Questions

1. Calculate the one-way and round-trip propagation delay for a 400 km fibre link.
2. Compare the theoretical propagation delay with the final traceroute RTT of 12.6 ms. Estimate the portion explained by propagation and discuss the remaining delay sources.
3. Explain the isolated 38.2 ms value at hop 3. Why does it not necessarily indicate forwarding delay or a fault?
4. Explain why hop 5 may show stars even though later hops respond.
5. Use the supplied hop table to identify which hop adds the most delay and explain the likely location of that delay.
6. Run traceroute/tracert and ping against a real server using the commands in the assignment. Save your own outputs and screenshots.
7. Capture ping and web-request traffic in Wireshark using the supplied display filters.
8. Annotate one captured packet with the Ethernet II, IPv4, TCP/ICMP and application-layer fields listed in the assignment.
9. Compare your measured minimum/average/maximum ping times with the propagation delay for the server distance.
10. Compare ping/traceroute, SNMP counters and NetFlow for identifying the hop-3 spike, hop-4 delay and hop-5 stars.
11. Explain why continuous monitoring should be used alongside occasional path tests.

**Evidence required:** your own terminal output and Wireshark capture. Do not use the PDF's example output as a substitute for your own measurements.