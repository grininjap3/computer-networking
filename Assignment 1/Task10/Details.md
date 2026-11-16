# Task 10 – Traceroute and delay analysis

Given sample: 400 km fibre propagation is 2 ms one-way / 4 ms RTT. Last-hop RTT=12.6 ms; straight-line propagation explains 31.7%. Hop 3 has a one-off 38.2 ms response but later hops are 11.8/12.6 ms, suggesting slow/rate-limited ICMP control-plane response rather than forwarding delay. Hop 5 stars mean no probe reply, while hop 6 responds. Hop 4 (103.21.8.17) rises from 4.0 to 11.8 ms, adding 7.8 ms (largest). IMPORTANT: PDF requires your own tracert/traceroute, ping and Wireshark evidence; sample data is not a substitute. Save real outputs/screenshots here. Filters: icmp and tcp.port == 80 || tcp.port == 443. Annotate Ethernet MAC/EtherType, IPv4 addresses/TTL/protocol, TCP or ICMP fields, and application data.

## Source
Transcribed and organized from the supplied 24-page Assignment 1 PDF. See the PDF for the complete original task wording and any additional figures/tables.
