# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого
# Примеры:
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет
#
a = int(input('введите а'))
b = int(input('введите b'))


def valid_square(a, b):
    if a > b:
        b, a = a, b
    val = a**2 == b
    return print(val)


valid_square(a, b)

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

def max_val(list):
    max = None
    for el in list:
        if max == None:
            max = el
        elif el > max:
            max = el
    return print(max)

max_val([78, 55, 36, 90, 2])


