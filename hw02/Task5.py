# 29 min
n = int(input())
k = int(input())
a = list(map(int, input().split()))
decrease_spot = 0
decrease_count = 0
for i in range(n):
    # if a[i] > a[(i + 1) % len(a)]:
    if a[i-1] > a[i]:
        decrease_spot = i+1
        decrease_count += 1
if decrease_count == 0:
   print(0)
elif decrease_count > 1:
   print(-1)
elif min(decrease_spot, (len(a)-decrease_spot)) > k:
   print(-1)
else:
   if decrease_spot < len(a)-decrease_spot:
       print(decrease_spot, "L")
   else:
       print(len(a)-decrease_spot, "R")