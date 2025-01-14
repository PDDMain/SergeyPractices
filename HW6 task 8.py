n, k = map(int, input().split())
h = list(map(int, input().split()))
correct_h = [0]*n
total_difference = 0
answer = "YES"

for i in range(n):
    if h[i] > correct_h[i]:
        correct_h[i] = h[i]
        j = i-1
        while j >= 0 and correct_h[j+1] - correct_h[j] > 1:
            correct_h[j] = correct_h[j+1] - 1
            j -= 1
        j = i+1
        while j < n and correct_h[j-1] - correct_h[j] > 1:
            correct_h[j] = correct_h[j-1] - 1
            j += 1
for i in range(n):
    total_difference += (correct_h[i] - h[i])
    if total_difference > k:
        answer = "NO"
        break
print(answer)