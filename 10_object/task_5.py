from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def classification(self):
        pass

    def document(self):
        pass


class Car(Vehicle):

    def classification(self):
        print("Drogowy, dwuśladowy")

    def document(self):
        print("Prawo jazdy B2")


class MountainBicycle(Vehicle):
    def classification(self):
        print("Górski, jednośladowy")

    def document(self):
        print("Karta rowerowa")


class Bus(Vehicle):
    def classification(self):
        print("Drogowy, wielośladowy")

    def document(self):
        print("Prawo jazdy D")


def main():
    autobus = Bus()
    autobus.classification()
    autobus.document()
    print("~~~~~~~~~~")
    rower = MountainBicycle()
    rower.classification()
    rower.document()
    print("~~~~~~~~~~")
    auto = Car()
    auto.classification()
    auto.document()


if __name__ == '__main__':
    main()
