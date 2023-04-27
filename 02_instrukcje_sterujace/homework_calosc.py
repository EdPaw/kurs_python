import random

# 2 Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby -
# za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
text = str(input("Wpisz dowolny tekst: "))
print(text[1::2])

for i in range(1, len(text), 2):
    print(text[i])


# 4 Napisz grę - kamień (k) / papier (p) / nożyce (n). #Użytkownik podaje jedną z 3 figur. #Komputer losuje jedną z 3 figur. Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik. #Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
wynik_komp = 0
wynik_uzytk = 0
print("Za chwilę podasz liczbę rund gry w kamień-papier-nożyce. Możesz z niej wyjść wpisując 'koniec'\n")

rundy = int(input("Podaj liczbę rund: "))

for i in range(0, rundy):

    uzytk = input("Wybierz jedną z figur: kamień (k) / papier (p) / nożyce (n): ")

    if uzytk == "koniec":
        break
    while uzytk not in ["k", "p", "n"]:
        uzytk = input("Wpisz poprawną literę figury: kamień (k) / papier (p) / nożyce (n): ")

    kam_pap_noz = ["k", "p", "n"]
    komp = random.choice(kam_pap_noz)

#cały tekst
    if komp == "k":
        kam_pap_noz_full = "kamień"
    elif komp == "p":
        kam_pap_noz_full = "papier"
    else:
        kam_pap_noz_full = "nożyce"

#gra
    if komp == uzytk:
        print("Remis!")
    elif komp == "k":
        if uzytk == "p":
            print("Wygrałeś! Komputer miał", kam_pap_noz_full)
            wynik_uzytk += 1
        else:
            print("Wygrał komputer. Miał", kam_pap_noz_full)
            wynik_komp += 1
    elif komp == "p":
        if uzytk == "n":
            print("Wygrałeś! Komputer miał", kam_pap_noz_full)
            wynik_uzytk += 1
        else:
            print("Wygrał komputer. Miał", kam_pap_noz_full)
            wynik_komp += 1
    elif komp == "n":
        if uzytk == "k":
            print("Wygrałeś! Komputer miał", kam_pap_noz_full)
            wynik_uzytk += 1
        else:
            print("Wygrał komputer. Miał", kam_pap_noz_full)
            wynik_komp += 1

if wynik_komp > wynik_uzytk:
    print("\nCałą grę wygrywa komputer")
elif wynik_komp < wynik_uzytk:
    print("\nCałą grę wygrywasz Ty")
else:
    print("\nCała gra skończyła się remisem")

print(f"Komputer: {wynik_komp}, Ty: {wynik_uzytk}. Koniec gry")

# 5 Stwórz grę ciepło zimno. #Komputer losuje liczbę z zakresu od 1 do 100. Użytkownik podaje swój traf. #Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#Jeśli użytkownik zgadnie wygrywa gracz. #Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
los_liczba = random.randrange(1, 100)
print(los_liczba)

for i in range(1, 8):
    if i == 7:
        print("\nPrzegrywasz")
    else:
        liczba_uzytkownik = int(input("Zgadnij liczbę: "))
        if liczba_uzytkownik == los_liczba:
            print("\nWygrywasz!")
            break
        elif abs(liczba_uzytkownik - los_liczba) < 10:
            print("bardzo ciepło")
        elif abs(liczba_uzytkownik - los_liczba) < 50:
            print("ciepło")
        elif abs(liczba_uzytkownik - los_liczba) > 80:
            print("bardzo zimno")
        else:
            print("zimno")
