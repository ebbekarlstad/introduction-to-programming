# Get the three different names
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")

# Get the first letter of the first name, middle name, and the first four letters of the last name.
first_name_short = first_name[0]
middle_name_short = middle_name[0]
last_name_short = last_name[0:4]

# Print the result with periods as separators
print(first_name_short + ". " + middle_name_short + ". " + last_name_short)