import sys
import guess_number
import rps

"""TO DO

Make Qutting guess_number.py and rps.py return to arcade.py menu.

"""

# Arcade Menu where you can access all the arcade games or exit.


def arcade(player_name: str):  # Store args.name in a variable

    greeting = f"\nHello {player_name}, Welcome to the Arcade!\n"
    print(greeting)

    def arcade_menu():

        menu_choice = input(
            """\n Please choose a game:
                            1 = Guess My Number
                            2 = Rock Paper Scissors
                            
                            Or press "x" to exit the Arcade\n\n"""
        )

        if menu_choice.lower() not in ["1", "2", "x"]:
            return arcade_menu()

        else:
            if menu_choice.lower() == "1":
                return guess_number.guess_num_game(
                    player_name
                )  # Launches guess_number.py
            elif menu_choice.lower() == "2":
                return rps.rps(player_name)  # Launches rps.py
            else:
                print(f"\nThanks for playing {player_name}. 🤖")
                sys.exit("See you again soon! 🚀")

    return arcade_menu()


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

    start_arcade = arcade(args.name)
