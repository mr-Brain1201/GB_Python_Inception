#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
#     Пример:
#
# - 6782 -> 23
# - 0,56 -> 11


def sum_numbers(num):
    sum_of_num = 0
    for el in str(num):
        if el.isdigit():
            sum_of_num += int(el)
    print(sum_of_num)


sum_numbers(float(input('Введите вещественное число: ')))