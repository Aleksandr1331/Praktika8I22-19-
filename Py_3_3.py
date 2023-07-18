Count = int(input("Введите число: "))
(lambda x: print(f"Число {Count} - четное") if (x % 2 == 0) else print(f"Число {Count} не является четным"))(Count)
