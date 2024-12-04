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
   if tw >= num // 2:
       return True
   else:
       return False


def solution(ones, twos, threes):
    total = (ones + 2 * twos + 3 * threes)
    Extra = 0
    if total % 2 == 0:
       half = total // 2
       if half % 2 == 0:
           if can_fill(ones, twos, threes, half):
               return True
           else:
               return False
       else:
           if ones > 0:
               ones -= 1
               Extra = 1
           elif threes > 0:
               threes -= 1
               Extra = 3
           if Extra != 0 and can_fill(ones, twos, threes, half - Extra):
               return True
           else:
               return False
    else:
       return False

# n = int(input())
# coins = input()
# ones = coins.count("1")
# twos = coins.count("2")
# threes = coins.count("3")
# if solution(ones, twos, threes):
#     print("YES")
# else:
#     print("NO")

def test_solution():
    # Case 1: Basic case, even split
    assert solution(2, 2, 2) == True  # [1, 3] vs [1, 3], [2, 2]

    # Case 2: All ones
    assert solution(4, 0, 0) == True  # [1, 1] vs [1, 1]
    assert solution(5, 0, 0) == False  # Cannot split 5 into two equal groups

    # Case 3: All twos
    assert solution(0, 4, 0) == True  # [2, 2] vs [2, 2]
    assert solution(0, 3, 0) == False  # Cannot split into two equal groups

    # Case 4: All threes
    assert solution(0, 0, 4) == True  # [3, 3] vs [3, 3]
    assert solution(0, 0, 5) == False  # Cannot split into two equal groups

    # Case 5: Mixed, edge values
    assert solution(1, 1, 1) == False  # Total = 6, no equal split
    assert solution(2, 1, 1) == True  # [3, 1] vs [2, 2]

    # Case 6: No coins at all
    assert solution(0, 0, 0) == True  # Both groups are empty

    # Case 7: Only one type of coin
    assert solution(3, 0, 0) == False  # Cannot split 3 into two equal groups
    assert solution(0, 3, 0) == False  # Cannot split 6 into two equal groups

    # Case 8: Large numbers of coins
    assert solution(100, 100, 100) == True  # Should balance easily
    assert solution(100, 100, 99) == False  # Odd total, cannot split

    # Case 9: Single coin
    assert solution(1, 0, 0) == False  # One coin cannot be split
    assert solution(0, 1, 0) == False  # Same for a two-value coin
    assert solution(0, 0, 1) == False  # Same for a three-value coin

    # Case 10: Odd and even mixes
    assert solution(3, 2, 1) == True  # [1, 3, 2] vs [3, 3]
    assert solution(5, 3, 2) == False  # Total sum = 20, cannot balance

    # Case 11: All zeros
    assert solution(0, 0, 0) == True  # Empty groups are equal

    # Case 12: Random mixes
    assert solution(10, 5, 3) == True  # Balanced split possible
    assert solution(7, 2, 4) == False  # Total sum = 21, odd
    assert solution(8, 2, 4) == True

    print("All tests passed!")

# Run the test function
test_solution()
