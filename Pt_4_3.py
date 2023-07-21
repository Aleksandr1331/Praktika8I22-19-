import math

a = math.ceil(float(input("Введите левую границу: ")))
b = math.floor(float(input("Введите правую границу: ")))


def Postie(o):
    if o == 2:
        return True
    for i in range(2, math.ceil(o ** 0.5) + 1):
        if int(o / i) == o / i:
            return False
    return True


print([i for i in range(a, b + 1) if Postie(i) if i != 1])
