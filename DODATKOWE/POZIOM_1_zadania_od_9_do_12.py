#➤ ZADANIE 9 Napisz program, który używa pętli for do wyznaczenia liczby wystąpień litery "a" w podanym przez użytkownika ciągu znaków.
ciag = input("Podaj ciąg znaków: ")

ile_a = 0
for i in ciag:
    if i == "a":
        ile_a += 1

print(f"W podanym ciągu znaków były {ile_a} litery 'a'")

#➤ ZADANIE 10 Napisz program, który używa pętli while do zsumowania wszystkich liczb nieparzystych z zakresu od 1 do 100.
suma = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        suma += i
    i += 1

print(f"Suma wszystkich liczb nieparzystych z zakresu od 1 do 100 wynosi {suma}")

#➤ ZADANIE 11 Napisz program, który używa pętli while do wyświetlenia kolejnych liczb parzystych, aż do momentu, gdy ich suma przekroczy wartość 100.
suma = 0
i = 1

while suma < 100:
    if i % 2 == 0:
        suma += i
        print(f"Kolejna liczba parzysta to {i}, suma wynosi teraz {suma}.")
    i += 1

#➤ ZADANIE 12 Napisz program, który używa pętli while do wyświetlenia kwadratów kolejnych liczb całkowitych, począwszy od 1, aż do momentu,
# gdy wartość największego wyświetlonego kwadratu przekroczy wartość 100.
liczby = 1
kwadrat = 1

while kwadrat < 100:
    kwadrat = liczby**2
    print(f"Kolejna liczba całkowita to {liczby}. Jej kwadrat to {kwadrat}.")
    liczby += 1


