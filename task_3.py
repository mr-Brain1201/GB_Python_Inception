# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной
# части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def maxmin_dec_part(lst: list) -> tuple:
    max_dec_part = None
    min_dec_part = None
    for el in lst:
        if max_dec_part is None:
            max_dec_part = el
            min_dec_part = el
        else:
            if el >= max_dec_part:
                max_dec_part = el
            if el <= min_dec_part and el != 0:
                min_dec_part = el
    return max_dec_part, min_dec_part


def diff_maxmin_dec_part(lst: list) -> None:
    list_dec_part = []
    for el in lst:
        list_dec_part.append(el % 1)
    max, min = maxmin_dec_part(list_dec_part)
    print(f'Разница между максимальной и минимальной'
          f' дробной частью чисел в списке составляет {max - min :.2f}')


diff_maxmin_dec_part([1.1, 1.2, 3.1, 5, 10.01])
