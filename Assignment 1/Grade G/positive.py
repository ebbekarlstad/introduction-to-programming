# Check if a number is even or odd
n = int(input("Please enter a positive integer: "))

if n < 0: # Check if negative
    print(n, "is negative")
else:
    if n > 0: # Check if positive
        print(n, "is positive")
    else:
        print(n, "is 0")