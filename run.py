# Welcome to the TIC-TAC-TOE game!

board = [' ' for x in range(10)]


def display_board(board):
    """
    Displays the board in a more styles manner
    """
    print('      |     |')
    print('   ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('      |     |')
    print('-------------------')
    print('      |     |')
    print('   ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('      |     |')
    print('-------------------')
    print('      |     |')
    print('   ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('      |     |')


def check_move(letter, position):
    board[position] = letter


def available_space(position):
    return board[position] == ' '


def winning_combs(brd, let):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)


def board_spaces(board):
    if board.count(' ') > 1:
        return True
    else:
        return False


def player_move():
    execute = True
    while execute:
        user_input = input('Please select a number ranging from 1 to 9 to place the \'X\':\n')
        try:
            user_input = int(user_input)
            if user_input >= 1 and user_input <= 9:
                if available_space(user_input):
                    execute = False
                    check_move('X', user_input)
                else:
                    print('Space was already taken, try another space!')
            else:
                print('Please select a number bewtween 1 and 9!')
        except:
            print('Please type a number!')


def main():
    print('Welcome to the TIC-TAC-TOE game!')
    display_board(board)
    



main()
