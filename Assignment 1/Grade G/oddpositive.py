# Import the random module
import random

# Randomize a number between -10 and 10
n = random.randint(-10, 10)

# Check if the number is even/odd and positive/negative,
# and printing the results.
if n < 0 and n % 2 == 0:
    print(n, "is negative and even")
elif n < 0 and n % 2 != 0:
    print(n, "is negative and odd")
elif n > 0 and n % 2 == 0:
    print(n, "is positive and even")
elif n > 0 and n % 2 != 0:
    print(n, "is positive and odd")