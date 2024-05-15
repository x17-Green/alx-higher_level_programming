#!/usr/bin/python3
# This function returns the maximum integer in a list
def max_integer(my_list=[]):

    # If the list is empty, return None
    if len(my_list) == 0:
        return None

    # Initialize the largest integer to the first element\
    # of the list
    largest = my_list[0]

    # Iterate over the list starting from the second element
    for num in my_list[1:]:

        # If the current number is greater than the largest\
        # integer, update the largest integer
        if num > largest:
            largest = num

    # Return the largest integer
    return largest
