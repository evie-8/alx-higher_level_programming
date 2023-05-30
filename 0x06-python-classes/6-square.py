#!/usr/bin/python3
""" Creating a class."""


class Square:
    """Creating class called Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Describing attributes of square.
        Note:
            do not include `self` parameter in the `Args` section
        Args:
            size: dimensions of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ a second attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Ensures tuple has two values.
        Args:
            value: first parameter
        """
        if len(value) != 2 and not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Finding area of a square.
        Returns:
            the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Print a square of given size.
        """
        if not self.__size:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
