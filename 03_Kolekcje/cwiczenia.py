#1
"""hobbits = ['Frodo', 'Sam', 'Pippin', 'Sam']
numbers = [1, 9, 4, 7, 4, 7]
bo = [True, False, True, False]
bo2 = [True, False, True, False]

hobbits_copy = hobbits.copy()

print(hobbits)
print(hobbits_copy)

#2
numbers.sort() #in place - wykonuje sie teraz, nadpisuje istniejaca od razu
hobbits.sort()
bo.sort()

bo2_sorted = sorted(bo2) #sorted trzeba zapisac (ed - funkcja)
print(bo2_sorted)

print(hobbits)
print(numbers)
print(bo)

#3
numbers.clear()
print(numbers)

#4
print(hobbits.count("Sam"))

#5
numbers2 = [1, 9, 4]
print(sum(numbers2))

#Zad 1
gory = ['telefon', 'buty', 'woda', 'plecaczek']
gory_sorted = sorted(gory)
print(gory_sorted)
for elem in gory:
    print("-", elem)

#Zad 2
liczby = input("Wprowadź 10 liczb po przecinku: ")
liczby = liczby.split(',')
print(liczby)

arr = []
for i in liczby:
    if int(i) % 2 == 0:
        arr.append(str(i))
print(arr)


#Zad 3
liczby_calk = input("Wprowadź liczby całkowite po przecinku: ")
liczby_calk = liczby_calk.split(',')

if liczby_calk[0] == liczby_calk[-1]:
    print("Elementy sa takie same")
else:
    print("Elementy nie sa takie same")"""

#Zad 5
osoby = [
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]

#print(osoby)

#for row in osoby:
    #print(row[0], row[1], '-', row[2])
    #print(" ".join(row))


# for row in osoby:
#     print()
#     for id, elem in enumerate(row):
#         if id == 1:
#             print(elem, end = " - ")
#         else:
#             print(elem, end = " ")

# print("\n")
# arr = ["ala", "ma", "kota", "i", "psa"]
# for id in range(5):
#     if id == 2:
#         print(arr[id], end="\n")
#     else:
#         print(arr[id], end="---> ")

# kro = (3, 4, 5, 34)
# num = int(input("Podaj: "))
# print(num)
#
# if num in kro:
#     print("jest")
#     print("Element index:", kro.index(num))
#
# else:
#     print("nie ma")

# mytuple = (1, 2, 11, 1, 2, 3, 4)
# se = set(mytuple)
# print(se)

# my_set = {1, 2, 3, 4, 5, 6}
# my_set.remove(10)
# print(my_set)

kro_1 = ("Ed", "Pit", "Mel", "Kin")
kro_2 = ("lof", "looof", "loff", "xyz")

nowa_lista = list(kro_1[0::2] + kro_2[1::2])

print(nowa_lista)

#set
list_to_set = set(nowa_lista)
print(list_to_set)




