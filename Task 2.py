# 6 min
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
exchange = []
for i in range(n):
    diff = a[i] - b[i]
    if diff > 0:
        exchange.append(diff // 3)
    else:
        exchange.append(diff)
if sum(exchange) >= 0:
    print("Yes")
else:
    print("No")