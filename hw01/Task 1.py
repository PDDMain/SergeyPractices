def is_magic(number):
    return True

counter = 3
for i in range(1, 10, 2):
   a = 15 - i
   for j in range(1, 10, 2):
       b = a - j
       if b in range(1, 10, 2):
           counter += 1
print(counter)
