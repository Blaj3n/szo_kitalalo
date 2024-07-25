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

while rejtett_szo_betuk != megoldas:
    megoldas = []
    tipp = input(f"Kérem a tippet: ")
    tipp_lista = []
    if tipp == "stop":
        jatek_vege = True  # Ha a felhasználó "stop"-ot ír be, akkor a játék véget ér
        break
    elif len(tipp) != 6:
        print("A tippnek pontosan hatbetűsnek kell lennie.")
        continue
    else:
        for egyelem in tipp:
            tipp_lista.append(egyelem)
        for i in range(0, len(rejtett_szo_betuk)):
            if tipp_lista[i] == rejtett_szo_betuk[i]:
                megoldas.append(tipp_lista[i])
            elif tipp_lista[i] != rejtett_szo_betuk[i]:
                megoldas.append(".")
        print(f"Az eredmény:", *megoldas)
        szamlalo += 1

if not jatek_vege:  # Csak akkor írja ki a tippelések számát, ha a játék nem ért véget idő előtt
    print(f"\n{szamlalo} tippeléssel sikerült kitalálni")
