a = input()
b = input()
c = input()
row0 = [0]*(len(a)+1)
current_plane = [row0.copy() for i in range(len(b)+1)]
previous_plane = [row0.copy() for j in range(len(b)+1)]
#пришлось скопировать строку кода - когда я копировал весь список, списки внутри оказывались одними и теми же объектами
current_best = 0
current_best_index = 0

for i in range(1, len(c)+1):
    temp = current_plane
    current_plane = previous_plane
    previous_plane = temp
    for j in range(1, len(b)+1):
        for k in range(1, len(a)+1):
            if a[k-1] == b[j-1] == c[i-1]:
                value = previous_plane[j-1][k-1] + 1
                current_plane[j][k] = value
            else:
                current_plane[j][k] = 0
            if current_plane[j][k] > current_best:
                current_best = current_plane[j][k]
                current_best_index = k

print(current_best)
print(a[current_best_index-current_best:current_best_index])