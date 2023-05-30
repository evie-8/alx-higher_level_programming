#!/usr/bin/python3
""" Creating a class."""


class Square:
    """Creating class called Square.
    """
    def __init__(self, size=0):
        """Describing attributes of square.
        Note:
            do not include `self` parameter in the `Args` section
        Args:
            size: dimensions of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Finding area of a square.
        Returns:
            the area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """how to retrieve size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Ensuring know wrong values are entered>
        Args:
            value: first parameter
       """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
