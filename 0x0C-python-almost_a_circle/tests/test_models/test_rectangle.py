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
        self.assertEqual(r1.id, 14)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, 15)
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
            r4 = Rectangle("1", 2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'height must be an integer'
        with self.assertRaises(TypeError)as error:
            r4 = Rectangle(1, "2")
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'x must be an integer'
        with self.assertRaises(TypeError)as error:
            r4 = Rectangle(1, 2, "3")
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'y must be an integer'
        with self.assertRaises(TypeError)as error:
            r4 = Rectangle(1, 2, 3, "4")
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'width must be > 0'
        with self.assertRaises(ValueError)as error:
            r4 = Rectangle(-1, 2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'height must be > 0'
        with self.assertRaises(ValueError)as error:
            r4 = Rectangle(1, -2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'width must be > 0'
        with self.assertRaises(ValueError)as error:
            r4 = Rectangle(0, 2)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'height must be > 0'
        with self.assertRaises(ValueError)as error:
            r4 = Rectangle(1, 0)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'x must be >= 0'
        with self.assertRaises(ValueError)as error:
            r4 = Rectangle(1, 2, -3)
        self.assertEqual(error_msg, str(error.exception))

        error_msg = 'y must be >= 0'
        with self.assertRaises(ValueError)as error:
            r4 = Rectangle(1, 2, 3, -4)
        self.assertEqual(error_msg, str(error.exception))

    def test_area(self):
        self.assertEqual(Rectangle(2, 3).area(), 6)

    def test_str(self):
        r200 = Rectangle(1, 2, id=200)
        self.assertEqual(str(r200), "[Rectangle] (200) 0/0 - 1/2")

    def test_display(self):
        r22 = Rectangle(2, 4)
        self.assertEqual(r22.display(),print('##\n##\n##\n##'))

        r22 = Rectangle(2, 4, 1)
        self.assertEqual(r22.display(),print(' ##\n ##\n ##\n ##'))

        r22 = Rectangle(2, 4, 1, 1)
        self.assertEqual(r22.display(),print('\n ##\n ##\n ##\n ##'))

    def test_to_dictionary(self):
        r23 = Rectangle(2, 4, 1, 1, 300)
        self.assertEqual(print(r23.to_dictionary()),
            print("{'x': 1, 'id': 300, 'height': 4, 'y': 1, 'width': 2}"))

    def test_update(self):
        attrs = (200, 4, 6, 2, 2)
        r23 = Rectangle(2, 4, 1, 1, 100)
        r23.update(*attrs)
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 6, 'x': 2, 'y': 2, 'width': 4, 'id': 200}"))

        r23.update(89)
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 6, 'x': 2, 'y': 2, 'width': 4, 'id': 89}"))

        r23.update(89, 1)
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 6, 'x': 2, 'y': 2, 'width': 1, 'id': 89}"))

        r23.update(89, 1, 2)
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 2, 'x': 2, 'y': 2, 'width': 1, 'id': 89}"))

        r23.update(89, 1, 2, 3)
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 1, 'id': 89}"))

        r23.update(89, 1, 2, 3, 4)
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 4, 'width': 1, 'id': 89}"))

        r23.update(**{ 'id': 100 })
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 1, 'id': 100}"))

        r23.update(**{ 'id': 100, 'width': 3 })
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 3, 'id': 100}"))

        r23.update(**{ 'id': 100, 'width': 3, 'height': 6 })
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 6, 'x': 3, 'y': 2, 'width': 3, 'id': 100}"))

        r23.update(**{ 'id': 100, 'width': 3, 'height': 6, 'x': 6 })
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 6, 'x': 6, 'y': 2, 'width': 3, 'id': 100}"))

        r23.update(**{ 'id': 100, 'width': 3, 'height': 6, 'x': 6, 'y': 4 })
        self.assertEqual(print(r23.to_dictionary()),
            print("{'height': 6, 'x': 6, 'y': 4, 'width': 3, 'id': 100}"))

    def test_create_rectangle(self):
        r24 = Rectangle.create(**{ 'id': 500 })
        self.assertEqual(print(r24.to_dictionary()),
            print("{'height': 1, 'x': 0, 'y': 0, 'width': 1, 'id': 500}"))

        r24 = Rectangle.create(**{ 'id': 500, 'width': 2 })
        self.assertEqual(print(r24.to_dictionary()),
            print("{'height': 1, 'x': 0, 'y': 0, 'width': 2, 'id': 500}"))

        r24 = Rectangle.create(**{ 'id': 500, 'width': 2, 'height': 2 })
        self.assertEqual(print(r24.to_dictionary()),
            print("{'height': 2, 'x': 0, 'y': 0, 'width': 2, 'id': 500}"))

        r24 = Rectangle.create(**{ 'id': 500, 'width': 2, 'height': 2, 'x': 3 })
        self.assertEqual(print(r24.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 0, 'width': 2, 'id': 500}"))

        r24 = Rectangle.create(**{ 'id': 500, 'width': 2, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(print(r24.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 4, 'width': 2, 'id': 500}"))

if __name__ == '__main__':
    unittest.main()
