# 12 min, 3 submission attempts
n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(input() + ".")
position = [n - 1, 0]
visited = set()
counter = 0
while position != [0, m - 1]:
    visited.add(tuple(position))
    arrow = grid[position[0]][position[1]]
    if arrow == ">":
        position[1] += 1
    elif arrow == "<":
        position[1] -= 1
    elif arrow == "^":
        position[0] -= 1
    elif arrow == "v":
        position[0] += 1
    if position[0] > n - 1 or position[1] > m - 1 or tuple(position) in visited:
        print("-1")
        exit()
    else:
        counter += 1
print(counter)
