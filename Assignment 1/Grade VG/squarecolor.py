# Get the chess identifier
identifier = input("Enter a chess square identifier (e.g. e5): ")

# Get the letter and number from the identifier
letter = identifier[0]
number = int(identifier[1])

# Check if the letter is on (a, c, e, g)
if letter in "aceg":
    if number % 2 != 0:
        square_color = "black"
    else:
        square_color = "white"

#  Check if the letter is on (b, d, f, h)
elif letter in "bdfh":
    if number % 2 == 0:
        square_color = "black"
    else:
        square_color = "white"
else:
    square_color = "invalid"

# Print the result
print(identifier, "is", square_color)