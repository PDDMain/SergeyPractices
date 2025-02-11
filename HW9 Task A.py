# 6 min
encoding = {"A":"B","B":"C","C":"A"}
initial_string = input()
final_string = ""
for i in range(len(initial_string)):
    next_letter = initial_string[i]
    for j in range(i % 4):
        next_letter = encoding[next_letter]
    final_string += next_letter
print(final_string)
