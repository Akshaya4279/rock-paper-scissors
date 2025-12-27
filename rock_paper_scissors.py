import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ").strip().lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid choice")
