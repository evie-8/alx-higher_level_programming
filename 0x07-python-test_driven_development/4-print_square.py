#!/usr/bin/python3
""" printing a square
"""


def print_square(size):
    """function to print a square.
    Args:
        size (int): dimensions of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
