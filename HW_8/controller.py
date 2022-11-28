'''
Данный модуль используется для навигации по нашей программе
'''

from logging import log_write_json, log_read_json
from operation import result_write_json, result_search_json, result_delete_json, result_edit_json


def menu():
    '''
    Функция главного меню. Позволяет получить доступ к основному спеутру выполнения задач нашей программы.
    Ничего на вход не принимает и ничего не возвращает. Предназначена только для вызова функционала программы.
    :return: None
    '''
    while True:
        text = input('Добро пожаловать в баззу данных студентов, что хотите сделать? (добавить/удалить/найти/редактировать) '
                 'Для выхода из программы введите "esc": ')
        if text == 'добавить':
            input_student()
        elif text == 'найти':
            search_student()
        elif text == 'редактировать':
            edit_student()
        elif text == 'удалить':
            delete_student()
        elif text == 'esc':
            return
        else:
            print('Некорректный ввод!')


def input_student():
    '''
    Данная функция позволяет добавить новых студентов. На вход ничего не принимает и на выход не отдает.
    Считывает базу и присваивает очередной id новому студенту.
    :return: None
    '''
    if len(log_read_json()) == 0:   # если база пуста, то присваивает первой записи нулевой id
        count = 0
    else:
        key_id = list(log_read_json().keys())[-1] # если база не пуста - получает последний id и присваевает очередной
        count = int(key_id[2:]) + 1
    while input('Для выхода из ввода данных студентов введите "esc", для продолжения нажмите enter: ') != 'esc':
        result = result_write_json(count) # вызов функции создания новой записи в базе
        count += 1   # в случае добавления нескольких студентов сразу добавляет 1 к счетчику id
        log_write_json(result)  # запись обновленной базы в файл
    else:
        menu()


def search_student():
    '''
    Данная функция осуществляет вызов поиска по базе студентов. На вход ничего не принимает и на выход не отдает.
    :return: None
    '''
    while input('Для выхода из поиска данных студентов введите "esc", для продолжения нажмите enter: ') != 'esc':
        result_search_json()
    else:
        menu()


def delete_student():
    '''
    Данная функция осуществляет вызов удаления из базы студентов. На вход ничего не принимает и на выход не отдает.
    :return: None
    '''
    while input('Для выхода из удаления данных студентов введите "esc", для продолжения нажмите enter: ') != 'esc':
        result = result_delete_json() # удаление из базы
        log_write_json(result) # запись обновленной базы в файл
    else:
        menu()


def edit_student():
    '''
    Данная функция осуществляет вызов редактирования базы студентов. На вход ничего не принимает и на выход не отдает.
    :return: None
    '''
    while input('Для выхода из редактированя данных студентов введите "esc", для продолжения нажмите enter: ') != 'esc':
        result = result_edit_json() # редактирование базы
        log_write_json(result)  # запись обновленной базы в файл
    else:
        menu()