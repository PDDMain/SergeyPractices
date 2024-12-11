# 8 days
# unfinished

numbers = list(map(int, input().split()))
n = len(numbers)
target_list = [i + 1 for i in range(n)]
index = [-1]
for i in range(n):
    for j in range(n):
        if numbers[j] == i+1:
            index.append(j)
            break
def flip(a_list, start_index, end_index):
    flip_part = a_list[start_index:end_index]
    for m in range(len(flip_part)//2):
        temp = flip_part[m]
        flip_part[m] = flip_part[-m-1]
        flip_part[-m-1] = temp
    a_list[:start_index].append(flip_part)
    return a_list