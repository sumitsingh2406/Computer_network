# AIM - Implement and verify routing table updates using Distance Vector and Link State Routing algorithms.

n = int(input("Number of routers: "))
cost = []

for i in range(n):
    while True:
        row = list(map(int, input(f"Costs from R{i + 1} (-1 = no link): ").split()))
        if len(row) == n:
            cost.append([float("inf") if x == -1 else x for x in row])
            break
        print(f"Enter exactly {n} costs.")

dist = [row[:] for row in cost]
hop = [[j if i != j and cost[i][j] != float("inf") else None
        for j in range(n)] for i in range(n)]

while True:
    new = [row[:] for row in dist]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                if cost[i][k] + dist[k][j] < new[i][j]:
                    new[i][j] = cost[i][k] + dist[k][j]
                    hop[i][j] = k
    if new == dist:
        break
    dist = new

for i in range(n):
    print(f"\nR{i + 1}: Destination  Cost  Next hop")
    for j in range(n):
        value = "INF" if dist[i][j] == float("inf") else int(dist[i][j])
        nxt = "-" if hop[i][j] is None else f"R{hop[i][j] + 1}"
        print(f"    R{j + 1}          {value}     {nxt}")

