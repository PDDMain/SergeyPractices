n = int(input())
the_input = input()
previous_options = 1

if n > 1 and the_input[1] == "D" or n == 1:
    current_options = 1
else:
    current_options = 0

for i in range(2, n):
    current_options, previous_options = previous_options, current_options
    if the_input[i] == "D":
        current_options += previous_options
    else:
        current_options = 0

print(current_options)
