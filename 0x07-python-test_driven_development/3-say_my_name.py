#!/usr/bin/python3
"""Module for writing name.
"""


def say_my_name(first_name, last_name=""):
    """print out name.
    Args:
        first_name (str): first name
        last_name (str): last name
    Raises:
        TypeError: if first_name or second_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
