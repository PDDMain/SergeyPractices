n = int(input())

# Function to check if a number is prime
def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generate primes up to n+1
n_max = n + 1
primes = [i for i in range(2, n_max + 1) if is_prime_number(i)]
print(primes, sep=', ')