# Via user input, get all the information needed for calculations
s = float(input("Initial savings: "))
p = float(input("Interest rate (in percentages): "))
n = int(input("Number of times interest is compounded per year: "))
y = float(input("Number of years: "))

# Convert from percentage to decimal
r = p / 100

# Calculate compound interest
A = s * (1 + r / n)**(n * y)

# Present the result
print("The value of your savings after", y, "years is:", round(A))