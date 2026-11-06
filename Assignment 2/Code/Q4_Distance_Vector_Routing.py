"""Distance-vector routing simulation using synchronous updates.
Source: Computer Networks Assignment 2, Question 4.
"""

INF = 99
names = "ABCDE"

cost = {
    ("A", "B"): 2,
    ("A", "C"): 7,
    ("B", "C"): 3,
    ("B", "D"): 8,
    ("C", "D"): 1,
    ("D", "E"): 4,
}

link = {}
for (u, v), c in cost.items():
    link[u, v] = link[v, u] = c

table = {
    u: {
        v: (0 if u == v else link.get((u, v), INF))
        for v in names
    }
    for u in names
}

rounds = 0
changed = True

while changed:
    changed = False
    rounds += 1
    old = {u: dict(table[u]) for u in names}

    for u in names:
        for n in names:
            if (u, n) not in link:
                continue

            for dest in names:
                candidate = link[u, n] + old[n][dest]
                if candidate < table[u][dest]:
                    table[u][dest] = candidate
                    changed = True

print(f"converged after {rounds} rounds")
for u in names:
    print(u, " ".join(f"{table[u][v]:2d}" for v in names))


# Simulate failure of the C-D link and recalculate.
failed_cost = dict(cost)
failed_cost[("C", "D")] = INF

link = {}
for (u, v), c in failed_cost.items():
    link[u, v] = link[v, u] = c

table = {
    u: {
        v: (0 if u == v else link.get((u, v), INF))
        for v in names
    }
    for u in names
}

rounds = 0
changed = True

while changed:
    changed = False
    rounds += 1
    old = {u: dict(table[u]) for u in names}

    for u in names:
        for n in names:
            if (u, n) not in link:
                continue

            for dest in names:
                candidate = link[u, n] + old[n][dest]
                if candidate < table[u][dest]:
                    table[u][dest] = candidate
                    changed = True

print(f"after C-D link failure: converged after {rounds} rounds")
for u in names:
    print(u, " ".join(f"{table[u][v]:2d}" for v in names))
