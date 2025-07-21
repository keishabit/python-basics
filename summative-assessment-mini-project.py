# --- Collection Value Tracker ---

# Function to check if item value meets highlight threshold
def is_high_value(item_value):
    if item_value >= 100.0:
        return True
    return False

# Function to format item info for display
def format_item(name, category, value):
    name = name.strip().title()
    category = category.strip().title()
    formatted = f"{name} ({category}) - Value: ${value:.2f}"
    if is_high_value(value):
        formatted += "  High-Value Item!"
    return formatted

# Function to save collection to a file
def save_to_file(collection, filename):
    with open(filename, "w") as file:
        for item in collection:
            name, category, value = item
            file.write(format_item(name, category, value) + "\n")

# Main program flow
def main():
    print("Welcome to the Collection Value Tracker!")
    collection = []

    while True:
        item_name = input("Enter the item name (or type 'done' to finish): ").strip()
        if item_name.lower() == "done":
            break

        category = input("Enter the item category: ").strip()

        try:
            value = float(input("Enter the item value ($): ").strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value for item value.")
            continue

        collection.append((item_name, category, value))
        print("Item added!\n")

    print("\n--- Collection Summary ---")
    for item in collection:
        print(format_item(*item))

    save_to_file(collection, "collection.txt")
    print("\nYour collection has been saved to collection.txt.")

# Run the program
main()
