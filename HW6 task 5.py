n = int(input())
indices = []
strings = []
for i in range(2**n):
    temp_input = str(input())
    indices.append(temp_input.find("?"))
    strings.append(temp_input)

def attempt_generation(initial_char):
    string_list = set()
    answers = strings.copy()
    def correct_string(answers, index):
        nonlocal string_list
        differences = sum([answers[index - 1][i] != strings[index][i] for i in range(n)])
        previous_character = answers[index - 1][indices[index]]
        if differences == 1:
            answers[index] = strings[index].replace("?", str(int(not (int(previous_character)))))
        elif differences == 2:
            answers[index] = strings[index].replace("?", previous_character)
        else:
            return -1
        if answers[index] in string_list:
            return -1
        else:
            string_list.add(answers[index])
        return answers[index]

    answers[0] = answers[0].replace("?", str(initial_char))
    for i in range(1, len(answers)):
        answers[i] = correct_string(answers, i)
        if answers[i] == -1:
            return -1
    if sum([answers[0][i] != answers[len(answers)-1][i] for i in range(n)]) == 1:
        return answers
    else:
        return -1

def print_on_lines(a_list):
    for j in a_list:
        print(j)
x = attempt_generation(0)
y = attempt_generation(1)
if x != -1:
    print("YES")
    print_on_lines(x)
elif y != -1:
    print("YES")
    print_on_lines(y)
else:
    print("NO")