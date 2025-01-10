n, m = map(int, input().split())
previous_row = []
current_row = [[-float("inf"), []] for i in range(m+1)]
def find_step(*args):
    for k in range(3):
        if args[k][0] == args[k-1][0] and args[k][0] != -float("inf"):
            if len(args[k][1]) < len(args[k-1][1]):
                args[k-1][0] = -float("inf")
            else:
                args[k][0] = -float("inf")

for i in range(n):
    previous_row = current_row
    current_row = list(map(int, input().split()))
    current_row.append([-float("inf"),[]])
    for j in range(0, m):
        if i != 0 and j != 0:
            last_step = find_step(previous_row[j][0], current_row[j-1][0], previous_row[j-1][0])
            current_row[j] = [current_row[j] + last_step, []]
            if current_row[j][0] < 0:
                current_row[j][0] = -float("inf")
        else:
            current_row[j] = [current_row[j], []]
if current_row[m-1][0] < 0:
    current_row[m-1][1] = -1
print(current_row[m-1][1])
