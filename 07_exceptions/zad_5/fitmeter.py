import bmi
import io


def validate_correctness(value, type):
    limit = 600 if type == int else 2.8
    if isinstance(value, type) and value > limit:
        raise ValueError("nieprawdopodobna wartosć")


def get_user_input(message, type_function):
    while True:
        try:
            x = type_function(input(message))
            validate_correctness(x, type)
            return x

        except ValueError:
            print("Podano złe dane")


def get_content(file, mode):
    try:
        with open(file, mode, encoding="UTF-8") as fopen:
            content = fopen.read()
        print(content)
    except FileNotFoundError:
        print("nie ma takiego pliku")
    except io.UnsupportedOperation:
        print("nie można odczytać pliku otwartego w trybie w")
    except FileExistsError:
        print("nie można utworzyć pliku, który już istnieje w tyrbie x")


def main():
    kg = get_user_input("Podaj masę (kg): ", int)
    height = get_user_input("Podaj wzrost (m): ", float)
    mode = "r"
    try:
        bmi_calc = bmi.calculate_bmi(kg, height)
        #bmi_calc = "lalalla"
        get_content(f"{bmi_calc}.txt", mode)
    except TypeError as err:
        print(err)


main()
