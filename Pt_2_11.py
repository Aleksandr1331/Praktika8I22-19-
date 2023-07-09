import math

a, b = math.ceil(float(input("Введите левую границу: "))), math.floor(float(input("Введите правую границу: ")))
print("Сумма всех целых чисел между {} и {} = {}".format(a, b, ((a + b) * (b - a + 1)) / 2))
