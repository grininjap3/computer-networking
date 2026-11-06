"""Variable-length subnetting of 192.168.10.0/24.
Source: Computer Networks Assignment 2, Question 2.
"""

import math


def to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d


def to_ip(n):
    return ".".join(str((n >> s) & 255) for s in (24, 16, 8, 0))


def vlsm(base, needs):
    addr = to_int(base)

    for name, hosts in sorted(needs, key=lambda x: -x[1]):
        block = 1 << math.ceil(math.log2(hosts + 2))
        prefix = 32 - int(math.log2(block))
        network = addr
        broadcast = network + block - 1
        first = network + 1
        last = broadcast - 1

        print(
            f"{name} {to_ip(network)}/{prefix} hosts "
            f"{to_ip(first)} - {to_ip(last)} "
            f"bcast {to_ip(broadcast)}"
        )
        addr = broadcast + 1

    return to_ip(addr)


needs = [
    ("Labs", 100),
    ("Staff", 50),
    ("Library", 25),
    ("WAN link", 2),
]

print("next free address:", vlsm("192.168.10.0", needs))
