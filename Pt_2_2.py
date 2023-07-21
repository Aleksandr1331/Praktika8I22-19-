TV = ["Наша раша", "Контрольая закупка", "Битва Экстрасенсов", "Интерны"]


def OutPutt(tele):
    print("\nТелепередачи:")
    for line in tele:
        print("\t" + line)
    print("")


OutPutt(TV)
NewPer = str(input("Введите название новой передачи: "))
ordinal = int(input("Его новая позиция: "))
TV.insert(ordinal - 1, NewPer)
OutPutt(TV)
