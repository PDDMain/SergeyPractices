# 34 min
n = int(input())
items = {}
def execute(command):
   if command[0] == "ADD":
       if command[1] in items.keys():
           items[command[1]] += int(command[2])
       else:
           items[command[1]] = int(command[2])
   if command[0] == "REMOVE":
       if command[1] in items.keys():
           items[command[1]] -= int(command[2])
       else:
           items[command[1]] = -int(command[2])
   if command[0] == "TOTAL":
       if command[1] in items.keys():
           print(items[command[1]])
       else:
           print("0")
the_input = input()
while the_input != "":
   execute(tuple(the_input.split()))
   the_input = input()