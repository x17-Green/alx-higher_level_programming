#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists): A 2D list of integers.

    Returns:
        None
    """
    for row in matrix:
        print(" ".join("{:d}".format(elem) for elem in row))
