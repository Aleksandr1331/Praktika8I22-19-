Number = str(input("Введите натуральное число: "))
Pos = 0

for i in range(Pos, len(Number)):
    if Number[Pos] < Number[i]:
        Pos = i
    else:
        continue

print("Позиция от начала числа:", Pos + 1)
print("Позиция с конца числа:", len(Number) - Pos)
