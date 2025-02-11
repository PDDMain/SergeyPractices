# 50 min
# ~15 minute fix the next day
a = list(map(int, input().split()))
corners = [(0,0), (a[0], a[1]), (a[2], a[3]), (a[4], a[5])]
sides = []
for i in range(4):
    for j in range(i+1, 4):
        sides.append((corners[i][0]-corners[j][0], corners[i][1] - corners[j][1]))
equal_counter = 0
parallel_counter = 0
perpendicular_counter = 0
for i in range(6):
    for j in range(i+1, 6):
        len1 = (sides[i][0]**2 + sides[i][1]**2)**0.5
        len2 = (sides[j][0]**2 + sides[j][1]**2)**0.5
        if len1 == len2:
            equal_counter += 1
        if sides[i][0]*sides[j][0] + sides[i][1]*sides[j][1] == 0:
            perpendicular_counter += 1

if perpendicular_counter == 4 or perpendicular_counter == 5:
    if equal_counter == 7:
        print("Square")
    else:
        print("Rectangle")
else:
    print("None")
