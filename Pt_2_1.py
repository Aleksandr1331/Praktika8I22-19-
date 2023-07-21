import random

Colors = ["Красный", "Бирюзовый", "Серый", "Белый", "Розовый"]
Hint = ["Цвет главной площади в Москве",
        "Цвет, названный в честь драгоценных камней",
        "Цвет, характеризующийся с невзрачным настроением человека",
        "Цвет, являющийся смесью всех существующих цветов",
        "Цвет, характеризующийся с линейкой кукол Барби"]
ChoseProgram = random.randint(1, 5)
print(Colors)
YourChose = int(input("Выбирете цвет(Введите порядковый номер): "))

while YourChose != ChoseProgram:
    print("Неверно. \nПодсказка:", Hint[ChoseProgram - 1], "\n")
    YourChose = int(input("Попробуйте снова угадать: "))
print("Отлично!")
