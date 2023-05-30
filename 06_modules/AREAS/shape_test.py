import shapes

def get_user_rooms():
    counter = input("Ile pomieszczeń chcesz dodać")
        while True:
            options = """Dostępne pokoje
            1 - kwadrat
            2 - koło
            3 - prostokąt->"""


def main():

    rooms = {
        "square": [4, 5, 6],
        "circle": [3, 4],
        "rectangle": [[3, 4], [4, 5], [1, 2]]
    }

    total = 0

    for shape, space in rooms.items():
        if shape == "square":
            for wall in space:
                total += shapes.square_area(wall)

        elif shape == "circle":
            for radius in space:
                total += shapes.circle_area(radius)

        elif shape == "rectangle":
            for walls in space:
                a, b = walls
                total += shapes.rectangle_area(a, b)

        else:
            print("nieznany kształt")

    print("Powierzchnia całkowita", total)


if __name__ == '__main__':
    main()
