n = int(input())
a = list(map(int, input().split()))

a.reverse()

moves = 0

for i in range(1, n):
    if a[i] > a[i - 1]:
        moves += a[i] - a[i - 1]
        a[i] = a[i - 1]

# Output the total moves
print(moves)
