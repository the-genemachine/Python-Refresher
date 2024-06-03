import pickle


class CryptoWallet:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self.balance

    def save_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_data(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def __str__(self):
        return f"Owner: {self.owner_name}, Balance: {self.balance} coins"
