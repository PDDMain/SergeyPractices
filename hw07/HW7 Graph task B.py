n = int(input())
final_output = set()

for i in range(n):
    inputs = list(map(int, input().split()))
    inputs.pop(0)
    for j in inputs:
        output = (min(i+1, j), max(i+1, j))
        final_output.add(output)

for i in final_output:
    print(*i)