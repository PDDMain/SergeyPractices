# 3 min
n = int(input())
paths = [1, 1]
for i in range(2, n):
    paths.append(paths[i-1] + paths[i-2])
print(paths[-1])