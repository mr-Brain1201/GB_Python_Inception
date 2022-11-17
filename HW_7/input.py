def input_contact() -> tuple:
    list_data = []
    list_questions = ["Введите фамилию: ", "Введите имя: ",
                      "Введите номер телефона", "Введите описание: "]
    for question in list_questions:
        list_data.append(input(f'{question}'))
    return tuple(list_data)


def input_func() -> None:
    while True:
        inp = input("Чтобы добавить контакт - нажмите 'Enter', "
                    "чтобы завершить добавление контактов введите 'q' или 'quit': ")
        if inp == '':
            contact = input_contact()
            with open("telephone_dictionary.csv", "a") as f:
                f.write(f"{','.join(contact)}\n")
        elif inp in ('q', 'quit'):
            break

