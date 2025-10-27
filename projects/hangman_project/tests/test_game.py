# def init_state(secret: str, max_tries: int) -> dict:
#     game_info = {"secret": secret,
#                  "display": list[str],
#                  "guessed": set[str],
#                  "last_letter": str,
#                  "wrong_guesses": 0,
#                  "max_tries": max_tries}
#
#     return game_info
#
# print(init_state("hello", 3))

# def validate_guess(ch: str, guessed: set[str]) -> bool:
#     if ch not in guessed and len(ch) == 1:
#         return True
#     return False
#
# print(validate_guess("h", {"h", "e"}))
# def apply_guess(state: dict, ch: str) -> bool:
#     if ch in state["secret"] and ch not in state["guessed"]:
#         return True
#     return False
#
# print(apply_guess(di, "l"))

# def is_won(state: dict) -> bool:
#     if len(state["secret"]) == len(state["guessed"]):
#         return True
#     return False
# print(is_won(di))

# def is_lost(state: dict) -> bool:
#     if state["wrong_guesses"] >= state["max_tries"]:
#         return True
#     return False
# print(is_lost(di))
di = {"secret": "hello", "guessed": ["h", "e"], "wrong_guesses": 3, "max_tries": 3, "display": list[str]}

di["guessed"].append("f" * 3)
print(di)




# def render_display(state: dict, ch: str = None) -> str:
#     state["display"] = "_" * len(state["secret"])
#     for idx, value in enumerate(state["secret"]):
#         if value == ch:
#             state["display"][idx] = ch
#     return state["display"]
#
# print(render_display(di))
#
# def prompt_guess() -> str:
#     while True:
#         user_guess = input("enter your guess: \n").strip().lower()
#         if user_guess.isalpha():
#             return user_guess
#         print("invalid input, try again. \ninput must be a letter")
# print(prompt_guess())
