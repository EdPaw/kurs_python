#➤ 2 Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).
def minimum_of_3(a, b, c):
    list_min = []
    list_min.extend([a, b, c])
    list_min.sort()
    return list_min[0]

#➤ 3 Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).
def maximum_of_3(a, b, c):
    list_max = []
    list_max.extend([a, b, c])
    list_max.sort()
    return list_max[2]


print(minimum_of_3(5, 2, 1))
print(maximum_of_3(5, 20, 10))
