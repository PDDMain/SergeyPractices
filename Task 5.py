# 9 min
n = int(input())
line1 = input()
line2 = input()
counter = 1
i = 0
prev = 0
while i < n:
    if line1[i] == line2[i]:
        current = 1
    else:
        current = 2
    if prev == 1:
        counter = counter * 2
    elif prev == 2:
        if current == 2:
            counter = counter * 3
    else:
        counter = counter * 3 * current
    i += current
    prev = current
print(counter)
