# Function to calculate the median
def calculate_median(salaries):
    salaries.sort()
    n = len(salaries)
    if n % 2 == 0:
        median1 = salaries[n // 2 - 1]
        median2 = salaries[n // 2]
        median = (median1 + median2) // 2
    else:
        median = salaries[n // 2]
    return median


# Function to calculate the average
def calculate_average(salaries):
    total = sum(salaries)
    n = len(salaries)
    average = total // n
    return average


# Function to calculate the salary gap
def calculate_salary_gap(salaries):
    highest_salary = max(salaries)
    lowest_salary = min(salaries)
    gap = highest_salary - lowest_salary
    return gap


# Input salaries as a space-separated string
salaries_input = input("Provide salaries: ")

# Convert the input string to a list of integers
salaries_list = [int(s) for s in salaries_input.split()]

# Calculate the median, average, and salary gap
median_salary = calculate_median(salaries_list)
average_salary = calculate_average(salaries_list)
salary_gap = calculate_salary_gap(salaries_list)

# Print the results
print(f"Median: {median_salary}")
print(f"Average: {average_salary}")
print(f"Gap: {salary_gap}")
