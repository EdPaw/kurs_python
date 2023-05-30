import csv


def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def main():
    file_path = 'generator_konferencji.csv'
    data = read_csv_file(file_path)
    for row in data:
        print(row)


main()
