import sys
from guess_number import guess_num_game
from rps import rps

"""TO DO

Make Qutting guess_number.py and rps.py return to arcade.py menu.

"""

# Arcade Menu where you can access all the arcade games or exit.


def arcade(player_name: str = "Player One"):  # Store args.name in a variable
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\nHello {player_name}, Welcome back to the Arcade menu!\n")

        menu_choice = input(
            """\n Please choose a game:
                            1 = Guess My Number
                            2 = Rock Paper Scissors
                            
                            Or press "x" to exit the Arcade\n\n"""
        )

        if menu_choice.lower() not in ["1", "2", "x"]:
            print("Invalid input, try again.\n")
            return arcade(player_name)

        welcome_back = True

        if menu_choice.lower() == "1":
            guess_num_game(player_name, from_arcade=True)  # Pass the flag
        elif menu_choice.lower() == "2":
            rps(player_name, from_arcade=True)  # Pass the flag
        else:
            print(f"\nThanks for playing {player_name}. 🤖")
            sys.exit("See you again soon! 🚀")


if __name__ == "__main__":
    import argparse

    # Create parser using argparse module
    parser = argparse.ArgumentParser(
        description="Creates a personalised game experience."
    )

    # Add arguments to parser
    parser.add_argument(
        "-n",
        "--name",
        metavar="NAME",
        required=True,
        help="Recieve player name, making the game personalized.",
    )

    # Parse the arguments
    args = parser.parse_args()

    print(f"\nHello {args.name}, Welcome to the Arcade! 👾\n")

    start_arcade = arcade(args.name)
