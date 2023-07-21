import csv

Start, End = input("Введите начальный год: "), input("Введите конечный год: ")
if Start.isdigit() and End.isdigit():
    Start = int(Start)
    End = int(End)
    if Start <= End:
        with open("Books.csv") as r_file:
            file_reader = csv.DictReader(r_file, delimiter=",")
            Count = 0
            for row in file_reader:
                if Start <= int(row["Год выпуска"]) <= End:
                    print(f'\t{row["Книга"]} - {row["Автор"]} - {row["Год"]}')
                    Count += 1
            if Count == 0:
                print(f"Книг, выпущеных с {Start} по {End} нет в файле")
    else:
        print("Ошибка: Конечный год меньше начального")
else:
    print("Некорректно введёные данные: Возможно это не целое число")
