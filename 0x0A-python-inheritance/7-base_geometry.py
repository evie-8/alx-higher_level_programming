#!/usr/bin/python3
"""empty module"""


class BaseGeometry:
    """ empty class."""

    def area(self):
        """empty"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating the arguments passed"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
