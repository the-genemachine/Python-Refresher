""" This program uses lambda functions with conditional expressions to define mathematical operations for addition,
subtraction, multiplication, and division. It utilizes the curses library to create a text-based user interface with
colors and better layout. The user can input two numbers and select an operation to perform. The program then
displays the result of the chosen operation, with the title and output displayed using curses for a more visually
appealing presentation."""

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
    print(Fore.YELLOW + "=" * len(title))
    print(Fore.YELLOW + title)
    print(Fore.YELLOW + "=" * len(title))
    print()


# Lambda functions with conditional expressions for mathematical operations
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"


# Main function
def main():
    # Clear screen
    clear_screen()

    # Title
    title = "Lambda Math Operations with Conditional Expressions"
    display_title(title)

    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 4.")

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
        if num2 != 0:
            result = divide(num1, num2)
            print(Fore.GREEN + f"Result: {result}")
        else:
            print(Fore.RED + "Cannot divide by zero")


# Execute the main function
if __name__ == "__main__":
    main()
