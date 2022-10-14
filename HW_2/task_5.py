# Реализуйте алгоритм перемешивания списка.

from random import randint

test_list = [randint(0, 20) for _ in range(100)]
print(test_list)


def shuffle_list(lst):
    ln = len(lst)
    result = []
    for i in range(ln):
        rand_indx = randint(0, ln - i - 1)
        result.append(lst[rand_indx])
        lst.pop(rand_indx)
    return result

print(shuffle_list(test_list))
