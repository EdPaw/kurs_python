#1
items = ["phone", "water", "headphones"]

for i in items:
    print("spakowano: ", i)
print("Great, we are ready")

#3
a = 0
for i in range(1, 11):
    a = a + i
    print(a)

cookies = 5
while cookies > 0:
    print('Zjedz ciastko')
    cookies = cookies - 1
    print('Zostało jeszcze ', cookies)
    print('---------------------------')

print('\nNo nie, znowu trzeba kupić ciastka!')

fahr = 0
while fahr <= 200:
    celc = round(5 / 9 * (fahr - 32), 2)
    print(f"temp {fahr} F -> {celc} C")
    fahr += 20


for val in "string":
  if val == "i":
      break
  print(val)

print("Koniec")


for val in "string":
  if val == "i":
      print('lalala')
      continue
  print(val)

print("Koniec")


#1
names = str(input("Podaj imiona po przecinku: "))
names_list = names.replace(" ", "").split(",")
print(names_list)

for i in names_list:
    print("Witaj:", i)

#3
txt = str(input("Podaj ciąg znaków: "))

lower_letters = 0
upper_letters = 0
digits = 0
other_chars = 0

for char in txt:
    if char.isupper():
        upper_letters += 1
    elif char.islower():
        lower_letters += 1
    elif char.isdigit():
        digits += 1
    else:
        other_chars += 1


print("lower letters:", lower_letters)
print("upper letters:", upper_letters)
print("digits:", digits)
print("other:", other_chars)

