n = int(input())
line1 = input()
line2 = input()

arr = []
i = 0
while i < n:
    if line1[i] == line2[i]:
        arr.append('I')
        i+=1
    else:
        arr.append('=')
        i+=2

available_colors = 3
drawings = 1
for item in arr:
    if item == 'I':
        drawings*=available_colors
        available_colors = 2
    else:
        if available_colors == 1:
            drawings*=3
        else:
            drawings*=available_colors*(available_colors-1)
            available_colors = 1
print(drawings)