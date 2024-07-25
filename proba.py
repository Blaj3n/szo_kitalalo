# lista = [["alma", "körte", "szilva", "banán"], ["alma", "körte", "szilva", "banán"], ["alma", "körte", "szilva", "banán"]]
#
# for egyelem in lista:
#     print(egyelem)
#     for egy in egyelem:
#         print(egy)
#         for kisebb in egy:
#             print(kisebb)

megoldas = ["a", "l", "m", "a"]
tipp = ["a", "m", "l", "a"]
tipp_tomb = []

# végigfut: i = 0, és belefut, aztán i = 1, és megnt belefut... i = len(megoldas)-1, ez utolsó alkalommal fut bele, és aztán vége a ciklusnak.
for i in range(0, len(megoldas), 1):
    if megoldas[i] == tipp[i]:
        tipp_tomb.append(tipp[i])
    elif megoldas[i] != tipp[i]:
        tipp_tomb.append(".")

for egyelem in tipp_tomb:
    print(egyelem, end="")
print()
# az end="" -> összeköt két printet azzal a karakterrel, amit az end= után megadunk, ez esetben egy semmivel. end=" "
