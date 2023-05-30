#➤ 6 Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
# Wejście: var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście ‘nnnnnnnnn’, 9
# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
# Zaimportuj generator bezpośrednio do programu.

from seq_generator import num_seq_generator, user_seq_generator
from seq_checker import seq_check


def pretty(any_list):
    return ", ". join(any_list)

def main():
    #1 Generator instancji tekstowych
    seq_n = num_seq_generator()
    seq_check(seq_n)
    print(seq_n)
    long_seq_n = seq_check(seq_n)
    print(f"Longest string is: {pretty(long_seq_n)}, len is: {len(long_seq_n[0])}")

    #Generator znaków użytkownika
    seq_u = user_seq_generator()
    seq_check(seq_u)
    print(seq_u)
    long_seq_u = seq_check(seq_u)
    print(f"Longest string is: {pretty(long_seq_u)}, len is: {len(long_seq_u[0])}")


main()
