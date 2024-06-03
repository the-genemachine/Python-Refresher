# Crypto Wallet Manager Program Documentation

## Overview
The Crypto Wallet Manager is a menu-driven Python program that allows users to manage cryptocurrency wallets. Users can create wallets for specific cryptocurrencies, perform various operations such as depositing, withdrawing, transferring coins, checking balance, and viewing account details. The program demonstrates object-oriented programming (OOP) concepts, including inheritance, by using different wallet types.

## Files

### `util.py`
Contains utility functions for clearing the screen and displaying titles in the console using the Colorama library for colored output.

### `crypto_wallet.py`
Defines the base `CryptoWallet` class, which provides methods for depositing, withdrawing, checking balance, and saving/loading wallet data using the pickle module.

### `crypto_inheritance.py`
Defines subclasses of `CryptoWallet` for specific cryptocurrencies:
- `BitcoinWallet`: Represents a wallet for Bitcoin.
- `EthereumWallet`: Represents a wallet for Ethereum.

### `main.py`
The main program file that provides a menu-driven interface for interacting with the crypto wallets. It allows users to:
- Create a new wallet
- Deposit coins
- Withdraw coins
- Transfer coins to another wallet
- Check balance
- View account details
- Exit the program

## Features

### Create a New Wallet
Users can create a new wallet by providing their name and selecting the type of wallet (Bitcoin or Ethereum). The wallet is then added to the list of wallets and can be used for further transactions.

### Deposit Coins
Users can deposit coins into their wallet by specifying the amount. The balance of the wallet is updated accordingly.

### Withdraw Coins
Users can withdraw coins from their wallet by specifying the amount. The balance of the wallet is updated, provided there are sufficient funds.

### Transfer Coins
Users can transfer coins to another wallet by specifying the recipient's name and the amount to transfer. The balance of both the sender's and recipient's wallets are updated accordingly.

### Check Balance
Users can check the balance of their wallet. The current balance is displayed in the console.

### View Account Details
Users can view the full account details of their wallet, including the owner's name and the current balance.

### Exit Program
Users can exit the program. A thank you message is displayed before the program terminates.

## How It Works

1. **Initialization**:
   - The program initializes Colorama for colored console output.
   - Utility functions for clearing the screen and displaying titles are imported from `util.py`.
   - Wallet classes are imported from `crypto_wallet.py` and `crypto_inheritance.py`.

2. **Menu-Driven Interface**:
   - The `main()` function provides a continuous loop displaying the menu options until the user chooses to exit.
   - Based on the user's choice, the corresponding functionality is executed:
     - **Create a New Wallet**: Prompts the user for their name and wallet type, creates the wallet, and stores it in the wallets dictionary.
     - **Deposit Coins**: Prompts the user for the amount to deposit and updates the wallet balance.
     - **Withdraw Coins**: Prompts the user for the amount to withdraw and updates the wallet balance if there are sufficient funds.
     - **Transfer Coins**: Prompts the user for the recipient's name and the amount to transfer, and updates both wallets' balances.
     - **Check Balance**: Displays the current balance of the user's wallet.
     - **View Account Details**: Displays the full account details of the user's wallet.
     - **Exit**: Exits the program with a thank you message.

3. **Persistence**:
   - Wallet data is saved to a file using the pickle module, allowing for data persistence across sessions. Users can load their wallet data from the file for future transactions.

## Requirements

- Python 3.x
- Colorama library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the Colorama library using pip:
   ```sh
   pip install colorama
