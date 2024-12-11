# 12 min
string = input()
new_string = ""
existing_words = set([])
unique_words = set([])
for i in string:
   if i.isalpha() or i == " ":
       new_string += i.lower()
for i in new_string.split():
   if i in existing_words:
       if i in unique_words:
           unique_words.remove(i)
   else:
       unique_words.add(i)
   existing_words.add(i)
print(len(unique_words))