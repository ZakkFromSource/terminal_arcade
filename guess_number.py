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
def player_choose():
    try:
        player_choice = input("Please pick the number 1, 2 or 3...\n\n ")

        if player_choice not in ["1", "2", "3"]:
            print("Try again...\n")
            player_choose()
        else:
            player_int = int(player_choice[0])
            return player_int

    except:
        print("Error. You eally fucked up. Follow the instructions.")


def python_choose():
    python_choice = random.choices(
        "123"
    )  # random module used to pick 1 element of the string '123'
    python_int = int(python_choice[0])  # Convert single list item to int
    return python_int


player_num = player_choose()
print(f"\nPlayer chose {player_num}.")

python_num = python_choose()
print(f"\nI was thinking of the number {python_num}.")
