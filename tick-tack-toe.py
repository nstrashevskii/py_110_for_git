# крестики-нолики на двоих, поле 3Х3

# рисуем поле

board = list(range(1, 10))


def paint_board(board):
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')


# функция проверки корректности ввода

def input_my(play_symbol):
    s = input(f'Куда поставить {play_symbol}:\n')
    while s.isdigit() is False or (int(s) <= 0 or int(s) > 9):
        s = input(f'Не верно. Введите число от 1 до 9:\n')
    else:
        s = int(s)
    return s


# ход игрока


def play_step(play_symbol):
    result = False
    while not result:
        step = input_my(play_symbol)
        if str(board[step - 1]) not in 'XO':
            board[step - 1] = play_symbol
            result = True
        else:
            print(f'Клетка занята')


# проверка победы


def win_chek(board):
    win_board = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_board:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

# сама игра


def main(board):
    counter = 0
    win = False
    while not win:
        paint_board(board)
        if counter % 2 == 0:
            play_step("X")
        else:
            play_step("O")
        counter += 1
        if counter > 4:
            chek = win_chek(board)
            if chek:
                print(chek, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    paint_board(board)


if __name__ == '__main__':

    main(board)
