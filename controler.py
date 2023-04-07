import contact
pb = contact.Phonebook("contacty.txt")

def main_meny() -> int:
    print(pb.meny())
    length_meny = len(pb.meny().split("\n")) - 1
    choice = input("Выберите пункт меню: ")
    while True:
        if choice.isdigit() and 0 < int(choice) <= length_meny:
            return int(choice)
        else:
            print(f"Неверный пункт меню, введите от 1 до {length_meny}")
            choice = input("Выберите пункт меню: ")


while True:
    # print(pb.meny())
    choice = main_meny()
    # while True:
    #     if choice.isdigit() and 0 < int(choice) <= len(pb.meny()):
    #
    #
    #
    #     else:
    #         print(f"Неверный пункт меню, введите от 1 до {len(pb.meny())}")
    #         choice = input("Выберите правильный пункт меню: ")

    match choice:
        case 1:
            print(pb)
        case 2:
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            comment = input("Введите комментарий: ")
            pb.new_contact(name, phone, comment)
        case 3:
            word = input("Поиск: ")
            print(pb.find_contact(word))
        case 4:
            print(pb)
            index = int(input("""Введите ID контакта, который хотите изменить
                                    Enter в случае если хотите оставить без изменений: """))
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            comment = input("Введите комментарий: ")
            print("")
            pb.change_contact(index - 1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input("Введите ID контакта, который хотите удалить: "))
            pb.delete_contact(index - 1)
        case 6:
            pb.save()
        case 7:
            break