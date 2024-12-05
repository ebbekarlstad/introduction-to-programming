# Get an int from user via input
n = int(input("Enter a positive integer: "))

# Check if n is positive
if n <= 0:
    print("Error: Please enter a positive integer.")
else:
    sum1 = 0
    sum2 = 0
    odd_k = 1
    even_k = 0

    # Find the smallest k such that 1 + 3 + 5 + ... + k > n
    while sum1 + odd_k <= n:
        sum1 += odd_k
        odd_k += 2
        if sum1 + odd_k > n:  # Check if the next k will exceed n
            break

    # Find the largest k such that 0 + 2 + 4 + 6 + ... + k < n
    while sum2 + even_k < n:
        even_k += 2
        sum2 += even_k

    # Print the results
    print(f"{odd_k} is the smallest k such that 1+3+5+...+k > {n}")
    print(f"{even_k} is the largest k such that 0+2+4+6+...+k < {n}")
