#!/usr/bin/pythnon3
"""modules on sqaures"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """construtor"""
        Rectangle.__init__(self, size, size)
