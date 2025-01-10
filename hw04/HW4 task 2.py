# 7 min
n = int(input())
m = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
j = 0
result = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        result.append(a[i])
        i += 1
        j += 1
if len(result):
    print(*result)
else:
    print(-1)