class Game:
    def __init__(self, board=0, player=0):
        self.board = board
        self.player = player
        self.chips = 6*7

    #Copy function
    def copy(self):
        return Game(self.board, self.player)


    def draw_board(self, turn=0):
        """
        Draws the board in the console.
        :param turn: 0 if it's the player's turn, 1 if it's the opponent's turn
        :return: None
        """
        player_chips = bin(self.player)[2:]
        player_chips = player_chips.zfill(48)[::-1]
        opponent = self.board ^ self.player
        opponent_chips = bin(opponent)[2:]
        opponent_chips = opponent_chips.zfill(48)[::-1]
        player_symbol, opponent_symbol = ('X', 'O') if turn else ('O', 'X')
        row = []
        print()
        for i in range(0, 6):
            row = []
            for j in range(0, 7):
                current = 5 - i + j*7
                if player_chips[current] == '1':
                    row.append(player_symbol)
                elif opponent_chips[current] == '1':
                    row.append(opponent_symbol)
                else:
                    row.append(' ')
            print('| ' + ' | '.join(row)+' |')
            print('|' + '|'.join('---' for _ in row) + '|')
        print('| ' + ' | '.join(str(i) for i, _ in enumerate(row, 1)) + ' |')
        print('|' + '|'.join('___' for _ in row) + '|')
        print('|'+' '*27+'|')
        print()

    def make_move(self, column):
        """
        Makes a move on the board.
        :param column: the column to make the move in the board
        :return: True if the move was successful, False otherwise
        """
        if column < 0 or column > 6 or self.board & (2**5 << 7*column) > 0:
            return False
        else:
            self.board = self.board | (self.board + (1 << 7*column))
            self.player = self.player ^ self.board
            self.chips -= 1
            return True

    def check_draw(self):
        """
        Checks if the game is a draw.
        :return: True if the game is a draw, False otherwise
        """
        return self.chips == 0

    def check_win(self):
        """
        Checks if the player has won.
        :return: True if the player has won, False otherwise
        """
        # Check for horizontal wins
        m = self.player & (self.player >> 7)
        if m & (m >> 14):
            return True

        # Check for vertical wins
        m = self.player & (self.player >> 6)
        if m & (m >> 12):
            return True

        # Check for diagonal wins
        m = self.player & (self.player >> 1)
        if m & (m >> 2):
            return True

        # Check for diagonal wins
        m = self.player & (self.player >> 8)
        if m & (m >> 16):
            return True

        return False
