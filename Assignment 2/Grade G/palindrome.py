def is_palindrome(s):
    # Convert the string to lowercase to make it case-insensitive
    s = s.lower()

    # Remove non-alphanumeric characters from the string
    s = ''.join(char for char in s if char.isalnum())

    # Compare the original string with its reverse
    return s == s[::-1]


# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("hello"))  # False
