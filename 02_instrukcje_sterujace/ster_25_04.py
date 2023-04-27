#1
num = int(input("Podaj liczbe: "))
if num % 3 == 0 :
    print("Twoja liczba jest podzielna przez 3")
else:
    print("Twoja liczba nie jest podzielna przez 3")

#3
op1 = int(input("Podaj opinie 1 1-10: "))
op2 = int(input("Podaj opinie 2 1-10: "))
op3 = int(input("Podaj opinie 3 1-10: "))

op_avg = (op1+op2+op3) / 3
#lub funkcja avg
if op_avg > 7:
    print("bardzo dobry")
elif op_avg >= 5:
    print("przecietna")
else:
    print("nie warta uwagi")

#5
password = str(input("Podaj hasło: "))
if len(password) < 8:
    print("hasło jest za krótkie")

if password.islower() == True:
    print("hasło nie zawiera wielkiej litery")

if password.isupper() == True:
    print("hasło nie zawiera małej litery")

if password.isalnum() and password.isalpha():
    print("hasło nie zawiera żadnej cyfry")

if password.isalnum() and password.isdigit():
    print("hasło nie zawiera żadnej litery")

print(f"Super password:", {password})

txt = "abrakadabra"
for letter in txt:
    print("-", letter)

my_list = ["Ada", "Ruby", "Julia"]
for step in my_list:
    print("Hello", step)

for step in range(5):
    print("krok: ", step)

for i in range(5, 20, 2):
    print(i)

for i in range(3):
    print(i + " : " + my_list[i])

pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)




