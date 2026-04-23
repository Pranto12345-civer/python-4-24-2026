import random

options = ["Rock", "Paper", "Scissors"]
computer = random.choice(options)
user = input("Choose Rock, Paper, or Scissors: ")

print(f"Computer chose: {computer}")
if user == computer:
    print("It's a tie!")
elif (user == "Rock" and computer == "Scissors") or \
     (user == "Paper" and computer == "Rock") or \
     (user == "Scissors" and computer == "Paper"):
    print("You win!")
else:
    print("Computer wins!")