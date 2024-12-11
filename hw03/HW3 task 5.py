# 2 min
n = int(input())
def fibonacci(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m-1)+fibonacci(m-2)
print(fibonacci(n))