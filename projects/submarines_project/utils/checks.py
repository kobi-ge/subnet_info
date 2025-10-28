def in_bounds(user_size: tuple, directions: tuple) -> bool:
    return user_size[0] > int(directions[0]) and user_size[1] > int(directions[1])


def hit_or_miss(spot: tuple, ships: list, state: dict) -> bool:
    outer_idx = int(spot[0])
    inner_idx = int(spot[1])
    if ships[outer_idx][inner_idx]:
        state["is_shot"].append((outer_idx, inner_idx))
        return True
    return False


def is_won(state: dict) -> bool:
    return not bool(state["ships_remaining"])


def is_lost(state: dict) -> bool:
    return not bool(state["shots_remaining"])