#     Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
#     Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(n):
    fctr = 1
    if n < 0:
        return str('Факториал определен только на неотрицательных целых числах')
    elif n == 0:
        return fctr
    else:
        for el in range(1, n + 1):
            fctr *= el
        return fctr


def init_list_fctr(N):
    list_fctr = []
    for el in range(1, N + 1):
        list_fctr.append(factorial(el))
    if list_fctr == []:
        list_fctr.append(factorial(N))
    print(list_fctr)


init_list_fctr(int(input('Введите целое неотрицательное число: ')))
