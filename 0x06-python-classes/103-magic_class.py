#!/usr/bin/python3
"""creating magic class.
"""


import math


class MagicClass:
    """class called magic.
    """
    def __init__(self, radius=0):
        """initialize object.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """area.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """circumference.
        """
        return (2 * math.pi) * self.__radius
