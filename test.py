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

# 3.1 Münzwurf

import random

def muenzwurf():

    muenze = random.randint(0, 1)

    if muenze == 0:
        print('Kopf')
    else:
        print('Zahl')

muenzwurf()

# 3.2 # Quadratische Gleichung

def QuadGleichung():

    float a = input('a: ')
    float b = input('b: ')
    float c = input('c: ')

    x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)

    if x is tuple:
        print(f'x hat zwei Werte: {x[0]} und {x[1]}.')
    elif x is complex:
        print(f'x ist eine komplexe Zahl: {x}.')

    print(x)

QuadGleichung()

# 3.3 Klassifizierung von Schrauben

def Schrauben(durchmesser, laenge):
    if durchmesser <= 3 and laenge <= 20:
        print('Die Schraube ist vom Typ1.')
    elif 4 <= durchmesser <= 6 and 21 <= laenge <= 30:
        print('Die Schraube ist vom Typ2.')
    elif 7 <= durchmesser <= 20 and 31 <= laenge <= 50:
        print('Die Schraube ist vom Typ3.')
    else:
        print('Unbekannter Schraubentyp')

Schraube(input('Durchmesser in mm: '), input('Länge in mm: '),)

# 3.4 Schaltjahr

jahreszahl = 0
schaltjahr = false

def Kalender(int(jahreszahl)):

    if jahreszahl % 4 == 0 and jahreszahl % 100 != 0 or jahreszahl % 400 == 0:
        schaltjahr = true

    if schaltjahr == true
        print:('Februar hat 28 Tage.')
    else:
        print('Februar hat 29 Tage.')

Kalender(input('Ganzzahlige Jahreszahl: '))

# 3.5 Maschinensteuerung

def Steuerung(int(alpha), x, a, b, w):

    y = 0
    anteil = 0

    if alpha == 1:
        y = w
    elif alpha == 2:
        if x < a:
            anteil = x / a
            y = w * anteil
        else:
            y = w
    else:
        print('Alpha muss den Wert 1 oder 2 haben.')
    
    print(y)

Steuerung(input('alpha: '), input('x: '), input('a: '), input('b: '), input('w: '))