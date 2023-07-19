import itertools

Numbers = list(map(int, input("Введите числа через пробел: ").replace("  ", " ").split()))
EnterNumber = int(input("Введите число: "))

([[print(j) for j in itertools.combinations(Numbers, i) if sum(j) == EnterNumber] for i in range(1, len(Numbers) + 1)])
