# 8 min
A = set(input().split())
B = set(input().split())
def print_without_brackets(a_set):
   return_string = ""
   for i in a_set:
       return_string = return_string + str(i) + " "
   print(return_string.strip())
print_without_brackets(A.intersection(B))
print_without_brackets(A.symmetric_difference(B))
print_without_brackets(A.difference(B))
