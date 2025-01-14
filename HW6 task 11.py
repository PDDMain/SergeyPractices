f, k = map(int, input().split())
operations = list(input().split())
operations.reverse()
for i in range(k):
    if operations[i] == "×3":
        f = f // 3
    elif operations[i] == "+10":
        f = f - 10
print(f)