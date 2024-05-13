"""This Python program calculates the factorial of a given number using a loop. The user is prompted to enter a
number, and the program calculates the factorial of that number using a for loop. The factorial is calculated
iteratively by multiplying the numbers from 1 to the given number. The program also includes functions to clear the
screen and display a title for better presentation."""

import os


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


# Function to calculate the factorial of a number using a loop
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


# Main function
def main():
    # Title
    title = "Factorial Calculator"
    display_title(title)

    # Input number from the user
    number = int(input("Enter a number to calculate its factorial: "))

    # Validate the input
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate and display the factorial using a loop
        factorial = calculate_factorial(number)
        print("Factorial of", number, "is:", factorial)


# Execute the main function
if __name__ == "__main__":
    main()
