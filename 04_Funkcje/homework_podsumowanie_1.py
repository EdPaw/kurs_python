#➤ 1 Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
#(niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru
def oblicz_bmi():
    kg = float(input("Podaj masę (kg): "))
    height = float(input("Podaj wzrost (m): "))
    bmi = round(kg / height ** 2, 2)
    return bmi

def jaka_kategoria_bmi(bmi):
    if bmi < 18.5:
        print("Your BMI is:",bmi, "- masz niedowagę.")
    elif bmi < 24.9:
        print("Your BMI is:",bmi, "- masz prawidłową wagę.")
    elif bmi < 29.9:
        print("Your BMI is:",bmi, "- masz nadwagę")
    else:
        print("Your BMI is:", bmi, "- masz otyłość")

bmi = oblicz_bmi()
jaka_kategoria_bmi(bmi)
