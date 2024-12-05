# Get input from the user
A = int(input("Please provide three integers A, B, C.\nEnter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

# Variable to store the largest number
largest = A

# Compare B and C to find the largest number
if B > largest:
    largest = B
if C > largest:
    largest = C

# Print the result
print("The largest number is:", largest)