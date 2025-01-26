n, k = map(int, input().split())
number = input()
final_sum = 0


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def C(n, k):
    if k >= 0:
        return factorial(n) // (factorial(k) * factorial(n - k))
    else:
        return 0

if k == 0:
    print(int(number))
    exit()

# n - k + 1
for length in range(1, n - k + 1):
    for i in range(n - length + 1):
        current_number = int(number[i:i + length])
        m = n - length - 2 + int(i == 0 or i == (n - length))
        r = k - 2 + int(i == 0 or i == (n - length))
        final_sum = (final_sum + current_number * C(m, r)) % 1000000007

print(final_sum)