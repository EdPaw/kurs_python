#➤ 5 Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
# Stwórz grę ciepło zimno. #Komputer losuje liczbę z zakresu od 1 do 100. Użytkownik podaje swój traf. Komputer odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz. Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random

def losuj_liczbe():
    los_liczba = random.randrange(1, 100)
    return los_liczba


def gra_cieplo_zimno(los):

    for i in range(1, 8):
        if i == 7:
            print("\nPrzegrywasz")
        else:
            liczba_uzytkownik = int(input("Zgadnij liczbę: "))
            if liczba_uzytkownik == los:
                print("\nWygrywasz!")
                break
            elif abs(liczba_uzytkownik - los) < 10:
                print("bardzo ciepło")
            elif abs(liczba_uzytkownik - los) < 50:
                print("ciepło")
            elif abs(liczba_uzytkownik - los) > 80:
                print("bardzo zimno")
            else:
                print("zimno")


def main():
    gra_cieplo_zimno(losuj_liczbe())


main()
