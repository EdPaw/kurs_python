
class Doggo:
    def __init__(self, name, color, bread):
        self.name = name
        self.color = color
        self.bread = bread

    def bark(self):
        print('woofwoof')

    def wave_tail(self):
        print("machumachu")


reks = Doggo("Reks", "beżowy", "owczarek niemiecki")
killer = Doggo("Figa", "kremowy", "owczarek australijski")

print(reks.bread)
print(killer.color)

reks.bark()
killer.wave_tail(

)