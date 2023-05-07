import random

#➤ ZADANIE 13 Napisz program, który używa pętli while do odgadnięcia liczby wylosowanej przez komputer z zakresu od 1 do 100.
# Program powinien umożliwiać użytkownikowi wprowadzenie próby odgadnięcia i wyświetlić odpowiedni komunikat, czy liczba jest za duża, za mała czy poprawna.
los = random.randrange(1, 100)
proba = int(input("Wprowadź liczbę prób odgadnięcia: "))
i = 1

while i <= proba:
    odgad = int(input(f"\nWprowadź {i} próbę odgadnięcia: "))
    if odgad == los:
        print("Gratulacje, zgadłaś.")
        break
    elif odgad > los:
        print("Liczba jest za duża.")
    else:
        print("Liczba jest za mała.")
    i += 1


#➤ ZADANIE 14 Napisz program, który używa pętli while do wyznaczenia liczby wystąpień litery "e" w podanym przez użytkownika ciągu znaków.
ciag = input("Wprowadź ciąg znaków: ")
ciag_len = len(ciag)
i = 0
ile_wystapien = 0

while i < ciag_len:
    if ciag[i].lower() == "e":
        ile_wystapien += 1
    i += 1

print(f"Było {ile_wystapien} liter 'e' w podanym ciągu znaków")

#➤ ZADANIE 15 Napisz program, który wyświetla sumę wszystkich liczb parzystych z zakresu od 1 do 100. Dodaj przy liczbie wykrzyknik tylko wtedy,
# gdy liczba jest podzielna przez 3.
suma = 0
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "!")
        suma += i
    elif i % 2 == 0:
        print(i)
        suma += i

print(f"Suma wszystkich liczba parzystych z zakresu 1 do 100 wynosi {suma}.")

#➤ ZADANIE 16 Napisz program, który stworzy listę zawierającą 10 liczb losowych z zakresu od 1 do 100 (skorzystaj z modułu random) i  wyświetla tylko te,
# które są mniejsze od 50.
zbior = []
zbior_50 = []

for i in range(1, 11):
    los = random.randint(1, 100)
    zbior.append(los)

for i in zbior:
    if i < 50:
        zbior_50.append(i)

print(zbior)
print("\nTylko mniejsze od 50:", zbior_50)
