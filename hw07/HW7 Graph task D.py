visited = set()
n, m = map(int, input().split())
adjacency_list = [[] for i in range (n + 1)]

for i in range(m):
    edge = tuple(map(int, input().split()))
    adjacency_list[edge[0]].append(edge[1])
    adjacency_list[edge[1]].append(edge[0])

def dfs(vertex_num):
    global visited
    visited.add(vertex_num)
    end = True
    for i in adjacency_list[vertex_num]:
        if i not in visited:
            end = False
            dfs(i)
    if end:
        return

dfs(1)

for i in range(1, n+1):
    if i not in visited:
        print("NO")
        exit()
print("YES")