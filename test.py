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