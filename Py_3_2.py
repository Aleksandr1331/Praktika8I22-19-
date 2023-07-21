from functools import reduce

b = int(input('Введите число: '))
print((reduce(lambda x, _: x + [x[- 1] + x[- 2]], range(b - 2), [0, 1])))
