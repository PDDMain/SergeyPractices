# 12 min
n = int(input())
costs = list(map(int, input().split()))
keys_inverted = tuple(map(int, input().split()))
keys = [[] for i in range(n)]
for i in range(n):
    if keys_inverted[i] != -1:
        keys[keys_inverted[i] - 1].append(i)

for i in range(n):
    for j in keys[i]:
        if j > i:
            costs[j] = 0

print(sum(costs))
