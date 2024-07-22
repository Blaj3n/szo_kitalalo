lista = [["alma", "körte", "szilva", "banán"], ["alma", "körte", "szilva", "banán"], ["alma", "körte", "szilva", "banán"]]

for egyelem in lista:
    print(egyelem)
    for egy in egyelem:
        print(egy)
        for kisebb in egy:
            print(kisebb)