#!/usr/bin/python3
"""creating a module to add two integers.
"""


def add_integer(a, b=98):
    """adding two numbers
    Args:
        a (int): first number
        b (int): second number
    Raises:
        TypeError: if either a or b are not integers
    Returns:
        the sum of a and b after typecasting to floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
