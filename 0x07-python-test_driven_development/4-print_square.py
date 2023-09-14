#!/usr/bin/python3
"""
<<<<<<< HEAD

This module is composed by a function that prints a square with the character #

"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer number


=======
This modyle composed by a function that prints a square with the character #
"""
def print_square(size):
    """ Functions that prints a square with the character #
    Args:
       size: size of the square printed
    Returns:
        No return
    Raises:
        TypeError: If size is not an integer number
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
