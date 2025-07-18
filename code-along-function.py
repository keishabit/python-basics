# functions are reusable pieces of code!

print("Hello!")
print("My name is Python.")

def greet(name):
    print(f"Hello, {name} Welcome to the party!")

def user_input(prompt):
    input_value = input(prompt)

def main_menu():
    print("Welcome to the party!")
    print("1. Start")
    print("2. Exit")

    choice = input("Please choose an option:")
    print(f' You chose option {choice}')
    return choice


print("Hello!")
print("My name is Python.")
greet("Keisha")
main_menu()

main_menu_choice = main_menu()

if main_menu_choice == 1:
    print("Starting the program...")
else:
    print("Exiting the program. Goodbye!")
    