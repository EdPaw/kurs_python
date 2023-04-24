# 2
# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
import math
print("TASK 2")
s1 = "pies"
s2 = "KOT"
len_s1 = len(s1)
middle_s1 = math.floor(len_s1 / 2)
s3 = s1[0:middle_s1] + s2 + s1[middle_s1:len_s1]

print(s3)

# 3
print("\nTASK 3")
# Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”
quote = "Honesty is the first chapter in the book of wisdom."

# Policz wszystkie znaki w napisie
quote_len = len(quote)
print(quote_len)

# Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])
quote_wisdom = quote.find("wisdom")
print(quote[quote_wisdom: quote_wisdom+6])

# Wyświetl tylko pierwszą połowę tekstu
quote_middle = int(quote_len/2)
print(quote[0:quote_middle])

# Wyświetl tylko kropkę
quote_dot = quote.find(".")
print(quote[quote_dot])

# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[quote_middle::3])

quote_no_space = quote.replace(" ", "")     #czy spacja jest traktowana jako litera?
quote_no_space_len = len(quote_no_space)
quote_no_space_middle = math.floor(quote_no_space_len / 2)
print(quote_no_space[quote_no_space_middle::3])

# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])

# Wyświetl cały cytat odwrotnie
print(quote[::-1])

# Zamień wisdom na słowo friendship
quote_friendship = quote.replace("wisdom", "friendship")
print(quote_friendship)

#4
print("\nTASK 4")
# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron. Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
title = input("Enter title of the book: ")
title_no_space = title.replace(" ", "")
while not title_no_space.isalpha():
    title = input("Wrong input format. Enter valid title of the book: ")
    title_no_space = title

surname = input("Enter surname of the author: ")
surname_no_space = surname.replace(" ", "")
while not surname_no_space.isalpha():
    surname = input("Wrong input format. Enter valid surname of the author: ")
    surname_no_space = surname

pages = input("Enter number of pages: ")
while not pages.isnumeric():
    pages = input("Wrong input format. Enter valid number of pages: ")
    pages = pages

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print(title.title())
print(surname.capitalize())

# Połącz dane w jeden ciąg book za pomocą spacji
book = title + " " + surname + " " + str(pages)
print("Your book is:", book)

# Policz liczbę wszystkich znaków w napisie book
book_len = len(book)
print(book_len)

#5 Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

#6 Przekopiuj zawartość import this do zmiennej.
print("\nTASK 6")
import this
txt = "".join([this.d.get(c, c) for c in this.s])

# Policz liczbę wystąpień słowa better.
txt_better = print("\nThere are", txt.count("better"), "better words in this text.\n")

# Usuń z tekstu symbol gwiazdki

txt_no_star = txt.replace("*", "")
print("WITHOUT STARS:\n", txt_no_star)

# Zamień jedno wystąpienie explain na understand
txt_explain = txt_no_star.replace("explain", "understand", 1)
print("\nFIRST EXPALIN = UNDERSTAND\n", txt_explain)

# Usuń spacje i połącz wszystkie słowa myślnikiem
txt_multiple_dash = txt_explain.replace("--", "")
txt_dash = txt_multiple_dash.replace(" ", "-")
print("\nDASHES INSTEAD OF SPACES\n", txt_dash)

# Podziel tekst na osobne zdania za pomocą kropki
print("\nTEXT DOTS\n")
txt_dot = txt_dash.split(".")
print(txt_dot)
