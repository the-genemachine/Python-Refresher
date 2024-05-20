""" This program uses lambda functions to define mathematical operations for addition, subtraction, multiplication,
and division. The user can input two numbers and select an operation to perform. The program then displays the result
of the chosen operation. The console screen is cleared before displaying the title."""

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


# Lambda functions for mathematical operations
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"


# Main function
def main():
    # Title
    title = "Lambda Math Operations"
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
        print(f"Result: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice")


# Execute the main function
if __name__ == "__main__":
    main()
