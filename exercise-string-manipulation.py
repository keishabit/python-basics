# Split string of names using '|'
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)

# Split lyrics by line using split()
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split("\n")
print(lyrics_split)

# Split lyrics by line using splitlines()
changed_values = lyrics.splitlines()
print(changed_values)

# Get length of long village name
long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

# Strip spaces and get folders from path
my_path = ' /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM '
my_folders = my_path.strip().split("/")
print(my_folders)

# Change the third name to "Wolfgang Mozart"
composers = "Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
composers_split = composers.split(";")
third_composer = composers_split[2]
comma_position = third_composer.find(",")
last_name = third_composer[:comma_position]
first_name = third_composer[comma_position+1:]
third_composer_name = f"{first_name.strip()} {last_name.strip()}"
print(third_composer_name)

# Combine padded strings to create full message
left_padded = ' Operators are standing by'
right_padded = 'Call now '
final_message = right_padded.strip() + '! ' + left_padded.strip()
print(final_message)

# Old-style formatting for student data
student_name = "Owen"
grade = 94.75
assignment_number = 12
print("Student name: %s, Assignment ID: %04d, Grade: %.2f%%" % (student_name, assignment_number, grade))

# Pad employee ID to 6 digits
employee_id = "30"
employee_id_padded = employee_id.zfill(6)
print(employee_id_padded)

# Print raw string to show newline character
print(r"\n represents a new line.")

# Apply string case conversions
i_want_to_yell = 'yeah'
I_NEED_TO_BE_QUIET = 'SHHHHH'
this_is_a_title = 'this is a title'
sWAPcASE = 'sWAPcASE'
capitalize_this = 'capitalize this'

print(i_want_to_yell.upper())
print(I_NEED_TO_BE_QUIET.lower())
print(this_is_a_title.title())
print(sWAPcASE.swapcase())
print(capitalize_this.capitalize())