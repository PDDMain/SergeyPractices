# Input
n, m = map(int, input().split())  # Read n and m
grid = [input() for _ in range(n)]  # Read the grid

# Directions: right, left, up, down
directions = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

# Start at the bottom-left corner (n-1, 0)
x, y = n - 1, 0
steps = 0

visited = set()  # To detect cycles

while (x, y) != (0, m - 1):
    if (x, y) in visited or x < 0 or y < 0 or x > n - 1 or y > m - 1:
        print(-1)
        exit()

    visited.add((x, y))

    dx, dy = directions[grid[x][y]]
    x, y = x + dx, y + dy
    steps += 1

print(steps)
