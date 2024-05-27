import os
from colorama import init, Fore
from customer import Customer
from bank import Bank

# Initialize Colorama
init(autoreset=True)


# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display a title with color
def display_title(title):
    clear_screen()
    print(Fore.YELLOW + "=" * len(title))
    print(Fore.YELLOW + title)
    print(Fore.YELLOW + "=" * len(title))
    print()


# Function to display menu options
def display_menu():
    print(Fore.CYAN + "Menu Options:")
    print("1. Create a new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. View full account information")
    print("6. Exit")


def main():
    # Clear screen and display title
    title = "Simple Banking System"
    display_title(title)

    # Create bank instance
    bank = Bank("bank_data.pkl")

    while True:
        # Display menu options
        display_menu()

        # Get user choice
        choice = input(Fore.YELLOW + "Enter your choice (1-6): ")

        # Process user choice
        if choice == '1':
            display_title("Create a New Account")
            name = input("Enter your name: ")
            balance = float(input("Enter initial balance: "))
            customer_id = len(bank.customers) + 1
            customer = Customer(customer_id, name, balance)
            bank.add_customer(customer)
            print(Fore.GREEN + "Account created successfully!")
        elif choice == '2':
            display_title("Deposit Money")
            customer_id = int(input("Enter customer ID: "))
            amount = float(input("Enter amount to deposit: "))
            customer = bank.get_customer(customer_id)
            if customer:
                customer.deposit(amount)
                bank.save_data()
                print(Fore.GREEN + f"${amount} deposited successfully!")
            else:
                print(Fore.RED + f"Customer with ID {customer_id} not found.")
        elif choice == '3':
            display_title("Withdraw Money")
            customer_id = int(input("Enter customer ID: "))
            amount = float(input("Enter amount to withdraw: "))
            customer = bank.get_customer(customer_id)
            if customer:
                customer.withdraw(amount)
                bank.save_data()
                print(Fore.GREEN + f"${amount} withdrawn successfully!")
            else:
                print(Fore.RED + f"Customer with ID {customer_id} not found.")
        elif choice == '4':
            display_title("Check Balance")
            customer_id = int(input("Enter customer ID: "))
            customer = bank.get_customer(customer_id)
            if customer:
                print(Fore.GREEN + f"Balance for customer {customer_id}: ${customer.get_balance()}")
            else:
                print(Fore.RED + f"Customer with ID {customer_id} not found.")
        elif choice == '5':
            display_title("View Full Account Information")
            customer_id = int(input("Enter customer ID: "))
            customer = bank.get_customer(customer_id)
            if customer:
                print(Fore.CYAN + "Account Information:")
                print(customer)
            else:
                print(Fore.RED + f"Customer with ID {customer_id} not found.")
        elif choice == '6':
            display_title("Exiting Program")
            print(Fore.YELLOW + "Thank you for using our banking system!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
