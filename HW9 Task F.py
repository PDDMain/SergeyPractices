# passed all tests

n = int(input())
signs = input()

def list_to_string(a_list):
    output = ""
    for i in a_list:
        output += str(i)
    return output

digits_max = [8, 7, 6, 5, 4, 3, 2, 1, 0]
digits_min = [1, 2, 3, 4, 5, 6, 7, 8, 9]
min_result = [0]
max_result = [9]
for i in range(n):
    if signs[i] == "<":
        min_result.append(digits_min.pop(0))
        j = i - 1
        while signs[j] != ">" and j >= 0:
            j -= 1
        j += 1
        free_digit = max_result[-1]
        for k in range(j, len(max_result)):
            max_result[k] -= 1
        digits_max.remove(max_result[j])
        max_result.append(free_digit)
    else:
        max_result.append(digits_max.pop(0))
        j = i - 1
        while signs[j] != "<" and j >= 0:
            j -= 1
        j += 1
        free_digit = min_result[-1]
        for k in range(j, len(min_result)):
            min_result[k] += 1
        digits_min.remove(min_result[j])
        min_result.append(free_digit)
print(list_to_string(max_result))
print(list_to_string(min_result))
