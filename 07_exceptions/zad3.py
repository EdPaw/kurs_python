#3▹ Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

def main():
    x = [13, 'string', 2.45, 0, True, False, 'a', -110, [1, 2, 3], {"a", "b", "c"}]

    index = input("Podaj index: ")
    try:
        index = int(index)
    except ValueError:
        print("Nie podałaś cyfry")

    try:
        result = 1 / x[index]
        print(result)
    except (TypeError, ZeroDivisionError, IndexError) as err:
        print(err)


if __name__ == "__main__":
    main()
