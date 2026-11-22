# Link State Routing using Dijkstra's algorithm

n = int(input("Number of routers: "))
print("Enter the cost matrix (0 = no direct link):")
graph = []
for i in range(n):
    row = list(map(int, input(f"Router R{i + 1}: ").split()))
    if len(row) != n or any(cost < 0 for cost in row):
        raise ValueError("Enter n non-negative costs in every row.")
    graph.append(row)

for source in range(n):
    dist = [float("inf")] * n
    hop = [None] * n
    visited = [False] * n
    dist[source] = 0

    for _ in range(n):
        current = min(
            (i for i in range(n) if not visited[i]),
            key=lambda i: dist[i],
            default=None,
        )
        if current is None or dist[current] == float("inf"):
            break
        visited[current] = True

        for neighbor, cost in enumerate(graph[current]):
            if cost > 0 and dist[current] + cost < dist[neighbor]:
                dist[neighbor] = dist[current] + cost
                hop[neighbor] = neighbor if current == source else hop[current]

    print(f"\nRouting table for R{source + 1}")
    print("Destination\tCost\tNext hop")
    for destination, cost in enumerate(dist):
        value = "INF" if cost == float("inf") else cost
        next_router = "-" if hop[destination] is None else f"R{hop[destination] + 1}"
        print(f"R{destination + 1}\t\t{value}\t{next_router}")
