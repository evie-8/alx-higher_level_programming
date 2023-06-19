#!/usr/bin/python3
"""tests for squsre class"""


import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class Testsquare(unittest.TestCase):
    """testing functions in the Square class"""
    def test_squareinstance(self):
        """checks for type of instance"""
        sq = Square(5)
        self.assertIsInstance(sq, Square)
        self.assertIsInstance(sq, Base)
        self.assertIsInstance(sq, Rectangle)

    def test_get(self):
        """testing for retrieval of values"""
        sq1 = Square(5)
        self.assertEqual(sq1.size, 5)

    def test_set(self):
        """testing for values given to size"""
        sq1 = Square(5)
        sq1.size = 7
        self.assertEqual(sq1.size, 7)

    def test_negative(self):
        """testing for error displayed if size is  negative"""
        sq1 = Square(5)
        with self.assertRaises(ValueError):
            sq1.size = -1

    def test_zero(self):
        """testing for error displayed if zero is passed"""
        sq1 = Square(5)
        with self.assertRaises(ValueError):
            sq1.size = -1

    def test_string(self):
        """testing for error displayed if string is passed"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = "five"

    def test_float(self):
        """testing for error displayed if size is a decimal"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = 5.6

    def test_tuples(self):
        """testing for error displayed if size is a tuple"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = (1, )

    def test_set(self):
        """testing for error displayed if size is a set"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = {2, 3}

    def test_lists(self):
        """testing for error displayed if size is list"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = [3]

    def test_none(self):
        """testing for error displayed if size is none"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = None

    def test_empty(self):
        """testing for error displayed if size is empty"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = ''

    def test_dicts(self):
        """testing for error displayed if size is dicts"""
        sq1 = Square(5)
        with self.assertRaises(TypeError):
            sq1.size = {'size': 5}

    def test_dimensions(self):
        """checking if dimensions are correct for square"""
        sq1 = Square(5)
        self.assertEqual(sq1.width, 5)
        self.assertEqual(sq1.height, 5)

    def test_dict(self):
        """checking for output of to_dictionary function"""
        sq1 = Square(5, 10, 10, 12)
        sq1_dict = sq1.to_dictionary()
        self.assertEqual(sq1_dict, {'id': 12, 'size': 5, 'x': 10, 'y': 10})

    def test_updates(self):
        """checks if changes are made"""
        sq = Square(5, 10, 10, 2)
        self.assertEqual(sq.id, 2)
        sq.update(6, 7)
        self.assertEqual(sq.id, 6)
        self.assertEqual(sq.width, 7)
        sq.update(x=67, y=0)
        self.assertEqual(sq.x, 67)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.width, 7)
