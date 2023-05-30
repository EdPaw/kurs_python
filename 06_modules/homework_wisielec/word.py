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