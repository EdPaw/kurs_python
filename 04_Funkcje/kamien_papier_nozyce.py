import random

#słownik wygrany : prze
WINNERS = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}


CORRECT_VALUES = ['k', 'n', 'p', 'j', 's']

def get_comp_choice():
    return random.choice(CORRECT_VALUES)


def get_user_choice():

    while True:
        user_choice = input("""Podaj wartość:
                    k - kamień 
                    n - nożyce
                    p - papier 
                    j - jaszczurka
                    s - spock
        -> """)

        if user_choice in CORRECT_VALUES:
            break
        else:
            print('Nieprawidłowa wartość')
            print('--- spróbuj jeszcze raz! ---')
    return user_choice


def show_result(comp, user):
    if comp == user:
        print("Remis")
    elif comp in WINNERS[user]:
        print("Wygrana użytkownika")
    else:
        print("Wygrana komputera")


def main():
    while True:
        comp = get_comp_choice()
        user = get_user_choice()
        print("--------WYBORY--------")
        print(f"komputer -> {comp} vs user -> {user}")
        show_result(comp, user)
        czy_ponownie = input("Czy chcesz zagrać jeszcze raz? t/n: ")
        if czy_ponownie.upper() == "N":
            break

    print("***Dzięki za grę")


main()
