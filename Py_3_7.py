a = str(input("Введите строчку (Можно с пробелами): ")).replace(" ", "")
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э",
           "ю", "я", "e", "y", "u", "i", "o", "a"]

print([{a[i]: True if a[i] in vse_gls else False}
       for i in range(len(a)) if a[i].isalpha()])
