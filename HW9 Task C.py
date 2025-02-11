# 26 min
n = int(input())

def get_valid_moves(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    return_list = []
    for y_offset in (-2, -1, 1, 2):
        for x_offset in (-2, -1, 1, 2):
            if abs(x_offset) != abs(y_offset):
                if 0 <= x+x_offset < n and 0 <= y+y_offset < n:
                    return_list.append((x+x_offset, y+y_offset))
    return return_list

start = tuple(map(int, input().split()))
destination = tuple(map(int, input().split()))
bfs_list = [(start, 0)]
visited = set()
target_reached = destination == start
for cell in bfs_list:
    if cell[0] == destination:
        print(cell[1])
        exit()
    if cell[0] not in visited:
        visited.add(cell[0])
        new_moves = get_valid_moves(cell[0])
        counter_list = [cell[1]+1]*len(new_moves)
        for i in range(len(new_moves)):
            bfs_list.append((new_moves[i], counter_list[i]))
print(-1)
