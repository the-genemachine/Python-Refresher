# Function to calculate the total price
def calculate_total_price(item_price, quantity):
    return item_price * quantity


# Function to process the payment and calculate change
def process_payment(total_price, payment_amount):
    if payment_amount >= total_price:
        change = payment_amount - total_price
        print("Payment successful. Change: ${:.2f}".format(change))
    else:
        print("Insufficient payment. Please provide more funds.")


# Main function
def main():
    # Product details
    item_price = 10.0  # Price per item
    quantity = 0  # Quantity of items purchased

    # Input quantity of items
    quantity = int(input("Enter the quantity of items: "))

    # Calculate total price
    total_price = calculate_total_price(item_price, quantity)
    print("Total price: ${:.2f}".format(total_price))

    # Input payment amount
    payment_amount = float(input("Enter the payment amount: $"))

    # Process payment
    process_payment(total_price, payment_amount)


# Execute the main function
if __name__ == "__main__":
    main()
