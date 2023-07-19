import csv

with open("Books.csv", mode="r", newline='') as r_file:
    Len = len(r_file.readlines()) - 1
Flag = True
a = input("Сколько записей ты хочешь добавить: ")
if a.isdigit():
    print()
    for i in range(int(a)):
        nameBook = input("Введите название {} книги: ".format(i + 1))
        AuthorBook = input("Его автора: ")
        ageBook = input("И его год выхода: ")
        if ageBook.isdigit():
            with open("Books.csv", mode="a", newline='') as w_file:
                file_writer = csv.writer(w_file, lineterminator="\r")
                file_writer.writerow([Len + i, nameBook, AuthorBook, ageBook])
            print("Добавлено\n")
        else:
            print("Ошибка ввода: Год не является числом")
            Flag = False
            break
else:
    print("Ошибка ввода: не число")
    Flag = False

if Flag:
    Autor = input("Введите автора: ")
    with open("Books.csv") as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            if row["Автор"] == Autor:
                print(f'\t{row["Книга"]} - {row["Автор"]} - {row["Год выпуска"]}')
                count += 1
        if count == 0:
            print("Книг с таким автором нет")
