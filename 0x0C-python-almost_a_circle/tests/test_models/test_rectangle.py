#!/usr/bin/python3
"""tests for Rectangle class"""


import unittest
import pep8
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class Testsquare(unittest.TestCase):
    """testing functions in the Square class"""
    def test_pep8_square(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/square.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]
        self.assertEqual(errs, [], f'errors: \n{chr(10).join(error_messages)}')

    def test_squareinstance(self):
        """checks for type of instance"""
        sq = Rectangle(5, 6, 2, 2, 7)
        self.assertIsInstance(sq, Base)
        self.assertIsInstance(sq, Rectangle)

    def test_get(self):
        """testing for retrieval of values"""
        sq1 = Rectangle(5, 4, 1, 1, 4)
        self.assertEqual(sq1.x, 1)
        self.assertEqual(sq1.y, 1)
        self.assertEqual(sq1.width, 5)
        self.assertEqual(sq1.height, 4)

    def test_set(self):
        """testing for values given to size"""
        sq1 = Rectangle(5, 4, 1, 1, 4)
        sq1.width = 6
        sq1.height = 10
        sq1.x = 70
        sq1.y = 75
        sq1.id = 6
        self.assertEqual(sq1.width, 6)
        self.assertEqual(sq1.height, 10)
        self.assertEqual(sq1.x, 70)
        self.assertEqual(sq1.y, 75)
        self.assertEqual(sq1.id, 6)

    def test_negative(self):
        """testing for error displayed if size is  negative"""
        sq1 = Rectangle(5, 6, 6, 2, 1)
        with self.assertRaises(ValueError):
            sq1.width = -6
        with self.assertRaises(ValueError):
            sq1.height = -10
        with self.assertRaises(ValueError):
            sq1.x = -70
        with self.assertRaises(ValueError):
            sq1.y = -75

    def test_zero(self):
        """testing for error displayed if zero is passed"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(ValueError):
            sq1.width = 0
        with self.assertRaises(ValueError):
            sq1.height = 0
        with self.assertRaises(ValueError):
            sq1.x = -1
        with self.assertRaises(ValueError):
            sq1.y = -1

    def test_string(self):
        """testing for error displayed if string is passed"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(TypeError):
            sq1.width = "hi"
        with self.assertRaises(TypeError):
            sq1.height = "gg"
        with self.assertRaises(TypeError):
            sq1.x = "g"
        with self.assertRaises(TypeError):
            sq1.y = "pp"

    def test_float(self):
        """testing for error displayed if size is a decimal"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(TypeError):
            sq1.width = 4.6
        with self.assertRaises(TypeError):
            sq1.height = 6.7
        with self.assertRaises(TypeError):
            sq1.x = 2.4
        with self.assertRaises(TypeError):
            sq1.y = 6.7

    def test_tuples(self):
        """testing for error displayed if size is a tuple"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(TypeError):
            sq1.width = (1, )
        with self.assertRaises(TypeError):
            sq1.height = (7, 6)
        with self.assertRaises(TypeError):
            sq1.x = (4, 6)
        with self.assertRaises(TypeError):
            sq1.y = (5, 8)

    def test_set(self):
        """testing for error displayed if size is a set"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(TypeError):
            sq1.width = {3, 5}
        with self.assertRaises(TypeError):
            sq1.height = {4, 6}
        with self.assertRaises(TypeError):
            sq1.x = {6, 7}
        with self.assertRaises(TypeError):
            sq1.y = {8, 1}

    def test_lists(self):
        """testing for error displayed if size is list"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(TypeError):
            sq1.width = [3, 5]
        with self.assertRaises(TypeError):
            sq1.height = [4, 6]
        with self.assertRaises(TypeError):
            sq1.x = [6, 7]
        with self.assertRaises(TypeError):
            sq1.y = [6, 7]

    def test_none(self):
        """testing for error displayed if size is none"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(TypeError):
            sq1.width = None
        with self.assertRaises(TypeError):
            sq1.height = None
        with self.assertRaises(TypeError):
            sq1.x = None
        with self.assertRaises(TypeError):
            sq1.y = None

    def test_empty(self):
        """testing for error displayed if size is empty"""
        sq1 = Rectangle(5, 3, 6, 2, 1)
        with self.assertRaises(TypeError):
            sq1.width = ''
        with self.assertRaises(TypeError):
            sq1.height = ''
        with self.assertRaises(TypeError):
            sq1.x = ''
        with self.assertRaises(TypeError):
            sq1.y = ''

    def test_dict(self):
        """checking for output of to_dictionary function"""
        sq1 = Rectangle(5, 6, 10, 10, 12)
        sq1_dict = sq1.to_dictionary()
        ex = {'id': 12, 'width': 5, 'height': 6, 'x': 10, 'y': 10}
        self.assertEqual(sq1_dict, ex)

    def test_updates(self):
        """checks if changes are made"""
        sq = Rectangle(5, 7, 10, 10, 2)
        self.assertEqual(sq.id, 2)
        sq.update(6, 8, 5, 7, 9)
        self.assertEqual(sq.id, 6)
        self.assertEqual(sq.width, 8)
        self.assertEqual(sq.height, 5)
        sq.update(x=67, y=0)
        self.assertEqual(sq.x, 67)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.width, 8)
