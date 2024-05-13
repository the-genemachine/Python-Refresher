"""This Python program demonstrates the use of loops to print various patterns, including a square pattern,
a right triangle pattern, an inverted right triangle pattern, and the Fibonacci sequence. Each pattern is printed
using loops to iterate over the rows and columns of the pattern. The program also includes a function to clear the
screen before printing each pattern and displays a title for each pattern."""

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


# Function to print a square pattern
def print_square_pattern(size):
    display_title("Square Pattern")

    for i in range(size):
        print("*" * size)


# Function to print a right triangle pattern
def print_right_triangle_pattern(size):
    display_title("Right Triangle Pattern")

    for i in range(1, size + 1):
        print("*" * i)


# Function to print an inverted right triangle pattern
def print_inverted_right_triangle_pattern(size):
    display_title("Inverted Right Triangle Pattern")

    for i in range(size, 0, -1):
        print("*" * i)


# Function to print the Fibonacci sequence
def print_fibonacci_sequence(size):
    display_title("Fibonacci Sequence")

    a, b = 0, 1
    print(a, end=" ")
    while b < size:
        print(b, end=" ")
        a, b = b, a + b


# Main function
def main():
    # Title
    title = "Print Patterns using Loops"
    display_title(title)

    # Print various patterns
    print_square_pattern(5)
    input("\nPress Enter to continue...")
    print_right_triangle_pattern(5)
    input("\nPress Enter to continue...")
    print_inverted_right_triangle_pattern(5)
    input("\nPress Enter to continue...")
    print_fibonacci_sequence(100)


# Execute the main function
if __name__ == "__main__":
    main()
