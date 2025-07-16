string1 = 'This a valide string'
string2 = "This is a also a valid string"
# string3 = 'This is NOT a value sting - see why?"

palindrome = "Go hang a salami, I'm a lasagna hog"

# Using a quote inside string

string3 = "'Always look on the bright side of life' -Monty Python"

# Use escape characters to include quote in strings

string4 = "\"Always look on the bright side of life\" -Monty python"
print(string4)

len(string4)
print(len(string4))

name = "   Keisha  "
print(len(name))
print(name)

name_no_spaces = name.strip()
print(len(name_no_spaces))
print("Hello " + name_no_spaces)

#split()

filepath = "/var/keisha/here"
folders = filepath.split("/")
print(folders)
print(type(folders))

fullname = "Keisha, bry"
name = fullname.split(",")
row = "keisha bry, 22, 5'2\""

#print(names): ['keisha',  'bry']
#fristname = name



# join 

windowsPath = "||".join(folders)
print(windowsPath)

#find()

reservation_name = "Froman, Abe"
char_to_find = ","
# Where is the comma?

char_location = reservation_name.find(char_to_find)
print(char_location)

#index()
char_location = reservation_name.index(char_to_find)
print(char_location)