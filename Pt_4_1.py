a = str(input("Введите число: "))
print(''.join(map(str, sorted([int(a[i]) for i in range(len(a))], reverse=True))))
