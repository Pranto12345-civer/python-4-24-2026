import random

target = random.randint(1, 50)
print("I am thinking of a number between 1 and 50.")

while True:
    guess = int(input("Make a guess: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")
        break