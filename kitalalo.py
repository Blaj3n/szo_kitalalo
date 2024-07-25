import random


szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis",
          "bagoly", "ecetes", "angyal", "boglya"]


rejtett_szo = szavak[random.randint(0, len(szavak)-1)]  # szavak[], -nak a..., (at = [])
rejtett_szo_betuk = []

for egyelem in rejtett_szo:
    rejtett_szo_betuk.append(egyelem)

# print(rejtett_szo)
# print(rejtett_szo_betuk)

szamlalo = 0
megoldas = []
jatek_vege = False  # Alapértelmezett érték False, mert a játék elején még nem ért véget
# A logikai változót azért állítjuk be alapértelmezetten False-ra, mert az jelzi, hogy egy adott esemény
# még nem következett be.

while rejtett_szo_betuk != megoldas:
    megoldas = []
    tipp = input(f"Kérem a tippet: ")
    tipp_lista = []
    if tipp == "stop":
        jatek_vege = True  # Ha a felhasználó "stop"-ot ír be, akkor a játék véget ér
        break
    elif len(tipp) != 6: # != nem egyenlő
        print("A tippnek pontosan hatbetűsnek kell lennie.")
        continue
    else:
        for egyelem in tipp:
            tipp_lista.append(egyelem)
        for i in range(0, len(rejtett_szo_betuk)):  # [x, y[ -> 0-tól el fog menni 5-ig, mert ugye előbb megvizsgáltad, hogy a len(tipp) == 6.
            if tipp_lista[i] == rejtett_szo_betuk[i]:
                megoldas.append(tipp_lista[i])
            elif tipp_lista[i] != rejtett_szo_betuk[i]:
                megoldas.append(".")
        print(f"Az eredmény: ", end="")
        for egyelem in megoldas:
            print(egyelem, end="")
        print("\n")
        szamlalo += 1

if not jatek_vege:  # Csak akkor írja ki a tippelések számát, ha a játék nem ért véget idő előtt
    print(f"{szamlalo} tippeléssel sikerült kitalálni. ")
if jatek_vege:
    print(f"A megfejtés: {rejtett_szo} ")
