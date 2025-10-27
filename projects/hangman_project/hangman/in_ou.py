from hangman import words
def prompt_guess() -> str:
    while True:
        user_guess = input("enter your guess: \n").strip().lower()
        if user_guess.isalpha():
            return user_guess
        print("invalid input, try again. \ninput must be a letter")

def print_status(state: dict) -> None:
    print(state)

def print_result(state: dict) -> None:
    return


