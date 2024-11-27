n, m = map(int, input())  # Read n and m
grid = [list(input()) for _ in range(n)]  # Read the grid

# Add an extra column and an extra row filled with 'X' at the end of the grid
grid.append(['X'] * (m + 1))  # Add an extra row at the bottom
for row in grid:
    row.append('X')  # Add an extra column to the end of each row

# Directions: right, left, up, down
directions = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

x, y = n - 1, 0
steps = 0

while grid[x][y] != '.' and grid[x][y] != 'X':
    # Move according to the arrow at grid[x][y]
    dx, dy = directions[grid[x][y]]

    # Mark the current cell as visited with 'X'
    grid[x][y] = 'X'

    x, y = x + dx, y + dy
    steps += 1

if grid[x][y] == '.':
    print(steps)
else:
    print(-1)