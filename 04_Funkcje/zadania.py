#Zad 1
def calculate_circle_area(r):
    circle_area = 3.14 * r**2
    return(circle_area)

def sum_elementy(items):
    result = 0
    for i in items:
        result += i

    return result

promien = int(input("Podaj promien: "))
print(calculate_circle_area(promien))

#Zad 3

summary = sum_elementy([4, 6, 7])
print(summary)


#operator 3 argumentowy
#return val1 if val1 > val2 else val2