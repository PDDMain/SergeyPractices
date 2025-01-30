n, m = map(int, input().split())
visited = set()
adjacency_list = [[] for i in range (n + 1)]

for i in range(m):
    edge = tuple(map(int, input().split()))
    adjacency_list[edge[0]].append(edge[1])
    adjacency_list[edge[1]].append(edge[0])

output_list = []

def dfs(vertex_num):
    global visited
    global output_list
    visited.add(vertex_num)
    output_list.append(vertex_num)
    end = True
    for i in adjacency_list[vertex_num]:
        if i not in visited:
            end = False
            dfs(i)
    if end:
        return

s = int(input())
dfs(s)
print(*output_list)
