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
title = "Python Lists Assignment"
display_title(title)

# Create a list of 5 animals
zoo = ["lion", "elephant", "zebra", "giraffe", "monkey"]
print("Original list of animals:", zoo)

# Delete the animal at the 3rd index
del zoo[2]
print("List after deleting animal at the 3rd index:", zoo)

# Append a new animal at the end of the list
zoo.append("tiger")
print("List after appending a new animal:", zoo)

# Delete the animal at the beginning of the list
del zoo[0]
print("List after deleting animal at the beginning:", zoo)

# Print all the animals
print("All animals in the list:", zoo)

# Print only the first 3 animals
print("First 3 animals in the list:", zoo[:3])
