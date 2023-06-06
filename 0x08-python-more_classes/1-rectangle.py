#!/usr/bin/python3
"""creating a rectangle module.
"""


class Rectangle:
    """an empty rectangle.
    """
    def __init__(self, width=0, height=0):
        """creating objects.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieving width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """restrictions on width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieving height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """restrictions on height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
