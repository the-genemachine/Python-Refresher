"""This program serves as an inventory management system for a store, where each item's details (name, price,
and quantity) are stored as values associated with their unique product ID as the key in a dictionary. The inventory
data is loaded from and saved to an external file named "inventory.data" using the pickle module for serialization.
The program provides options to add new items to inventory, update existing items, remove items, display all items,
and save the inventory data before exiting."""

import os
import pickle


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


# Function to load inventory data from file
def load_inventory(filename):
    try:
        with open(filename, 'rb') as file:
            inventory = pickle.load(file)
    except FileNotFoundError:
        print("Inventory data file not found. Creating a new one with default data.")
        inventory = {
            "101": {"name": "Laptop", "price": 999.99, "quantity": 10},
            "102": {"name": "Smartphone", "price": 599.99, "quantity": 20},
            "103": {"name": "Tablet", "price": 399.99, "quantity": 15}
        }
        save_inventory(inventory, filename)
    return inventory


# Function to save inventory data to file
def save_inventory(inventory, filename):
    with open(filename, 'wb') as file:
        pickle.dump(inventory, file)


# Function to add a new item to inventory
def add_item(inventory, product_id, name, price, quantity):
    if product_id in inventory:
        print("Product ID already exists. Use update function to modify existing item.")
    else:
        inventory[product_id] = {"name": name, "price": price, "quantity": quantity}
        print("Item added to inventory.")


# Function to update an existing item in inventory
def update_item(inventory, product_id, name, price, quantity):
    if product_id in inventory:
        inventory[product_id] = {"name": name, "price": price, "quantity": quantity}
        print("Item updated in inventory.")
    else:
        print("Product ID does not exist. Use add function to add a new item.")


# Function to remove an item from inventory
def remove_item(inventory, product_id):
    if product_id in inventory:
        del inventory[product_id]
        print("Item removed from inventory.")
    else:
        print("Product ID does not exist.")


# Function to display all items in inventory
def display_inventory(inventory):
    if inventory:
        print("Inventory Items:")
        for product_id, details in inventory.items():
            print(
                f"Product ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Quantity: {details['quantity']}")
    else:
        print("Inventory is empty.")


# Main function
def main():
    # Title
    title = "Inventory Management System"
    display_title(title)

    # Load inventory data from file or create new file with default data
    filename = "inventory.data"
    inventory = load_inventory(filename)

    # Menu loop
    while True:
        print("\nMenu:")
        print("1. Add a new item to inventory")
        print("2. Update an item in inventory")
        print("3. Remove an item from inventory")
        print("4. Display all items in inventory")
        print("5. Save inventory and exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_item(inventory, product_id, name, price, quantity)
        elif choice == '2':
            product_id = input("Enter product ID to update: ")
            name = input("Enter updated product name: ")
            price = float(input("Enter updated product price: "))
            quantity = int(input("Enter updated product quantity: "))
            update_item(inventory, product_id, name, price, quantity)
        elif choice == '3':
            product_id = input("Enter product ID to remove: ")
            remove_item(inventory, product_id)
        elif choice == '4':
            display_inventory(inventory)
        elif choice == '5':
            save_inventory(inventory, filename)
            print("Inventory saved. Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Execute the main function
if __name__ == "__main__":
    main()
