import random

ChooseProg = None
ChooseChe = None
Score = Count = 0
# Десятки - Выигрышей, единицы - Проигрышей
while Count != 3:
    ChooseProg = random.randint(0, 1)
    # print(ChooseProg) #Для проверки
    ChooseChe = int(input("Орел или Решка?\n (0 или 1): "))

    if ChooseChe < 0 or ChooseChe > 1 or ChooseProg < 0 or ChooseProg > 1:
        print("Неподходящая цифра")
        break
    if ChooseChe == ChooseProg:
        Score += 10
        Count = 0
    else:
        Score += 1
        Count += 1
    print(Score // 10, ":", Score % 10, "(Выигрышей : Проигрышей)\n")
print("---------Проигрыш---------")
