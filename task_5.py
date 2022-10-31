# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def negafib(k):
    lst = []
    for el in range(k + 1):
        if el > 1 and el % 2 == 0:
            next_num = lst[-2] + lst[-1]
            lst.append(next_num)
            lst.insert(0, -next_num)
        elif el > 1 and el % 2 == 1:
            next_num = lst[-2] + lst[-1]
            lst.append(next_num)
            lst.insert(0, next_num)
        elif el == 0:
            lst.append(el)
        else:
            lst.append(el)
            lst.insert(0, el)
    print(lst)

negafib(10)

