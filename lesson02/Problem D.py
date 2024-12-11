#time limit exceeded on test 10

n = int(input())
a = list(map(int, input().split()))
avg = sum(a)/n
counter = 0
indices = []
output = ""
if avg % 1 == 0:
    for i in range(n):
        if a[i] == avg:
            indices.append(i+1)
            counter += 1
print(counter)
for i in indices:
    output = output + " " + str(i)
print(output.strip())