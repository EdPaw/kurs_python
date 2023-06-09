
MAILE = ['ewa@gmail.com', 'edyta@gmail.com', 'piotr@gamil.com']


def check_if_mail_on_list(mail, lista):
    mail_empty = ""
    for i in lista:
        if i == mail:
            print("Mail jest na liście!")
            mail_empty = mail

    if mail_empty == "":
        print("Nie ma maila na liście!")


def main():

    mail = input("Podaj adres email do wyszukania -> ")
    check_if_mail_on_list(mail, MAILE)


main()

