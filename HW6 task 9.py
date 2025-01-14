n = int(input())
k = list(map(int, input().split()))

i = 0
answer = "YES"
visited = set()
while i != n-1:
    visited.add(i)
    i += k[i]
    if i < 0:
        answer = "NO"
        break
    elif i >= n:
        answer = "NO"
        break
    elif i in visited:
        answer = "NO"
        break

print(answer)