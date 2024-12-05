# Import random module
import random

# Save a random int from 1 to 100 in "n"
n = random.randint(1, 100)


# Create variables guesses and answer
guesses = 0
answer = 0

# Create loop
while answer != n:
    guesses += 1
    # Get the  answer from user every try
    answer = int(input(f"Guess {guesses}: "))
    if answer > n:  # Check if it's right or not
        print("Lower")
    elif answer < n:
        print("Higher")
    else:   # If correct, print result
        print(f"Correct answer after {guesses} guesses!")
