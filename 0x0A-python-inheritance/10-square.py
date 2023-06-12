#!/usr/bin/pythnon3
"""modules on sqaures"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        """construtor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
