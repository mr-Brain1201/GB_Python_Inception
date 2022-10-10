'''Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''


def quart_defin(x, y):
    if x == 0 or y == 0:
        print('Координата не принадлежит ни одной четверти - она находится на оси!')
    elif x > 0 and y > 0:
        print('Координата принадлежит I четверти')
    elif x < 0 and y > 0:
        print('Координата принадлежит II четверти')
    elif x < 0 and y < 0:
        print('Координата принадлежит III четверти')
    else:
        print('Координата принадлежит IV четверти')


quart_defin(float(input('Введите координату по оси оX; ')), float(input('Введите координату по оси оY; ')))