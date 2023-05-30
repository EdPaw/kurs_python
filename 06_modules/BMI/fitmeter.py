import bmi


def get_content(file):
    with open(file, encoding="UTF-8") as fopen:
        content = fopen.read()
    print(content)


def main():
    kg = float(input("Podaj masę (kg): "))
    height = float(input("Podaj wzrost (m): "))

    bmi_calc = bmi.calculate_bmi(kg, height)
    get_content(f"{bmi_calc}.txt")


main()
