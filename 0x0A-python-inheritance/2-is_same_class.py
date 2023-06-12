#!/usr/bin/python3
"""test if object is an instance class."""


def is_same_class(obj, a_class):
    """checks if they are the same class."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
