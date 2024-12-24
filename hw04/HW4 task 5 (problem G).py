n = int(input())
a = list(map(int, input().split()))

index = {}
for i in range(n):
    index[a[i]] = i

is_prime = [True for i in range(n+1)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(n**0.5)+int(bool(n**0.5 % 1)+1)):
    if is_prime[i]:
        for j in range(i**2, n+1, i):
            is_prime[j] = False
minus_one_primes = [i - 1 for i in range(n+1) if is_prime[i]]

print(a)

def move(starting_place, destination, number_list):
    global index
    distance = starting_place - destination
    while distance > 0:
        next_jump = 0
        for i in minus_one_primes:
            if i <= distance:
                next_jump = i
            else:
                break
        print(starting_place - next_jump + 1, starting_place + 1)
        index[number_list[starting_place]] = starting_place - next_jump
        index[number_list[starting_place - next_jump]] = starting_place
        temp = number_list[starting_place]
        number_list[starting_place] = number_list[starting_place - next_jump]
        number_list[starting_place - next_jump] = temp
        starting_place -= next_jump
        distance -= next_jump
        print(number_list)
    return number_list

expected_value = 1
while expected_value < n:
    a = move(index[expected_value], expected_value - 1, a)
    expected_value += 1