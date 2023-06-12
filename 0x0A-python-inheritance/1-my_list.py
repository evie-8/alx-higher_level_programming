#!/usr/bin/python3
"""module to inherit class list."""


class MyList(list):
    """class that inherits the class list"""
    def __init__(self):
        """creating object / instance."""
        pass

    def print_sorted(self):
        """sorts list."""
        list_copy = list.copy(self)
        list.sort(list_copy)
        print(list_copy)
