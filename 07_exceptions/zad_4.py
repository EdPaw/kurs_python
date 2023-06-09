# 4▹ Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję,
# która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def get_user_numbers():
    while True:
        try:
            numb = input("Podaj liczby po przecinku: ")
        except ValueError:
            print("Spróbuj ponownie")

        return numb


def calculate_avg(nums):
    return 1


def main():
    get_user_numbers()


if __name__ == "__main__":
    main()


