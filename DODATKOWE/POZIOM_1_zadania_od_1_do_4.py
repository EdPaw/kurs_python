#➤ ZADANIE 1 Napisz program, który pyta użytkownika o dwie liczby i wyświetla wynik ich mnożenia, ale tylko wtedy, gdy obie liczby są dodatnie.
# W przeciwnym wypadku wyświetl komunikat ”Nie mnożę!”
liczba_1 = float(input("Podaj pierwszą liczbę: "))
liczba_2 = float(input("Podaj drugą liczbę: "))

if liczba_1 > 0 and liczba_2 > 0:
    mnoz = liczba_1 * liczba_2
    print(f"Wynik mnożenia {liczba_1} * {liczba_2} to {mnoz}")
else:
    print("Nie mnożę!")

#➤ ZADANIE 2 Napisz program, który używa pętli for do wyświetlenia tabliczki mnożenia (1 do 10) dla wybranej przez użytkownika liczby do.
mnoz = int(input("Podaj liczbę dla której wyświetlić tabliczkę mnożenia: "))

mnozniki = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elem in mnozniki:
    wynik = mnoz * elem
    print(f"{mnoz} * {elem} = {wynik}")

#➤ ZADANIE 3 Napisz program, który wyświetla liczbę wyrazów w podanym przez użytkownika ciągu znaków (zakładamy, że wyrazy dzielą się spacją).
ciag = str(input("Podaj ciąg znaków: "))
ciag_lista = ciag.split(" ")
ciag_wyrazy = len(ciag_lista)
print(f"Są {ciag_wyrazy} wyrazy w Twoim ciągu znaków")


#➤ ZADANIE 4 Napisz program, który używa pętli for do zsumowania wszystkich liczb parzystych z zakresu od 1 do 100.
suma = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma += i
print(suma)







