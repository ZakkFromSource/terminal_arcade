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


def play_guess_num():

    try:
        player_choice = input("\nPlease pick the number 1, 2 or 3...\n\n")

        if player_choice not in ["1", "2", "3"]:
            print("\nTry again...\n")
            return play_guess_num()
        else:
            player_int = int(player_choice[0])  # Player's Number

    except:
        sys.exit("MAJOR ERROR! ☠️")

    python_choice = random.choices(
        "123"
    )  # random module used to pick 1 element of the string '123'
    python_int = int(python_choice[0])  # Python's number

    def guess_check(player, python):

        print(f"\nPlayer chose {player}.\n")

        print(f"I was thinking of the number {python}.\n")

        if player == python:
            print("You win! 🎉")
        else:
            print("🐍 Python wins, you lose... 😿\n")

    guess_check(player_int, python_int)


play_guess_num()
