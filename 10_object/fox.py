
class Canis:
    paws = 4
    ears = 2
    tails = 1

    def __init__(self):
        print("Jestem wilkowaty")

    def show_description(self):
        print('''Species of this genus are distinguished
by their moderate to large size, their massive,
well-developed skulls and dentition,
long legs, and comparatively short ears and tails''')


class Fox(Canis): #Lisy dziedziczą z psowatych
    #wykonuje się tylko jeden init - jeśli tu by nie było to wykona się init rodzica Canis. Tutaj jest nadpisanie
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Ring-ding-ding-ding-dingeringeding! Gering-ding-ding-ding-dingeringeding!")

    def eat(self, what):
        print(f"Fox eats {what}")

    def describe(self):
        print(f"Fox has {self.paws} paws and {self.ears} ears and {self.tails} tail.")

    def show_description(self):
        #super tylko wewnątrz klasy odzywa się do klasy rodzica
        super().show_description()
        print('''\nFoxes are small to medium-sized, omnivorous mammals belonging to several genera of the family Canidae. 
They have a flattened skull, upright, triangular ears, a pointed, slightly upturned snout, and a long bushy 
tail ("brush").''')


def main():
    foxy = Fox("Reks")
    Fox.sound(foxy)
    Fox.eat(foxy, "tomato")
    Fox.describe(foxy)
    print(foxy.tails)
    foxy.show_description()


if __name__ == '__main__':
    main()
