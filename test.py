# This is a python test file!

# 1.2

def Personendaten():
    print('Hallo! Wie heißen Sie?')
    meinName = input()
    print('Wie alt sind Sie in Jahren?')
    meinAlter = input()
    print('Wie viel Geld verdienen Sie jährlich Brutto in Euro?')
    meinGehalt = input()

    print('Sie heißen ', meinName, 'sind ', meinAlter ' Jahre alt und verdienen ', meinGehalt, 'Euro im Jahr.')

Personendaten()

# 1.3

def Produktdaten():
    pk1 = input('Erste Produktkategorie: ')
    pk2 = input('Zweite Produktkategorie: ')
    pk3 = input('Dritte Produktkategorie: ')

    hersteller = input('Hersteller: ')
    
    preis = input('Preis:')

    print(pk1, pk2, pk3, hersteller, preis)

produktdaten()

# 2.1

def Personendaten_Liste():

    personendaten = []

    print('Hallo! Wie heißen Sie?')
    personendaten[1] = input()
    print('Wie alt sind Sie in Jahren?')
    personendaten[2] = input()
    print('Wie viel Geld verdienen Sie jährlich Brutto in Euro?')
    personendaten[3] = input()

    print(*personendaten, sep = ', ')

Personendaten()

def Produktdaten():

    pk = []

    pk[1] = input('Erste Produktkategorie: ')
    pk[2] = input('Zweite Produktkategorie: ')
    pk[3] = input('Dritte Produktkategorie: ')

    pk[4] = input('Hersteller: ')
    
    pk[5] = input('Preis:')

    print(*pk, sep = ', ')

produktdaten()

# 2.2

def Zinsen():
    float anfangskapital = 0
    float zinssatz = 0
    float jahre = 0

    anfangskapital = input('Anfangskapital: ')
    zinssatz = input('Zinssatz in Dezimal: ')
    jahre = input('Jahre: ')

    for jahr in range(jahre):
        anfangskapital = anfangskapital * (1 + zinssatz) ** jahre
    
    print(anfangskapital)

Zinsen()

# 2.3

def Dreieck():
    P1 = (0, 0)
    P2 = (0, 0)
    P3 = (0, 0)

Dreieck()

# 2.4

def Zaehlmass():

    int einzelstuecke = input('Einzelstücke: ')

    dutzend = einzelstuecke / 12
    Schock = dutzend * 5
    Gros = dutzend * 12

    print(dutzend, Schock, Gros)

Zaehlmass()

# 2.5

def QuadGleichung():

    float a = input('a: ')
    float b = input('b: ')
    float c = input('c: ')

    x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)

    round(x, 4)

    print(x)

QuadGleichung()