# wrong answer on test 8

n, c = map(int, input().split())
x = list(map(int, input().split()))
current_best = 0
for i in range(n-1):
    profit = x[i] - x[i+1]
    if profit > current_best:
        current_best = profit
print(max(0, current_best-c))