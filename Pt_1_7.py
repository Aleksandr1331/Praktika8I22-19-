Line = str(input("Введите строчку: "))
answer = ""

for i in range(len(Line)):
    if str.islower(Line[i]):
        answer += str.upper(Line[i])
    elif str.isupper(Line[i]):
        answer += str.lower(Line[i])
    else:
        answer += Line[i]
print(answer)
