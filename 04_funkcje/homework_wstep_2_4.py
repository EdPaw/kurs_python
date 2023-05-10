#➤ 2 Napisać funkcję, która sprawdza czy liczba jest parzysta.

def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

#➤ 4 Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
def wypisz_parzyste(lista):
    for i in lista:
        if czy_parzysta(int(i)):
            print("*", int(i))


elementy = input("Wprowadź listę liczb po przecinku: ")
elementy_list = elementy.split(",")

#print(elementy_list)
wypisz_parzyste(elementy_list)
