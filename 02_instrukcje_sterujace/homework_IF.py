#➤ 2 Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
liczba_1 = int(input("Podaj pierwszą liczbę: "))
liczba_2 = int(input("Podaj drugą liczbę: "))

liczba_sum = liczba_1 + liczba_2

if liczba_sum > 100:
    print("Twój wynik to:", liczba_sum)
else:
    print("Koniec")

#➤ 4 Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
znaki = str(input("Wpisz dowolny ciąg znaków: "))

warunek_1 = len(znaki) > 5
warunek_2 = znaki.count("a") != 0

if warunek_1 and warunek_2:
    print(znaki.replace("a", "z"))
else:
    print("brak rezultatu")


#➤ 6 Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.
liczba_prog = 7
liczba = int(input("Podaj liczbę od 1 do 100: "))

if liczba < 1 or liczba > 100:
    print("Liczba nie mieści się w wymaganym zakresie")
elif liczba == liczba_prog:
    print("gratulacje!")
else:
    print("pudło!")

#➤ 7 Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga.txt / waga normalna / nadwaga.txt / otyłość.txt.
kg = float(input("Podaj masę (kg): "))
height = float(input("Podaj wzrost (m): "))

BMI = round(kg / height**2 , 2)

if BMI < 18.5:
    print("Your BMI is:",BMI, "- masz niedowagę.")
elif BMI < 24.9:
    print("Your BMI is:",BMI, "- masz prawidłową wagę.")
elif BMI < 29.9:
    print("Your BMI is:",BMI, "- masz nadwagę")
else:
    print("Your BMI is:", BMI, "- masz otyłość.txt")

#➤ 8 Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.
nr_1 = float(input("Podaj pierwszą liczbę: "))
nr_2 = float(input("Podaj drugą liczbę: "))
nr_3 = float(input("Podaj trzecią liczbę: "))

if nr_1 > nr_2 and nr_1 > nr_3:
    if nr_2 > nr_3:
        print(nr_1, nr_2, nr_3)
    else:
        print(nr_1, nr_3, nr_2)
elif nr_2 > nr_1 and nr_2 > nr_3:
    if nr_1 > nr_3:
        print(nr_2, nr_1, nr_3)
    else:
        print(nr_2, nr_3, nr_1)
elif nr_3 > nr_1 and nr_3 > nr_2:
    if nr_1 > nr_2:
        print(nr_3, nr_1, nr_2)
    else:
        print(nr_3, nr_2, nr_1)

# 2 sposób
nr_min = min(nr_1, nr_2, nr_3)
nr_max = max(nr_1, nr_2, nr_3)

if nr_1 != nr_min and nr_1 != nr_max:
    print(nr_max, nr_1, nr_min)
elif nr_2 != nr_min and nr_2 != nr_max:
    print(nr_max, nr_2, nr_min)
else:
    print(nr_max, nr_3, nr_min)

