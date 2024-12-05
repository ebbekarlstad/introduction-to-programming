# Create list to store positive integers
positive_numbers = []

count = 0

# Start loop
while True:
    try:
        # Read an int from the user
        num = int(input(f"Integer {count + 1}: "))
        # Check if the number is positive
        if num >= 0:
            positive_numbers.append(num)
            count += 1
        else:
            break  # Exit the loop if num is negative.
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Print the result
print(f"Number of positive integers: {count}")
print(f"Positive numbers: {positive_numbers}")
