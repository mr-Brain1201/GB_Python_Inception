from export_contact import export_contact
from import_contact import import_contact # поржал с этого ипорта))
from input import input_func
from output import output


def tel_dict() -> None:
    while True:
        print('1 - добавление контакта\n'
              '2 - поиск контакта\n'
              '3 - импорт контактов\n'
              '4 - экспорт контактов')
        mode = int(input('Введите цифру от 1 до 4 для выбора режима работы и нажмите "Ввод" или введите "quit", '
                      'чтобы завершить работу: '))
        if mode == 1:
            input_func()
        elif mode == 2:
            cntct = input('Введите Имя/Фамилию/телефон: ')
            output(cntct)
        elif mode == 3:
            import_contact(input('Введите имя файла для импорта: '))
        elif mode == 4:
            export_contact()


if __name__ == "__main__":
    tel_dict()