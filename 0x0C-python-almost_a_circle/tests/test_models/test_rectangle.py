#!/usr/bin/python3

'''
Unittest for rectangle
'''

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import json
import unittest


class TestRectangleMethods(unittest.TestCase):
    def test_rectangle(self):
        ''' Tests for rectangle base'''
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, 6)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)

        r3 = Rectangle(1, 2, 3, 4, 100)
        self.assertEqual(r3.id, 100)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)

    def test_rectangle_args(self):
        error_msg = 'width must be an integer'
        with self.assertRaises(TypeError)as error:
            Rectangle("1", 2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'height must be an integer'
        with self.assertRaises(TypeError)as error:
            Rectangle(1, "2")
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'x must be an integer'
        with self.assertRaises(TypeError)as error:
            Rectangle(1, 2, "3")
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'y must be an integer'
        with self.assertRaises(TypeError)as error:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'width must be > 0'
        with self.assertRaises(ValueError)as error:
            Rectangle(-1, 2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'height must be > 0'
        with self.assertRaises(ValueError)as error:
            Rectangle(1, -2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'width must be > 0'
        with self.assertRaises(ValueError)as error:
            Rectangle(0, 2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'x must be > 0'
        with self.assertRaises(ValueError)as error:
            Rectangle(1, 2, -3)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'y must be > 0'
        with self.assertRaises(ValueError)as error:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(error_msg, str(error.exception))


if __name__ == '__main__':
    unittest.main()
