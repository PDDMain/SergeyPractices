# 31 min
n = int(input())
strings = []
for _ in range(2**n):
    strings.append(input())

def correct_string(prev, this_string):
    differences = sum([int(prev[i] != this_string[i] and this_string[i] != "?") for i in range(n)])
    if differences > 1:
        return False
    index = this_string.find("?")
    if prev[index] == "0":
        new_char = 1 - differences
    else:
        new_char = differences
    return this_string[:index] + str(new_char) + this_string[(index + 1):]

def generate_strings(starting_fill):
    used = set()
    answers = [strings[0].replace("?", starting_fill)] + strings[1:]
    for i in range(1, len(answers)):
        next_string = correct_string(answers[i - 1], answers[i])
        if not next_string:
            return False
        if next_string not in used:
            used.add(next_string)
            answers[i] = next_string
        else:
            return False
    if correct_string(answers[-1], strings[0]) == answers[0]:
        return answers
    else:
        return False

def print_on_lines(a_list):
    for i in a_list:
        print(i)

a = generate_strings("1")
b = generate_strings("0")
if a:
    print("YES")
    print_on_lines(a)
elif b:
    print("YES")
    print_on_lines(b)
else:
    print("NO")