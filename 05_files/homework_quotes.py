import random
import os


def get_content(file):
    with open(file, encoding="UTF-8") as fopen:
        content = fopen.readlines()

    return content


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
    file = input('Podaj nazwę pliku: ')
    quotes = get_content(file)
    how_many = int(input('Podaj ile cytatów: '))
    show(quotes, how_many)

    file_size = os.path.getsize(file)
    print(f"\nSize of file: {file_size}")


main()
