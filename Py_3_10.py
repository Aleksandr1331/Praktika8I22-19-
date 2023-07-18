Stroka = str(input("Введите строку: ")).lower()
print({i.upper(): Stroka.count(i) for i in Stroka if i.isalpha()})
