# wrong answer on test 2

t = int(input())
constants = []
locations_lists = []
for i in range(t):
    constants.append(list(map(int, input().split())))
    locations_lists.append(list(map(int, input().split())))
for i in range(t):
    n = constants[i][0]
    k = constants[i][1]
    locations = locations_lists[i]
    distances = [locations[0]-1, n - locations[-1]]
    for j in range(len(locations)-1):
        if locations[j+1] <= locations[j] + 1:
            distances.append(0)
        else:
            distances.append((locations[j+1] - locations[j]) // 2 + (locations[j+1] - locations[j]) % 2)
    print(max(distances)+1)