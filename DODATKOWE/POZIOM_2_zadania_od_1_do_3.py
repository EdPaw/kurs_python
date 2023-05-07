import random
#➤ ZADANIE 1 Napisz program, który wypisze liczby od 1 do 100, ale:
#jeśli liczba jest podzielna przez 3, zamiast niej wypisz "Fizz"
#jeśli liczba jest podzielna przez 5, zamiast niej wypisz "Buzz"
#jeśli liczba jest podzielna przez 3 i przez 5, zamiast niej wypisz "FizzBuzz"

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#➤ ZADANIE 2 Napisz skrypt orzeł 🦅 / reszka 🪙, w której “komputer rzuca monetą” - losuje wynik.
# Program powinien pytać użytkownika, czy chce rzucać monetą ponownie, a także podawać wynik każdego rzutu.
result = ['🦅', '🪙']
komputer = random.choice(result)
print(f"Komputer rzuca monetą. To {komputer}")
czy_dalej = input("Czy chcesz rzucać ponownie? T/N: ")

while czy_dalej == 'T':
    komputer = random.choice(result)
    print(f"Komputer rzuca monetą. To {komputer}")
    czy_dalej = input("Czy chcesz rzucać ponownie? T/N: ")

print("Koniec gry")

#➤ ZADANIE 3 Napisz grę w Większa / Mniejsza, w której komputer losuje liczbę z przedziału 1-100, a gracz musi odgadnąć, czy kolejna wylosowana liczba będzie większa czy mniejsza.
#Po każdym strzale program powinien podawać wynik, czy gracz wygrał czy przegrał, a także liczbę prób. Wygrana kończy działanie programu

czy_wygrana = 0
proba = 1
while czy_wygrana == 0:
    los1 = random.randrange(1, 100, 1)
    uzytk = input(f"Czy kolejna liczba będzie większa czy mniejsza od {los1}? W/M: ")
    los2 = random.randrange(1, 100, 1)
    print(f"\nWylosowana liczba to {los2}.")
    if los2 > los1 and uzytk == 'W':
        czy_wygrana = 1
        print(f"Gratulacje wygranej! Kolejna liczba była wyższa niż {los1}. Liczba prób: {proba}")
    elif los2 < los1 and uzytk == 'M':
        czy_wygrana = 1
        print(f"Gratulacje wygranej! Kolejna liczba była niższa niż {los1}. Liczba prób: {proba}")
    else:
        czy_wygrana = 0
        if los2 > los1:
            print(f"Przegrana. Kolejna liczba była wyższa niż {los1}. To Twoja {proba} próba\n")
        else:
            print(f"Przegrana. Kolejna liczba była niższa niż {los1}. To Twoja {proba} próba\n")
        proba += 1
