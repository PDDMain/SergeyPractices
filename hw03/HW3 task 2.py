# 9 min
a = list(map(int, input().split()))
frequency = {}
for i in a:
    if i in frequency.keys():
        frequency[i] += 1
    else:
        frequency[i] = 1
for i in sorted(frequency.keys()):
    print(i, frequency[i])