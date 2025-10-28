import random
def create_boards(user_size: tuple, owner) -> list[list]:
    if owner == "dev":
        value = 0
    else:
        value = "o"
    game_board = []
    for i in range(user_size[0]):
        game_board.append([])
        for j in range(user_size[1]):
            game_board[-1].append(value)
    return game_board


def create_ships(board: list[list[int]], ships_amount: int) -> list[list[int]]:
    board_size_x = len(board)
    board_size_y = len(board[0])
    ships = 0
    while ships < ships_amount:
        outer_idx = random.randint(0, board_size_x - 1)
        inner_idx = random.randint(0, board_size_y - 1)
        if board[outer_idx][inner_idx] == 1:
            continue
        board[outer_idx][inner_idx] = 1
        ships += 1
    return board


def crate_random_ships(state_game):
    for x, y in random.sample(
            [(i, j) for i in range(state_game['board_size'][0]) for j in range(state_game['board_size'][1])],
            state_game['ships_amount']):
        state_game['board'][x][y] = 1