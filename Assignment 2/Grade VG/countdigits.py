# Function to count zeros, odd digits, and even digits in a number
def count_digits(number):
    num_str = str(number)
    zero_count = 0
    odd_count = 0
    even_count = 0

    for digit in num_str:
        if digit == '0':
            zero_count += 1
        elif int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return zero_count, odd_count, even_count


# Main program
try:
    n = int(input("Enter a large positive integer: "))
    if n < 0:
        print("Please enter a positive integer.")
    else:
        zero_count, odd_count, even_count = count_digits(n)
        print("Zeros:", zero_count)
        print("Odd:", odd_count)
        print("Even:", even_count)
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
