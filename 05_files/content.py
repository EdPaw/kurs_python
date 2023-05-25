def czytaj_plik():
    with open("pan_tadeusz.txt") as fopen:
        content = fopen.read()

    return content

def wyswietlaj(tekst):
    print(tekst)


def main():
    ksiazka = czytaj_plik()
    wyswietlaj(ksiazka)


main()
