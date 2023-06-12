#!/usr/bin/python3
"""checks if is instance."""


def is_kind_of_class(obj, a_class):
    """checks if instance of any class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
