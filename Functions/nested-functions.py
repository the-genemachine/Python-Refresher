""" This program provides a clear and colorful interface using Colorama, allowing the user to input two numbers and
select an operation to perform. The result of the operation is displayed with green color, and error messages are
displayed with red color for better visibility. Nested functions are used to encapsulate the mathematical operations
within the math_operations function."""

import os
from colorama import init, Fore

# Initialize Colorama
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


# Nested functions for mathematical operations
def math_operations():
    # Addition function
    def add(x, y):
        return x + y

    # Subtraction function
    def subtract(x, y):
        return x - y

    # Multiplication function
    def multiply(x, y):
        return x * y

    # Division function
    def divide(x, y):
        return x / y if y != 0 else "Cannot divide by zero"

    return add, subtract, multiply, divide


# Main function
def main():
    # Clear screen and display title
    title = "Nested Functions for Math Operations"
    display_title(title)

    # Input two numbers from the user
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

    # Display available operations
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Input the desired operation from the user
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 4.")

    # Perform the selected operation using nested functions
    add, subtract, multiply, divide = math_operations()
    if choice == '1':
        result = add(num1, num2)
        print(Fore.GREEN + f"Result of addition: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(Fore.GREEN + f"Result of subtraction: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(Fore.GREEN + f"Result of multiplication: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(Fore.GREEN + f"Result of division: {result}")


# Execute the main function
if __name__ == "__main__":
    main()
