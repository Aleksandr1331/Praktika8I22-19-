import math

n = int(input("По какое число искать: "))
print([x for x in range(1, n) if [True for i in range(2, math.ceil(x ** 0.5) + 1) if int(x / i) == x / i and i != x]])
