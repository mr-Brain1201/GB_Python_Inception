# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec_to_bin(n: int) -> None:
    list_of_bit = []
    int_div = 0
    while (int_div > 3 or int_div == 0) and n > 3:
        if int_div != 0:
            list_of_bit.append(int_div % 2)
            int_div //= 2
        else:
            list_of_bit.append(n % 2)
            int_div = n // 2
    else:
        if n > 3:
            list_of_bit.append(int_div % 2)
            list_of_bit.append(1)
        else:
            list_of_bit.append(n % 2)
            list_of_bit.append(1)
    list_of_bit.reverse()
    list_of_bit = [str(x) for x in list_of_bit]
    print(''.join(list_of_bit))


dec_to_bin(10)