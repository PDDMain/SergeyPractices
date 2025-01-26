n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
current_best = 0
missed_theorems = []
for i in range(n):
    if t[i] == 0:
        missed_theorems.append(a[i])
    else:
        missed_theorems.append(0)


# def my_sum(array, pref_sum, begin, end):
#     pass


for i in range(n - k + 1):
    if my_sum(missed_theorems[i:i+k]) > current_best:
        current_best = my_sum(missed_theorems[i:i+k])
print(my_sum(a) - my_sum(missed_theorems) + current_best)

# a = [1, 4, 2, 12, 3, 0, 23]
# pref_my_sum = [0, 1, ]
# pref_my_sum[i] = my_sum(a[0:i])