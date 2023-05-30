import random


def num_seq_generator():
    n = int(input("Podaj długość ciągu -> "))

    while n == 1:
        n = int(input("Podaj sługość ciągu >1 -> "))

    seq = ""
    seq_double = str(random.randint(0, 9)) * 2
    #n- długosc sekwencji
    if n == 2:
        seq = seq_double
    else:
        for i in range(0, n-2):
            seq += str(random.randint(0, 9))
        seq += seq_double

    return seq


def user_seq_generator():
    signs = input("Podaj 4 znaki po przecinku -> ")
    signs = signs.replace(",", "")
    sign_l = list(signs)

    n = int(input("Podaj długość ciągu znaków -> "))

    while n == 1:
        n = int(input("Podaj liczbę >1 -> "))

    seq = ""
    seq_double = str(random.choice(sign_l)) * 2
    #n- długosc sekwencji
    if n == 2:
        seq = seq_double
    else:
        for i in range(0, n-2):
            seq += str(random.choice(sign_l)) * 2
        seq += seq_double

    return seq






