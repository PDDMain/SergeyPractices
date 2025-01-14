l = int(input())
outputs = list(map(int, input().split()))

bound = max(outputs)
fibonacci = [0, 1]
j = 1
while fibonacci[j] < bound:
    fibonacci.append(fibonacci[j] + fibonacci[j-1])
    j += 1

j = 1
i = 0
while i < l:
    if fibonacci[j] == outputs[i]:
        print("PRINT")
        i += 1
    else:
        print("FIBB")
        j += 1
