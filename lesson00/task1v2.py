n = int(input())
coordinates = list(map(int, input().split()))

min_coordinates = min(coordinates)
max_coordinates = max(coordinates)

# Calculate the minimum distance
# Travel from the smallest to the largest coordinate, then return
distance = (max_coordinates - min_coordinates) * 2

print(distance)
