'''Напишите программу, которая по заданному номеру четверти, показывает
 диапазон возможных координат точек в этой четверти (x и y).'''


dict_quart = {1: 'x - (0, +inf), y - (0, +inf)',
              2: 'x - (0, -inf), y - (0, +inf)',
              3: 'x - (0, -inf), y - (0, -inf)',
              4: 'x - (0, +inf), y - (0, -inf)'}


def coord_quart(n, dict_quart):
    if n in [x for x in range(1, 5)]:
        print(f'Координаты {n} четверти лежат в пределах {dict_quart.get(n)}')
    else:
        print('Введите номер четверти от 1 до 4!')


coord_quart(int(input('Введите номер четверти: ')), dict_quart)