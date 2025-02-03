# 31 min
# wrong answer on test 44

matrix = []
for i in range(10):
    matrix.append(input())

def can_win(start_x, start_y, step_x, step_y):
    x = start_x
    y = start_y
    buffer = ["O", "O", "O", "O", "O"]
    step_count = 0
    while x < 10 and y < 10:
        buffer[step_count % 5] = matrix[y][x]
        if buffer.count("X") == 4 and buffer.count("O") == 0:
            return True
        step_count += 1
        x += step_x
        y += step_y
    return False

for i in range(10):
    # going left through row i
    if can_win(0, i, 1, 0):
        print("YES")
        exit()
    # going down column i
    if can_win(i, 0, 0, 1):
        print("YES")
        exit()
    # going right-down over diagonal starting with x = i
    if can_win(i, 0, 1, 1):
        print("YES")
        exit()
    # going left-down over diagonal starting with x = i
    if can_win(i, 0, -1, 1):
        print("YES")
        exit()
    # going right-down over diagonal starting with y = i
    if can_win(0, i, 1, 1):
        print("YES")
        exit()
    # going right-up over diagonal starting with y = i
    if can_win(0, i, 1, -1):
        print("YES")
        exit()

print("NO")