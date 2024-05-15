#!/usr/bin/python3

# This is a function that deletes the item at a\
# specific position in a list
def delete_at(my_list=[], idx=0):
    # Check if the index is out of range
    if idx < 0 or idx >= len(my_list):
        # If it is, return the same list without modifying it
        return my_list

    # Use a slice assignment to replace the elements at indices\
    # idx and greater with the elements at indices idx + 1 and greater.\
    # This effectively deletes the element at index idx from the list.
    my_list[idx:] = my_list[idx + 1:]

    # Use the del statement to remove the last element from the list.
    # This is the element that was originally at index idx, but was\
    # shifted to the end of the list by the slice assignment.
    del my_list[len(my_list):]

    # Return the modified list
    return my_list
