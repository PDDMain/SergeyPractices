# 7 min
n = int(input())
a = list(input().split())
b = set(a)
b.remove("?")
print(b)
goal = set(map(str, range(1, n+1, 1)))
b = goal.difference(b)
print(b)
for i in range(n):
   if a[i] == "?":
       a[i] = b.pop()
print(a)