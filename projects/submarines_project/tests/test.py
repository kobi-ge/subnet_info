# game_info = {
#         "total_ships": 15,
#         "ships_remaining": 0,
#         "total_shots": 20,
#         "shots_remaining": 0,
#         "total_hits": 0,
#         "is_shot": []
#     }
#
#
# def is_won(state: dict) ->bool:
#     return not bool(state["ships_remaining"])
#
# def is_lost(state: dict) ->bool:
#     return not bool(state["shots_remaining"])
#
# print(is_lost(game_info))
#
# a = input("num")
# print(a)
# print(a.split(","))
import random
#
# def create_cells() -> list[list]:
#     game_board =[]
#     for i in range(board_size):
#         game_board.append([])
#         for j in range(board_size):
#             game_board[-1].append(0)
#
#     return game_board
#
#
# def create_ships(board: list[list]) -> list[list]:
#     ships = 0
#     while ships < ships_amount:
#         outer_idx = random.randint(0, 9)
#         inner_idx = random.randint(0, 9)
#         if board[outer_idx][inner_idx] == 1:
#             continue
#         board[outer_idx][inner_idx] = 1
#         ships += 1
#     return board
#
# print(create_ships(create_cells()))




# def shooting_direction(state: dict) -> tuple:
#     while True:
#         shot_direction = tuple(input("enter 2 numbers separated by a comma, 1-10 for shooting directions. \n").split(","))
#         if len(shot_direction) != 2:
#             print("invalid input' try again")
#         elif not in_bounds(state["board_size"] ,shot_direction):
#             print("your directions are off board")
#             continue
#         elif shot_direction not in state["is_shot"]:
#             return shot_direction
# def shooting_direction(state: dict) -> tuple:
#     res = tuple(input("enter 2 numbers separated by a comma, 1-10 for shooting directions. \n").split(","))
#     if not good:
#         print
#         return shooting_direction(state)
#     return res


