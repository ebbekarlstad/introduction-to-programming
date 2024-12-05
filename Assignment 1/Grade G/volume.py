# Get the radius from user input, as well as define pi
r = float(input("Provide a radius: "))
pi = 3.141593

# Calculate the volume
v = float(4/3 * pi * r**3)

# Present result
print("Volume is:", round(v, 1))