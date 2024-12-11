# 15 min
text = input()
k = int(input())
new_text = ""
counter = {}
for i in text:
   if i.isalpha() or i == " ":
       new_text += i.lower()
for i in new_text.split():
   if i in counter.keys():
       counter[i] += 1
   else:
       counter[i] = 1
for i in range(k):
   current_max = 0
   current_best = ""
   for j in counter.keys():
       if counter[j] > current_max:
           current_max = counter[j]
           current_best = j
   print(current_best, current_max)
   counter[current_best] = -1