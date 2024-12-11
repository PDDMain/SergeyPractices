# 17 min
string = input()
k = int(input())
current_best = 0
for i in range(len(string)):
    # TODO: use set instead of string to save unique items
    used_letters = ""
    count = 0
    j = i
    while len(used_letters) <= k and j < len(string):
        if string[j] not in used_letters:
            used_letters += string[j]
        j += 1
        count += 1
    if count > current_best:
        current_best = count
print(current_best - 1)

# wrong
# ecebaaaaa
# 2