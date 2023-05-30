#➤ 8 Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
# Program zacznie ze stworzonym słownikiem o trzech kluczach: # marka (str) # model (str) # rocznik (int)
# Wypisze ten słownik na ekran (bez żadnego formatowania)
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat: “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:  “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.

#➤ 9 Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy,
# że rzeczoznawca określił jego oryginalność w kategorii tak/nie. Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.# ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.

import random
import datetime

def get_car_details():
    brand_in = input("Type a brand of your car: ")
    model_in = input("Type a model of your car: ")
    year_in = int(input("Type year of production of your car: "))

    car = dict(brand=brand_in, model=model_in, year=year_in)
    car["original"] = bool(random.randint(0, 1))

    return car


def check_age(car_dict):
    year_val = car_dict["year"]
    brand_val = car_dict["brand"]
    model_val = car_dict["model"]
    original_val = car_dict["original"]

    current_year = int(datetime.datetime.now().year)
    age_val = current_year - year_val

    how_many_years_left = 25 - age_val

    if age_val >= 25 and original_val == True:
        print(f"Gratulacje! Twój samochód {brand_val} {model_val} może być zarejestrowany jako zabytek.")
    elif age_val >= 25 and original_val == False:
        print(f"Twój samochód {brand_val} {model_val} ma więcej niż 25 lat, ale posiada nieoryginalne części i nie może być zarejestrowany jako zabytek.")
    elif age_val < 25 and original_val == False:
        print(f"Twój samochód {brand_val} {model_val} jest za młody i posiada nieoryginalne części i nie może być zarejestrowany jako zabytek.")
    else:
        print(f"Twój samochód {brand_val} {model_val} jest jeszcze zbyt młody, ale posiada oryginalne części. "
              f"Będzie mógł być zarejestrowany jako zabytek za {how_many_years_left} lat.")


def main():
    car = get_car_details()
    print(car)
    check_age(car)


main()
