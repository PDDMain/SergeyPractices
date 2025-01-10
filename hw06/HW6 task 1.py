n, m = map(int, input().split())
previous_row = []
current_row = [0 for i in range(m)]
for i in range(n):
    previous_row = current_row
    current_row = list(map(int, input().split()))
    current_row.append(0)
    for j in range(0, m):
        current_row[j] = current_row[j] + max(previous_row[j], current_row[j-1])
print(current_row[m-1])
