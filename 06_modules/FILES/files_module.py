"""Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku."""
import os


def read_file(file):
    if not os.path.exists(file):
        print("plik nie istnieje")
        return None
    elif os.path.getsize(file) == 0:
        print("plik jest pusty")
        return None
    else:
        with open(file, "r", encoding="UTF-8") as f:
            content = f.read()
            return content

     # try:
     #    with open(file, "r", encoding="UTF-8") as f:
     #        content = f.read()
     #        return content
     # except FileNotFoundError:
     #    print("nie ma takiego pliku")


def write_file(file, content):
    if os.path.exists(file) and os.path.getsize(file) > 0:
        print("plik już istnieje i nie jest pusty")
        return None
    else:
        with open(file, "w", encoding="UTF-8") as f:
            f.write(content)
            print("Plik został zapisany")


    # try:
    #     with open(file, "x", encoding="UTF-8") as f:
    #         f.write(content)
    #         return file
    # except FileExistsError:
    #     print("plik już istnieje")

