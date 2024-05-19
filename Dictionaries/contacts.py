"""This program provides a simple contact management system where you can add, update, remove, and display contact
information. If the "contacts.data" file doesn't exist, it creates it and populates it with default contact data. The
contact details include name, phone number, and email address, and each contact is associated with a unique contact
ID."""

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


# Function to load contact data from file
def load_contacts(filename):
    """
    Load contact data from a specified file using pickle.

    This function attempts to open and load contact data from a file specified by the filename parameter.
    If the file does not exist (FileNotFoundError is raised), it creates a new file with default contact data.
    The default data includes two contacts, John Doe and Jane Smith, with predefined details.

    Parameters:
    - filename (str): The name of the file from which to load the contact data.

    Returns:
    - dict: A dictionary containing the loaded contact data. If the file was not found, returns a dictionary
            with default contact data.
    """
    try:
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
    except FileNotFoundError:
        print("Contacts data file not found. Creating a new one with default data.")
        contacts = {
            "1": {"name": "John Doe", "phone": "1234567890", "email": "john@example.com"},
            "2": {"name": "Jane Smith", "phone": "0987654321", "email": "jane@example.com"}
        }
        save_contacts(contacts, filename)
    return contacts


def load_contacts(filename):
    try:
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
    except FileNotFoundError:
        print("Contacts data file not found. Creating a new one with default data.")
        contacts = {
            "1": {"name": "John Doe", "phone": "1234567890", "email": "john@example.com"},
            "2": {"name": "Jane Smith", "phone": "0987654321", "email": "jane@example.com"}
        }
        save_contacts(contacts, filename)
    return contacts


# Function to save contact data to file
def save_contacts(contacts, filename):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)


# Function to add a new contact
def add_contact(contacts, contact_id, name, phone, email):
    if contact_id in contacts:
        print("Contact ID already exists. Use update function to modify existing contact.")
    else:
        contacts[contact_id] = {"name": name, "phone": phone, "email": email}
        print("Contact added successfully.")


# Function to update an existing contact
def update_contact(contacts, contact_id, name, phone, email):
    if contact_id in contacts:
        contacts[contact_id] = {"name": name, "phone": phone, "email": email}
        print("Contact updated successfully.")
    else:
        print("Contact ID does not exist. Use add function to add a new contact.")


# Function to remove a contact
def remove_contact(contacts, contact_id):
    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact removed successfully.")
    else:
        print("Contact ID does not exist.")


# Function to display all contacts
def display_contacts(contacts):
    if contacts:
        print("Contacts:")
        for contact_id, details in contacts.items():
            print(f"ID: {contact_id}, Name: {details['name']}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")


# Main function
def main():
    # Title
    title = "Contact Management System"
    display_title(title)

    # Load contact data from file or create new file with default data
    filename = "contacts.data"
    contacts = load_contacts(filename)

    # Menu loop
    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Update a contact")
        print("3. Remove a contact")
        print("4. Display all contacts")
        print("5. Save contacts and exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            contact_id = input("Enter contact ID: ")
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            add_contact(contacts, contact_id, name, phone, email)
        elif choice == '2':
            contact_id = input("Enter contact ID to update: ")
            name = input("Enter updated contact name: ")
            phone = input("Enter updated contact phone number: ")
            email = input("Enter updated contact email address: ")
            update_contact(contacts, contact_id, name, phone, email)
        elif choice == '3':
            contact_id = input("Enter contact ID to remove: ")
            remove_contact(contacts, contact_id)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts, filename)
            print("Contacts saved. Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Execute the main function
if __name__ == "__main__":
    main()
