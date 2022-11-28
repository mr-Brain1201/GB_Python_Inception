a = '1 + 22 * 4 / 3'

num = a.split()
operand = [i for i in num if i.isdigit()]
operation = [i for i in num if i in ['+', '-', '*', '/']]
print(operand)

priority = [i for i, el in enumerate(operation) if el in ['*', '/']]


print(priority)