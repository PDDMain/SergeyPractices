# 6 min
a = list(map(int, input().split()))
counter = 1
current_best = 0
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        counter += 1
    else:
        counter = 1
    if counter > current_best:
        current_best = counter
print(current_best)