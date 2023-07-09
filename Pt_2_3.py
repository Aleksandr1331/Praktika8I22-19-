Count = int(input("Введите число: "))
Sum = 0
temp = Count

while temp > 0:
    Sum += (temp % 10) ** 3
    temp //= 10

if Count == Sum:
    print("Число " + str(Count) + " - число Армстронга")
else:
    print("Число " + str(Count) + " - не является числом Армстронга")
