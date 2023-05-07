#➤ 1 Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.
my_tuple = (1, 1, 2, 3, 4, 5, 3, 7, 8)

my_set = set(my_tuple)
print(my_set)

#➤ 2 Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?
L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

#Wszystkie metody, które wymagają modyfikacji elementów:
#append
#extend
#insert
#remove
#pop
#sort
#reverse

#Na krotce nie można użyć:
#clear
#copy

#Na secie nie można użyć:
#index