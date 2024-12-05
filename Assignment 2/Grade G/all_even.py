# Create a variable to store the running sum
sum = 0

# Create a loop that goes through all even numbers from 2 to 100
for i in range(2, 101, 2):  # (start, end, step size)
    sum += i

# Print out result
print("Sum of the 100 first even numbers is:", sum)
