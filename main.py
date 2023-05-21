#NB 2023-05-20
class UtasszallitoRepulo:
    def __init__(self, tipus, ev, utas, szemelyzet, utazo_sebesseg, felszallotomeg, fesztav):
        self.tipus = tipus
        self.ev = ev
        self.utas = utas
        self.szemelyzet = szemelyzet
        self.utazo_sebesseg = utazo_sebesseg
        self.felszallotomeg = felszallotomeg
        self.fesztav = fesztav
        self.sebessegkategoria = self.hataroz_sebessegkategoria(utazo_sebesseg)

    def hataroz_sebessegkategoria(self, utazo_sebesseg):
        if utazo_sebesseg < 500:
            return "Alacsony sebességű"
        elif utazo_sebesseg < 1000:
            return "Szubszonikus"
        elif utazo_sebesseg < 1200:
            return "Transzszonikus"
        else:
            return "Szuperszonikus"

# Lista inicializálása az objektumok tárolására
objektumok = []

# Fájl beolvasása és objektumok létrehozása
with open('utasszallitok.txt', 'r') as file:
    for line in file.readlines()[1:]:  # A 2. sortól kezdjük a beolvasást
        sor = line.strip().split(';')
        fesztav = float(sor[6].replace(',', '.'))  # Tizedesvessző cseréje tizedesponttal
        objektum = UtasszallitoRepulo(sor[0], int(sor[1]), sor[2], sor[3], int(sor[4]), int(sor[5]), fesztav)
        objektumok.append(objektum)


darabszam = len(objektumok)
print(f"4. feladat \tA repülőgéptípusok darabszáma: {darabszam}")

szamlalo = 0

for objektum in objektumok:
    if objektum.tipus.startswith ('Boeing'):
        szamlalo += 1

print(f'5. feladat\tA Boeing {szamlalo} típust gyártott.')
legtobb_utas = 0
legtobb_tipus = ""

for objektum in objektumok:
    if "-" in objektum.utas:
        utas_szam = objektum.utas.split("-")[1]  # Az "ig" érték használata
        if int(utas_szam) > legtobb_utas:
            legtobb_utas = int(utas_szam)
            legtobb_tipus = objektum.tipus


print(f"6. feladat\tA legtöbb utast szállító repülőgéptípus: {legtobb_tipus}, {legtobb_utas} fő")

# 7. feladat: Hiányzó sebességkategória
sebessegkategoriak = [
    "Alacsony sebességű",
    "Szubszonikus",
    "Transzszonikus",
    "Szuperszonikus"
]

hianyzo_kategoriak = []

for kategoria in sebessegkategoriak:
    van_kategoria = False
    for objektum in objektumok:
        if objektum.sebessegkategoria == kategoria:
            van_kategoria = True
            break
    if not van_kategoria:
        hianyzo_kategoriak.append(kategoria)

if len(hianyzo_kategoriak) == 0:
    print("Minden sebességkategóriából van repülőgéptípus.")
else:
    hianyzo_kategoria_str = " ".join(hianyzo_kategoriak)
    print(f"7. feladat\tA hiányzó sebességkategória(k): {hianyzo_kategoria_str}")

    # Fájl létrehozása és adattartalom írása
    with open('utasszallitok_new.txt', 'w') as file:
        # Fejléc sor írása
        fejlec_sor = "típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n"
        file.write(fejlec_sor)

        # Adatok írása
        for objektum in objektumok:
            # Adatsor összeállítása
            tipus = objektum.tipus
            ev = objektum.ev
            utas = objektum.utas.split("-")[-1]  # Csak az "ig" érték kerül az új állományba
            szemelyzet = objektum.szemelyzet.split("-")[-1]  # Csak az "ig" érték kerül az új állományba
            utazosebesseg = objektum.utazo_sebesseg
            felszallotomeg_tonna = round(objektum.felszallotomeg * 0.001)  # Felszállótömeg tonnában kerekítve
            fesztav_labbal = round(objektum.fesztav * 3.2808)  # Fesztáv láb mértékegységben kerekítve

            adatsor = f"{tipus};{ev};{utas};{szemelyzet};{utazosebesseg};{felszallotomeg_tonna};{fesztav_labbal}\n"
            file.write(adatsor)
print('8. feladat\tAz adatokat elmentettem ')
'''
for objektum in objektumok:
    print(f"Típus: {objektum.tipus}")
    print(f"Ev: {objektum.ev}")
    print(f"Utasok: {objektum.utas}")
    print(f"Szemelyzet: {objektum.szemelyzet}")
    print(f"Utazo sebesseg: {objektum.utazo_sebesseg}")
    print(f"Felszallotomeg: {objektum.felszallotomeg}")
    print(f"Fesztav: {objektum.fesztav}")
    print("---------------------")
    '''
