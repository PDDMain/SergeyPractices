string = input()
k = int(input())
current_best = 0
i = 0
j = -1
used_letters = set()
last_instance = {}
while j < len(string) - 1:
    j += 1
    if len(used_letters) == k and string[j] not in used_letters:
        i = min(last_instance.values()) + 1
        used_letters.remove(string[i-1])
        last_instance.pop(string[i-1])
    if string[j] not in used_letters:
        used_letters.add(string[j])
    last_instance[string[j]] = j
    if j - i + 1 > current_best:
        current_best = j - i + 1
print(current_best)