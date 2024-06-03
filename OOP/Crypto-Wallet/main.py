import os
import pickle
from colorama import init, Fore
from util import clear_screen, display_title
from crypto_inheritance import BitcoinWallet, EthereumWallet

# Initialize Colorama
init(autoreset=True)

DATA_FILE = 'wallets_data.pkl'


def save_wallets(wallets):
    with open(DATA_FILE, 'wb') as file:
        pickle.dump(wallets, file)


def load_wallets():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as file:
            return pickle.load(file)
    return {}


def display_menu():
    print(Fore.CYAN + "Menu Options:")
    print("1. Create a new wallet")
    print("2. Deposit coins")
    print("3. Withdraw coins")
    print("4. Transfer coins")
    print("5. Check balance")
    print("6. View account details")
    print("7. Exit")


def main():
    title = "Crypto Wallet Manager"
    display_title(title)

    wallets = load_wallets()

    while True:
        display_menu()

        choice = input(Fore.YELLOW + "Enter your choice (1-7): ")

        if choice == '1':
            display_title("Create a New Wallet")
            owner_name = input("Enter your name: ")
            wallet_type = input("Enter wallet type (Bitcoin/Ethereum): ").lower()
            if wallet_type == 'bitcoin':
                wallet = BitcoinWallet(owner_name)
            elif wallet_type == 'ethereum':
                wallet = EthereumWallet(owner_name)
            else:
                print(Fore.RED + "Invalid wallet type. Please choose Bitcoin or Ethereum.")
                continue
            wallets[owner_name] = wallet
            save_wallets(wallets)
            print(Fore.GREEN + "Wallet created successfully!")
        elif choice in ['2', '3', '4', '5', '6']:
            owner_name = input("Enter your name: ")
            if owner_name not in wallets:
                print(Fore.RED + "No wallet found. Please create a wallet first.")
                continue
            wallet = wallets[owner_name]
            if choice == '2':
                display_title("Deposit Coins")
                amount = float(input("Enter amount to deposit: "))
                wallet.deposit(amount)
                save_wallets(wallets)
                print(Fore.GREEN + f"{amount} coins deposited successfully!")
            elif choice == '3':
                display_title("Withdraw Coins")
                amount = float(input("Enter amount to withdraw: "))
                wallet.withdraw(amount)
                save_wallets(wallets)
                print(Fore.GREEN + f"{amount} coins withdrawn successfully!")
            elif choice == '4':
                display_title("Transfer Coins")
                recipient_name = input("Enter recipient's name: ")
                amount = float(input("Enter amount to transfer: "))
                if recipient_name not in wallets:
                    print(Fore.RED + "Recipient wallet not found.")
                else:
                    recipient_wallet = wallets[recipient_name]
                    wallet.withdraw(amount)
                    recipient_wallet.deposit(amount)
                    save_wallets(wallets)
                    print(Fore.GREEN + f"{amount} coins transferred successfully to {recipient_name}!")
            elif choice == '5':
                display_title("Check Balance")
                print(Fore.GREEN + f"Balance in your wallet: {wallet.check_balance()} coins")
            elif choice == '6':
                display_title("View Account Details")
                print(Fore.CYAN + "Account Information:")
                print(wallet)
        elif choice == '7':
            display_title("Exiting Program")
            print(Fore.YELLOW + "Thank you for using our Crypto Wallet Manager!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
