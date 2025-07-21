## --- Pseudocode: Collection Value Tracker ---

## START PROGRAM

## 1. DEFINE a function called is_high_value(value)
##    IF value is greater than or equal to 100
##        RETURN True
##    ELSE
##        RETURN False

## 2. DEFINE a function called format_item(name, category, value)
##    CAPITALIZE name and category
##    FORMAT string like: "Item (Category) - Value: $value"
##    IF value is high (use is_high_value), add " High-Value Item!" to it
##    RETURN the formatted string

## 3. DEFINE a function called save_to_file(collection, filename)
##    OPEN a file with the given filename in write mode
##    FOR each item in collection
##        USE format_item() on the item
##        WRITE formatted string to the file
##    CLOSE the file

## 4. DEFINE the main function
##    PRINT welcome message
##    CREATE an empty list called collection

##    WHILE True
##        ASK user to enter item name
##        IF user types "done"
##            BREAK the loop

##        ASK user to enter category
##        ASK user to enter value (convert to a number)

##        IF value is not a number
##            SHOW error message
##            CONTINUE to next loop

##        ADD (name, category, value) to collection
##        PRINT "Item added!"

##    PRINT "--- Collection Summary ---"
##    FOR each item in collection
##        PRINT the formatted item using format_item()

##    CALL save_to_file(collection, "collection.txt")
##    PRINT confirmation that items were saved

## 5. CALL the main function to start the program

## END PROGRAM
