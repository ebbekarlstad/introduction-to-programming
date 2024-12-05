import random


# Function to simulate the walks of drunken sailors
def simulate_drunken_sailors(size, max_steps, num_sailors):
    sailors_fallen = 0

    # Loop through each sailor
    for _ in range(num_sailors):
        x, y = 0, 0  # Initialize the sailor's position
        for _ in range(max_steps):
            # Randomly choose the direction of the next step
            step = random.choice(['up', 'down', 'left', 'right'])

            # Update the sailor's position based on the chosen step
            if step == 'up':
                y += 1
            elif step == 'down':
                y -= 1
            elif step == 'left':
                x -= 1
            elif step == 'right':
                x += 1

            # Check if the sailor goes outside the boundary of the platform
            if abs(x) > size or abs(y) > size:
                sailors_fallen += 1
                break

    return sailors_fallen


if __name__ == "__main__":
    size = int(input("Enter the size: "))  # Input: Size of the platform
    max_steps = int(input("Enter number of steps: "))  # Max number of steps
    num_sailors = int(input("Enter number of sailors: "))  # Number of sailors

    # Simulate the walks of sailors and count how many fall into the water
    sailors_fallen = simulate_drunken_sailors(size, max_steps, num_sailors)

    # Calculate and display the percentage of sailors who fell into the water
    percentage_fallen = (sailors_fallen / num_sailors) * 100
    print(f"Out of {num_sailors} drunk sailors, {sailors_fallen}\
({percentage_fallen:.2f}%) fell into the water.")
