# Simple Interactive Vending Machine Simulator

# Set up the product menu
items = {
    "soda": 1.50,
    "chips": 2.00,
    "candy": 1.00
}

# Display menu function
def display_menu():
    print("Vending Machine Menu:")
    for item in items:
        print(f" - {item.title()}: ${items[item]:.2f}")

# Prompt for initial funds
funds = float(input("Insert money to start (e.g., 5.00 , 20.00): $"))

# Main transaction loop
while funds > 0:
    print()  # Blank line for separation
    display_menu()
    print()
    print(f"Current Balance: ${funds:.2f}")
    print()
    choice = input("Type the name of the item you want, or 'exit' to finish: ").lower()
    
    if choice == 'exit':
        break

    if choice not in items:
        print("Item not found. Please select from the menu.")
        continue

    price = items[choice]
    if funds >= price:
        funds -= price
        print()  # Blank line for separation
        print(f"Dispensing {choice.title()}... Enjoy!")
        print(f"Remaining Balance: ${funds:.2f}")
        again = input("Would you like to make another purchase? (yes/no): ").lower()
        if again != "yes":
            break
    else:
        print("Insufficient funds.")
        add_more = input("Would you like to add more money? (yes/no): ").lower()
        if add_more == "yes":
            extra = float(input("How much would you like to add?: $"))
            funds += extra
        else:
            break

print()
print("Thank you for using the vending machine!")
print(f"Your change is: ${funds:.2f}")