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
                    print(f'\t{row["Книга"]} - {row["Автор"]} - {row["Год выпуска"]}')
                    Count += 1
            if Count == 0:
                print("Книг, выпущеных с {} по {} нет в данном файле".format(Start, End))
    else:
        print("Ошибка: Конечный год меньше начального")
else:
    print("Ошибка. Некорректные введёные данные: либо введено не число, либо введено не целое число")
