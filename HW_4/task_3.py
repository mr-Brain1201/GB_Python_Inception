# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

def my_set(number_list: list) -> list:
    count_dict = dict()
    for item in number_list:
        if not count_dict.get(item):
            count_dict[item] = 1
        else:
            count_dict[item] += 1

    res_lst = []
    for k, v in count_dict.items():
        if v == 1:
            res_lst.append(k)

    print(res_lst)
    return res_lst

lst = [2, 4, 34, 3, 2, 16, 34, 3]
my_set(lst)