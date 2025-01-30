n, m = map(int, input().split())
flights = [{} for j in range(n)]
for i in range(m):
    u, v, t = map(int, input().split())
    flights[u-1][v-1] = t + 2
a, b = map(int, input().split())
if a == b:
    print(0)
    exit()
a = a - 1
b = b - 1
costs = ["IMPOSSIBLE" for i in range(n)]
depths = [-1 for i in range(n)]
depths[a] = 0
costs[a] = -2
open_nodes = {a : 0}
while len(open_nodes) > 0:
    current_min = float("inf")
    next_node = -1
    for i in open_nodes.keys():
        if open_nodes[i] < current_min:
            current_min = open_nodes[i]
            next_node = i
    if next_node == b:
        break
    open_nodes.pop(next_node)
    if depths[next_node] < 4:
        for i in flights[next_node].keys():
            new_value = flights[next_node][i] + costs[next_node]
            if i not in open_nodes.keys() or open_nodes[i] > new_value:
                costs[i] = open_nodes[i] = new_value
                depths[i] = depths[next_node] + 1
print(costs[b])