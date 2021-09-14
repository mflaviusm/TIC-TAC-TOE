#Welcome to the TIC-TAC-TOE game!

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


def main():
    print('Welcome to the TIC-TAC-TOE game!')
    display_board(board)

main()