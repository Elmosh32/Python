import ui


def create_game(size):
    board = create_board(size)
    run_game(board, size)
    ui.new_game()
    start_new_game = input()
    if start_new_game == 'n':
        create_game(4)
    elif start_new_game != 'q':
        while True:
            ui.invalid_choice()
            ui.new_game()
            start_new_game = input()
            if start_new_game == 'n':
                create_game(size)
            elif start_new_game == 'q':
                break


def run_game(board, size):
    round = 0
    ui.print_board(board, size)

    while (True):
        player_turn(board, size)
        round += 1
        ui.print_board(board, size)

        if round >= (size + (size - 1)):
            if winner(board, size) == True:
                break

        if round == (size * size):
            ui.no_winners()
            break

        bot_turn(board, round, size)
        round += 1
        ui.print_board(board, size)

        if round == (size * size):
            ui.no_winners()
            break

        if round >= (size + (size - 1)):
            if winner(board, size) == True:
                break


def create_board(num):
    board = [[str(y) + "|" + str(x) for x in range(num)] for y in range(num)]
    return board


def bot_turn(board, round, size):
    length = len(board)

    if round == 1:
        if center(board, size) == True:
            return

    if almost_full_line_of_o(board, length, size) == True:
        return

    if almost_full_line_of_x(board, length, size) == True:
        return

    if size == 3:
        if three_cells(board, length, round) == True:
            return

    if corners_and_center(board, size) == True:
        return

    any_cell(board, length)


def center(board, size):
    if size % 2 == 1:
        mid = int(size / 2)
        if board[mid][mid] != ' X ':
            board[mid][mid] = ' O '
            return True
    else:
        for i in range(1, size - 2):
            for j in range(1, size - 2):
                if board[i][j] != ' X ' and board[i][j] != ' O ':
                    board[i][j] = ' O '
                    return True
    return False


def three_cells(board, length, round):
    if round == 3 and board[1][1] == ' O ':
        for i in range(length):
            if board[0][0] == ' X ' and board[2][2] == ' X ':
                board[0][2] = ' O '
                return True
            if board[1][0] == ' X ' and board[1][2] == ' X ':
                board[0][2] = ' O '
                return True
            if board[2][0] == ' X ' and board[0][2] == ' X ':
                board[0][0] = ' O '
                return True
            if board[0][1] == ' X ' and board[2][1] == ' X ':
                board[0][0] = ' O '
                return True
        return False


def any_cell(board, length):
    for i in range(length):
        for j in range(length):
            if board[i][j] != ' O ' and board[i][j] != ' X ':
                board[i][j] = ' O '
                return


def corners_and_center(board, size):
    if center(board, size) == True:
        return True
    if board[0][size - 1] != ' O ' and board[0][(size - 1)] != ' X ':
        board[0][size - 1] = ' O '
        return True
    if board[0][0] != ' O ' and board[0][0] != ' X ':
        board[0][0] = ' O '
        return True
    if board[(size - 1)][0] != ' O ' and board[size - 1][0] != ' X ':
        board[size - 1][0] = ' O '
        return True
    if board[size - 1][size - 1] != ' O ' and board[size - 1][size - 1] != ' X ':
        board[size - 1][size - 1] = ' O '
        return True
    return False


def almost_full_line_of_x(board, length, size):
    bool, x, y = check_rows(board, length, ' X ', size)
    if x is not None and y is not None and board[x][y] != ' X ' and board[x][y] != ' O ':
        board[x][y] = ' O '
        return True

    bool, x, y = check_cols(board, length, ' X ', size)
    if x is not None and y is not None and board[x][y] != ' X ' and board[x][y] != ' O ':
        board[x][y] = ' O '
        return True

    bool, x, y = check_diagonals(board, length, ' X ', size)
    if x is not None and y is not None and board[x][y] != ' X ' and board[x][y] != ' O ':
        board[x][y] = ' O '
        return True

    return False


def almost_full_line_of_o(board, length, size):
    bool, x, y = check_rows(board, length, ' O ', size)
    if x is not None and y is not None and board[x][y] != ' X ' and board[x][y] != ' O ':
        board[x][y] = ' O '
        return True

    bool, x, y = check_cols(board, length, ' O ', size)
    if x is not None and y is not None and board[x][y] != ' X ' and board[x][y] != ' O ':
        board[x][y] = ' O '
        return True

    bool, x, y = check_diagonals(board, length, ' O ', size)
    if x is not None and y is not None and board[x][y] != ' X ' and board[x][y] != ' O ':
        board[x][y] = ' O '
        return True

    return False


def player_turn(board, size):
    ui.chose_cell_x()
    x = int(input())
    ui.chose_cell_y()
    y = int(input())
    if x > (size - 1) or x < 0 or y > (size - 1) or y < 0 or board[x][y] == ' X ' or board[x][y] == ' O ':
        while True:
            if x > (size - 1) or x < 0 or y > (size - 1) or y < 0:
                ui.invalid_cell()
                ui.chose_cell_x()
                x = int(input())
                ui.chose_cell_y()
                y = int(input())
            elif board[x][y] == ' X ' or board[x][y] == ' O ':
                ui.invalid_pos()
                ui.chose_cell_x()
                x = int(input())
                ui.chose_cell_y()
                y = int(input())
            else:
                break

    board[x][y] = ' X '


def winner(board, size):
    length = len(board)
    win1, temp, temp = check_rows(board, length, ' X ', size)
    win2, temp, temp = check_cols(board, length, ' X ', size)
    win3, temp, temp = check_diagonals(board, length, ' X ', size)
    if win1 or win2 or win3:
        ui.player_wins()
        return True

    win1, temp, temp = check_rows(board, length, ' O ', size)
    win2, temp, temp = check_cols(board, length, ' O ', size)
    win3, temp, temp = check_diagonals(board, length, ' O ', size)
    if win1 or win2 or win3:
        ui.bot_wins()
        return True
    return False


def check_rows(board, board_len, ch, size):
    ret_x = None
    ret_y = None
    counter = 0

    for i in range(board_len):

        win = True
        counter = 0
        for j in range(board_len):
            if board[i][j] != ch:
                win = False
                x, y = i, j
            else:
                counter += 1
        if counter == (size - 1):
            ret_x, ret_y = x, y
        if win == True:
            return True, None, None

    return False, ret_x, ret_y


def check_cols(board, board_len, ch, size):
    ret_x = None
    ret_y = None

    for i in range(board_len):
        win = True
        counter = 0
        for j in range(board_len):
            if board[j][i] != ch:
                win = False
                x, y = j, i
            else:
                counter += 1
        if counter == (size - 1):
            ret_x, ret_y = x, y
        if win == True:
            return True, None, None
    return False, ret_x, ret_y


def check_diagonals(board, board_len, ch, size):
    counter = 0
    win = True
    for i in range(board_len):
        if board[i][i] != ch:
            win = False
            x, y = i, i
        else:
            counter += 1
    if win == True:
        return True, None, None

    if counter == (size - 1):
        ret_x, ret_y = x, y
    else:
        ret_x, ret_y = None, None

    counter = 0
    win = True
    for i in range(board_len):
        if board[i][board_len - 1 - i] != ch:
            win = False
            x, y = i, board_len - 1 - i
        else:
            counter += 1
    if win == True:
        return True, None, None

    if counter == (size - 1):
        ret_x, ret_y = x, y

    return False, ret_x, ret_y
