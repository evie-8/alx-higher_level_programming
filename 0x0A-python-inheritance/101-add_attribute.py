#!/usr/bin/python3
"""module to add attribute to object"""


def add_attribute(obj, attr, value):
    """adding attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
