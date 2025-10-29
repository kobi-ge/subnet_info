def in_bounds(nums: tuple, size: int) -> bool:
    return nums[0][0] <= size-1 and nums[0][1] <= size-1 and nums[1][0] <= size-1 and nums[1][1] <= size-1

def was_not_revealed(game_info: dict, card: tuple) -> bool:
    return card not in game_info["revealed_cards_idx"]

def check_cards_match(cards: tuple) -> bool:
    return cards[0] == cards[1]

def is_won(game_info: dict) -> bool:
    return game_info["pairs_revealed"] == game_info["pairs_amount"]

