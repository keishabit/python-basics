'''
our_number = 42

is_guessed = False

# the while loop runs until a condtion turns true
while not is_guessed == False:

# get input from the user

    guess = int(input("Enter your guess:"))

# conditional statements to check the guess

if guess == our_number:
    print('Hooray!')
elif guess > our_number:
    print('Too high!')
else:
    print('Too low!')
'''
'''
counter = 1

while counter < 20:
 
    if counter % 3 == 0 and counter % 5 == 0:
        print(f'{counter}: Fizzbuzz')
        counter += 1
        continue
    elif counter % 3 == 0:
        print(f'{counter}: Fizz')
    elif counter % 5 == 0:
        print(f'{counter}: Buzz')
    counter+= 1 # This is a shortcut for counter = counter + 1
else:
    print('Done with while loop')
    '''

# for loop example

loop_range = range(1,11)

for i in range(1, 11+1):
 print(f'Iteration{i}')

print(max(loop_range))

# for loop with a list

fruits = ['apple' , 'banna', 'cherry' , 3, 4.5]

for i in fruits:
    print(f'Fruits{i}') 
