n = int(input())

n_max = n + 1
is_prime = [True] * (n_max + 1)
is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

for i in range(2, int(n_max ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n_max + 1, i):  # Mark multiples of i as non-prime
            is_prime[j] = False

# Collect all prime numbers
primes = [i for i in range(n_max + 1) if is_prime[i]]
print(primes, sep=', ')
