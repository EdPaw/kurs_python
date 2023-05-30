#➤ 4 Zmodyfikuj swoją grę wisielec tak, aby w dowolny uzasadniony sposób wykorzystać moduł lub moduły.

from word import draw_word, mask_word, print_pretty
from hangman import hanging_man


def main():

    attempts = input("Podaj liczbę prób: ")

    while not attempts.isdigit():
        attempts = input("Podaj cyfrę jako liczbę prób: ")

    hanging_man(int(attempts))


main()


