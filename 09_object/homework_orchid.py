class Orchid:
    kingdom = 'roślin'
    status = ''

    def __init__(self, name, color, flowering_times, species):
        self.name = name
        self.color = color
        self.flowering_times = flowering_times
        self.species = species

    def water(self, amount):
        self.status += f"Podlana {amount} ml wody. "

    def fertilize(self, fert_type):
        self.status += f"{self.name} nawieziona {fert_type}. "

    def get_status(self):
        print(self.status)


my_cymbidium = Orchid("my_cymbidium", "pink", "4 months", "cymbidium")
my_dedrobium = Orchid("my_dedrobium", "white", "2 months", "dendrobium")


my_cymbidium.water(50)
my_cymbidium.fertilize("SUPERNAWÓZ")
my_cymbidium.get_status()
print(f"Królestwo {my_cymbidium.kingdom}")
