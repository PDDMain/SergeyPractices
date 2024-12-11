# ~19:20 - ~19:45
n = int(input())
a = list(map(int, input().split()))
minus_one_primes = []
index = {}
for i in range(n):
    index[a[i]] = i

def move(starting_place, destination, number_list):
    distance = starting_place - destination
    while distance > 0:
        jumps = [j for j in minus_one_primes if j <= distance]
        number_list[]
    return number_list
expected_value = 1
while expected_value < n:
    for i in range(len(a)):
        if a[i] == expected_value:
            a = move(i, expected_value - 1, a)
            expected_value += 1