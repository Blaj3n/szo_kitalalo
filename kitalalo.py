import random

# print("1. feladat")

szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]

# print(f"1. feladat:", *szavak)
# print("2. feladat")

rejtett_szo = szavak[random.randint(0, len(szavak)-1)] # szavak[], -nak a..., (at = [])
rejtett_szo_betuk = []
for egyelem in rejtett_szo:
    rejtett_szo_betuk.append(egyelem)
print(rejtett_szo)
print(rejtett_szo_betuk)

# print("3. feladat")

szamlalo = 0
megoldas = []
while rejtett_szo_betuk != megoldas:
    megoldas = []
    tipp = input(f"Kérem a tippet: ")
    tipp_lista = []
    for egyelem in tipp:
        tipp_lista.append(egyelem)
    for i in range(0, len(rejtett_szo_betuk)):
        if tipp_lista[i] == rejtett_szo_betuk[i]:
            megoldas.append(tipp_lista[i])
        elif tipp_lista[i] != rejtett_szo_betuk[i]:
            megoldas.append(".")
    print(f"Az eredmény:", *megoldas)
    szamlalo += 1
print(f"\n{szamlalo} tippeléssel sikerült kitalálni")


    # HÁZI: STOP ÉS SZÁMLÁLÓ