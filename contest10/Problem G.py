n, x = map(int, input().split())
a = list(map(int, input().split()))

power_of_result = 0
max_a = max(a)
sum_a = sum(a)
powers_of_x = [sum_a - i for i in a]
constant = 0
coefficients = [1 for i in powers_of_x]

while True:
    minimal_power = min(powers_of_x)
    power_of_result += minimal_power
    powers_of_x = [i - minimal_power for i in powers_of_x]
    constant = 0
    for i in range(len(powers_of_x)):
        if powers_of_x[i] == 0:
            constant += coefficients[i]
            powers_of_x[i] = float("inf")
    if constant % x != 0:
        break
    else:
        log = 0
        while constant % x == 0:
            constant = constant // x
            log += 1
        powers_of_x.append(log)
        coefficients.append(constant)

result = pow(x, power_of_result, 1000000007)
print(result)