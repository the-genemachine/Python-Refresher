""" This program uses lambda functions with default arguments to define mathematical operations for addition,
subtraction, multiplication, and division. The user can input two numbers and select an operation to perform. The
program then displays the result of the chosen operation, with the title and output colored for better visibility
using Colorama. The console screen is cleared before displaying the title."""

import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)


# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display a title with color
def display_title(title):
    clear_screen()
    title_length = len(title)
    print(Fore.YELLOW + "=" * title_length)
    print(Fore.YELLOW + title)
    print(Fore.YELLOW + "=" * title_length)
    print()


# Lambda functions with default arguments for mathematical operations
# Lambda functions with default arguments for mathematical operations

# Addition: Adds two numbers. If the second number is not provided, it defaults to 0.
add = lambda x, y=0: x + y

# Subtraction: Subtracts the second number from the first. If the second number is not provided, it defaults to 0.
subtract = lambda x, y=0: x - y

# Multiplication: Multiplies two numbers. If the second number is not provided, it defaults to 1.
multiply = lambda x, y=1: x * y

# Division: Divides the first number by the second. If the second number is not provided, it defaults to 1.
# If the second number is 0, returns "Cannot divide by zero" to avoid division by zero error.
divide = lambda x, y=1: x / y if y != 0 else "Cannot divide by zero"


# Main function
def main():
    # Title
    title = "Lambda Math Operations with Default Arguments"
    display_title(title)

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        result = add(num1, num2)
        print(Fore.GREEN + f"Result: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(Fore.GREEN + f"Result: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(Fore.GREEN + f"Result: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(Fore.GREEN + f"Result: {result}")
    else:
        print(Fore.RED + "Invalid choice")


# Execute the main function
if __name__ == "__main__":
    main()
