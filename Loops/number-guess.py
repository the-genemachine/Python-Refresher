"""This Python program implements a simple number guessing game. The player has to guess a randomly generated number 
between 1 and 100 within a limited number of attempts. After each guess, the program provides feedback on whether the 
guess was too high, too low, or correct. The game ends when the player either guesses the correct number or runs out 
of attempts."""

import os
import random


# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display a title
def display_title(title):
    clear_screen()
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()


# Function to generate a random number within a specified range
def generate_random_number(start, end):
    return random.randint(start, end)


# Main function for the guessing game
def guessing_game():
    # Title
    title = "Number Guessing Game"
    display_title(title)

    # Generate a random number between 1 and 100
    secret_number = generate_random_number(1, 100)

    # Number of attempts allowed
    max_attempts = 5
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have", max_attempts, "attempts to guess it.")

    # Loop until the player runs out of attempts or guesses correctly
    while attempts < max_attempts:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the number correctly in", attempts, "attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    if attempts == max_attempts:
        print("\nSorry, you have run out of attempts. The correct number was:", secret_number)


# Execute the guessing game
if __name__ == "__main__":
    guessing_game()
