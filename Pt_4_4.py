import itertools

Numbers = input("Введите числа через пробел: ").replace("  ", " ").split()
Numbers = list(map(int, Numbers))
EnterNumber = int(input("Введите число: "))

([[print(j) for j in itertools.combinations(Numbers, i)
   if sum(j) == EnterNumber] for i in range(1, len(Numbers) + 1)])
