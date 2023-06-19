#!/usr/bin/python3
"""tests for Base class"""


import os
import pep8
import unittest
import turtle
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """methods to test verify how base class works"""
    def test_pep8_square(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/square.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]
        self.assertEqual(errs, [], f'errors: \n{chr(10).join(error_messages)}')

    def test_id_positive(self):
        """testing for id"""
        b = Base(91)
        b1 = Base(1006)
        self.assertEqual(b.id, 91)
        self.assertEqual(b1.id, 1006)

    def test_id_negative(self):
        """"testing value when id is negative"""
        b2 = Base(-9)
        b3 = Base(-3)
        self.assertEqual(b2.id, -9)
        self.assertEqual(b3.id, -3)

    def test_id_empty(self):
        """test id when nothing is passed"""
        b4 = Base()
        b5 = Base(None)
        self.assertEqual(b4.id, 1)
        self.assertEqual(b5.id, 2)

    def test_id_float(self):
        """testing for id"""
        b = Base(91.5)
        b1 = Base(1006.67)
        self.assertEqual(b.id, 91.5)
        self.assertEqual(b1.id, 1006.67)

    def test_id_string(self):
        """testing for id"""
        b = Base("python")
        b1 = Base("i am one")
        self.assertEqual(b.id, "python")
        self.assertEqual(b1.id, "i am one")

    def test_id_tuple(self):
        """testing for id"""
        b = Base((91, 5))
        b1 = Base((1006, 5))
        self.assertEqual(b.id, (91, 5))
        self.assertEqual(b1.id, (1006, 5))

    def test_id_set(self):
        """testing for id"""
        b1 = Base({1006})
        self.assertEqual(b1.id, {1006})

    def test_id_dicts(self):
        """testing for id"""
        b1 = Base(id=2)
        self.assertEqual(b1.id, 2)
        self.assertIsInstance(b1, Base)

    def test_to_json_string(self):
        """testing to serialization to json"""
        sq = Square(5, 10, 20, 4)
        sq.dict = sq.to_dictionary()
        json_form = Base.to_json_string([sq.dict])
        self.assertEqual(type(json_form), str)

        sq1 = []
        json_form = Base.to_json_string(sq1)
        self.assertEqual(json_form, '[]')

        sq2 = None
        json_form = Base.to_json_string(sq2)
        self.assertEqual(json_form, '[]')

        with self.assertRaises(TypeError):
            jsons = Base.to_json_string()

        sq = [48, 49]
        if all(i for i in sq if type(i) != Square or type(i) != Rectangle):
            self.assertRaises(TypeError)

    def test_save_to_file(self):
        """testing if we have saved the write things"""
        sq = Square(5, 10, 10, 2)
        sq1 = Square(6, 10, 4, 6)
        s = [sq, sq1]
        Square.save_to_file(s)
        self.assertEqual(type(s), list)

        rect = Base()
        rect1 = Base()
        s = [rect, rect1]
        if all(i for i in s if type(i) != Square or type(i) != Rectangle):
            self.assertRaises(TypeError)

    def test_from_json_string(self):
        """testing function from_json_string"""
        jsons = [{"id": 3, "size": 5, "x": 0, "y": 0}]
        string = Base.from_json_string(Base.to_json_string(jsons))
        self.assertIsInstance(string, list)

    def test_create(self):
        """tests for create function"""
        r1 = Rectangle(3, 5, 1, 3, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)

    def test_load_from_file(self):
        """loading from file"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")
        rect = Rectangle.load_from_file()
        self.assertEqual(rect, [])

        sq = Square.load_from_file()
        self.assertEqual(sq, [])

        with self.assertRaises(TypeError):
            s = Square.load_from_file('hi')

    def test_save_to_file_csv(self):
        """testing for csv file"""
        r1 = Rectangle(10, 7, 2, 8, 90)
        r2 = Rectangle(2, 4, 6, 8, 91)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        lists = Rectangle.load_from_file_csv()
        self.assertIsInstance(lists, list)

        r2 = [78, 67]
        if all(i for i in r2 if type(i) != Rectangle or type(i) != Square):
            self.assertRaises(TypeError)

    def test_draw(self):
        """draw test"""
        list_rectangles = [Rectangle(90, 110, 30, 10, 6),
                           Rectangle(20, 25, 110, 80, 33)]
        list_squares = [Square(15, 70, 50, 67),
                        Square(80, 30, 70, 66)]
        Base.draw(list_rectangles, list_squares)
