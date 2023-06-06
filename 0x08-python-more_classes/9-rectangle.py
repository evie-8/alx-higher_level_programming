#!/usr/bin/python3
"""creating a rectangle module.
"""


class Rectangle:
    """a defining rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """creating objects.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """area of a rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """ perimter of a rectangle.
        """
        p = 0
        if self.__width == 0 or self.__height == 0:
            p = 0
        else:
            p = 2 * (self.__width + self.__height)
        return p

    def __str__(self):
        """how to output rectangle.
        """
        r = ""
        if self.__width == 0 or self.__height == 0:
            return r
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    r += str(self.print_symbol)
                if i < self.__height - 1:
                    r += "\n"
            return r

    def __repr__(self):
        """string representation of the recatangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """message to show instance has been deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """rectangle with biggest area.
        Args:
            rect_1: first rectangle
            rect_2: second recatangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """creating a square.
        """
        return cls(size, size)
