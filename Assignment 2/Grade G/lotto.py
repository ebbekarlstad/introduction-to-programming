import random


def generate_lotto_sequence():
    # Create a list to store the Lotto numbers
    lotto_numbers = []

    # Generate seven random numbers between 1 and 35
    while len(lotto_numbers) < 7:
        # Generate a random number between 1 and 35
        number = random.randint(1, 35)

        # Check if the number is not already in the list
        if number not in lotto_numbers:
            # Add the number to the list
            lotto_numbers.append(number)

    # Sort the list in ascending order
    lotto_numbers.sort()
    return lotto_numbers


def main():
    # Generate the Lotto sequence
    lotto_sequence = generate_lotto_sequence()

    # Print the Lotto numbers for this week
    print("The Lotto numbers this week:")
    for number in lotto_sequence:
        print(number, end=" ")
    print()


# Execute main() function
main()
