# wrong answer on test 7

n = int(input())
i = 0
string1 = input()
string2 = input()
prev = None
counter = 1
while i < n:
    if string1[i] == string2[i]:
        if prev == "d":
            pass
        elif prev == "s":
            counter = counter*2
        else:
            counter = 3
        i += 1
        prev = "s"
    else:
        if prev == "d":
            counter = counter*3
        elif prev == "s":
            counter = counter*2
        else:
            counter = 6
        i += 2
        prev = "d"
print(counter)
