"""def mood(answer):
    return answer * 2
#return wraca do miejsca z którego wywołaliśmy funkcję


resp = input("How are you? ")

twiced = mood(resp)
print("My mood is like", twiced) """

def add_books(number):
    library = {}

    for i in range(number):
        title = input("Podaj książkę: ")
        review = input("Podaj ocene: ")
        library[title] = review
    return library

def show_books(library):
    shelf = list(library.items())
    size = len(library)

    while True:
        numer = int(input(f"Podaj numer książki od 1 do {size}: "))
        if numer > size or numer < 1:
            print("Nie ma takiej ksiazki. Spróbuj jeszcze raz.")
        else:
            break

    title, review = shelf[numer-1]
    print(f"Ksiazka pt {title} ma ocene {review}")


#glowna czesc
counter = int(input("Ile książek chcesz dodać? "))
data = add_books(counter)
print(data)

show_books(data)

