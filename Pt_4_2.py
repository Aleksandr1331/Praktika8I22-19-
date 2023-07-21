Stroka = str(input("Введите строку: "))
Polidroms = set()


def Poisk(a, low, high):
    result = []
    while (low >= 0) and (high < len(a)) and (a[low] == a[high]):
        result.append(a[low:high + 1])
        low -= 1
        high += 1
    return result


for i in range(len(Stroka)):
    Polidroms.update((Poisk(Stroka, i, i + 1)))
    Polidroms.update((Poisk(Stroka, i, i)))

print(Polidroms)
