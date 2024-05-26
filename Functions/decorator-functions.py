""" This program provides a clear and colorful interface using Colorama, allowing the user to input two numbers and
select an operation to perform. The result of the operation is displayed with green color, and error messages are
displayed with red color for better visibility. Decorator functions are used to measure the execution time of each
mathematical operation. Finally, cProfile is used to measure the overall execution time of the main function,
and the results are displayed at the end of the program."""

import os
import cProfile
import time
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


# Decorator function to measure the execution time of functions
def measure_execution_time(func):
    """
    Decorator function to measure the execution time of a function. It wraps the function, measures the time before and
    after the function execution, calculates the execution time, and prints it. The function's result is then returned.

    Parameters:
    func (function): The function whose execution time is to be measured.

    Returns:
    function: The wrapped function.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that calls the original function, measures the time before and after the function execution,
        calculates the execution time, and prints it. The function's result is then returned.

        Parameters:
        *args: Variable length argument list for the original function.
        **kwargs: Arbitrary keyword arguments for the original function.

        Returns:
        The result of the original function.
        """
        start_time = time.time()  # Time before the function execution
        result = func(*args, **kwargs)  # Call the original function and store the result
        end_time = time.time()  # Time after the function execution
        execution_time = end_time - start_time  # Calculate the execution time
        print(Fore.CYAN + f"Execution time of {func.__name__}: {execution_time:.6f} seconds")  # Print the execution time
        return result  # Return the function's result

    return wrapper  # Return the wrapped function


# Function to perform addition
@measure_execution_time
def add(x, y):
    return x + y


# Function to perform subtraction
@measure_execution_time
def subtract(x, y):
    return x - y


# Function to perform multiplication
@measure_execution_time
def multiply(x, y):
    return x * y


# Function to perform division
@measure_execution_time
def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"


# Main function
def main():
    # Clear screen and display title
    title = "Decorator Functions for Math Operations"
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

    # Perform the selected operation
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

    # Measure the execution time using cProfile
    print()
    print(Fore.MAGENTA + "Execution time using cProfile:")
    cProfile.run('main()')
