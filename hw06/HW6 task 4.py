a = input()
b = input()
current_row = [0 for i in range(len(a)+1)]
current_best = 0
current_best_index = 0
for i in range(len(b)):
    previous_row = current_row.copy()
    for j in range(1, len(current_row)):
        if a[j-1] == b[i]:
            current_row[j] = 1 + previous_row[j-1]
            if current_row[j] > current_best:
                current_best = current_row[j]
                current_best_index = j
        else:
            current_row[j] = 0
print(current_best)
print(a[(current_best_index - current_best) : current_best_index])
