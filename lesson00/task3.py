n = int(input())
a = list(map(int, input().split()))

moves = 0

# Traverse the array from right to left
for i in range(n - 2, -1, -1):  # Start from the second last element
    if a[i] > a[i + 1]:
        moves += a[i] - a[i + 1]
        a[i] = a[i + 1]

# Output the total moves
print(moves)
