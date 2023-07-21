import itertools

Nabor = input("Введите через пробел: ").replace("  ", " ").split()
[print(i) for i in itertools.permutations(Nabor)]
