n, k = map(int, input().split())
c = list(map(int, input().split()))
capitals = list(map(int, input().split()))
capitals = [i - 1 for i in capitals]
paths = set([])
for i in range(n):
    if i+1 == n:
        paths.add(tuple([i, 0]))
    else:
        paths.add(tuple([i+1, i]))
for i in capitals:
    for j in range(n):
        if j != i:
            paths.add(tuple([max(j, i), min(j, i)]))
counter = 0
for i in paths:
    counter += (c[i[0]] * c[i[1]])
print(counter)