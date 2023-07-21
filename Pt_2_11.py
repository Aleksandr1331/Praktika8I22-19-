import math

a = math.ceil(float(input("Введите левую границу: ")))
b = math.floor(float(input("Введите правую границу: ")))
print(f"Сумма целых чисел от {a} до {b} = {((a + b) * (b - a + 1)) / 2}")
