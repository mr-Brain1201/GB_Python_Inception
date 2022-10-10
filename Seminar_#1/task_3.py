n = int(input('Введите целое число: '))
if n > 0:
    print([x for x in range(-n, n + 1)])
else:
    print([x for x in range(n, -n + 1)])
