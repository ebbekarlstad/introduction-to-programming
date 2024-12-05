from list_functions import random_list, average, only_odd
from list_functions import to_string, contains, has_duplicates

# Generate a random list of 10 integers
random_lst = random_list(10)
print("Random List:", random_lst)

# Calculate the average of the list
avg = average(random_lst)
print("Average:", avg)

# Filter the odd numbers from the list
odd_lst = only_odd(random_lst)
print("Odd Numbers:", odd_lst)

# Convert the list to a comma-separated string
str_lst = to_string(random_lst)
print("String Representation:", str_lst)

# Check if 2 is directly followed by 3 in the list
contains_2_3 = contains(random_lst, 2, 3)
print("Contains 2 followed by 3:", contains_2_3)

# Check if the list has duplicates
has_dupes = has_duplicates(random_lst)
print("Has Duplicates:", has_dupes)
