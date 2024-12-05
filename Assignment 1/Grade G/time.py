# Get the total amount of seconds from user input
total_seconds = int(input("Give a number of seconds: "))

# Calculate the seperate hours, minutes, and seconds using integer division and modulus
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Present the result in a user friendly way
print("Total time:", hours, "hours,", minutes, "minutes, and",seconds,"seconds.")