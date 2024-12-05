# Import math module
import math

# Gets points from user
x1 = int(input("Enter point x1: "))
y1 = int(input("Enter point y1: "))
x2 = int(input("Enter point x2: "))
y2 = int(input("Enter point y2: "))


# Create a function that calculates distance
def calc_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance  # End function and return value of distance


distance = calc_distance(x1, y1, x2, y2)

# Print results
print(
    f"The distance between {(x1, y1)}, "
    f"and {(x2, y2)} is {round(distance, 3)}"
)
