# This is a python test file!

# 1.2

def Personendaten():
    print('Hallo! Wie heißen Sie?')
    meinName = input()
    print('Wie alt sind Sie in Jahren?')
    meinAlter = input()
    print('Wie viel Geld verdienen Sie jährlich Brutto in Euro?')
    meinGehalt = input()

    print('Sie heißen ', meinName, 'sind ', meinAlter, ' Jahre alt und verdienen ', meinGehalt, 'Euro im Jahr.')

Personendaten()

# 1.3

def Produktdaten():
    pk1 = input('Erste Produktkategorie: ')
    pk2 = input('Zweite Produktkategorie: ')
    pk3 = input('Dritte Produktkategorie: ')

    hersteller = input('Hersteller: ')
    
    preis = input('Preis:')

    print(pk1, pk2, pk3, hersteller, preis)

Produktdaten()

# 2.1

def Personendaten_Liste():

    personendaten = [1, 2, 3]

    personendaten[0] = input('Hallo! Wie heißen Sie?')
    personendaten[1] = input('Wie alt sind Sie in Jahren?')
    personendaten[2] = input('Wie viel Geld verdienen Sie jährlich Brutto in Euro?')

    # print(*personendaten, sep = ', ') # Nur eine Alternative

    print(f'Sie heißen {personendaten[0]}, sind {personendaten[1]} Jahre alt und verdienen {personendaten[2]} Euro im Jahr.')

Personendaten_Liste()


def Produktdaten_Liste():

    pk = []

    pk[1] = input('Erste Produktkategorie: ')
    pk[2] = input('Zweite Produktkategorie: ')
    pk[3] = input('Dritte Produktkategorie: ')

    pk[4] = input('Hersteller: ')
    
    pk[5] = input('Preis:')

    print(*pk, sep = ', ')

Produktdaten_Liste()

# 2.2

def Zinsen():
    
    anfangskapital = float(input('Anfangskapital in Euro: '))
    zinssatz = float(input('Zinssatz in Prozent (ohne %-Zeichen geschrieben): '))
    jahre = int(input('Jahre: '))

    for jahr in range(jahre):
        anfangskapital = anfangskapital * (1 + zinssatz/100)
    
    print(f'Endkapital inkl. Zinsen: {round(anfangskapital, 2)} €')

Zinsen()

# 2.3

def Dreieck():
    P1 = (0, 0)
    P2 = (-2, 1)
    P3 = (2, 1)

    a = ((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)**0.5
    b = ((P2[0] - P3[0])**2 + (P2[1] - P3[1])**2)**0.5
    c = ((P3[0] - P1[0])**2 + (P3[1] - P1[1])**2)**0.5

    # print(a)
    # print(b)
    # print(c)

    s = (a + b + c)/2

    # print(s)

    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print(f'Fläche: {A} FE')

Dreieck()

# 2.4

def Zaehlmass():

    einzelstuecke = int(input('Einzelstücke: '))

    dutzend = einzelstuecke / 12
    schock = dutzend / 5
    gros = dutzend / 12

    print(f' {einzelstuecke} Einzelstücke sind äquivalent zu: \n {dutzend} Dutzend | {schock} Schock | {gros} Gros')
    # Formatierung des Strings mittels 'f'

Zaehlmass()

# 2.5

def QuadGleichung():

    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    print(f'x1: {round(( - b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), 4)}')
    print(f'x2: {round(( - b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), 4)}')

QuadGleichung()
