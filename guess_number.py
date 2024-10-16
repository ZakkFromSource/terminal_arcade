import sys
import random


def guess_num_game(player_name: str = "Player One", from_arcade: bool = False):
    gamecount = 0
    player_wins = 0
    python_wins = 0
    greeting = f"\nHello {player_name}, Let's play!"
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
            if from_arcade:
                return  # Don't exit if launched from arcade, just return
            else:
                sys.exit("\nInvalid input. Please enter a valid number.\n")

        python_int = random.randint(1, 3)  # Python's number between 1-3

        print(f"\n{player_name} chose {player_int}.")
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
                return f"{player_name} wins! 🎉\n"
            else:
                nonlocal python_wins
                python_wins += 1
                return f"🐍 Python wins, you lose... Unlucky {player_name}. 😞\n"

        print(game_result(player_int, python_int))

        nonlocal gamecount
        gamecount += 1
        print(f"Game Count: {gamecount}\n")
        print(f"{player_name}'s Total Wins: {player_wins}\n")
        print(f"Current Win Percentage: {win_rate():.2f}%")
        # player_win_percentage = win_rate()
        # print(f"Current Win Percentage: {player_win_percentage:.2f}%\n")
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
            print(f"\nThanks for playing {player_name}! 😊")
            if from_arcade:
                return  # Return control to arcade if launched from arcade
            else:
                sys.exit("Goodbye for now. 👋")

    return play_guess_num()


# If the script is run directly (not imported)
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
    guess_game()
