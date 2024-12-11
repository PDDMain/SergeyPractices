n = int(input())
books = list(map(int, input().split()))
counter = 0
is_sorted = False
while not is_sorted:
   is_sorted = True
   for i in range(n-1):
       if books[i] > books[i+1]:
           is_sorted = False
           temp = books[i]
           books[i] = books[i+1]
           books[i+1] = temp
           counter += 1
           print(books)
print(counter)