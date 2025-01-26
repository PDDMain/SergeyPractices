string_1 = input()
string_2 = input()


def equivalent(str1, str2):
    # argument strings must have equal length
    if str1 == str2:
        return True
    elif len(str1) % 2 == 1:
        return False
    else:
        midpoint = len(str1) // 2
        return equivalent(str1[:midpoint], str2[midpoint:]) or equivalent(str1[midpoint:], str2[:midpoint])


if len(string_1) == len(string_2):
    if equivalent(string_1, string_2):
        print("YES")
    else:
        print("NO")
else:
    print("NO")