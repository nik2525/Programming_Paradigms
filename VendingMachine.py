# Define products and their prices
products = {
    "Mentos": 5,
    "Max": 10,
    "Judge": 25,
    "Vfresh" : 13,
    "Bobot" : 14
}

# Function to display available products and their prices
def display_products():
    print("Available Products:")
    for item, price in products.items():
        print(f"{item}: ₱{price:.2f}")

# Function to simulate the vending machine
def start_vending_machine():
    while True:  # Continue running until the customer chooses to exit
        print("\nWelcome to the Candy Vending Machine")
        print("1. Press 1 to select a product")
        print("2. Press 2 to Exit")
        choice = input("Enter your choice: ")

        if choice == "1":  # If the customer chooses to select a product
            display_products()
            product = input("Enter the name of the product you want: ").capitalize()

            if product in products:  # If the chosen product is available
                money_inserted = float(input("Please insert your money: "))

                if money_inserted >= products[product]:  # If the entered money is sufficient
                    print(f"Dispensing {product}...")
                    change = money_inserted - products[product]
                    print(f"Thank you! Your change: ₱{change:.2f}")
                    money_inserted = 0.0
                else:
                    print("Insufficient funds!")  # Prompt for insufficient funds
            else:
                print("Product unavailable!")  # Prompt for unavailable product
        elif choice == "2":  # If the customer chooses to exit
            print("Exiting...")
            break
        else:
            print("Invalid choice!")  # Prompt for invalid input

# Run the vending machine
start_vending_machine()
