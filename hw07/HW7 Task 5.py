from email.utils import specialsre

l = int(input())
n = int(input())
runners = []
for i in range(n):
    runners.append(tuple(map(int, input().split())))
current_min = float("inf")
for i in runners:
    for j in runners:
        do_meet = True
        if i[1] > j[1]:
            faster = i
            slower = j
        elif i[1] < j[1]:
            faster = j
            slower = i
        else:
            do_meet = False
        if do_meet:
            d = (slower[0] - faster[0]) % l
            t = d / (faster[1] - slower[1])
            if t < current_min:
                current_min = t
if current_min == float("inf"):
    print("NO")
else:
    print(current_min)