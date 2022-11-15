def print_board(board, size):
    print("\n")
    for i in range(size):
        print("\t", sep="", end="")
        print("          |" * (size - 1), sep="")
        for j in range(size):
            if j == size - 1:
                print("  {}  ".format("[" + board[i][j] + "]"), sep="")
                if i != (size - 1):
                    print("\t", sep="", end="")
                    print('__________|' * (size - 1), sep="", end="")
                    print('__________')
                elif i == (size - 1):
                    print("\t", sep="", end="")
                    print('          |' * (size - 1))
            else:
                if j == 0:
                    print("\t  {}   |".format("[" + board[i][j] + "]"), end="")
                else:
                    print("  {}   |".format("[" + board[i][j] + "]"), end="")
    print("\n")


def chose_cell_x():
    print("Enter column number", end=' ')


def chose_cell_y():
    print("Enter row number", end=' ')


def invalid_pos():
    print("ERROR!!\nThere is already content in the selected cell\nPlease chose another cell")


def invalid_cell():
    print("ERROR!!\nInvalid cell index\nPlease chose another cell")


def player_wins():
    print("The winner is: player")


def bot_wins():
    print("The winner is: bot")


def no_winners():
    print("nobody won\nthe game ended in a tie.")


def new_game():
    print("Enter n to start a new game or q to exit", end=' ')


def invalid_choice():
    print("Invalid choice")
