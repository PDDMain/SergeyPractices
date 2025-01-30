n, m = map(int, input().split())
final_output = []
for i in range(n):
    final_output.append([0]*n)

for i in range(m):
    edge = tuple(map(int, input().split()))
    final_output[edge[0] - 1][edge[1] - 1] = 1
    final_output[edge[1] - 1][edge[0] - 1] = 1

for i in final_output:
    print(*i)