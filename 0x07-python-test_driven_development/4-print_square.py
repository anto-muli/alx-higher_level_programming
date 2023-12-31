#!/usr/bin/python3
"""
The module has a function to prints a square
"""


def print_square(size):
    """The function to print squares with the character #
    Args:
        size (int): This represents the squares length
    Raises:
        TypeError: If size isn't an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
