#➤ 1 Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”
mypet1 = ('kot', 'norweski leśny', 'Kini')
mypet2 = ('kot', 'europejski krótkowłosy', 'Mela')

rodzaj1, rasa1, imie1 = mypet1
rodzaj2, rasa2, imie2 = mypet2

print(f"Mój {rodzaj1}, rasy {rasa1} wabi się {imie1}.")
print(f"Mój {rodzaj2}, rasy {rasa2} wabi się {imie2}.")


#➤ 2 Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
my_tuple = (1, 2, 3, 2, 'kot', 'pies', 'kot', 'kot', 'pies')

my_set = set()
for elem in my_tuple:
    my_tuple_count = my_tuple.count(elem)
    if my_tuple_count != 1:
        my_set.add(elem)

print(my_set)
