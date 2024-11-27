n = int(input())
coordinates = list(map(int, input().split()))

coordinates.sort()

# Calculate the minimum distance
# Travel from the smallest to the largest coordinate, then return
distance = (coordinates[-1] - coordinates[0]) * 2

print(distance)
