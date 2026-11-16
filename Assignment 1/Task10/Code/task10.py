# Run these commands in your own terminal and save the real outputs/screenshots.
# Windows: tracert -d 8.8.8.8
#           ping -n 20 8.8.8.8
# Linux/macOS: traceroute -n 8.8.8.8
#               ping -c 20 8.8.8.8
# Wireshark filters: icmp
#                    tcp.port == 80 || tcp.port == 443
print('400 km fibre: 2 ms one-way propagation and about 4 ms RTT propagation.')
print('Sample hop 4 adds the largest delay: 7.8 ms.')
print('Traceroute stars may mean a router does not answer probes, even if it forwards traffic.')
