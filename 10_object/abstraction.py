from abc import ABC, abstractmethod

#Abstrakcja nie jest filarem OOP - w python trzeba ją zaimportować

class Shape(ABC):
    @abstractmethod
    #kontrakt tej klasy, który mówi, że ma powstać taka metoda i zostać wypełniona, rodzaj komentarza dla mnie, dla
    #kogoś innego, bo jak tego nie wypełnimy, to będzie błąd
    def sides(self): # abstract method
        pass


class Triangle(Shape):

    def sides(self):
        print("I have 3 sides")


class Circle(Shape):

    def sides(self):
        print("I have 0 sides")


class Square(Shape):

    def sides(self):
        print("I have 4 sides")


T = Triangle()
T.sides()

C = Circle()
C.sides()

S = Square()
S.sides()

print('************')

A = Shape()
A.sides()
