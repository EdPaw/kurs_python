# ➤ 10 Stwórz grę wisielec “bez wisielca”.
# Komputer losuje wyraz z dostępnej w programie listy wyrazów. Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
# Użykownik podaje literę.
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.
# W przeciwnym wpadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.
# Możesz ograniczyć liczbę prób do np. 10.

import random

WORDS = ["WORD", "GUESSING", "HANGING", "LETTERS", "HANGMAN", "HINT", "GALLOWS", "GUESS", "LOSE", "WIN"]


def draw_word():
    word = list(random.choice(WORDS))
    return word


def mask_word(word):

    masked_word = []
    for i in word:
        masked_word += "💀"

    return masked_word


def print_pretty(any_list):
    return print("". join(any_list))


def hanging_man(attempts):

    word = draw_word()
    masked_word = mask_word(word)

    #odkomentuj do sprawdzenia słowa:
    #print_pretty(word)
    print_pretty(masked_word)

    #próba nalicza się tylko wtedy, kiedy użytkownik nie trafi w literę
    how_many_attempts = 1

    while True:
        letter = input("\nPodaj literę: ").upper()

        while len(letter) != 1 or not letter.isalpha():
            letter = input("\nŹle wpisana litera. Podaj jedną literę: ").upper()

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
