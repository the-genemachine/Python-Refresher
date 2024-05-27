import os
import pickle


class Bank:
    def __init__(self, data_file):
        self.data_file = data_file
        if os.path.exists(data_file):
            with open(data_file, 'rb') as file:
                self.customers = pickle.load(file)
        else:
            self.customers = {}

    def save_data(self):
        with open(self.data_file, 'wb') as file:
            pickle.dump(self.customers, file)

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        self.save_data()

    def get_customer(self, customer_id):
        return self.customers.get(customer_id)

    def __str__(self):
        return f"Bank: {self.customers}"
