import math

Number = float(input("Введите ваше число: "))
print("Первое натуральное число, квадрат которого больше {} ---> {}".format(Number, math.ceil(math.sqrt(Number))))
