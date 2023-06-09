
class Mammal:
    characteristic = 'Presence of mammary glands in females and warm-blooded'

    def __init__ (self, name, family, fur):
        self.name = name
        self.family = family
        self.fur = fur

    def describe_mammal(self):
        print(f"Mammal {self.name} from {self.family} family has {self.fur}. {self.characteristic} is characteristic.")


wolf = Mammal("wolf", "canid", "fur")
horse = Mammal("horse", "equine", "fur")
hippo = Mammal("hippo", "hippopotamidae", "no fur")

wolf.describe_mammal()
horse.describe_mammal()
hippo.describe_mammal()
