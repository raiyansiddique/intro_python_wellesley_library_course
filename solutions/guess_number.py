#Guess the Number: Create a program that generates a random number between 1 and 100, 
# and asks the user to guess it. The program should tell the user if their guess 
# is too high or too low.

import random

secret_number = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while True:
    guess_str = input("Enter your guess: ")
    guess = int(guess_str)
    attempts += 1

    if guess < secret_number:
        print("Too low! Guess again.")
    elif guess > secret_number:
        print("Too high! Guess again.")
    else:
        print(f"Congratulations, you guessed the number in {attempts} attempts!")
        break
