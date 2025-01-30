n, k = map(int, input().split())
a = ["NONE" for i in range(n)]
for i in range(k):
    segment, color = input().split()
    a[int(segment) - 1] = color
print(*a)
