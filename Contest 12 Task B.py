# Wrong answer on test 6

Vasya_string = input().strip()
address = ""
pointer = 0
temp_letters = []
for letter in Vasya_string:
    pointer += 1
    temp_letters.append(letter)
    if temp_letters == ["h", "t", "t", "p"] or temp_letters == ["f", "t", "p"]:
        break
address = "".join(temp_letters) + "://"
temp_letters = []
for letter in Vasya_string[pointer:]:
    pointer += 1
    temp_letters.append(letter)
    if len(temp_letters) > 1:
        if temp_letters[-1] == "u" and temp_letters[-2] == "r":
            temp_letters.insert(-2, ".")
            break
if len(Vasya_string[pointer:]):
    address = address + "".join(temp_letters) + "/" + Vasya_string[pointer:]
else:
    address = address + "".join(temp_letters)
print(address)
