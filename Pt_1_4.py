Chislo = float(input("Введите число от 10 до 20: "))
while Chislo < 10 or Chislo > 20:
    if Chislo < 10:
        print("Число меньше требуемого диапазона")
    else:
        print("Число больше требуемого диапазона")
    Chislo = float(input("Введите новое число: "))
print("Спасибо")
