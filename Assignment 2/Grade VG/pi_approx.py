import random


# Function to estimate pi
def estimate_pi(N):
    inside_circle = 0

    # Generate N random points and check if they are inside the unit circle
    for i in range(N):
        x = random.uniform(-1, 1)  # Random x-coordinate between -1 and 1
        y = random.uniform(-1, 1)  # Random y-coordinate between -1 and 1
        distance = x**2 + y**2    # Calculate the distance from the origin

        if distance <= 1:         # Check if the point is
            inside_circle += 1    # inside the unit circle

    # Calculate the pi approximation
    # using the ratio of points inside the circle
    pi_approx = (inside_circle / N) * 4
    return pi_approx


def main():
    N_values = [100, 10000, 1000000]

    # Calculate pi approximation for different values of N
    for N in N_values:
        pi_approx = estimate_pi(N)
        pi_actual = 3.14159265358979323846  # Actual value of pi
        error = abs(pi_actual - pi_approx)
        print(f"N = {N}, Approximated pi = {pi_approx}, Error = {error}")


main()
