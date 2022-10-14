# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных
# позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


def subsequence(n):
    result = []
    with open("file.txt", "w") as f:
        for el in range(1, n + 1):
            result.append(randint(- n, n))
            f.write(f'{el-1}\n')
    print(result)
    return result


def get_list_index():
    list_indx = []
    with open("file.txt", "r") as f:
        for line in f:
            list_indx.append(int(line))
    return list_indx


def mul_num(len_list, rand_list, list_subseq):
    random_indx = [randint(0, len_list) for _ in range(rand_list)]
    print(random_indx)
    list_indx = get_list_index()
    list_rand_item = [list_indx[x] for x in random_indx]
    rand_item = [list_subseq[x] for x in list_rand_item]
    # Руки чешутся здесь сделать через reduce)))
    result = 1
    for el in rand_item:
        result *= el
    print(result)


LEN_LIST = int(input('Введите длину списка: '))
LEN_RAND_LIST = int(input('Введите количество множителей: '))
subseq = subsequence(LEN_LIST)
mul_num(LEN_LIST, LEN_RAND_LIST, subseq)
