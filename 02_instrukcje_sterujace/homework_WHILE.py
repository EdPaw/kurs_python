#➤ 1 Napisac w petli for
fahr = 0
for fahr in range(0, 200):
    celc = round(5 / 9 * (fahr - 32), 2)
    print(f"temp {fahr} F -> {celc} C")
    fahr += 20


#➤ 2 Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
secret_num = 5
quest = int(input("Zgadnij liczbę od 0-20: "))

#PĘTLA WHILE
while quest != secret_num:
    quest = int(input("Źle. Zgadnij liczbę od 0-20: "))

print("Gratulacje! Zgadłaś!")


#PĘTLA FOR
for i in "quest":
    if quest != secret_num:
        quest = int(input("Źle. Zgadnij liczbę od 0-20: "))

print("Gratulacje! Zgadłaś!")