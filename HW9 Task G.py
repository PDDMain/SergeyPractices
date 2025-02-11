# Time limit exceeded on test 8
# Про более оптимальньное решение читал, но пока ещё к сожалению не понял
n = int(input())
items = list(map(int, input().split()))
lengths = []
for i in range(n):
    item = items[i]
    j = i
    current_best = 0
    while j > 0:
        j -= 1
        if items[j] <= items[i] and lengths[j] > current_best:
            current_best = lengths[j]
    lengths.append(current_best + 1)
print(max(lengths))
