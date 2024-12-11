# 29 min
N = int(input())
N_is_odd = bool(N % 2)
pairs = N // 2
def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m-1)
def C(n, k):
    return factorial(n) // (factorial(k)*factorial(n-k))
count = 0
if not N_is_odd:
    for i in range(pairs+1):
        length = i + pairs
        num_ones = i * 2
        count += C(length, num_ones)
else:
    for i in range(pairs+1):
        length = i + pairs + 1
        num_ones = i * 2 + 1
        count += C(length, num_ones)
print(count)