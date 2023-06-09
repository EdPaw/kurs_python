def calculate_bmi(kg, height):
    BMI = round(kg / height**2, 2)

    if BMI < 18.5:
        return "niedowaga"
    elif BMI < 24.9:
        return "prawidłowa"
    elif BMI < 29.9:
        return "nadwaga"
    else:
        return "otyłość"
