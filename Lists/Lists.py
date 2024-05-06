"""This Python code demonstrates the basic operations on sets such as creation, addition, removal, membership check,
set operations like union, intersection, difference, and iteration."""

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

# Example code demonstrating the use of sets

# Display title
title = "Demonstrating the Use of Sets in Python"
display_title(title)

# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print the sets
print("Set 1:", set1)
print("Set 2:", set2)

# Adding elements to a set
set1.add(6)
print("After adding 6 to Set 1:", set1)

# Removing elements from a set
set2.remove(8)
print("After removing 8 from Set 2:", set2)

# Checking membership
print("Is 3 in Set 1?", 3 in set1)
print("Is 9 in Set 2?", 9 in set2)

# Set operations
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of Set 1 and Set 2:", difference_set)

# Iterating over a set
print("Iterating over Set 1:")
for element in set1:
    print(element)







