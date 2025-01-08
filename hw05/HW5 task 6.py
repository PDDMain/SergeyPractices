n = int(input())
steps = []
for i in range(n):
    next_input = input()
    if next_input == "|":
        steps.append(-1)
    else:
        steps.append(int(next_input[2:]))
if n > 2:
    if steps[2] == -1:
        routes = ["1", "", ""]
        max_coins = [steps[0], 0, 0]
    else:
        routes = ["1", "", "1 3"]
        max_coins = [steps[0], 0, steps[2]+steps[0]]
    for i in range(3, n):
        if steps[i] == -1:
            max_coins.append(0)
            routes.append("")
        else:
            if max_coins[i-2] > max_coins[i-3]:
                max_coins.append(steps[i] + max_coins[i-2])
                routes.append(routes[i-2] + " " + str(i + 1))
            else:
                max_coins.append(steps[i] + max_coins[i-3])
                routes.append(routes[i-3] + " " + str(i + 1))
else:
    max_coins = [0]
    routes = ["You shall not pass"]
print(routes[-1])