import random


def random_list(n):
    # Returns a list containing n random integers in the interval 1 to 100.
    return [random.randint(1, 100) for i in range(n)]


def average(lst):
    # Returns the average (rounded off integer) of all values in the list lst.
    if not lst:
        return 0
    return round(sum(lst) / len(lst))


def only_odd(lst):
    # Returns a new list containing only the odd integers in lst.
    return [x for x in lst if x % 2 != 0]


def to_string(lst):
    # Returns a comma-separated string representation of the elements in lst.
    return "[" + ",".join(map(str, lst)) + "]"


def contains(lst, a, b):
    # Returns True if a is directly followed by b anywhere in the list lst,
    # otherwise False.
    for i in range(len(lst) - 1):
        if lst[i] == a and lst[i + 1] == b:
            return True
    return False


def has_duplicates(lst):
    # Returns True if the list lst contains any duplicate elements,
    # otherwise False.
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False
