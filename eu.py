#Ausztria;1995.01.01
#Belgium;1958.01.01
f = open("EUcsatlakozas.txt", encoding='latin2')
lista = []
for sor in f:
    print(sor.strip())
    lista.append(sor.strip().split(";"))
f.close()

#3. feladat: EU tagállamainak száma: ? db
print(f"3. feladat: EU tagállamainak száma: {len(lista)}")

#4. feladat: 2007-ben {} ország catlakozott.
szamlalo = 0
for sor in lista:
    if sor[1][0:4] == '2007':
        szamlalo = szamlalo + 1
print(f'4. feladat: 2007-ben {szamlalo} ország catlakozott.')

#5. feladat: Magyarország csatlakozásának dátuma: {}
for sor in lista:
    if sor [0] == 'Magyarország':
        print(f'5. feladat: Magyarország csatlakozásának dátuma: {sor[1]}')

#6. feladat: Májusban {} csatlakozás
volt_csatlakozas = False
for sor in lista:
    if sor[1][5:7] == '05':
        volt_csatlakotas = True
if volt_csatlakozas:
    print(f'6. feladat: Májusban volt csatlakozás')
else:
    print(f'6. feladat: Májusban nem volt csatlakozás')

#7. feladat: Legutoljára csatlakozott ország: {}
utoljara = ''
for sor in lista:
    if utoljara < sor[1]:
        utoljara = sor[1]
        orszag = sor[0]
print(f'7. feladat: Legutoljára csatlakozott ország: {orszag}')

#8. feladat: Statisztika
statisztika = dict()
for sor in lista:
    ev = sor[1][0:4]
    statisztika[ev] = statisztika.get(ev, 0) + 1
print(f'8. feladat: Statisztika')
for sor in statisztika.items():
    print(f'        {sor[0]} - {sor[1]} ország')
    