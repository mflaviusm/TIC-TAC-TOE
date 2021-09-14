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


def player_move():
    correct = True
    while correct:
        move = input('Please select a number ranging from 1 to 9 to place the \'X\':\n')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if available_space(move):
                    correct = False
                    check_move('X', move)
                else:
                    print('Space was already taken, try another space!')
            else:
                print('Please select a number bewtween 1 and 9!')
        except:
            print('Please type a number!')


def main():
    print('Welcome to the TIC-TAC-TOE game!')
    display_board(board)
    player_move()


main()
