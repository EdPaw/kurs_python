import random
import os


def get_content():
    while True:
        try:
            file = input('Podaj nazwę pliku: ')
            with open(file, encoding="UTF-8") as fopen:
                content = fopen.readlines()
                return content, file
        except FileNotFoundError:
            print("Błąd w nazwie pliku")


def show(quotes, how_many):
    for i in range(how_many):
        quote = random.choice(quotes)
        print('\nQuote of the day is:')
        width = 120
        print(('*' * width).center(width))
        cit = quote.split("-")

        print(cit[0].strip().center(width))
        print(cit[1].strip().center(width))
        print('*' * width)


def main():

    content, file = get_content()

    how_many = int(input('Podaj ile cytatów: '))
    show(content, how_many)

    file_size = os.path.getsize(file)
    print(f"\nSize of file: {file_size}")


main()
