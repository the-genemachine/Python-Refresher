class Customer:
    def __init__(self, customer_id, name, balance):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Balance: ${self.balance}"
