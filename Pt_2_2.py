TV = ["Наша раша", "Контрольая закупка", "Битва Экстрасенсов", "Интерны"]


def OutPutt(tele):
    print("\nТелепередачи:")
    for line in tele:
        print("\t" + line)
    print("")


OutPutt(TV)
NewPer, ordinal = str(input("Введите название новой передачи: ")), int(input("Его новая позиция: "))
TV.insert(ordinal-1, NewPer)
OutPutt(TV)
