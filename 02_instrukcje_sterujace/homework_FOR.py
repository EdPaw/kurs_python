#➤ 2 Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
sklad = ["boczek", "jajka", "parmezan", "spaghetti"]
print("Podsmażaj i gotuj:\n")

for i in sklad:
    print(i)

print("\nPodawaj natychmiast po przygotowaniu.")

#➤ 4 Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).
n = int(input("Podaj liczbę N do obliczenia silni (nie większa niż 8): "))

if n > 8:
    n = int(input("Liczba N musi być mniejsza lub równa 8: "))

#sposob 1
#n_list = [int(i) for i in range(1, n+1)]
#operation = star.join(str(num) for num in n_list)

n_list = []
for i in range(1, n+1):
    n_list.append(str(i))

#print(n_list)

result = 1
for i in range(1, n+1):
    result *= i

star = "*"
operation = star.join(n_list)

print(operation, f"= {result}")
print(f"Silnia z {n} to: {result}")