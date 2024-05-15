#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list with the same size as the original list
    result = [False] * len(my_list)

    # Iterate over the original list
    for i in range(len(my_list)):
        # If the integer at the current position is a multiple\
        # of 2, set the corresponding element in the result\
        # list to True
        if my_list[i] % 2 == 0:
            result[i] = True

    # Return the result list
    return result
