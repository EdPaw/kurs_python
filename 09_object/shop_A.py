# Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:
    def __init__(self):
        self.products = [('sukienka', 39), ('buty', 100), ('spodnie', 50), ('koszula', 60)]

    def show(self):
        for item, price in self.products:
            print(item, 'cena ->', price, 'PLN')

    def show_product(self, name):
        prods = dict(self.products)
        if name not in prods.keys():
            print(f'Nie ma takiego produktu: {name}')
        else:
            print(name, '->', prods[name])

    def try_product(self, name):
        prods = dict(self.products)
        if name not in prods.keys():
            print(f'Nie ma takiego produktu: {name}')
        else:
            print('Przymierzam...', name)

    def buy_product(self, name):
        found = False
        for item, price in self.products:
            if name == item:
                found = True
                product = (item, price)
                self.products.remove(product)
                print('Kupuję!', product)
                break

        if not found:
            print('Nie ma produktu do kupienia')

    def return_product(self, name, price):
        prods = dict(self.products)
        if name not in prods.keys():
            print(f'Mogę dokonać zwrotu -> {name}')
            new_prod = (name, price)
            self.products.append(new_prod)
        else:
            print('Przymierzam...', name)



def main():
    myszop = Shop()
    myszop.show()
    print('-' * 10)
    myszop.show_product('buty')
    myszop.show_product('skarpetki')
    print('-' * 10)
    myszop.try_product('sukienka')
    myszop.try_product('spódnica')
    print('-' * 10)
    myszop.buy_product('buty')
    myszop.buy_product('skarpetki')
    myszop.show()
    print('-' * 10)
    myszop.return_product('spódnica', 49)
    myszop.show()


if __name__ == '__main__':
    main()