current_names = list(input().split())
input_names = []
n = int(input())
for i in range(n):
    input_names.append(list(input().split()))
print(current_names[0] + " " + current_names[1])
def replace(location, replaced, replacement):
    l = location
    if l[0] == replaced:
        l[0] = replacement
    else:
        l[1] = replacement
    return l
for i in range(len(input_names)):
    current_names = (replace(current_names, input_names[i][0], input_names[i][1]))
    print(current_names[0] + " " + current_names[1])