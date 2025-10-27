
from hangman.words import choose_secret_word , words_list

from hangman import in_ou


def init_state(secret: str, max_tries: int) -> dict:
    game_info = {"secret": secret,
                 "display": list[str],
                 "guessed": [],
                 "wrong_guesses": 0,
                 "max_tries": max_tries}

    return game_info

def init_game():
    print("welcome to the hangman game!!!")

    while words_list:
        secret = choose_secret_word(words_list)
        word_length = len(secret)
        game_state = init_state(secret, 35)

        while not is_won(game_state):
            print(f"your word is: {render_display(game_state)}")
            user_guess = in_ou.prompt_guess()
            if validate_guess(user_guess, game_state["guessed"]):
                if apply_guess(game_state, user_guess):
                    count = secret.count(user_guess)
                    game_state["guessed"].append(user_guess * count)
                    print(render_display(game_state))
                    print(game_state["guessed"])
                else:
                    print("incorrect!")
                    game_state["wrong_guesses"] += 1
            else:
                print("invalid input! \nmake sure you enter a new letter and that it's only one letter")

            if is_lost(game_state):
                print("game over!! to many failed guesses")
                return

        print(f"well done! \nyou've guessed the word ({secret}), we're moving to the next word.")



def validate_guess(ch: str, guessed: set[str]) -> bool:
    if ch not in guessed and len(ch) == 1:
        return True
    return False

def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["secret"] and ch not in state["guessed"]:
        return True
    return False

def is_won(state: dict) -> bool:
    if len(state["secret"]) == len(list(state["guessed"])):
        return True
    return False

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    return False

def render_display(state: dict, ch: str = None) -> str:
    state["display"] = "_" * len(state["secret"])
    for idx, value in enumerate(state["secret"]):
        if value == ch:
            state["display"][idx] = ch
    return state["display"]

def render_summary(state: dict) -> str:
    return f" the secret word is: {state["secret"]}, you've guessed: {state["guessed"]}"

