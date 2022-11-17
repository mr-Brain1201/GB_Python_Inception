def get_search_list() -> tuple:
    search_lst = []
    while True:
        mode = input('чтобы добавить контакт на экспорт нажмите Ввод, чтобы завершить добавление нажмите "q": ')
        if mode == '':
            contact = input('Введите Имя/Фамилию/телефон контакта, который хотим экспортировать: ')
            search_lst.append(contact)
        elif mode == "q":
            break
    return tuple(search_lst)


def export_contact() -> None:
    format_file = input('Чтобы записать файл с разделителем "," введите ",", '
                        'чтобы выбрать разделителем "-", введите "-": ')
    list_contacts = []
    lst = get_search_list()
    with open("telephone_dictionary.csv", "r") as f1:
        for line in f1:
            contact = tuple(line.split(','))
            for el in lst:
                if el in contact:
                    list_contacts.append(contact)
    with open('export_contact.csv', "a") as f2:
        for contact in list_contacts:
            f2.write(f"{format_file.join(contact)}")