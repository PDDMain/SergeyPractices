# 1125899906842624

n, l, r = map(int, input().split())
temp_n = n
remainders = []
result = 0

while temp_n >= 1:
    remainders.append(temp_n % 2)
    temp_n = temp_n // 2
remainders.reverse()

def twos_in_prime_factors_of(number):
    counter = 0
    while number % 2 == 0:
        number = number // 2
        counter += 1
    return counter

# O - числа
# A,B,C... - остатки разных уровней
# O
# O A O
# O B O A O B O
# O C O B O A O B O C O

# N
# [N/2, N mod 2, N/2]
# [N/2^2, N/2 mod 2, N/2^2, N mod 2, N/2^2, N/2 mod 2, N/2^2]

for i in range(l, r + 1):
    result += remainders[min(twos_in_prime_factors_of(i), len(remainders) - 1)]

print(result)