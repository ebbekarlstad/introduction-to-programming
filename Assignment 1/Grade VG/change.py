# Get the price and payment from user input
price = float(input("\nPrice: "))
payment = int(input("Payment: "))
print(" ")

# Calculate the change
change = payment - price
original_change = payment - price

# Calculate the number of denominations
thousand = change // 1000
change %= 1000

five_hundred = change // 500
change %= 500

two_hundred = change // 200
change %= 200

one_hundred = change // 100
change %= 100

fifty = change // 50
change %= 50

twenty = change // 20
change %= 20

ten = change // 10
change %= 10

five = change // 5
change %= 5

two = change // 2
change %= 2

one = change // 1

# Print the different bills and coins returned
print("Change:", round(original_change), "kr")
print(round(thousand), "1000kr bills")
print(round(five_hundred), "500kr bills")
print(round(two_hundred), "200kr bills")
print(round(one_hundred), "100kr bills")
print(round(fifty), "50kr bills")
print(round(twenty), "20kr bills")
print(round(ten), "10kr coins")
print(round(five), "5kr coins")
print(round(two), "2kr coins")
print(round(one), "1kr coins")