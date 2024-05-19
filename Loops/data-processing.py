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


# Function to read data from a file and process it
def process_data(filename):
    # Read data from the file
    with open(filename, 'r') as file:
        data = file.readlines()

    # Convert data to integers
    data = [int(line.strip()) for line in data]

    # Calculate statistics
    total = sum(data)
    average = total / len(data)
    maximum = max(data)
    minimum = min(data)

    # Display statistics
    print("Total:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)


# Main function
def main():
    # Title
    title = "Data Processing from File"
    display_title(title)

    # Process data from a file
    filename = "data.txt"  # Update with the filename containing your data
    process_data(filename)


# Execute the main function
if __name__ == "__main__":
    main()
