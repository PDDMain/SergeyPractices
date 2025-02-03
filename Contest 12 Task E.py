# ~20 min
# correct

n = int(input())
a = list(map(int, input().split()))
swap_string = input()
swappable = []
for i in swap_string:
    swappable.append(i == "1")
swappable.append(False)
final_list = []
temp_list = []
for i in range(n):
    if swappable[i]:
        temp_list.append(a[i])
    elif not swappable[i] and swappable[i-1] and i != 0:
        temp_list.append(a[i])
        final_list += sorted(temp_list)
        temp_list = []
    else:
        final_list.append(a[i])
for i in range(1, n):
    if final_list[i] < final_list[i-1]:
        print("NO")
        exit()
print("YES")