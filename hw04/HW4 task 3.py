# 23 minutes, but with breaks, so about 10 - 15 minutes
n = int(input())
target = int(input())
a = list(map(int, input().split()))
i = 0
j = n-1
result = -1
while j > i:
    if a[i] + a[j] > target:
        j -= 1
    elif a[i] + a[j] < target:
        i += 1
    else:
        found = True
        result = [a[i], a[j]]
        break
print(*result)