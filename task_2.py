# Напишите программу, которая найдёт
# произведение пар чисел списка. Парой считаем
# первый и последний элемент, второй и
# предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mul_of_pair_num(lst: list) -> None:
    list_mul = []
    num_pair = int((len(lst) / 2) + 0.5)
    for el in range(num_pair):
        list_mul.append(lst[el] * lst[-el - 1])
    print(f'Список произведения парных элементов: {list_mul}')

mul_of_pair_num([2, 3, 5, 6])
