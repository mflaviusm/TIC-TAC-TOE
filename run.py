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
    return (brd[7] == let and brd[8] == let and brd[9] == let) or (brd[4] == let and brd[5] == let and brd[6] == let) or (brd[1] == let and brd[2] == let and brd[3] == let) or (brd[1] == let and brd[4] == let and brd[7] == let) or (brd[2] == let and brd[5] == let and brd[8] == let) or (brd[3] == let and brd[6] == let and brd[9] == let) or (brd[1] == let and brd[5] == let and brd[9] == let) or (brd[3] == let and brd[5] == let and brd[7] == let)


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


def ai_move():
    pass


def main():
    print('Welcome to the TIC-TAC-TOE game!')
    display_board(board)

    while not(board_spaces(board)):
        if not(winning_combs(board, 'O')):
            player_move()
            display_board(board)
        else:
            print('Game was won by the computer. Better luck next time!')
            break

        if not(winning_combs(board, 'X')):
            move = ai_move()
            if move == 0:
                print('Game is Tie! Better luck next time!')
            else:
                check_move('O', board)
                print(f'The computer placed an O in {move}')
        else:
            print('You won the game! Congratulations!')
            break
    if board_spaces(board):
        print('Game is Tie! Better luck next time!')


main()
