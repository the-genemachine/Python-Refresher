""" This program provides a clear and colorful interface using Colorama, allowing the user to input two numbers and
select an operation to perform. The result of the operation is displayed with green color, and error messages are
displayed with red color for better visibility. Generator functions are used to generate the results of mathematical
operations on the input numbers."""

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


# Generator function for mathematical operations
def math_operations(x, y):
    """
    This function defines four generator functions for basic mathematical operations: addition, subtraction,
    multiplication, and division. Each generator function takes two arguments and yields the result of the
    corresponding operation. The function then yields from each of the generator functions in turn.

    Parameters:
    x (float): The first number for the operations.
    y (float): The second number for the operations.

    Yields:
    float: The result of the operation.
    """

    # Addition generator
    def add(x, y):
        """
        This generator function takes two arguments and yields the result of their addition.

        Parameters:
        x (float): The first number.
        y (float): The second number.

        Yields:
        float: The result of the addition.
        """
        yield x + y

    # Subtraction generator
    def subtract(x, y):
        """
        This generator function takes two arguments and yields the result of subtracting the second number from the first.

        Parameters:
        x (float): The first number.
        y (float): The second number.

        Yields:
        float: The result of the subtraction.
        """
        yield x - y

    # Multiplication generator
    def multiply(x, y):
        """
        This generator function takes two arguments and yields the result of their multiplication.

        Parameters:
        x (float): The first number.
        y (float): The second number.

        Yields:
        float: The result of the multiplication.
        """
        yield x * y

    # Division generator
    def divide(x, y):
        """
        This generator function takes two arguments and yields the result of dividing the first number by the second.
        If the second number is zero, it yields a specific message to avoid division by zero error.

        Parameters:
        x (float): The first number.
        y (float): The second number.

        Yields:
        float or str: The result of the division, or a message if division by zero is attempted.
        """
        yield x / y if y != 0 else "Cannot divide by zero"

    # Yield from each of the generator functions
    yield from add(x, y)
    yield from subtract(x, y)
    yield from multiply(x, y)
    yield from divide(x, y)


# Main function
def main():
    # Clear screen and display title
    title = "Generator Functions for Math Operations"
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

    # Perform the selected operation using generator functions
    operations = math_operations(num1, num2)
    result = next(operations)  # Get the first result
    if choice == '1':
        print(Fore.GREEN + f"Result of addition: {result}")
    elif choice == '2':
        print(Fore.GREEN + f"Result of subtraction: {result}")
    elif choice == '3':
        print(Fore.GREEN + f"Result of multiplication: {result}")
    elif choice == '4':
        print(Fore.GREEN + f"Result of division: {result}")


# Execute the main function
if __name__ == "__main__":
    main()
