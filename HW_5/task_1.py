# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def some_text(text):
    return " ".join([i for i in text.split() if 'абв' not in i])


print(some_text(input()))