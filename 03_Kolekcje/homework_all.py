#➤ 2 Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe. Przekształć ją w słownik dict_from_tuples.
tuples_to_dict = [{"avocado", "green"}, {"tomato", "red"}, {"onion", "yellow"}]
dict_from_tuples = dict(tuples_to_dict)

print(dict_from_tuples)

#➤ 4 Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.
wiersz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kolumna = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tabliczka = []

for w in range(len(wiersz)):
    tabliczka_wynik = []
    for k in range(len(kolumna)):
        tabliczka_wynik.append(kolumna[w] * wiersz[k])
    tabliczka.append(tabliczka_wynik)

for i in range(1, 10):
    print(tabliczka[i])

#➤ 6 Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

days_list = list(days.values())
print(days_list)

set_days = set(days_list)
print(set_days)

days_list_final = list(set_days)
print(days_list_final)


#➤ 8 Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich. Zapisz imiona w wersji anglojęzycznej.
# Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
imiona_slownik = {
    'Polska': ['Zuzanna', 'Maja', 'Hanna', 'Lena', 'Alice', 'Maria', 'Amelia', 'Julia', 'Oliwia', 'Natalia'],
    'Niemcy': ['Mia', 'Emma', 'Hannah', 'Sophia', 'Emilia', 'Lina', 'Marie', 'Anna', 'Leonie', 'Lena'],
    'Francja': ['Louise', 'Jade', 'Alice', 'Chloé', 'Léa', 'Emma', 'Lola', 'Manon', 'Inès', 'Camille'],
    'Włochy': ['Sofia', 'Giulia', 'Aurora', 'Martina', 'Sara', 'Alice', 'Emma', 'Ginevra', 'Beatrice', 'Alessia'],
    'Hiszpania': ['Lucía', 'Sofía', 'Martina', 'María', 'Paula', 'Valeria', 'Daniela', 'Alba', 'Claudia', 'Julia'],
    'Portugalia': ['Mariana', 'Matilde', 'Leonor', 'Francisca', 'Beatriz', 'Carolina', 'Margarida', 'Alice', 'Mafalda', 'Ines'],
    'Wielka Brytania': ['Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Sophia', 'Grace', 'Ella', 'Poppy', 'Lily'],
    'Rosja': ['Sofia', 'Anna', 'Maria', 'Daria', 'Polina', 'Arina', 'Alina', 'Ksenia', 'Elena', 'Natalia'],
    'Szwecja': ['Alice', 'Maja', 'Elsa', 'Olivia', 'Ebba', 'Astrid', 'Alva', 'Lilly', 'Vera', 'Ida'],
    'Holandia': ['Emma', 'Tess', 'Sophie', 'Julia', 'Mila', 'Anna', 'Eva', 'Saar', 'Lotte', 'Lena']
}

imiona_lista = []

for i in imiona_slownik.values():
    imiona_lista.append(i)

imiona_lista_all = []

for elem in imiona_lista:
    imiona_lista_all.extend(elem)

#print(imiona_lista_all)

counting_name = {}

for name in imiona_lista_all:
    if name in counting_name:
        counting_name[name] += 1
    else:
        counting_name[name] = 1

print(counting_name)

for name, counter in counting_name.items():
    if counter >= 3:
        print("*", name, "-", counter)

#➤ 9 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
przedmioty = []
for i in range(1, 6):
    u = input(f"User {i}. Podaj 4 przedmioty szkolne po przecinku: ")
    przedmioty += u.split(",")

print(przedmioty)

counting_przedmioty = {}

for elem in przedmioty:
    if elem in counting_przedmioty:
        counting_przedmioty[elem] += 1
    else:
        counting_przedmioty[elem] = 1

#print(counting_przedmioty)

max_przedmiot = max(counting_przedmioty.values())

for elem, counter in counting_przedmioty.items():
    if counter == max_przedmiot:
        print("Przedmiot", elem, "wystąpił", counter, "razy")

#➤ 10 Użytkownik podaje dowolną liczbę N. Napis, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
#Załóżmy, że użytkownik podał N = 8
#Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

liczba_n = int(input("Podaj dowolną liczbę N: "))

lista_n = []
for i in range(1, liczba_n+1):
    lista_n.append(i)

lista_n2 = []
for i in range(1, liczba_n+1):
    lista_n2.append(i*i)

print(lista_n)
print(lista_n2)

lista_all = []
for n, n2 in zip(lista_n, lista_n2):
    robocza = []
    robocza.append(n)
    robocza.append(n2)
    lista_all.append(robocza)

slownik = dict(lista_all)
print(slownik)
