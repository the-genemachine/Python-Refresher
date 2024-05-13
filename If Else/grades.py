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


# Function to determine letter grade
def determine_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


# Main function
def main():
    # Title
    title = "Grade Calculator"

    # Run the program until a specific key is pressed
    while True:
        display_title(title)

        # Input the grade
        grade = int(input("Enter the grade (0 - 100): "))

        # Validate the grade
        if grade < 0 or grade > 100:
            print("Invalid grade! Grade must be between 0 and 100.")
            input("Press Enter to continue...")
            continue

        # Determine and print the letter grade
        letter_grade = determine_letter_grade(grade)
        print("Letter grade:", letter_grade)

        # Check if the user wants to continue
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            break


# Execute the main function
if __name__ == "__main__":
    main()
