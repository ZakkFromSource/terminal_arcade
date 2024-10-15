import sys
import random


#     def guess_num_game():
#         print(greeting)

# if __name__ == "__main__":
#     import argparse

#     # Create parser using argparse module
#     parser = argparse.ArgumentParser(
#         description="Creates a personalised game experience."
#     )

#     # Add arguments to parser
#     parser.add_argument("name", help="The name of the player.")

#     # Parse the arguments
#     args = parser.parse_args()


#     greeting = f"Hello {args.name}!"
#     guess_num_game()
def guess_no_game():
    gamecount = 0

    def play_guess_num():

        try:
            player_choice = input("\nPlease pick the number 1, 2 or 3...\n\n")

            if player_choice not in ["1", "2", "3"]:
                print("\nTry again...")
                return play_guess_num()
            else:
                player_int = int(player_choice[0])  # Player's Number

        except ValueError:
            sys.exit("\nInvalid input. Please enter a valid number next time.\n")

        python_int = random.randint(1, 3)  # Python's number

        print(f"\nPlayer chose {player_int}.")

        print(f"I was thinking of the number {python_int}.\n")

        if player_int == python_int:
            print("You win! 🎉\n")
        else:
            print("🐍 Python wins, you lose... 😿\n")

        nonlocal gamecount
        gamecount += 1
        print(f"Game Count: {gamecount}")

        print("\nPlay Again? 🕹️")

        while True:
            play_again = input("\nPress 'Y' for yes, or 'Q' to quit.\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess_num()
        else:
            sys.exit("\nThanks for playing! 👋")

    return play_guess_num()


guess_no_game()
