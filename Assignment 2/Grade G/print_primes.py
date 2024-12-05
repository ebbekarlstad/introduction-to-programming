# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False    # Not prime
    if num <= 3:
        return True    # Is prime
    if num % 2 == 0 or num % 3 == 0:
        return False    # Not prime
    i = 5   # Check for divisibility from 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False    # Not prime
        # Add 6 to i to check divisibility with 5 and 7, 11 and 13, etc.
        i += 6
    return True    # If no divisors, it is prime


# Get prime numbers to print
num_primes = int(input("How many primes? "))

# Create variables for counters
count = 0
line_count = 0
num = 2  # First prime number

# Loop to generate and print prime numbers
while count < num_primes:
    if is_prime(num):   # Check if num is a prime number
        print(num, end=" ")
        count += 1
        line_count += 1

        if line_count == 10:
            print()  # Move to the next line
            line_count = 0
    num += 1
