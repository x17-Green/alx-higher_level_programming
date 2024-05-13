#!/usr/bin/python3
def no_c(my_string):
    """
    Description: This function removes all occurrences of\
    the characters 'c' and 'C' from a given string my_string.

    Arguments:
        my_string (str): The input string to be modified.

    Returns:
        new_string (str): The modified string with all\
        occurrences of 'c' and 'C' removed.
    """
    new_string = ''
    for char in my_string:
        if char != "c" and char != "C":
            new_string += char
    return new_string
