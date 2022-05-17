# Tik Tac Toe Game

def example_board():
    print('1|2|3')
    print('-----')
    print('4|5|6')
    print('-----')
    print('7|8|9')


def choose_piece():
    piece = ''
    while piece not in ['X', 'x', 'O', 'o']:
        piece = input('PLayer 1, do you want X\'s or O\'s?: ')
        if piece not in ['X', 'x', 'O', 'o']:
            print('Please enter either X or O.\n')
        else:
            pass
    return piece


def player_choice(player, check_list):
    choice = ''
    while choice.isdecimal() is False:
        choice = input(f'{player}, please select the square you want (1-9): ')
        if choice.isdecimal() is True:
            int_choice = int(choice)
            if int_choice in range(1, 10):
                if int_choice not in check_list:
                    check_list.append(int_choice)
                    return int_choice, check_list
                else:
                    choice = ''
                    print('Error: That square has already been chosen')
            else:
                choice = ''
                print('Error: Please enter an integer between 1 and 9')
        else:
            print('Error: Please enter an integer between 1 and 9')


def update_board(game_board, choice, piece):
    index = choice - 1
    game_board[index] = piece

    print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
    print('-----')
    print(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
    print('-----')
    print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])
    print()


def win_check(board, piece):
    if board[0] == board[1] == board[2] == piece:
        return True
    elif board[3] == board[4] == board[5] == piece:
        return True
    elif board[6] == board[7] == board[8] == piece:
        return True
    elif board[0] == board[3] == board[6] == piece:
        return True
    elif board[1] == board[4] == board[7] == piece:
        return True
    elif board[2] == board[5] == board[8] == piece:
        return True
    elif board[0] == board[4] == board[8] == piece:
        return True
    elif board[2] == board[4] == board[6] == piece:
        return True
    elif ' ' not in board:
        return True
    return False


def main():
    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    choice_list = []
    p1_piece = choose_piece().upper()
    if p1_piece == 'X':
        p2_piece = 'O'
    else:
        p2_piece = 'X'

    print(f'Okay Player 1, you will be {p1_piece}\'s.')
    print(f'Player 2, you will be {p2_piece}\'s.\n')

    print('Player 1, you will go first.')
    print('Here is how the board is laid out:')
    example_board()
    print()

    player = 'Player 1'
    piece = p1_piece
    square_choice, choice_list = player_choice(player, choice_list)
    update_board(game_board, square_choice, piece)
    print()

    print('Player 2 it\'s your turn.')
    player = 'Player 2'
    piece = p2_piece
    square_choice, choice_list = player_choice(player, choice_list)
    update_board(game_board, square_choice, piece)

    winner = False
    while winner is False:
        if player == 'Player 1':
            player = 'Player 2'
            piece = p2_piece
        elif player == 'Player 2':
            player = 'Player 1'
            piece = p1_piece

        square_choice, choice_list = player_choice(player, choice_list)
        print(choice_list)
        update_board(game_board, square_choice, piece)
        winner = win_check(game_board, piece)
        if (winner is True) and (' ' not in game_board):
            print('No more spaces left, it\'s a draw!\n')
        elif winner is True:
            print(f'Congrats {player} you win!\n')
        else:
            pass

    repeat = ''
    while repeat not in ['Y', 'y', 'N', 'n']:
        repeat = input('Would you like to play another game? (Y/N): ')
        if repeat not in ['Y', 'y', 'N', 'n']:
            print('Error: Not a valid in put, please enter (Y/N)')
        elif repeat in ['Y', 'y']:
            main()
        elif repeat in ['N', 'n']:
            print('Okay, goodbye!')
            break
        else:
            pass


if __name__ == '__main__':
    main()
