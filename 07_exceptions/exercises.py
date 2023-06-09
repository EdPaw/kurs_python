
try:
    x = 8 / 0
except ArithmeticError as error:
    print("dzielenie przez 0")
    print(error)
    x = 8


print(x)
