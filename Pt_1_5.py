Points = int(input("Введите количество очков за матч: "))
if Points == 0:
    print("Команда проиграла")
elif Points == 1:
    print("Команда одержала ничью")
elif Points == 3:
    print("Команда победила")
else:
    print("Такого результата не может быть")
