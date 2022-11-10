# Создайте программу для игры в ""Крестики-нолики"".
board = list(map(str, range(1, 10)))


def game_board():
    print("-" * 11)
    for i in range(3):
        for e in range(3):
            print(f'{board[e + i * 3]} |', end=' ')

        print('\n' + "-" * 11)


def enter_X0(y):
    global board
    while True:
        a = input('Выберете номер ячейки игрового поля от 1 до 9')
        if a.isdigit() and int(a) in range(1, 10):
            if board[int(a) - 1] not in 'X0':
                board[int(a) - 1] = 'X' if y == 'X' else '0'
                break
            else:
                print('поле занято!')
        else:
            print('некорректный ввод, попробуйте еще раз!')


def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main_game():
    count = 0
    game_board()
    while True:

        enter_X0('X') if count % 2 == 0 else enter_X0('0')
        count += 1
        game_board()
        if count > 4:
            tmp = check_win()
            if tmp:
                print(tmp, "выиграл!")
                break
        if count == 9:
            print('нет победителя!')
            break


main_game()