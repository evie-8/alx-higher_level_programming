#!/usr/bin/python3
"""module to act like int."""


class MyInt(int):
    """ inherits from int class"""
    def __eq__(self, value):
        """ return not equal to"""
        return self.real != value

    def __ne__(self, value):
        """return equals to"""
        return self.real == value
