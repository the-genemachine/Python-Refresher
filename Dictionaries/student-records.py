"""This program serves as a student record management system using a dictionary to store student records. It provides
options to add new student records, remove existing student records, and display all student records. Each student's
information (name and grades) is stored as values associated with their unique student ID as the key in the
dictionary. The program includes functions to clear the screen, display a title, and handle user input for a
menu-driven interface."""

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


# Function to add a new student record
def add_student(records, student_id, name, grades):
    records[student_id] = {
        "name": name,
        "grades": grades
    }
    print("Student record added successfully.")


# Function to remove a student record
def remove_student(records, student_id):
    if student_id in records:
        del records[student_id]
        print("Student record removed successfully.")
    else:
        print("Student ID not found.")


# Function to display all student records
def display_students(records):
    if records:
        print("Student Records:")
        for student_id, info in records.items():
            print(f"ID: {student_id}, Name: {info['name']}, Grades: {info['grades']}")
    else:
        print("No student records found.")


# Main function
def main():
    # Title
    title = "Student Record Management System"
    display_title(title)

    # Dictionary to store student records (student_id: {name, grades})
    student_records = {}

    # Menu loop
    while True:
        print("\nMenu:")
        print("1. Add a new student record")
        print("2. Remove a student record")
        print("3. Display all student records")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grades = input("Enter student grades (comma-separated): ").split(',')
            add_student(student_records, student_id, name, grades)
        elif choice == '2':
            student_id = input("Enter student ID to remove: ")
            remove_student(student_records, student_id)
        elif choice == '3':
            display_students(student_records)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Execute the main function
if __name__ == "__main__":
    main()
