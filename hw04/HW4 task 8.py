# 15 min
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
i = 0
j = 0
current_best = abs(a[0] - b[0])
current_best_pair = [a[0], b[0]]
while i < len(a) and j < len(b):
    if abs(a[i] - b[j]) < current_best:
        current_best = abs(a[i] - b[j])
        current_best_pair = [a[i], b[j]]
    if a[i] > b[j]:
        j += 1
    elif a[i] == b[j]:
        current_best_pair = [a[i], b[j]]
        break
    else:
        i += 1
print(current_best_pair)
print(current_best)