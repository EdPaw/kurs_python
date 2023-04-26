# 1
x = "123a456"
x_isdigit = x.isdigit()
print(x_isdigit)

#2
y = "mata"
y_center = y.center(10, "*")
print(y_center)

#3
z = "www.abc.pl"
z_strip = z.lstrip("www")
print(z_strip)

#4
q = "ABC"
print(q.isupper())

#5
w = "bananana"
print(w.count("na"))

#6 nie alphanumeryczny, czy sa duzymi czy malymi
e = "12abcW"

#e_solution = e.isalnum() AND e.isupper()
#print(e_solution)


#5 Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
pal = str(input("Enter sentence: "))
pal_reversed = pal[::-1].upper().replace(" ", "")

is_pal = pal.upper().replace(" ", "") == pal_reversed

print("If palindrom:", is_pal)