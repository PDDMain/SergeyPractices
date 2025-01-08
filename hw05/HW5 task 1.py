# 4 min
prev = -1
num = 1
n = int(input())
for i in range(n+1):
    temp = num + prev
    prev = num
    num = temp
print(num)