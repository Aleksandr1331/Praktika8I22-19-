C = int(input("Введите число: "))
(lambda x: print(f"{C} - чет") if (x % 2 == 0) else print(f"{C} - не чет"))(C)
