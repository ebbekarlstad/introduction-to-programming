import random

# Create a list to store 11 elements, all set to 0
sum_counts = [0] * 11

# Simulate the two dice rolling 10000 times
for i in range(10000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Calculate the sum of the two dice
    total = dice1 + dice2

    # Update the count
    sum_counts[total - 2] += 1

# Print the frequency table
print("Frequency table (sum, count) for rolling two dice 10000 times")
for i, count in enumerate(sum_counts, start=2):
    print(f"{i}\t{count}")
