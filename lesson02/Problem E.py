#runtime error on test 4

strings = list(input().split("."))
files = []
pieces = [strings[0]]
separable = "YES"
for i in strings[1:len(strings)]:
    if len(i) > 11:
        separable = "NO"
        break
    elif len(i) > 8:
        pieces.append(i[:-8])
        pieces.append(i[-8:])
    else:
        pieces.append(i[0])
        pieces.append(i[1:])
if separable == "YES":
    if len(strings) == 2:
        files = [pieces[0]+"."+pieces[1]]
    else:
        for i in range(0, len(strings)+1, 2):
            next_file = pieces[i]+"."+pieces[i+1]
            files.append(next_file)
        files[-1] += pieces[-1]
print(separable)
for i in files:
    print(i)