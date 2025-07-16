# 1. Create a variable named onomatopoeia and set its value to 'pop'. Print the type of onomatopoeia.
onomatopoeia = 'pop'
print(type(onomatopoeia))

# 2. Create a variable named lyrics and assign it the following multiline string:
lyrics = """Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:\""""

# 3. Create a variable named gpa and set it to 3.75. Print the variable and its type.
gpa = 3.75
print(gpa)
print(type(gpa))

# 4. Create a variable named empty_var and assign it the Python equivalent of null. Print the variable and its type.
empty_var = None
print(empty_var)
print(type(empty_var))

# 5. Create a variable that stores the value of 828^282. Print the variable.
power_result = 828**282
print(power_result)

# 6. Create a variable to store the result of the following mathematical expression:
# a. (52 - 52) + (64 / 8) + the remainder of 42 / 8
# b. Print the final result.
math_result = (52 - 52) + (64 / 8) + (42 % 8)
print(math_result)

# 7. Create a variable named true and set it to the boolean value for true. Create a second variable named isTrue and set it to check whether true is not False. Print isTrue.
true = True
isTrue = true is not False
print(isTrue)

# 8. Write the following:
# a. Create a variable named weird_word and set its value to 'Weird'.
weird_word = 'Weird'
# b. Create a second variable to check whether weird_word matches 'weird'.
string_comparison = weird_word == 'weird'
# c. Print out the second variable.
print(string_comparison)

# 9. Create a variable named false. What error occurs? Explain why.
# false = True  # This causes a SyntaxError
# Error: SyntaxError: invalid syntax
# Explanation: 'false' is a reserved keyword in Python. Python uses 'False' (capitalized) 
# as the boolean false value, so 'false' cannot be used as a variable name.

# 10. Create a variable for the value of 35/7. Create another variable for the value of 15^3. Create a third variable for the value of variable 2 % variable 1. Create a fourth variable for the value of variable 2 / variable 1. Compare the results.
num1 = 35 / 7
num2 = 15 ** 3
num3 = num2 % num1
num4 = num2 / num1
print(f"num1 (35/7): {num1}")
print(f"num2 (15^3): {num2}")
print(f"num3 (num2 % num1): {num3}")
print(f"num4 (num2 / num1): {num4}")
print(f"Comparison - Are num3 and num4 equal? {num3 == num4}")