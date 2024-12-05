# Adds string 's' to itself 'n' times
def concat(s, n):
    return s * n


# Calculates amount of times 'x' is used in 's'
def count(s, x):
    count = 0
    for char in s:
        if char == x:
            count += 1
    return count


# Reverses the string 's'
def reverse(s):
    return s[::-1]


# First and last characters
def first_last(s):
    first = s[0]
    last = s[-1]
    return first, last


# Checks if string contains exactly two 'X'
def has_two_X(s):
    return s.count('X') == 2


# Checks if string contains duplicate characters
def has_duplicates(s):
    unique_chars = set()
    for char in s:
        if char in unique_chars:
            return True
        unique_chars.add(char)
    return False
