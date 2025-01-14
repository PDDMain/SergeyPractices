n, x = map(int, input().split())
a = list(map(int, input().split()))

power_of_result = 0
max_a = max(a)
sum_a = sum(a)
powers_of_x = [sum_a - i for i in a]
constant = 0
coefficients = [1 for i in powers_of_x]

while True:
    minimal_power = min(powers_of_x)
    power_of_result += minimal_power
    powers_of_x = [i - minimal_power for i in powers_of_x]
    constant = 0
    for i in range(len(powers_of_x)):
        if powers_of_x[i] == 0:
            constant += coefficients[i]
            powers_of_x[i] = float("inf")
    if constant % x != 0:
        break
    else:
        log = 0
        while constant % x == 0:
            constant = constant // x
            log += 1
        powers_of_x.append(log)
        coefficients.append(constant)

num2 = constant
for i in range(len(powers_of_x)):
    if i != float("inf"):
        num2 += x**i

def primes(boundary):
    is_prime = [True]*(boundary+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(boundary**0.5+1)):
        if is_prime[i]:
            for j in range(i, boundary+1, i):
                is_prime[j] = False
    return [i for i in range(boundary+1) if is_prime[i]]
primes = primes((max(num2, x)) // 2)

def factorize(number):
    factors = []
    for i in primes:
        if number % i == 0:
            number = number // i
            factors.append(i)
    return factors

num2 = factorize(num2)
num1 = []
for i in range(sum_a - power_of_result):
    num1.append(x*(sum_a-power_of_result))
common_factors = []

k = l = 0
while k < len(num1) and l < len(num2):
    if num1[k] > num2[l]:
        l += 1
    elif num1[k] < num2[l]:
        k += 1
    else:
        common_factors.append(num1[k])
        k += 1
        l += 1


result = pow(x, power_of_result, 1000000007)
for i in common_factors:
    result = result * i
result = result % 1000000007

print(result)