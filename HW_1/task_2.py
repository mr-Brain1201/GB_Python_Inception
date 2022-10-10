'''Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''


bool_list = [0, 1]
result = []

for x in bool_list:
    for y in bool_list:
        for z in bool_list:
            left = not (x or y or z)
            right = (not x) and (not y) and (not z)
            result.append(left == right)

print(result)
if len(result) == result.count(1):
    print('Выражение верно при любых значениях предикатов')

# Вариант 2 без вложенности


from itertools import product

combination = [x for x in product([0, 1], repeat=3)]
result_ = []
for el in combination:
    left = not (el[0] or el[1] or el[2])
    right = (not el[0]) and (not el[1]) and (not el[2])
    result_.append(left == right)
print(result_)

if len(result_) == result_.count(1):
    print('Выражение верно при любых значениях предикатов')