# 9 min
n, m = map(int, input().split())
connections = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    connections[u].append(v)
    connections[v].append(u)
s = int(input())

def bfs(start, connections_list):
    bfs_list = [start]
    visited = {start}
    for i in bfs_list:
        for j in connections_list[i]:
            if j not in visited:
                bfs_list.append(j)
                visited.add(j)
    return bfs_list

answer = bfs(s, connections)
print(*answer)
