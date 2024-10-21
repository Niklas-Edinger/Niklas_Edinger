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

    a = input('a: ')
    b = input('b: ')
    c = input('c: ')

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

Schrauben(input('Durchmesser in mm: '), input('Länge in mm: '),)

# 3.4 Schaltjahr

jahreszahl = 0
schaltjahr = False

def Kalender(jahreszahl):

    if jahreszahl % 4 == 0 and jahreszahl % 100 != 0 or jahreszahl % 400 == 0:
        schaltjahr = True

    if schaltjahr == True:
        print('Februar hat 28 Tage.')
    else:
        print('Februar hat 29 Tage.')

Kalender(input('Ganzzahlige Jahreszahl: '))

# 3.5 Maschinensteuerung

def Steuerung(alpha, x, a, b, w):

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

# 4.1 Würfelspiel

# (a)

import random

def Wuerfelspiel():

    wurf = 0
    spieler1 = 0
    spieler2 = 0

    for i in range(10):
        wurf = random.randint(1,6)
        if i % 2 == 0:
            spieler1 += wurf
        else:
            spieler2 += wurf

    if spieler1 > spieler2:
        print("Spieler 1 gewinnt!")
    elif spieler2 > spieler1:
        print("Spieler 2 gewinnt!")
    else:
        print("Unentschieden!")

for i in range (100):
    Wuerfelspiel()

# (b)

wurf = 0
i = 0
spieler1 = 0
spieler2 = 0

while spieler1 < 100 and spieler2 < 100:
    wurf = random.randint(1,6)
    if i % 2 == 0:
        spieler1 += wurf
        i += 1
    else:
        spieler2 += wurf
        i += 1

if spieler1 > spieler2:
    print("Spieler 1 gewinnt!")
elif spieler2 > spieler1:
    print("Spieler 2 gewinnt!")
else:
    print("Unentschieden!")

# (c)

wurf = 0
i = 0
streak1 = [0,1,0]
streak2 = [0,1,0]

while True:
    wurf = random.randint(1,6)
    if i % 2 == 0:
        streak1.append(wurf)
    else:
        streak2.append(wurf)

    i += 1

    if streak1[-1] == streak1[-2] == streak1[-3]:
        print("Spieler 1 gewinnt!")
        break
    elif streak2[-1] == streak2[-2] == streak2[-3]:
        print("Spieler 2 gewinnt!")
        break

# (d)

wurf = 0
i = 0
spieler1 = 0
spieler2 = 0

while wurf != 6:
    wurf = random.randint(1,6)
    if i % 2 == 0 and wurf == 6:
        print("Spieler 1 gewinnt!")
        break
    elif i % 2 != 0 and wurf == 6:
        print("Spieler 2 gewinnt!")
        break
    else:
        i += 1

# 4.2 Mustererzeugung

def Muster():

    i = 0
    p = [1]
    max = 5

    for i in range(max * 2 - 1):
        for q in p:
            print("*", end = "")
        print()
        if i < max - 1:
            p.append(1)
        else:
            p.remove(1)

Muster()

# 4.3 Menü

def Menue():

    print("Bitte wählen Sie eine Option:\n",
    "1 Funktion 1\n",
    "2 Funktion 2\n",
    "3 Funktion 3\n",
    "4 Programm beenden")

    x = int(input())

    if x == 4:
        print("--- Programm beendet ---")
    else:
        print(x)
        Menue()

Menue()

# 4.4 Zeichenkette

def Zeichenkette():

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    kette = input("Bitte geben Sie eine Zeichenkette ein: ")
    gesuchteKette = input("Bitte geben Sie die gesuchte Zeichenkette ein: ")

    anzahlZeichen = 0
    anzahlBuchstaben = 0
    anzahlGesuchteZeichen = 0

    for char in kette:
        anzahlZeichen += 1

    for char in kette:
        if char in alphabet:
            anzahlBuchstaben += 1
    
    for i in range(len(kette)):
        if kette[i] == gesuchteKette:
            anzahlGesuchteZeichen += 1

    print(f'Ursprüngliche Zeichenkette: {kette}')
    print(f'Gesuchte Zeichenkette: {gesuchteKette}')
    print(f'Anzahl Zeichen in ursprüngliche Zeichenkette: {anzahlZeichen}')
    print(f'Anzahl Buchstaben in ursprüngliche Zeichenkette: {anzahlBuchstaben}')
    print(f'Anzahl gesuchte Zeichen in ursprüngliche Zeichenkette: {anzahlGesuchteZeichen}')

Zeichenkette()

# 4.5 Menü mit Funktionsaufruf

def Menue():

    print("Bitte wählen Sie eine Option:\n",
    "1 Wuerfelspiel 1\n",
    "2 Muster 2\n",
    "3 Zeichenkette 3\n",
    "4 Programm beenden")

    x = int(input())

    if x == 1:
        Wuerfelspiel()
    elif x == 2:
        Muster()
    elif x == 3:
        Zeichenkette()
    elif x == 4:
        print("--- Programm beendet ---")
    else:
        print("ungültige Eingabe")

Menue()
