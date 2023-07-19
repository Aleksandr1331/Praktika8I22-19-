print("".join([chr(97 + (ord(i) - 84) % 26) if i.islower() else chr(65 + (ord(i) - 52) % 26) if i.isupper() else i
               for i in str(input("Введите строчку: "))]))
