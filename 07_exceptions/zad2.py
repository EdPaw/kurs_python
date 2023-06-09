# 2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość. Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd
def main():

    my_tuple = (1, 2, 3, 4, 5, 5, 6, 7, 8)

    index = input("Podaj index: ")
    value = input("Podaj wartość: ")

    try:
        index = int(index)
        value = int(value)
        my_tuple[index] = value

    except TypeError:
        print("Type error")

    except ValueError:
        print("Value error")


if __name__ == "__main__":
    main()
