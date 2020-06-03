#!/usr/bin/python3
'''Python in HOlberton'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class inherited from BaseGeometry'''
    def __init__(self, width, height):
        '''Instantiates the object'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
