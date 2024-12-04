n, m = map(int, input().split())
b = list(map(int, input().split()))
for i in range(n):
   best = 0
   total = 0
   for j in range(m):
       if i+j < len(b):
           total += b[i+j]
           if total > best:
               best = total
       else:
           break
   b[i] = best
print(max(b))
print(b)