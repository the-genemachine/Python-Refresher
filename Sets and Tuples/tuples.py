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

# Example code demonstrating the use of tuples

# Display title
title = "Demonstrating the Use of Tuples in Python"
display_title(title)

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Print the tuple
print("Tuple:", my_tuple)

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked elements:", a, b, c, d, e)

# Immutable nature of tuples
# Trying to modify a tuple will result in an error
# Uncomment the following lines to see the error
# my_tuple[0] = 10

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Slicing tuples
slice_tuple = my_tuple[1:4]
print("Slice of the tuple:", slice_tuple)

# Length of a tuple
print("Length of the tuple:", len(my_tuple))

# Checking membership
print("Is 3 in the tuple?", 3 in my_tuple)

# Iterating over a tuple
print("Iterating over the tuple:")
for element in my_tuple:
    print(element)
