# wrong answer on test 8 - did not yet debug

board = tuple(map(int, input().split()))
painting1 = tuple(map(int, input().split()))
painting2 = tuple(map(int, input().split()))
output = "NO"
for i in range(1):
    for j in range(1):
        for k in range(1):
            if painting1[i] + painting2[j] <= board[k] and max(painting1[int(not i)], painting2[int(not j)] <= board[int(not k)]):
                output = "YES"
print(output)
