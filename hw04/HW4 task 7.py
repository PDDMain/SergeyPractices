# 36 min (старая, нерабочая версия), 11 min (перебор)
s = input()
k = int(input())
strings = set()
for i in range(len(s) - k + 1):
    used_letters = set()
    j = i - 1
    while len(used_letters) <= k and j < len(s) - 1:
        j += 1
        used_letters.add(s[j])
        if len(used_letters) == k:
            strings.add(s[i:j+1])
the_output = sorted(list(strings))
for i in the_output:
    print(i)