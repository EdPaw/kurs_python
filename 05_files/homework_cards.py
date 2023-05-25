def get_content(file):
    with open(file, encoding="UTF-8") as fopen:
        content = fopen.readlines()

    return content


def czy_visa(nr_karty):
    if str(nr_karty)[0] == '4' and (len(nr_karty) == 16 or len(nr_karty) == 13):
        return "visa"


def czy_american(nr_karty):
    start_cond = str(nr_karty)[:2] == '34'
    end_cond = str(nr_karty)[:2] == '37'
    if (start_cond or end_cond) and (len(nr_karty) == 16):
        return "american"


def czy_mastercard(nr_karty):
    start_cond = int((str(nr_karty)[:2])) in range(51, 56)
    end_cond = int((str(nr_karty)[:2])) in range(2221, 2720)
    if (start_cond or end_cond) and (len(nr_karty) == 16):
        return "mastercard"


def sprawdz_karte(nr_karty):
    if czy_visa(nr_karty):
        return czy_visa(nr_karty)
    elif czy_american(nr_karty):
        return czy_american(nr_karty)
    elif czy_mastercard(nr_karty):
        return czy_mastercard(nr_karty)
    else:
        return print("Żadna z powyższych")


def przydziel_do_pliku(content):
    for elem in content:
        curr_card = elem.strip()
        jaka_karta = sprawdz_karte(curr_card)
        #print(curr_card, sprawdz_karte(curr_card))
        with open(f"{jaka_karta}.txt", "a", encoding="UTF-8") as f:
            f.write(f"{curr_card}\n")


def main():
    file = "credit_cards.txt"
    content = get_content(file)
    przydziel_do_pliku(content)


main()
