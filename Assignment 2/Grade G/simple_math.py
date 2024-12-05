# Increments n with one
def inc(n):
    return n + 1


print('\n41 plus 1:', inc(41))


# Increments n with the value of t
def inc_with(n, t):
    return n + t


print('30 plus 12:', inc_with(30, 12))


# Returns the largest of the values n1 and n2
def greatest(n1, n2):
    return max(n1, n2)


print('Which is greater, 24 or 42?', greatest(24, 42))


# Returns True if n is even, otherwise false
def is_even(n):
    return n % 2 == 0


print('Is 42 even?: ', is_even(42))


# Returns x to the power of n
def power(x, n):
    return x ** n


print('2 to the power of 10:', power(2, 10))


# Returns the factorial of n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print('Factorial of 5:', factorial(5))


# Returns True if n is a prime, otherwise false
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


print('Is 41 a prime?:', is_prime(41))
