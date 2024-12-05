# Get a three digit number from user input
number = int(input("Input a three digit number: "))

# Calculate the hundreds, tens, and single digits
a = number // 100
b = number // 10 % 10
c = number % 10

# Present the respective digits added to each other
print(a + b + c)