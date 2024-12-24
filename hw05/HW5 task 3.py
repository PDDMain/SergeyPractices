# 12 min
n = int(input())
the_input = input()
steps = []
for i in the_input:
    if i == "|":
        steps.append(False)
    else:
        steps.append(True)
if len(steps) > 1:
    options = [1, int(steps[1])]
    for i in range(2, n):
        if not steps[i]:
            options.append(0)
        else:
            options.append(options[i-1] + options[i-2])
else:
    options = [1]
print(options[n-1])