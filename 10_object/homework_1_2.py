class Animals:
    def describe(self):
        print('\nI am animal')


class Mammal(Animals):

    characteristic = 'Presence of mammary glands in females and warm-blooded'

    def __init__(self, name, species, fur):
        self.name = name
        self.species = species
        self.fur = fur

    def describe(self):
        super().describe()
        print(f"Mammal {self.name} - {self.species} species. Has {self.fur}. {self.characteristic} is characteristic.")


class Cat(Mammal):
    def describe(self):
        super().describe()
        print(f"""The cat (Felis catus) is a domestic species of small carnivorous mammal.[1][2] 
        It is the only domesticated species in the family Felidae and is commonly referred to as the domestic cat or 
        house cat to distinguish it from the wild members of the family.[4] Cats are commonly kept as house pets but c
        an also be farm cats or feral cats; the feral cat ranges freely and avoids human contact.[5] Domestic cats are 
        valued by humans for companionship and their ability to kill small rodents. About 60 cat breeds are recognized 
        by various cat registries.[6]""")


class Dog(Mammal):
    def describe(self):
        super().describe()
        print(f"""The dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the 
        wolf. Also called the domestic dog, it is derived from extinct Pleistocene wolves,[6][7] and the modern 
        wolf is the dog's nearest living relative.[8] Dogs were the first species to be domesticated[9][8] by 
        hunter-gatherers over 15,000 years ago[7]""")


class Human(Mammal):
    def describe(self):
        super().describe()
        print(f"""Humans (Homo sapiens) are the most common and widespread species of primate. A great ape characterized 
        by their bipedalism and high intelligence, humans have a large brain and resulting cognitive skills that enable 
        them to thrive in varied environments and develop complex societies and civilizations.""")


def main():
    kitku = Cat("Kitku", "Cat", "Fur")
    kitku.describe()

    doggo = Dog("Doggo", "Dog", "Fur")
    doggo.describe()

    ed = Human("Ed", "Human", "No Fur")
    ed.describe()


if __name__ == '__main__':
    main()
