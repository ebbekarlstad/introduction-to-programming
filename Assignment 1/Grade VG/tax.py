# Get monthly income from input
income = int(input("Please provide monthly income: "))

# Define the tax rates
original_tax = 30 * 0.01
extra_tax1 = 35 * 0.01
extra_tax2 = 40 * 0.01

# Calculate the different taxes
if income < 38000:
    tax = income * original_tax
elif income > 38000 and income < 50000:
    zone_2 = income % 38000
    tax = (38000 * original_tax) + (zone_2 * extra_tax1)
elif income > 50000:
    zone_2 = 12000
    zone_3 = income % 50000
    tax = (38000 * original_tax) + (zone_2 * extra_tax1) + (zone_3 * extra_tax2)

# Print out result
print("Corresponding income tax:", round(tax))