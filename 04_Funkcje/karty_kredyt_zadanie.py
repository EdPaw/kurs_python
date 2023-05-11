def pobierz_karte(nr_karty):
    nr_karty = nr_karty.replace("-", "")
    nr_karty = nr_karty.replace(" ", "")

    while not nr_karty.isdigit() or not (len(nr_karty) in range(13, 25)):
        nr_karty = input("To nie jest numer karty. Podaj poprawny numer: ")
    else:
        return sprawdz_karte(nr_karty)


def czy_visa(nr_karty):
    if str(nr_karty)[0] == '4' and (len(nr_karty) == 16 or len(nr_karty) == 13):
        return "To Visa"


def czy_american(nr_karty):
    start_cond = str(nr_karty)[:2] == '34'
    end_cond = str(nr_karty)[:2] == '37'
    if (start_cond or end_cond) and (len(nr_karty) == 16):
        return "To American"


def czy_mastercard(nr_karty):
    start_cond = int((str(nr_karty)[:2])) in range(51, 56)
    end_cond = int((str(nr_karty)[:2])) in range(2221, 2720)
    if (start_cond or end_cond) and (len(nr_karty) == 16):
        return "To Mastercard"


def sprawdz_karte(nr_karty):
    if czy_visa(nr_karty):
        return czy_visa(nr_karty)
    elif czy_american(nr_karty):
        return czy_american(nr_karty)
    elif czy_mastercard(nr_karty):
        return czy_mastercard(nr_karty)
    else:
        return print("Żadna z powyższych")


def main():
    karta = input("Podaj nr karty: ")
    print(pobierz_karte(karta))


main()

#VISA 4126789036274
#AMERICAN 341234567891234
#MASTER 5112367890981234