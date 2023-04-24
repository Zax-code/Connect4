from board import Game
from ai import ia_move

if __name__ == '__main__':
    my_board = Game(0, 0)
    win = False
    i = 0
    opponent_turn = False
    while not win:
        my_board.draw_board(i % 2)
        if opponent_turn:
            move = ia_move(my_board, 5)
            print('Computer plays column {}'.format(move+1))
            my_board.make_move(move)
            i += 1
            if my_board.check_win():
                print('You win!' if not opponent_turn else 'You lose!')
                win = True
                break
            opponent_turn = not opponent_turn
            continue
        while True:
            try:
                move = int(input('Enter a column: '))-1
                if not my_board.make_move(move):
                    print('Invalid move')
                    continue
                i += 1
                if my_board.check_win():
                    print('You win!' if not opponent_turn else 'You lose!')
                    win = True
                    break
                opponent_turn = not opponent_turn
                break
            except Exception:
                print('Invalid input')
                continue
    my_board.draw_board(i % 2)
