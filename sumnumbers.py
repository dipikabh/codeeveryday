def sum_numbers(numbers=None):
    """ PyBites Code Challenge: Add a list of given numbers

    If the list is None or no list is given, return the sum of numbers 1 to 100.
    """
    
    if numbers == []:
        return 0
    elif numbers is None:
        return sum_numbers(range(1, 101))

    sum = 0
    for n in numbers:
        sum += n
        
    return sum

print sum_numbers([1, 2, 3])
print sum_numbers(None)
print sum_numbers()
print sum_numbers([])
