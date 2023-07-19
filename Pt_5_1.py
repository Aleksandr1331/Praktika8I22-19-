import csv


with open("Books.csv", mode="w", newline='') as w_file:
    file_writer = csv.writer(w_file, lineterminator="\r")
    file_writer.writerow(["", "Книга", "Автор", "Год выпуска"])
    file_writer.writerow(["0", "Стальной алхимик", "Хирому Аракава", "2001"])
    file_writer.writerow(["1", "Алхимик", "Роман Пауло Коэльо", "1988"])
    file_writer.writerow(["2", "Наруто", "Масаси Кисимото", "1999"])
    file_writer.writerow(["3", "Проза бродячих псов", "Кафка Асагири", "2014"])
    file_writer.writerow(["4", "Берсерк", "Кэнтаро Миура", "1989"])
