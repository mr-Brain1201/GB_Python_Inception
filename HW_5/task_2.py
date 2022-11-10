# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

from random import shuffle, randint

all_amount = 120
max_sweet = 28
a = int(input('play PvP - 1 or PvB - 0?'))
players = ['pl_1', 'pl_2' if a else 'bot']
shuffle(players)
activ_player = players[0]
print(f'Первым ходит игрок {players[0]},вторым - {players[1]}')


def game_bot():
    result = all_amount % 29
    if not result:
        result = randint(1, 28)
    return result


def all_game(s):
    f_1, f_2 = players
    return f_2 if s == f_1 else f_1


def run_game(all_amount, max_sweet, activ_player):
    activ_player = activ_player
    while all_amount > 0:
        print(f'всего конфет {all_amount}, лимит - {max_sweet} ')
        if activ_player == 'bot':
            x = game_bot()
            print(f'бот взял {x} конфет')
        else:
            x = int(input(f' Сейчас конфеты берет  {activ_player}'))
        if x not in range(1, max_sweet + 1):
            print(f'неверный ввод(( прочтите правила!((')
        else:
            all_amount -= x
            if all_amount > 0:
                activ_player = all_game(activ_player)
            else:
                print(f' {activ_player}, вы победили!!!')


run_game(all_amount, max_sweet, activ_player)