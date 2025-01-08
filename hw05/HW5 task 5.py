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
        steps[2] = 0
    max_coins = [steps[0], 0, steps[2]+steps[0]]
    for i in range(3, n):
        if steps[i] == -1:
            max_coins.append(0)
        else:
            max_coins.append(steps[i] + max(max_coins[i-2], max_coins[i-3]))
else:
    max_coins = [0]
print(max_coins)
print(max_coins[-1])