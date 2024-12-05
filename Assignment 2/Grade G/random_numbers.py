import random

n = int(input("Enter number of integers to be generated: "))

# Check if n is non-positive and display an error message
if n <= 0:
    print("Error: Please enter a positive integer.")
else:
    total = 0
    min_num = float('inf')
    max_num = float('-inf')

    # Loop to generate the numbers
    for i in range(n):
        random_num = random.randint(1, 100)
        # Print the generated number
        print(random_num, end=" ")

        # Update total sum
        total += random_num

        # Check for min number
        if random_num < min_num:
            min_num = random_num

        # Check for max number
        if random_num > max_num:
            max_num = random_num

    avg = total / n

    # Print the average, min, and max values
    print(f"\nAverage, min, and max are: {avg}, {min_num}, and {max_num}")
