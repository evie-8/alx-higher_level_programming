#!/usr/bin/python3
"""module for rectangles"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of retangle"""
        return self.__width * self.__height

    def __str__(self):
        """how to print a rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
