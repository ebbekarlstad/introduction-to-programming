n = int(input("Enter a positive integer: "))

print("\nRight-Angled Triangle:")
spaces = ""
stars = "*"

for i in range(n, 0, -1):
    if i <= n and i > 0:
        print(spaces, end="")
        spaces += " "
    print(f"{stars * i}")

print("\nIscoceles Triangle:")
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2 * " "
    stars = i * "*"
    print(spaces, stars)
