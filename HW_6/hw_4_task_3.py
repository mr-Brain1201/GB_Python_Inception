

# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

def my_set(number_list: list) -> list:
    count_dict = dict()
    for item in number_list:
        if not count_dict.get(item):
            count_dict[item] = 1
        else:
            count_dict[item] += 1

    # res_lst = []
    # for k, v in count_dict.items():
    #     if v == 1:
    #         res_lst.append(k)

    res_lst = list(filter(lambda x: x if count_dict[x] == 1 else None, list([x[0] for x in count_dict.items()])))
    # да, четыре строки заменил одной, но меня одолевают смешанные ощущения, глядя на нее))
    print(res_lst)
    return res_lst

lst = [2, 4, 34, 3, 2, 16, 34, 3]
my_set(lst)
