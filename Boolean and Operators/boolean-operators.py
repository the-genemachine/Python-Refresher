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


# Title
title = "Demonstrating the Use of Boolean Operators in Python"
display_title(title)

# Boolean AND operator
print("Boolean AND Operator:")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

# Boolean OR operator
print("\nBoolean OR Operator:")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

# Boolean NOT operator
print("\nBoolean NOT Operator:")
print("not True:", not True)
print("not False:", not False)
