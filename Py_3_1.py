from functools import reduce

Numbers = [1, 4, 86, 102.83, 7]
print(round(reduce(lambda x, y: x+y, Numbers)/len(Numbers), 2))
