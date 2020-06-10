#!/usr/bin/python3

'''
Unittest for base
'''

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import json
import unittest


class TestBaseMethods(unittest.TestCase):
    '''class TestBase'''

    def test_base_id(self):
        '''
        tests for base class
        '''
        b1 = Base()
        self.assertEqual(b1.id, 1, 'Id assigned in a wrong way')
        self.assertIsInstance(b1, Base, 'Wrong instance\'s class')

        b2 = Base()
        self.assertEqual(b2.id, 2, 'Id assigned in a wrong way')
        self.assertIsInstance(b2, Base, 'Wrong instance\'s class')

        b3 = Base()
        self.assertEqual(b3.id, 3, 'Id assigned in a wrong way')
        self.assertIsInstance(b3, Base, 'Wrong instance\'s class')

        b4 = Base(12)
        self.assertEqual(b4.id, 12, 'Id assigned in a wrong way')
        self.assertIsInstance(b4, Base, 'Wrong instance\'s class')

        b5 = Base()
        self.assertEqual(b5.id, 4, 'Id assigned in a wrong way')
        self.assertIsInstance(b5, Base, 'Wrong instance\'s class')

    def test_base_args(self):

        error_msg = 'type object \'Base\' has no attribute \'_TestBaseMethods__nb_objects\''
        with self.assertRaises(AttributeError) as error:
            Base.__nb_objects
        self.assertEqual(error_msg, str(error.exception))

        with self.assertRaises(TypeError) as error:
            b6 = Base(10, 20)
        self.assertEqual(
            '__init__() takes from 1 to 2 positional arguments but 3 were given',
            str(error.exception))

    def test_to_json_string(self):
        result = Base.to_json_string(None)
        assertEquals(result, "[]")

        result = Base.to_json_string([])
        assertEquals(result, "[]")


if __name__ == '__main__':
    unittest.main()
