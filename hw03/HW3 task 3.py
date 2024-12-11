# 16 min
n = int(input())
words = []
letter_sets = []
counter = {}
for i in range(n):
    words.append(input())
for i in words:
    letter_sets.append(str(sorted([j for j in i])))
for i in range(n):
    if letter_sets[i] in counter.keys():
        counter[letter_sets[i]] += " " + words[i]
    else:
        counter[letter_sets[i]] = words[i]
for i in counter.keys():
    print(counter[i])

# Cool!