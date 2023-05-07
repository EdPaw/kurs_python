#➤ ZADANIE 5 Napisz program, który używa pętli for do wyświetlenia gwiazdek w następującym kształcie.
# Liczba “pięter” powinna zależeć od liczby wprowadzonej przez użytkownika w zakresie od 4 do 10

pietra = int(input("Podaj liczbę pięter gwiazdek od 4 do 10: "))

for i in range(1, pietra+1):
    print("*" * i)


#➤ ZADANIE 6 Napisz program do odwrócenia ciągu znaków podanego przez użytkownika (np. "hello" powinno być wyświetlone jako "olleh").
ciag = str(input("Podaj ciag znaków: "))

# a Za pomocą string slicing
print(ciag[::-1])

# b Za pomocą pętli for
len_ciag = len(ciag)

reversed_ciag = ""
for i in range(len_ciag-1, -1, -1):
    reversed_ciag += ciag[i]

print(reversed_ciag)

# c Za pomocą pętli while
reversed_ciag2 = ""
iterator = len_ciag - 1

while iterator >= 0:
    reversed_ciag2 += ciag[iterator]
    iterator -= 1

print(reversed_ciag2)


#➤ ZADANIE 7 Napisz program, który używa pętli for do wyznaczenia największej liczby spośród:
#a [3, 6, 12, 54, 21, 35, 2, 9]
lista_a = [3, 6, 12, 54, 21, 35, 2, 9]
najwieksza_a = lista_a[0]

for i in lista_a:
    if i > najwieksza_a:
        najwieksza_a = i
print(najwieksza_a)

#b [9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]
lista_b = [9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]
najwieksza_b = lista_b[0]
for i in lista_b:
    if i > najwieksza_b:
        najwieksza_b = i
print(najwieksza_b)

#c Liczb w dowolny sposób wprowadzonych przez użytkownika.

liczby = input("Wprowadź liczby po przecinku: ")
lista_c = liczby.split(",")

for i in range(len(lista_c)):
    lista_c[i] = int(lista_c[i])

najwieksza_c = lista_c[0]
for i in lista_c:
    if i > najwieksza_c:
        najwieksza_c = i

print(najwieksza_c)

#➤ ZADANIE 8 Napisz program, który używa pętli for do zamiany miejscami dwóch elementów tablicy o określonych przez użytkownika indeksach.
tab = ["Ala", "ma", "kota", "kot", "lubi", "Alę"]
print(f"Twoja tablica to {tab}.")
index_1 = int(input("Podaj index 1: "))
index_2 = int(input("Podaj index 2: "))

wart_index_1 = tab[index_1]
wart_index_2 = tab[index_2]

tab.pop(index_1)
tab.pop(index_2-1)

tab.insert(index_1, wart_index_2)
tab.insert(index_2, wart_index_1)

print(tab)
