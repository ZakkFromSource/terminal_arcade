import sys
import random

"""TO DO

Make Qutting guess_number.py and rps.py return to arcade.py menu.

Make Press 'X' to exit game from arcade menu.

"""


def guess_num_game(name="Player One"):
    gamecount = 0
    player_wins = 0
    python_wins = 0
    greeting = f"\nHello {args.name}!"
    print(greeting)

    def play_guess_num():

        try:
            player_choice = input("\nPlease pick the number 1, 2 or 3...\n\n")

            if player_choice not in [
                "1",
                "2",
                "3",
            ]:  # Ensures player can only pick between 1-3
                print("\nTry again...")
                return play_guess_num()
            else:
                player_int = int(player_choice[0])  # Player's Number

        except ValueError:
            sys.exit("\nInvalid input. Please enter a valid number next time.\n")

        python_int = random.randint(1, 3)  # Python's number between 1-3

        print(f"\n{args.name} chose {player_int}.")

        print(f"I was thinking of the number {python_int}.\n")

        def win_rate():  # Player Win Percentage calculator
            nonlocal player_wins
            nonlocal python_wins
            win_percentage = player_wins / (player_wins + python_wins) * 100
            return win_percentage

        def game_result(player_int, python_int):

            if player_int == python_int:
                nonlocal player_wins
                player_wins += 1
                return f"{args.name} wins! 🎉\n"
            else:
                nonlocal python_wins
                python_wins += 1
                return f"🐍 Python wins, you lose... Unlucky {args.name}. 😞\n"

        decide_victor = game_result(player_int, python_int)
        print(decide_victor)

        nonlocal gamecount
        gamecount += 1
        print(f"Game Count: {gamecount}\n")

        print(f"{args.name}'s Total Wins: {player_wins}\n")

        player_win_percentage = win_rate()
        print(f"Current Win Percentage: {player_win_percentage:.2f}%\n")

        print("Play Again? 🕹️")

        while True:
            play_again = input("\nPress 'Y' for yes, or 'Q' to quit.\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess_num()
        else:
            print(f"\nThanks for playing {args.name}! 😊")
            sys.exit("Goodbye for now. 👋")

    return play_guess_num()


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

    guess_game = guess_num_game(args.name)
