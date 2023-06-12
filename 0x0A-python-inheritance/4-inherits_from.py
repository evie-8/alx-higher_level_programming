#!/usr/bin/python3
"""checks if subclass"""


def inherits_from(obj, a_class):
    """check if inherits from that class"""
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    else:
        return False
