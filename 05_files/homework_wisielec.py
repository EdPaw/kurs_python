import random


def draw_from_category(category):
    with open("wisielec.txt", encoding="UTF-8") as fopen:
        content = fopen.readlines()
        to_choose = []
        for i in content:
            word_curr = i.strip()
            if str(category) in word_curr:
                to_choose.append(word_curr)

    word = random.choice(to_choose)
    word = word.split(":")
    word = word[1]
    return word


def mask_word(word):

    masked_word = []
    for i in word:
        masked_word += "💀"

    return masked_word


def print_pretty(any_list):
    return print("". join(any_list))


def hanging_man(attempts):

    category = int(input("""Podaj kategorię:
    1 - zwierzęta
    2 - owoce
    3 - warzywa  -> """))

    word = draw_from_category(category)
    masked_word = mask_word(word)
    print_pretty(masked_word)

    #print_pretty(word)
    word_str = "". join(word)

    how_long_word = len(masked_word)
    how_many_attempts = 1

    while True:
        letter = input("\nPodaj literę: ").upper()

        while (len(letter) != 1 or len(letter) != how_long_word) and not letter.isalpha():
            letter = input("\nŹle wpisana litera. Podaj jedną literę lub całe słowo: ").upper()

        if letter == word_str:
            print("\nGratulacje! Wygrałaś!")
            break

        if letter in word:
            print(f"\nPróba: {how_many_attempts}. Trafione! ")
            for index, elem in enumerate(word):
                if elem == letter:
                    masked_word[index] = letter
            how_many_attempts += 0
        else:
            print(f"\nPróba: {how_many_attempts}. Nietrafione!")
            how_many_attempts += 1
        print_pretty(masked_word)

        if masked_word == word:
            print("\nGratulacje! Wygrałaś!")
            break
        if how_many_attempts == attempts + 1:
            print(f"\nPrzegrana! Przekroczyłaś liczbę prób = {attempts}.")
            break


def main():

    attempts = input("Podaj liczbę prób: ")

    while not attempts.isdigit():
        attempts = input("Podaj cyfrę jako liczbę prób: ")

    hanging_man(int(attempts))


main()
