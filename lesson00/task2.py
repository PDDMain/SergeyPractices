n = int(input())
a = list(map(int, input().split()))  # Current resources
b = list(map(int, input().split()))  # Required resources

surplus = 0
deficit = 0

for i in range(n):
    if a[i] > b[i]:
        surplus += (a[i] - b[i]) // 3  # Only surplus units that can be converted
    else:
        deficit += b[i] - a[i]  # Total deficit units

# Check if the surplus can cover the deficit
if surplus >= deficit:
    print("Yes")
else:
    print("No")
