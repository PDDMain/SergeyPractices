n = int(input())
points = {}
sum_of_y = 0
answer = "YES"
for i in range(n):
    the_input = tuple(map(int, input().split()))
    if the_input in points.keys():
        points[the_input] += 1
    else:
        points[the_input] = 1
    sum_of_y += the_input[1]

if n % 2 == 1:
    answer = "NO"

if answer == "YES":
    c = sum_of_y / n

    for i in points.keys():
        if points[i]:
            x = i[0]
            y = 2*c - i[1]
            if y % 1 != 0:
                answer = "NO"
                break
            else:
                y = int(y)
            if (x,y) in points.keys():
                points[(x,y)] -= 1
                points[i] -= 1
            else:
                answer = "NO"
else:
    answer = "NO"
print(answer)