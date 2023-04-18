kg = float(input("Podaj masę (kg): "))
height = float(input("Podaj wzrost (m): "))

BMI = round(kg / height**2 , 2)
print("Your BMI is:",BMI)