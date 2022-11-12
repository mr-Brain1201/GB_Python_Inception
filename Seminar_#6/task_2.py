my_list = [1, 2, 10, 2, 5, 7, 8, 10]

my_list_2 = [i for i in my_list if my_list.count(i) == 1]
print(my_list_2)