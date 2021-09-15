# Welcome to the TIC-TAC-TOE game!

board = [' ' for x in range(10)]
"""
The board is list accessed using a for loop.
"""


def check_move(letter, position):
    """
    This function is an auxiliary function for player_move
    function that will insert the player chosen position onto the board.
    """
    board[position] = letter


def available_space(position):
    """
    This function is an auxiliary function for player_move that will
    check that the user choice can be inserted onto the chosen location.
    """
    return board[position] == ' '


def display_board(board):
    """
    Displays the board to the user using print statements
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


def winning_combs(brd, let):
    """
    This function checks for any possible combinations to ensure
    that if either the user or the ai get 3 in a line, the game ends.
    """
    return (brd[7] == let and brd[8] == let and brd[9] == let) or (brd[4] == let and brd[5] == let and brd[6] == let) or (brd[1] == let and brd[2] == let and brd[3] == let) or (brd[1] == let and brd[4] == let and brd[7] == let) or (brd[2] == let and brd[5] == let and brd[8] == let) or (brd[3] == let and brd[6] == let and brd[9] == let) or (brd[1] == let and brd[5] == let and brd[9] == let) or (brd[3] == let and brd[5] == let and brd[7] == let)


def board_spaces(board):
    """
    This function checks if there are any empty
    spaces remaining on the board
    """
    if board.count(' ') > 1:
        return False
    else:
        return True


def player_move():
    """
    This function record the player's input,
    converts it into an integer and then validates it to ensure the user
    inputs a number form 1 to 9, using a while loop and a try-except statement.
    """
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


def random_choice(list):
    """
    This in an auxiliary function for the ai_move function
    that will generate a random number using the python ramdom library.
    """
    import random
    length = len(list)
    range = random.randrange(0, length)
    return list[range]


def ai_move():
    """
    This function makes the move for the computer.
    First it will check if the computer can do a winning move,
    if not it will check to see if the player can make a winning move.
    If not it will check for available spaces in the corners,
    then the sides and lastly the middle.
    """
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letr in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letr
            if winning_combs(board_copy, letr):
                move = i
                return move

    check_corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            check_corners.append(i)

    if len(check_corners) > 0:
        move = random_choice(check_corners)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    check_sides = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            check_sides.append(i)

    if len(check_sides) > 0:
        move = random_choice(check_sides)

    return move


def main():
    """
    The main function prints the board and the welcome message,
    and uses a while loop to check for empty spaces and winning moves,
    if the game is a tie, if not the player and ai will take another turn.
    """
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
                check_move('O', move)
                print(f'The computer placed an O in {move}')
                display_board(board)
        else:
            print('You won the game! Congratulations!')
            break


main()


"""
This while loop is used to check if the user would like to play another game.
"""
while True:
    user_reply = input('Would you like to have another go? (Y/N):\n')
    if user_reply.lower() == 'y' or user_reply.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('----------------------------------------------------')
        main()
    else:
        break
