import itertools

Nabor = input("Введите через пробел элементы списка: ").replace("  ", " ").split()
[print(i) for i in itertools.permutations(Nabor)]
