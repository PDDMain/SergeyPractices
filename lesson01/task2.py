n = int(input())
coins = input()
ones = coins.count("1")
twos = coins.count("2")
threes = coins.count("3")
total = (ones + 2 * twos + 3 * threes)
Extra = 0
def can_fill(on, tw, th, num):
   fo = min(th, on)
   si = 0
   if on > th:
       on -= fo
       th = 0
       tw += on // 2
   elif on < th:
       th -= fo
       on = 0
       si += th // 2
   else:
       on = 0
       th = 0
   if si > num // 6:
       si -= num // 6
       num = num % 6
   else:
       num -= si*6
       si = 0
   if fo > num // 4:
       fo -= num // 4
       num = num % 4
   else:
       num -= fo*4
       fo = 0
   if tw > num // 2:
       return True
   else:
       return False
if total % 2 == 0:
   half = total // 2
   if half % 2 == 0:
       if can_fill(ones, twos, threes, half):
           print("YES")
       else:
           print("NO")
   else:
       if ones > 0:
           ones -= 1
           Extra = 1
       elif threes > 0:
           threes -= 1
           Extra = 3
       if Extra != 0 and can_fill(ones, twos, threes, half - Extra):
           print("YES")
       else:
           print("NO")
else:
   print("NO")