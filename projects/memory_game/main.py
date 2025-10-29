import logic.game as g
import utils.in_ou as io
import random
from timeit import default_timer as timer

if __name__ == "__main__":
    def main():
        game_info = g.init_game()
        g.game_loop(game_info)
        again = input("would you like to play again? (yes/no) \n").lower()
        if again == "yes":
            return main()
        return None

main()