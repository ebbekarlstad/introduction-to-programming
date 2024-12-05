n = int(input("Enter a positive integer: "))

print("Odd numbers using for:", end=" ")
for i in range(1, n, 2):
    print(i, end=" ")

print("\nOdd numbers using while:", end=" ")
i = 1
while i <= n:
    print(i, end=" ")
    i += 2
