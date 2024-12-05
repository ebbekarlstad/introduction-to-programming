# Import functions from previous script
import string_functions

# Start values
s = "hello"
n = 4
x = "l"


# Function concat
result = string_functions.concat(s, n)
print(f"\nString repeated {n} times: '{result}'")

# Function count
count_result = string_functions.count(s, x)
print(f"\nThe character '{x}' occurs {count_result} "
      f"times in the string '{s}'.")

# Function reverse
reverse_result = string_functions.reverse(s)
print(f"\nReversed string: '{reverse_result}'")

# Function first_last
first, last = string_functions.first_last(s)
print(f"\nFirst char: '{first}', last char: '{last}'")

# Function has_two_X
if string_functions.has_two_X(s):
    print(f"\nThe string '{s}' does contain exactly two 'X'")
else:
    print(f"\nThe string '{s}' does not contain exactly two 'X'")

# Function has_duplicates
if string_functions.has_duplicates(s):
    print(f"\nThe string '{s}' has duplicates.\n")
else:
    print(f"\nThe string '{s}' does not have duplicates.\n")
