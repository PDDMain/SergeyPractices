n = int(input())
p = list(map(int, input().split()))
black_total = 0
white_total = 0
current_spot = 1
for i in p:
    black_total += abs(i - current_spot)
    current_spot += 2
current_spot = len(p)
for i in p[::-1]:
    white_total += abs(current_spot - i)
    current_spot -= 2
print(min(black_total, white_total))