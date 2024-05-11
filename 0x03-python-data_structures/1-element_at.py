#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list at a given index.

    Args:
    my_list (list): The list to retrieve the element from.
    idx (int): The index of the element to retrieve.

    Returns:
    The element at the specified index if it exists, None otherwise.
    """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
