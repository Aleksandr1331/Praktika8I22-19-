a = float(input("Введите первое число: "))
b = float(input("Введите Второе число: "))
c = float(input("Введите третье число: "))

_min = min(a, b, c)
_max = max(a, b, c)
_mid = a + b + c - _min - _max
print(_max, " ", _mid, " ", _min)
