# 7 minutes
n = int(input())
a = list(map(int, input().split()))
counter = 0
for i in range(n - 2, -1, -1):
    if a[i] > a[i + 1]:
        counter += a[i] - a[i+1]
        a[i] = a[i+1]
print(counter)