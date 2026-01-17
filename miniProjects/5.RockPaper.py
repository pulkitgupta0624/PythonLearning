'''
Rock paper scissors game is gane where players use hand gestures to represent rock, paper, or scissors.
Rules: 
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

Write a python program to create a rock paper scissors game in python using if else statements. Do not create any fancy GUI.
Use proper function to check for win, loss or draw.
'''

import random

def check_result(user, computer):
    # draw condition
    if user == computer:
        return "draw"

    # winning conditions for user
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "win"

    # otherwise user loses
    return "lose"


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    print("🎮 Welcome to Rock Paper Scissors Game 🎮")
    print("Type: rock / paper / scissors")
    print("Type 'exit' to stop the game.\n")

    while True:
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "exit":
            print("Game exited ✅")
            break

        if user_choice not in choices:
            print("❌ Invalid choice! Please type rock, paper, or scissors.\n")
            continue

        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)

        result = check_result(user_choice, computer_choice)

        if result == "win":
            print("✅ You Win!\n")
        elif result == "lose":
            print("❌ You Lose!\n")
        else:
            print("😄 It's a Draw!\n")


# Run the game
rock_paper_scissors()
