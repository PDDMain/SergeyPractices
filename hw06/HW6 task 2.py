n, m = map(int, input().split())
previous_row = []
current_row = [-float("inf") for i in range(m+1)]
for i in range(n):
    previous_row = current_row
    current_row = list(map(int, input().split()))
    current_row.append(-float("inf"))
    for j in range(0, m):
        if j != 0 or i != 0:
            current_row[j] = current_row[j] + max(previous_row[j], current_row[j-1], previous_row[j-1])
            if current_row[j] < 0:
                current_row[j] = -float("inf")
if current_row[m-1] < 0:
    current_row[m-1] = -1
print(current_row[m-1])

