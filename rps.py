import sys
import random
from enum import Enum


def rps(player_name: str = "Player One", from_arcade: bool = False):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_name, player_wins, python_wins
        # nonlocal player_wins
        # nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{player_name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{player_name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)
        computer = random.randint(1, 3)

        print(
            f"\n{player_name}, you chose {str(RPS(player)).replace('RPS.', '').title()}."
        )
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {player_name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {player_name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {player_name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {player_name}.. 😢"

        print(decide_winner(player, computer))

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\nPython wins: {python_wins}")
        print(f"\n{player_name}'s wins: {player_wins}")

        print(f"\nPlay again, {player_name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if from_arcade:
                return  # Return control to arcade menu if launched from arcade
            else:
                sys.exit(f"Bye {player_name}! 👋")

    return play_rps()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
