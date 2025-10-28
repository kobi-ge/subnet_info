import random
import utils.in_ou as io,  utils.checks as c
import utils.creating as cr
import time

def calculate_ships_fires(board_size: tuple) -> tuple:
    level = input("choose difficulty level: \n1 for beginner \n2 for intermediate \n3 for top player. \n")
    spots = board_size[0] * board_size[1]
    match level:
        case 1 | "1":
            return int(spots * 0.12), int(spots * 0.7)
        case 2 | "2":
            return int(spots * 0.17), int(spots * 0.45)
        case 3 | "3":
            return int(spots * 0.2), int(spots * 0.33)
    return calculate_ships_fires(board_size)


def init_game():
    game_info = {
        "board_size": io.input_size(),
        "total_hits": 0,
        "is_shot": [],
    }

    ships_fires = calculate_ships_fires(game_info["board_size"])
    game_info["shots_amount"] = ships_fires[0]
    game_info["shots_remaining"] = game_info["shots_amount"]
    game_info["ships_amount"] = ships_fires[1]
    game_info["ships_remaining"] = game_info["ships_amount"]
    game_info["dev_board"] = cr.create_ships(cr.create_boards(game_info["board_size"], "dev"), game_info["ships_amount"])
    game_info["public_board"] = cr.create_boards(game_info["board_size"], "public")

    print("welcome to the submarines game!")
    print(f"this is our game's board: {game_info["public_board"]}")
    return game_info

def game():
    game_info = init_game()
    while True:
        shot = shooting_direction(game_info)
        game_info["shots_amount"] = subtract_fire(game_info["shots_amount"])
        if c.hit_or_miss(shot, game_info["dev_board"], game_info):
            update_hits(game_info["public_board"], shot, True)
            game_info["ships_remaining"] -= 1
            game_info["total_hits"] += 1
        else:
            update_hits(game_info["public_board"], shot, False)
        print(game_info["public_board"])
        print(game_info["shots_remaining"])

        if c.is_won(game_info):
            print("congratulations! you've won the game!.")
            return

        if c.is_lost(game_info):
            print("game over! you can replay anytime.")
            return


def print_status(state: dict):
    print(f"""
    Total ships: {state['total_ships']}
    Ships remaining: {state['ships_remaining']}
    Total shots: {state['total_shots']}
    Shots remaining: {state['shots_remaining']}
    Total hits: {state['total_hits']}
    Shots history: {state['is_shot']}
    -----------------
    """)


def update_hits(public_board: list, spot: tuple, hit: bool) -> list:
    outer_idx = int(spot[0])
    inner_idx = int(spot[1])
    if hit:
        public_board[outer_idx][inner_idx] = "v"
        print(f"success! here's the updated board.")
    else:
        public_board[outer_idx][inner_idx] = "x"
        print("oops, you missed. ")
    return public_board


def subtract_fire(fires):
    fires -= 1
    return fires

def shooting_direction(state: dict) -> tuple | None:
    shot_direction = tuple(input("enter 2 numbers separated by a comma, 1-10 for shooting directions. \n").split(","))
    if len(shot_direction) != 2:
        print("invalid input' try again")
        return shooting_direction(state)
    elif not c.in_bounds(state["board_size"], shot_direction):
        print("your directions are off board")
        return shooting_direction(state)
    elif shot_direction not in state["is_shot"]:
        return shot_direction
    return None





