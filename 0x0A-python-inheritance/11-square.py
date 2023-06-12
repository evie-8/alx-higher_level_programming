#!/usr/bin/python3
"""modules on sqaures"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inheriting from Rectangle class"""
    def __init__(self, size):
        """construtor that creates instances of sqaure"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """how to print a square"""
        return (f"[Square] {self.__size}/{self.__size}")
