#➤ ZADANIE 1 Algorytm szyfrowania: Napisz program, który zaszyfruje tekst, wprowadzony przez użytkownika, używając prostej metody szyfrowania przesunięciowego.
# Program powinien prosić użytkownika o wpisanie tekstu oraz przesunięcie, o które chce przesunąć każdą literę tekstu. Następnie program powinien wypisać zaszyfrowany tekst.
#97-122 - małe litery w ascii
#65-90 - duże litery w ascii

tekst = input("Wprowadź tekst do zaszyfrowania: ")

#sprawdzenie czy tekst zawiera same litery/spacje
while not all(c.isalpha() or c.isspace() for c in tekst):
    tekst = input("Wprowadzony tekst musi zawierać same litery. Wprowadź tekst do zaszyfrowania: ")

klucz = int(input("Wprowadź przesunięcie: "))

tekst_lista = list(tekst)

num_lista = []
num_lista_klucz = []
tekst_lista_klucz = []
tekst_szyfr = ""

#zamiana na liczby
for litera in tekst_lista:
    num_lista.append(ord(litera))

#przesunięcie
for i in num_lista:
    if i in range(97, 123):
        if i + klucz > 122:
            i = klucz - (122 - i) + 96
            num_lista_klucz.append(i)
        else:
            i += klucz
            num_lista_klucz.append(i)
    elif i in range(65, 91):
        if i + klucz > 90:
            i = klucz - (90 - i) + 64
            num_lista_klucz.append(i)
        else:
            i += klucz
            num_lista_klucz.append(i)
    elif i == 32:
        i = 32
        num_lista_klucz.append(i)

#lista przesuniętych liter
for numer in num_lista_klucz:
   tekst_lista_klucz.append(chr(numer))

tekst_szyfr = ''.join(tekst_lista_klucz)
print("Zaszyfrowany tekst:", tekst_szyfr)

#➤ ZADANIE 2 Algorytm deszyfrowania: Napisz program, który deszyfruje zaszyfrowany tekst, wprowadzony przez użytkownika, używając prostej metody deszyfrowania przesunięciowego.
# Program powinien prosić użytkownika o wpisanie zaszyfrowanego tekstu oraz przesunięcie, o które został on zaszyfrowany. Następnie program powinien wypisać odszyfrowany tekst.

tekst = input("Wprowadź tekst do odszyfrowania: ")

#sprawdzenie czy tekst zawiera same litery/spacje
while not all(c.isalpha() or c.isspace() for c in tekst):
    tekst = input("Wprowadzony tekst musi zawierać same litery. Wprowadź tekst do odszyfrowania: ")

klucz = int(input("Wprowadź przesunięcie: "))

tekst_lista = list(tekst)

num_lista = []
num_lista_klucz = []
tekst_lista_klucz = []
tekst_odszyfr = ""

#zamiana na liczby
for litera in tekst_lista:
    num_lista.append(ord(litera))

#przesunięcie
for i in num_lista:
    if i in range(97, 123):
        if i - klucz < 97:
            i = 123 - (klucz - (i - 97))
            num_lista_klucz.append(i)
        else:
            i -= klucz
            num_lista_klucz.append(i)
    elif i in range(65, 91):
        if i - klucz < 65:
            i = 91 - (klucz - (i - 65))
            num_lista_klucz.append(i)
        else:
            i -= klucz
            num_lista_klucz.append(i)
    elif i == 32:
        i = 32
        num_lista_klucz.append(i)

#lista przesuniętych liter
for numer in num_lista_klucz:
   tekst_lista_klucz.append(chr(numer))

tekst_odszyfr = ''.join(tekst_lista_klucz)
print("Odszyfrowany tekst:", tekst_odszyfr)
