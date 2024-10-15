import sys
import random

"""TO DO

Add Player name entry and personalize the game.

Make Qutting guess_number.py and rps.py return to arcade.py menu.

Make Press 'X' to exit game from arcade menu.

"""


def guess_no_game():
    gamecount = 0
    player_wins = 0
    python_wins = 0

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

        print(f"\nPlayer chose {player_int}.")

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
                return "You win! 🎉\n"
            else:
                nonlocal python_wins
                python_wins += 1
                return "🐍 Python wins, you lose... 😿\n"

        decide_victor = game_result(player_int, python_int)
        print(decide_victor)

        nonlocal gamecount
        gamecount += 1
        print(f"Game Count: {gamecount}\n")

        print(f"Player Wins: {player_wins}\n")

        player_win_percentage = win_rate()
        print(f"Player win percentage: {player_win_percentage:.2f}%\n")

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
            sys.exit("\nThanks for playing! 👋")

    return play_guess_num()


guess_no_game()


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
