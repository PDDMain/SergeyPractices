n = int(input())
final_output = []

for i in range(n):
    inputs = tuple(map(int,input().split()))
    output = []
    for j in range(n):
        if inputs[j] == 1:
            output.append(j+1)
    final_output.append(output)

for i in final_output:
    print(*i)