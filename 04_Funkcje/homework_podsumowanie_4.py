#➤ 4 Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić komunikat:
# “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def czy_liczba_w_zakresie(liczba, zakres_od, zakres_do):
    if liczba in range(zakres_od, zakres_do+1):
        print(f"tak, liczba {liczba} znajduje się w zadanym zakresie {zakres_od} - {zakres_do}")
    else:
        print(f"nie, liczba {liczba} jest spoza zakresu {zakres_od} - {zakres_do}")


def main():
    liczba_uzytk = int(input("Podaj liczbę: "))
    zakres_od_uzytk = int(input("Podaj zakres od: "))
    zakres_do_uzytk = int(input("Podaj zakres do: "))

    czy_liczba_w_zakresie(liczba_uzytk, zakres_od_uzytk, zakres_do_uzytk)


main()