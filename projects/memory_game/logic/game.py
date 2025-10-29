import utils.in_ou as io, random, utils.checkings as c
from timeit import default_timer as timer

def create_game_board(size: int) -> list[list]:
    game_board = []
    for row in range(size):
        game_board.append([])
    return game_board

def create_cards(size: int) -> list:
    pairs = int(size * size / 2)
    pairs_list = []
    for card in range(pairs):
        pair = [card + 1, card + 1]
        pairs_list.extend(pair)
    return pairs_list

def shuffle(pairs_list: list) -> list:
        random.shuffle(pairs_list)
        return pairs_list

def insert_cards(game_board: list[list], cards: list) -> list[list]:
    cards_idx = 0
    for row in range(len(game_board)):
        for card in range(len(game_board)):
            game_board[row].append(cards[cards_idx])
            cards_idx += 1
    return game_board

def create_public_board(size: int) -> list[list]:
    public_list = []
    for row in range(size):
        public_list.append([])
        for val in range(size):
            public_list[row].append("x")
    return public_list

def game_state(size: int) -> dict:
    game_info = {
        "board_size": size,
        "start_time":None,
        "end_time": None,
        "game_board": None,
        "steps": 0,
        "pairs_amount": size * size / 2,
        "pairs_revealed": 0,
        "revealed_cards_idx": [],
        "public_board": None
    }
    return game_info

def cards_reveal(game_board: list[list], card_1: tuple, card_2: tuple) -> tuple:
    cards = (game_board[card_1[0]][card_1[1]], game_board[card_2[0]][card_2[1]])
    print(cards)
    return cards

def update_public_board(public_board: list[list],  cards: tuple, card_1: tuple, card_2: tuple) -> list[list]:
    public_board[card_1[0]][card_1[1]] = cards[0]
    public_board[card_2[0]][card_2[1]] = cards[1]
    return public_board

def init_game():
    board_size = io.choose_amount()
    game_info = game_state(board_size)
    game_info["game_board"] = create_game_board(board_size)
    cards_list = shuffle(create_cards(board_size))
    insert_cards(game_info["game_board"], cards_list)
    game_info["public_board"] = create_public_board(board_size)
    return game_info

def game_loop(game_info: dict):
    while True:
        io.print_public_board(game_info["public_board"])
        game_info["start_time"] = timer()
        cards_idx = io.picking_cards(game_info["board_size"])
        game_info["steps"] += 1
        if c.was_not_revealed(game_info, cards_idx[0]):
            pass
        if c.was_not_revealed(game_info, cards_idx[1]):
            pass
        if c.in_bounds(cards_idx, game_info["board_size"]):
            pass
        else:
            return "invalid input"

        cards = cards_reveal(game_info["game_board"], cards_idx[0], cards_idx[1])

        if c.check_cards_match(cards):
            update_public_board(game_info["public_board"], cards, cards_idx[0], cards_idx[1])
            game_info["revealed_cards_idx"].append(cards_idx)
            game_info["pairs_revealed"] += 1
        else:
            print("oops, cards do not match!")

        if c.is_won(game_info):
            game_info["end_time"] = timer() - game_info["start_time"]
            print("congratulations!!! you've won the game!")
            io.print_status(game_info)







