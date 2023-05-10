"""
#Zad 1
lists_to_dict = [["avocado", "green"], ["tomato", "red"], ["onion", "yellow"]]
dict_from_list = dict(lists_to_dict)

print(dict_from_list)

for k, v in dict_from_list.items():
    print(k, "->", v)

#Zad 2
tuples_to_dict = [{"avocado", "green"}, {"tomato", "red"}, {"onion", "yellow"}]
dict_from_tuples= dict(tuples_to_dict)

print(dict_from_tuples)

#Zad 3
wejscie = int(input("Podaj n: "))
znak = "*"

tab = [[str(znak)] * wejscie] * wejscie

txt = " "
for elem in tab:
    txt.join(elem)
    print(txt.join(elem))
"""
#Zad 5
poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.replace(",", "").lower().split()
counting_word = {}

for word in poem:
    if word in counting_word:
        counting_word[word] += 1
    else:
        counting_word[word] = 1

print(counting_word)

for word, counter in counting_word.items():
    print("*", word, "-", counter)
