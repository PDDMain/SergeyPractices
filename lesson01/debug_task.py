import os

def complicated_function(a, b, c, d, e, f, g, h):
    i = (a * b + c) % d
    j = ((e ** 2 - f * g) // h) + (a % b)
    k = (a + b + c + d + e + f + g + h) / 8

    with open("output.txt", "w") as file:
        if ((i > 10 and j < 20) or (a % 2 == 0 and b % 3 == 0)) and not (c - d > e):
            if ((a * c - e) % f == 0) or ((g // h) == 2):
                file.write("Complex Condition Met\n")
                #"Complex condition met"
            else:
                file.write("First Nested Else\n")
        elif ((a + b * c - d) / e == f) and (g % h != 0):
            if (k ** 2 - j) // i > 50:
                file.write("Second Complex Condition\n")
            else:
                file.write("Second Nested Else\n")
        else:
            file.write("General Case\n")

        # Another set of long conditions
        if (((a * e - b * f + c * g - d * h) % (a + 1)) % 2 == 0) or ((e + f + g) / h > 5):
            file.write("Another Complex Condition Met\n")
            #"Another Complex Condition Met"
        else:
            file.write("Final Else Case\n")

    #os.remove("output.txt") # comment this line to check your answer


if __name__ == "__main__":
    complicated_function(12, 15, 7, 5, 9, 4, 6, 3)
