#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))

    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]

    if len(tuple_b) > 2:
        tuple_b = tuple_b[:2]

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

"""
    Adds two tuples element-wise.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A new tuple with the sum of corresponding elements.
"""

"""
Script explanation:

Function: add_tuple(tuple_a=(), tuple_b=())

Purpose: Add corresponding elements of two tuples, padding\
with zeros if necessary and truncating if necessary.

Inputs:

    tuple_a: A tuple of integers, defaulting to an empty tuple ().
    tuple_b: A tuple of integers, defaulting to an empty tuple ().

Output: A tuple containing the sum of corresponding elements\
from tuple_a and tuple_b.

Steps:

    If tuple_a has fewer than 2 elements, pad it with zeros\
    to make it at least 2 elements long.
    If tuple_b has fewer than 2 elements, pad it with zeros\
    to make it at least 2 elements long.
    If tuple_a has more than 2 elements, truncate it to only\
    keep the first 2 elements.
    If tuple_b has more than 2 elements, truncate it to only\
    keep the first 2 elements.
    Return a new tuple containing the sum of corresponding\
    elements from tuple_a and tuple_b.

Example:

    Input: tuple_a = (1, 2), tuple_b = (3, 4)
    Output: (4, 6)
"""
