## Daily Cooking Routine Guide
## Pre-Cooking Setup (5 minutes)

1. Wash your hands thoroughly with soap and warm water
1. Clean and sanitize all countertops and cutting boards
1. Gather all ingredients and place them within easy reach
1. Check that all required cooking equipment is clean and ready
1. Preheat oven, stovetop, or any appliances as needed
1. IF cooking requires oven or appliances, THEN preheat them now

## Ingredient Preparation (10-15 minutes)

1. Read through the entire recipe from start to finish
1. Measure out all dry ingredients into separate bowls
1. Measure all liquid ingredients and set aside
1. Wash and prep all vegetables (chop, dice, slice as needed)
1. IF using protein, THEN prepare by trimming, seasoning, or marinating
1. Organize prepped ingredients in order of use

## Active Cooking Process (20-45 minutes)

1. Start with ingredients that take the longest to cook
1. Use timers for each cooking step to avoid overcooking
1. Taste and adjust seasonings throughout the process
1. Keep cooking areas clean as you go - wash utensils between uses
1. Monitor heat levels and adjust as needed for optimal results
1. IF making multiple dishes, THEN prepare side dishes simultaneously

## Plating and Presentation (5 minutes)

1. IF serving hot meal, THEN warm plates in low oven or with warm water
1. Arrange food thoughtfully on plates for visual appeal
1. IF available, THEN add fresh herbs, garnishes, or finishing touches
1. Check that all components are at proper serving temperature

## Post-Cooking Cleanup (10 minutes)

1. Turn off all appliances and burners immediately after use
1. Soak pots and pans in warm soapy water while eating
1. Store leftover ingredients properly in refrigerator or pantry
1. Wipe down all surfaces and put away cooking utensils
1. Load dishwasher or wash dishes by hand promptly

## Final Steps

1. Take a moment to evaluate the meal and note any improvements
1. Plan ahead for tomorrow's meal to streamline the process
1. Ensure kitchen is completely clean and ready for next use
1. Enjoy your home-cooked meal and the satisfaction of cooking!






## Excercise for Vending machine


## Product Menu Setup
items = { ... }
Creates a “menu” for the vending machine—a dictionary of what products are available and how much each costs.
This is like the internal memory of the real vending machine: it always knows which products are in stock and their prices.

## Display Menu Function
def display_menu(): ...

Defines a function that prints the full menu for the user, showing each product (with the first letter capitalized) alongside its price in dollars.
1. Whenever this function is called, it helps the user know what choices they have and how much money each choice will require.

## Prompt for Initial Funds
funds = float(input(...))
1. Asks the user how much money they are putting into the machine (like inserting bills or coins). It converts the user’s answer into a number for calculations.
1. This represents the user’s initial credit before they start shopping.

## Main Transaction Loop
while funds > 0: ...
The core shopping loop. As long as the user still has money left, the vending machine keeps operating:

1. It prints a blank line for neat spacing.
1. It shows the current menu with display_menu().
1. It prints how much money the user has left.
1. It asks the user for what they want to buy, or if they want to quit with "exit".

## Processing the User’s Choice
Handling what the user types:

1. If the user types "exit", the program breaks the loop and moves to "thank you/return change."
1. If the choice isn’t one of the product names in the menu, the user is told the item is not found and the loop starts over so they can try again.

## Price and Funds Check
Selecting and buying the item:

1. Finds the price of the chosen product.
1. If the user has enough money (funds >= price):
1. Subtracts the item price from funds (simulates payment).
1. Displays a blank line, a message "dispensing" the item, and their updated balance.
1. Asks if they want to buy something else. If not, the loop ends.

## Not Enough Money
If the user wants something too expensive:
1. Tells them "Insufficient funds."
1. Asks if they want to add more money.
1. If yes, asks how much and adds it to their funds.
1. If not, the loop ends and the program moves to the final message and change.

## Program End and Change
After the loop completes, either by running out of money or the user choosing to exit:

1. Prints a blank line.
1. Thanks the user for using the vending machine.
1. Shows exactly how much money the user has left as change—what they get back if anything is still in their "wallet".



