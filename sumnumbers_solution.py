def sum_numbers(numbers=None):
    """ PyBites Code Challenge: Add a list of given numbers

    If the list is None or no list is given, return the sum of numbers 1 to 100.
    """
    if numbers == None:
        numbers = range(1, 101)

    return sum(numbers)

print sum_numbers([1, 2, 3])
print sum_numbers(None)
print sum_numbers()
print sum_numbers([])