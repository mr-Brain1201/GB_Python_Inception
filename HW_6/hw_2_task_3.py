#     Задайте список из n чисел последовательности $(1+1/n)^n$ и выведите на экран их сумму.
#
#     Пример:
#
# - Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
# Решил сделать чуть более универсальное решение, часть которого можно импортировать для решения задач
# создания других последовательностей))


# def subsequence(n, func):
#     result = []
#     for el in range(1, n + 1):
#         result.append(round(func(el), 3))
#     print(result)
#
#
# def task_func(n):
#     return (1 + 1 / n) ** n
#
#
# subsequence(int(input('Введите целое число: ')), task_func)

n = int(input('Введите целое число: '))
f = list(map(lambda x: round((1 + 1 / x) ** x, 3), [el for el in range(1, n + 1)]))
print(f)

