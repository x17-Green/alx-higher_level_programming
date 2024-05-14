#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise.

    Args:
        tuple1 (tuple): First tuple to add.
        tuple2 (tuple): Second tuple to add.

    Returns:
        tuple: A tuple with the sum of corresponding\
        elements from both input tuples.
    """
    # Ensure both tuples have at least 2 elements, padding\
    # with 0 if necessary
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    # Add corresponding elements from both tuples
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
