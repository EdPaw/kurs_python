
class Account:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        #atrybut prywatny
        self.__number = '12 3000 0000 1212 2111'

    def show_number(self):
        print('Account number: ', self.__number)

    def modify_number(self, new_number):
        self.__number = new_number


user = Account('Anna', 'Kowal')
print(user.firstname)
print(user.lastname)
user.show_number()
user.__number = '1234'
user.show_number()
# user.modify_number('1234')
# user.show_number()
