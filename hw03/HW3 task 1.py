# 31 min
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []
i = 0
j = 0
def add_to_result(value, results_list):
    if value not in results_list:
        return results_list.append(value)
    else:
        return results_list
while len(a) and len(b):
    if a[i] > b[j]:
        result = add_to_result(b[j], result)
        j += 1
    else:
        result = add_to_result(a[i], result)
        i += 1
result += a+b
print(result)

# wrong
# 1 3 5 7
# 2 3 5 8