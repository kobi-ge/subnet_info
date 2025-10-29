from timeit import default_timer as timer
def choose_amount() -> int:
    user_size = input("hi! how many cards would you like? \npick a number, 4 for 4*4 etc. "
                      "bare in mind that there should be at least 2 pairs! \nand the number must be even. \n")
    if user_size.isdigit() and int(user_size) >= 2:
        return int(user_size)
    return choose_amount()
def print_public_board(public_board: list[list]):
    print(public_board)

def picking_cards(size: int):
    print(f"picking cards: \nplease follow the following rules: \n"
                            f"1: it cannot be greater than {size - 1}. \n2: it cannot be"
                            f"number of a card that is already open.\n")
    card_1_pick = tuple(input("for the first card: enter two digits separated by a comma. \n").split(","))
    card_1_pick = (int(card_1_pick[0]), int(card_1_pick[1]))
    card_2_pick = tuple(input("for the second card: enter two digits separated by a comma. \n").split(","))
    card_2_pick = (int(card_2_pick[0]), int(card_2_pick[1]))
    return card_1_pick, card_2_pick

def print_status(game_info: dict):
    print(game_info)







