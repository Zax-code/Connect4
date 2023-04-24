from board import Game


def minmax(game: Game, opponent_turn: bool = False, depth: int = 5, move: int = -1):
    game_copy = game.copy()
    if game_copy.check_win():
        return float('inf') if opponent_turn else -float('inf')
    if game_copy.check_draw():
        return 0
    if depth == 0:
        return heuristic(game_copy, opponent_turn)
    if opponent_turn:
        moves = []
        for m in range(7):
            if game_copy.make_move(m):
                moves.append(
                    minmax(game_copy, not opponent_turn, depth - 1, m))
            game_copy = game.copy()
        return min(moves)
    else:
        moves = []
        for m in range(7):
            if game_copy.make_move(m):
                moves.append(
                    minmax(game_copy, not opponent_turn, depth - 1, m))
            game_copy = game.copy()
        return max(moves)


def ia_move(game: Game, depth):
    game_copy = game.copy()
    moves = {}
    for m in range(7):
        if game_copy.make_move(m):
            moves[m] = minmax(game_copy, True, depth, m)
        game_copy = game.copy()
    return max(moves.keys(), key=lambda k: moves[k])


def heuristic(game: Game, opponent_turn: bool = False):
    two_aligned = 0
    three_aligned = 0
    board = game.board

    player = game.player
    if opponent_turn:
        player = board ^ game.player

    two_aligned += bin(player & (player >> 7)).count('1')
    two_aligned += bin(player & (player >> 1)).count('1')
    two_aligned += bin(player & (player >> 8)).count('1')
    two_aligned += bin(player & (player >> 6)).count('1')
    three_aligned += bin(player & (player >> 7) & (player >> 14)).count('1')
    three_aligned += bin(player & (player >> 1) & (player >> 2)).count('1')
    three_aligned += bin(player & (player >> 8) & (player >> 16)).count('1')
    three_aligned += bin(player & (player >> 6) & (player >> 12)).count('1')

    return two_aligned + three_aligned * 10


def alphabeta(game: Game):
    pass
