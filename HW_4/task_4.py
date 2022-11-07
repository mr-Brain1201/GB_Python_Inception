# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def get_rand_list(n: int) -> tuple:
    return tuple([randint(0, 100), n])


def make_str(exp, val, k):
    if exp == k:
        if val > 1:
            return f'{val} * x^{exp}'
        else:
            return f'x^{exp}'
    elif exp > 1:
        if val > 1:
            return f'{val} * x^{exp}'
        elif val == 1:
            return f'x^{exp}'
    elif exp == 1:
        if val > 1:
            return f'{val} * x'
        elif val == 1:
            return f'x'
    else:
        return f'{val}'


def set_degree_values(exp):
    # сначала создаем список членов
    list_of_members = [make_str(i, v, exp) for v, i in map(get_rand_list, range(exp, -1, -1))]
    # потом джойним их
    result = ' + '.join(list_of_members)
    print(result + ' = 0')
    with open("polynomials.txt", "a") as f:
        f.write(f'{result} \n')
        return result

set_degree_values(10)
