# 16 min
n = int(input())
steps = []
for i in range(n):
    next_input = input()
    if next_input == "|":
        steps.append(-1)
    else:
        steps.append(int(next_input[2]))
#max_coins = [steps[0]]
#if len(steps) > 1:
#    if steps[1] == -1:
#        max_coins.append(0)
#    else:
#        max_coins.append(steps[1] + steps[0])
#    for i in range(2, n):
#        if steps[i] == -1:
#            max_coins.append(0)
#        else:
#            max_coins.append(steps[i] + max(max_coins[i-1], max_coins[i-2]))
#print(max_coins)
#print(max_coins[-1])

for i in range(len(steps)):
    if steps[i] == -1:
        steps[i] = 0
print(sum(steps))

# Разве не всегда оптимальной стретегией будет перепрыгивать через небезопасные ступеньки, но безопасные проходить все, подряд?
# Так можно собрать все монеты на лестнице при любом раскладе