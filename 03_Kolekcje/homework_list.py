#➤ 2 Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
liczby = input("Wprowadź 10 liczb po przecinku: ")
liczby = liczby.split(',')
#print(liczby)

arr = []
for i in liczby:
    if int(i) % 2 != 0:
        arr.append(str(i))
print('Liczby nieparzyste z podanych to: ')

for elem in arr:
    print("➤", elem)

#➤ 4 Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
elementy = input("Wprowadź parzystą listę elementów. Wpisuj je po przecinku: ")
elementy = elementy.split(',')
#print(elementy)
len_elementy = len(elementy)
middle_elem = int(len_elementy / 2)

first_elem = elementy[middle_elem-1]
second_elem = elementy[middle_elem]

if first_elem == second_elem:
    print(f"2 środkowe elementy są takie same i równe {first_elem}")
else:
    print(f"2 środkowe elementy nie są takie same. To {first_elem} i {second_elem}.")
