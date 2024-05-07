# Create a set
fruits = {"apple", "banana", "orange", "grape", "banana"}

# Print the set
print("Fruits set:", fruits)

# Add an element to the set
fruits.add("pineapple")
print("Fruits set after adding 'pineapple':", fruits)

# Remove an element from the set
fruits.remove("banana")
print("Fruits set after removing 'banana':", fruits)

# Check if an element is in the set
print("Is 'orange' in the fruits set?", "orange" in fruits)

# Iterate over the set
print("Iterating over the fruits set:")
for fruit in fruits:
    print(fruit)

# Create another set
vegetables = {"carrot", "potato", "tomato", "onion"}

# Union of sets
combined_set = fruits.union(vegetables)
print("Combined set of fruits and vegetables:", combined_set)

# Intersection of sets
common_items = fruits.intersection(vegetables)
print("Common items between fruits and vegetables:", common_items)

# Difference between sets
unique_fruits = fruits.difference(vegetables)
print("Fruits not present in vegetables set:", unique_fruits)
